# Slack Presence Scheduler

This Python script allows you to automatically set your Slack presence (`auto` or `away`) based on the current time. It's designed to be run as a cron job, making it ideal for scheduling presence updates at specific times, such as during working hours or after hours.

## Features

- **Automatic Presence Updates**: Set your Slack presence to `auto` or `away` based on the current UTC time.
- **Customizable**: Easily adjust the time conditions to fit your schedule.
- **Integration with Slack API**: Utilizes the Slack API to set user presence.

## Prerequisites

Before running this script, ensure you have the following:

- **Python 3.x** installed.
- A **Slack User OAuth token** with the `users:write` scope. You can obtain this from your Slack App settings under OAuth & Permissions.

## Cron Setup

1. **Clone the repository (Optional)**:

   ```bash
   git clone https://github.com/rikki-martin/slack-presence-scheduler.git
   cd slack-presence-scheduler

2. **Fork the repository**:

   This is more ideal since everything will be almost set up.

3. **Add your Slack OAuth Token in Github Secrets**:

    On the repo, click `settings`, then `secrets and variables`, then `actions`, and `new repository secret`. Have the name be
    `SLACK_OAUTH_TOKEN` and the value your slack token starting with `xoxp-your-token`.

4. **Configure start and end time configs**:

   Change the scheduler in `.github/workflows/slack-presence.yml` for when you want to run the script.
   Make sure to also set the `START_HOUR` and `END_HOUR` in `slack_presence_scheduler.py` to correspond with the hour set in the yml file or it will NOT work. ***NOTE: The times are all in UTC***