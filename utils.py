import os
import csv
import json

def read_file_content(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    try:
        if ext in [".txt", ".log"]:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read().lower()

        elif ext == ".csv":
            data = []
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                reader = csv.reader(f)
                for row in reader:
                    data.append(" ".join(row).lower())
            return "\n".join(data)

        elif ext == ".json":
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                obj = json.load(f)
            return json.dumps(obj).lower()

        else:
            return ""
    except Exception:
        return ""