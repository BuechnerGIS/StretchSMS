import smtplib
CARRIERS = {
        'att': '@mms.att.net',
        'tmobile': '@tmomail.net',
        'verizon': '@vtext.com',
        'sprint': '@page.nextel.com'
}

EXERCISES = {
    "Overhead Stretch": 10,
    "Twist": 15,
    "Push-up": 10,
    "Curl": 10,
    "Chest Press": 10
}


def send(email_acc, email_pw, target_phone, carrier, message):
    # Ensure a supported carrier was provided
    validate_carrier(carrier)

    # Replace the number with your own, or consider using an argument\dict for multiple people.
    to_number = f'{target_phone}{CARRIERS[carrier]}'
    auth = (email_acc, email_pw)

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    print("Securing session..")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    print("Starting TLS..")
    server.starttls()
    print("Authenticating..")
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    print("Sending Mail..")
    server.sendmail(auth[0], to_number, message)

def validate_carrier(carrier):
    if carrier not in CARRIERS.keys():
        raise ValueError(f"Carrier \"{carrier}\" not supported!")
