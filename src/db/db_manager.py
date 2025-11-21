import os
import uuid
import psycopg2
from psycopg2.extras import Json, RealDictCursor, RealDictRow
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:
    def __init__(self):
        db_name = os.getenv("DB_NAME", "spautofy")
        db_host = os.getenv("DB_HOST", "localhost")
        db_user = os.getenv("DB_USER", "postgres")
        db_password = os.getenv("DB_PASSWORD", "")
        
        admin_conn = psycopg2.connect(
            host=db_host,
            database="postgres",
            user=db_user,
            password=db_password
        )
        admin_conn.autocommit = True
        admin_cursor = admin_conn.cursor()
        
        admin_cursor.execute(
            "SELECT 1 FROM pg_database WHERE datname = %s", (db_name,)
        )
        if not admin_cursor.fetchone():
            admin_cursor.execute("CREATE DATABASE %s", (db_name,))
        
        admin_cursor.close()
        admin_conn.close()
        
        self.conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )
        self.conn.autocommit = True
        
        schema_path = "src/db/schema.sql"
        cursor = self.conn.cursor()
        with open(schema_path, "r") as f:
            cursor.execute(f.read())
        cursor.close()
    
    def create_chat(self) -> RealDictRow:
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        chat_id = uuid.uuid4()
        cursor.execute("INSERT INTO chats (id) VALUES (%s) RETURNING *", (str(chat_id),))
        chat = cursor.fetchone()
        cursor.close()
        return chat
    
    def get_all_chats(self) -> list[RealDictRow]:
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM chats ORDER BY created_at ASC")
        chats = cursor.fetchall()
        cursor.close()
        return list(chats)
    
    def get_chat_events(self, chat_id: str) -> list[RealDictRow]:
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            "SELECT * FROM chat_events WHERE chat_id = %s ORDER BY created_at ASC",
            (str(chat_id),)
        )
        events = cursor.fetchall()
        cursor.close()
        return list(events)
    
    def create_llm_response(self, chat_id: str, input_tokens: int, cached_tokens: int, output_tokens: int) -> RealDictRow:
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        llm_response_id = uuid.uuid4()
        cursor.execute(
            "INSERT INTO llm_responses (id, chat_id, input_tokens, cached_tokens, output_tokens) VALUES (%s, %s, %s, %s, %s) RETURNING *",
            (str(llm_response_id), str(chat_id), input_tokens, cached_tokens, output_tokens)
        )
        llm_response = cursor.fetchone()
        cursor.close()
        return llm_response
    
    def create_chat_event(self, chat_id: str, event_type: str, event_object: dict) -> RealDictRow:
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        chat_event_id = uuid.uuid4()
        cursor.execute(
            "INSERT INTO chat_events (id, chat_id, event_type, event_object) VALUES (%s, %s, %s, %s) RETURNING *",
            (str(chat_event_id), str(chat_id), event_type, Json(event_object))
        )
        event = cursor.fetchone()
        cursor.close()
        return event