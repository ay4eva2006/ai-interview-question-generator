import datetime
import json
import os


class AILogger:

    LOG_FILE = "logs/ai_logs.json"

    @staticmethod
    def log(event_type, data):

        log_entry = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "event": event_type,
            "data": data
        }

        os.makedirs("logs", exist_ok=True)

        with open(AILogger.LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")