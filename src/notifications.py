import smtplib
from email.message import EmailMessage

sender = "totallyrea616@gmail.com"
receiver = "someone@example.com"
password = "wvvckenltserjxbc"

def main():
    msg = EmailMessage()
    msg["Subject"] = "This is a test"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("This was sent from the terminal")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
            print("Success")
    except Exception as e:
        print("Didn't work", e)

if __name__ == "__main__":
    main()
