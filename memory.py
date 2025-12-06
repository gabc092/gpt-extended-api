import json
import os
from datetime import datetime

MEMORY_DIR = "memory_storage"
os.makedirs(MEMORY_DIR, exist_ok=True)

def save_to_memory(data):
    timestamp = datetime.utcnow().isoformat()
    filename = f"{timestamp}.json"
    filepath = os.path.join(MEMORY_DIR, filename)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
