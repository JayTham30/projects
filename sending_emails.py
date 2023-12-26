import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # os.path


html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Jay Thammavongsa"
email["to"] = "thammavongsajay@gmail.com"
email["subject"] = "You won 1,000,000 dollars!"


email.set_content(html.substitute({"name": "Jay", "money": "$10,000"}), "html")


# Logs into google gmail server.
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    # Sends a "hello" signal to server
    smtp.ehlo()
    # Starts server
    smtp.starttls()
    # Login into email. Putting in Email and Password App Credintials
    smtp.login("spam.thammavongsajay@gmail.com", "mbad mdxa aihc pcir")
    # Sends Email
    smtp.send_message(email)
    print("all good boss!")
