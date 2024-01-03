from datetime import datetime


def log(message):
    curr_time = datetime.utcnow().isoformat()
    print(f"{curr_time} - {message}")


log("log 1")
