import os
import StretchSMS as SMS
import time
from datetime import datetime

EMAIL_ADDR=os.environ.get("SMS_EMAIL_ACCOUNT").lower()
EMAIL_PASS=os.environ.get("SMS_EMAIL_PASSWORD")
TARGET_PHONE=os.environ.get("SMS_TARGET_PHONE")
TARGET_PHONE_CARRIER=os.environ.get("SMS_TARGET_PHONE_CARRIER").lower()

if __name__ == "__main__":
    #TODO - Cron job
    #time = str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    #text_message="\nIt's time to stretch! Another message will be coming at " + time + "."
    text_message="\nIt's time to stretch!" # Leading newline strips extra text from SMS.
    SMS.send(EMAIL_ADDR, EMAIL_PASS, TARGET_PHONE, TARGET_PHONE_CARRIER, text_message)
    print("Complete")
