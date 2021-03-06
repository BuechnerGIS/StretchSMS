import os
import StretchSMS as SMS
import time
from datetime import datetime
import argparse
from random import randrange

EMAIL_ADDR=os.environ.get("SMS_EMAIL_ACCOUNT").lower()
EMAIL_PASS=os.environ.get("SMS_EMAIL_PASSWORD")
TARGET_PHONE=os.environ.get("SMS_TARGET_PHONE").split(" ")
TARGET_PHONE_CARRIER=os.environ.get("SMS_TARGET_PHONE_CARRIER").lower().split(" ")

def get_exercise():
    exercises = list(SMS.EXERCISES.keys())
    idx = randrange(len(exercises))
    exercise = exercises[idx]
    reps = SMS.EXERCISES[exercise]
    return (exercise, reps)

def parse_args():
    parser = argparse.ArgumentParser(description='Argument Parsing for StretchSMS')

    # Add the arguments
    parser.add_argument('-d', dest='debug', action='store_true')

    # Execute the parse_args() method
    return parser.parse_args()


if __name__ == "__main__":
    # Parse Args and get timestamp
    args = parse_args()
    time = str(datetime.now().strftime("%I:%M:%S %p"))

    # Format message depending on runtype
    if args.debug:
        text_message=f"\n{time}\nDebug message from StretchSMS." # Leading newline strips extra text from SMS.

    else:
        ex, reps = get_exercise()
        text_message=f"\n{time}\nIt's time to stretch!\nDo {reps} {ex}(s)!" # Leading newline strips extra text from SMS.
       
    # Send messages to all phones listed in .env
    for i in range(0, len(TARGET_PHONE)):
        phone=TARGET_PHONE[i]
        carrier=TARGET_PHONE_CARRIER[i]
        print(f"{time}: Sending SMS to {phone}: {text_message}")
        SMS.send(EMAIL_ADDR, EMAIL_PASS, phone, carrier, text_message)
    
    print("Complete!")
