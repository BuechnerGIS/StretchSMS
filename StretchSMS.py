import smtplib
CARRIERS = {
        'att': '@mms.att.net',
        'tmobile': '@tmomail.net',
        'verizon': '@vtext.com',
        'sprint': '@page.nextel.com'
}

def send(email_acc, email_pw, target_phone, carrier, message):
    # Ensure a supported carrier was provided
    validate_carrier(carrier)

    # Replace the number with your own, or consider using an argument\dict for multiple people.
    to_number = f'{target_phone}{carriers[carrier]}'
    auth = (email_acc, email_pw)

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    server.sendmail(auth[0], to_number, message)

def validate_carrier(carrier):
    if carrier not in CARRIERS.keys():
        raise ValueError(f"Carrier \"{carrier}\" not supported!")