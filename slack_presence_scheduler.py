import os
import requests
from datetime import datetime

AUTO = "auto"
AWAY = "away"
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
    response_json = response.json()

    if response_json.get("ok"):
        print(f"Presence set to {presence} at {datetime.now()}")
    else:
        print(f"Failed to set presence. Error: {response_json.get('error')}")
        sys.exit(1)

def failureMessage():
    print("Failed to set presence due to time constraints. Please try again later.")
    sys.exit(1)

def main():
    current_hour = datetime.utcnow().hour

    if current_hour == 14: # If it's within 2PM UTC (8AM CST), set presence to auto
        set_presence(AUTO)
    elif current_hour == 23: # If it's within 11PM UTC (5PM CST), set presence to away
        set_presence(AWAY)
    else:
        failureMessage()

if __name__ == "__main__":
    main()