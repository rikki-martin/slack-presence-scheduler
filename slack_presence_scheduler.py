import os
import requests
from datetime import datetime

slack_token = os.getenv("SLACK_OAUTH_TOKEN")

url = "https://slack.com/api/users.setPresence"

headers = {
    "Authorization": f"Bearer {slack_token}",
    "Content-Type": "application/json; charset=utf-8"
}

def set_presence(presence):
    data = {
        "presence": presence
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    print(f"Presence set to {presence} at {datetime.now()}")

def main():
    current_hour = datetime.utcnow().hour

    if current_hour == 14: # If it's within 2PM UTC (8AM CST), set presence to auto
        set_presence("auto")
    elif current_hour == 23: # If it's within 11PM UTC (5PM CST), set presence to away
        set_presence("away")
    else:
        set_presence("away")

if __name__ == "__main__":
    main()