import os
import slackweb


def slack(message):
    WEBHOOK_URL = os.environ.get('MY_INC_URL', '')
    sl = slackweb.Slack(url=WEBHOOK_URL)
    sl.notify(text=message)
