import uuid

def generate_index_name(filename: str) -> str:
    base = filename.rsplit(".", 1)[0].replace(" ", "_").lower()
    return f"{base}_{uuid.uuid4().hex[:8]}"