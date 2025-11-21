CREATE TABLE IF NOT EXISTS chats (
    id UUID PRIMARY KEY,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS llm_responses (
    id UUID PRIMARY KEY,
    chat_id UUID NOT NULL,
    input_tokens INT NOT NULL,
    cached_tokens INT NOT NULL,
    output_tokens INT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    FOREIGN KEY (chat_id) REFERENCES chats(id)
);

CREATE TABLE IF NOT EXISTS chat_events (
    id UUID PRIMARY KEY,
    chat_id UUID NOT NULL,
    event_type TEXT NOT NULL,
    event_object JSONB NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    FOREIGN KEY (chat_id) REFERENCES chats(id)
);
