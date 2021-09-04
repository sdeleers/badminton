import smtplib
from time import sleep
import datetime
import requests
import time

wednesday = 2
thursday = 3
url = 'https://www.ucll.be/studeren/student-aan-ucll/campussen/campus-hertogstraat/sporthal/sportaanbod-heverlee/badminton'
mailSender = ""  # Removed for security purposes
mailRecipient = ""  # Removed for security purposes
mailContent = "De inschrijvingen voor badminton zijn open."

def enrollmentIsOpen(page_html, next_badminton_date):
    string_one_to_look_for = "Inschrijving voor activiteit op datum van"
    string_two_to_look_for = next_badminton_date.strftime("%d/%m/%Y")
    string_three_to_look_for = "21h00"

    if (string_one_to_look_for in page_html) and \
       (string_two_to_look_for in page_html) and \
       (string_three_to_look_for in page_html):
        return True
    else:
        return False

def nextBadmintonDate(current_date):
    next_date = current_date
    while next_date.weekday() != wednesday:
        next_date += datetime.timedelta(days=1)
    return next_date

def getDate():
    return datetime.datetime.utcnow()

def sendMail(sender, recipient, content):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login("", "") # Removed for security purposes # https://support.google.com/mail/answer/185833?hl=en
    server.sendmail(sender, recipient, content)
    print("Mail was sent on " + time.strftime("%d/%m/%Y"))

def main():
    mail_was_sent = False
    next_badminton_date = nextBadmintonDate(getDate())
    while True:
        sleep(300)
        current_date = getDate()
        current_date_string = current_date.strftime("%d/%m/%Y %H:%M")

        # Reset mail_was_sent if next badminton date is one week further.
        if next_badminton_date.day != nextBadmintonDate(current_date).day:
            print(current_date_string + ". Reset")
            mail_was_sent = False

        next_badminton_date = nextBadmintonDate(current_date)
        if not mail_was_sent:
            page_html = requests.get(url).text
            if(enrollmentIsOpen(page_html, next_badminton_date)):
                print(current_date_string + ". Registration is open. Mail was sent")
                sendMail(mailSender, mailRecipient, mailContent)
                mail_was_sent = True
            else:
                print(current_date_string + ". Registration is not yet open.")

if __name__ == "__main__":
    main()
