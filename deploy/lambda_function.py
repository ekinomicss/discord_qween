import json
import requests as req
from random import choice 


def main():
    path = 'https://discord.com/api/webhooks/1019010209034813480/W2GLv2r0v-6E5Xz2sF8HwPYlAgg7pZjpyTfL3uIWn3W3exTDVRzCWj8TYQCPtDXNZZ_q'
    msg = random_msg()

    r = req.post(path, data={"content": msg, "username": "ur mom"})
    r.raise_for_status()


def random_msg():
    msgs = [
        "it's time to stretch bitchezzzzzzz",
        "You better get your fucking ass up and get to stretching",
        "Time to stretchironi, HOMEY",
        "FLASH NEWS: the aliens have landed from stretchuranus",
        "wdym you did NOT stretch today?? *gasping pikachu*"
        ]
    return choice(msgs)


def lambda_handler(event, context):
    # TODO implement
    main()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

