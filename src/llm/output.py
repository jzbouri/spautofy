from rich.text import Text
from rich.markdown import Markdown
from rich.console import Group

DASH_COUNT = 150

def get_output_text(event_object):
    if "role" in event_object and event_object["role"] == "user":
        text = Text()
        text.append("-" * DASH_COUNT + "\n", style="dim")
        text.append("You:\n\n", style="bold cyan")
        text.append(f"{event_object['content']}\n", style="white")
        text.append("-" * DASH_COUNT, style="dim")
        return text
    elif "role" in event_object and event_object["role"] == "assistant":
        header = Text()
        header.append("-" * DASH_COUNT + "\n", style="dim")
        header.append("Assistant:\n", style="bold green")
        content = Markdown(event_object['content'][0]['text'])
        return Group(header, content)
    elif "type" in event_object and event_object["type"] == "reasoning":
        text = Text("Assistant is reasoning...", style="italic dim")
        return text
    elif "type" in event_object and event_object["type"] == "function_call":
        text = Text()
        text.append("Assistant is calling ", style="dim")
        text.append(event_object['name'], style="bold yellow")
        text.append(" with arguments ", style="dim")
        text.append(event_object['arguments'], style="yellow")
        return text
    elif "type" in event_object and event_object["type"] == "function_call_output":
        text = Text("Function call completed", style="dim green")
        return text
    elif "type" in event_object and event_object["type"] == "web_search_call":
        text = Text()
        text.append("Assistant is searching the web for ", style="dim")
        text.append(f"\"{event_object['action']['query']}\"", style="bold blue")
        return text
    else:
        return Text("")