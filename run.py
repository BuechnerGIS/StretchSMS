import os
import StretchSMS as SMS
import time
from datetime import datetime
import argparse

EMAIL_ADDR=os.environ.get("SMS_EMAIL_ACCOUNT").lower()
EMAIL_PASS=os.environ.get("SMS_EMAIL_PASSWORD")
TARGET_PHONE=os.environ.get("SMS_TARGET_PHONE")
TARGET_PHONE_CARRIER=os.environ.get("SMS_TARGET_PHONE_CARRIER").lower()


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
        text_message=f"\n{time}\nIt's time to stretch!" # Leading newline strips extra text from SMS.
    
    #text_message="\nIt's time to stretch! Another message will be coming at " + time + "."    
    SMS.send(EMAIL_ADDR, EMAIL_PASS, TARGET_PHONE, TARGET_PHONE_CARRIER, text_message)
    print("Complete")
