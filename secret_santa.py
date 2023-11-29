import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import random
import pandas as pd
import os


def read_env_file(file_path='.env'):
    """
    Read and parse the contents of a .env file.

    Args:
    - file_path (str): Path to the .env file. Default is '.env'.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            key, value = line.split('=', 1)
            os.environ[key] = value

# Read and parse the contents of the .env file
read_env_file()
username = os.environ.get('ssUSERNAME')
password = os.environ.get('ssPASSWORD')
smtp_server = 'smtp.gmail.com'
smtp_port = 465

attachment = 'dwight.gif'
df = pd.read_csv('SS_Data.csv')
sender_email = 'cysecret.santa24@gmail.com'


def send_secret_santa_email(name, recipient):

    corresponding_name = df.loc[df['email'] == recipient, 'Name'].values[0].split()[0]

    subject = "Secret Santa Gift Exchange"
    body = f"Dear {corresponding_name},\n\nYou are the Secret Santa for {name}! 🎁\n\nHappy holidays!\nYour Secret Santa Bot\n\n"

    # Compose the email
    msg = MIMEMultipart()
    msg['From'] = 'Secret Santa Bot'
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with open(attachment, 'rb') as fp:
        img = MIMEImage(fp.read())
    img.add_header('Content-ID', '<{}>'.format(attachment))
    msg.attach(img)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as smtp:
            smtp.login(username, password)

            # Send the email
            smtp.send_message(msg)
            print('Email sent successfully.')

    except Exception as e:
        print(f'Error: {e}')

def secret_santa(df):
    names = df['Name'].tolist()
    email_list = df['email'].tolist()
    shuffled_list = email_list.copy()

    random.shuffle(shuffled_list)

    for i in range(len(email_list)):
        sender = names[i]
        temp_shuffled_list = shuffled_list.copy()
        sender_index = temp_shuffled_list.index(email_list[i])
        temp_shuffled_list.pop(sender_index)

        # Ensure recipient is not the sender
        recipient_index = sender_index % len(temp_shuffled_list)
        recipient = temp_shuffled_list[recipient_index]

        # If recipient is the same as sender, choose the next person in the shuffled list
        while recipient == sender:
            recipient_index = (recipient_index + 1) % len(temp_shuffled_list)
            recipient = temp_shuffled_list[recipient_index]

        send_secret_santa_email(sender, recipient)
        # print(f"Email sent from {sender} to {recipient}")


if __name__ == "__main__":
    secret_santa(df)
