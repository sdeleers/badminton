from badmintonScript import enrollmentIsOpen, nextBadmintonDate, wednesday
import datetime

def testEnrollmentIsOpen():
    with open('html/badminton_open.html', 'r') as myfile:
        page_html_open = myfile.read()

    with open('html/badminton_closed.html', 'r') as myfile:
        page_html_closed = myfile.read()

    return (enrollmentIsOpen(page_html_open, datetime.date(2017, 11, 8)) == True) and \
           (enrollmentIsOpen(page_html_open, datetime.date(2017, 11, 9)) == False) and \
           (enrollmentIsOpen(page_html_closed, datetime.date(2017, 11, 8)) == False) and \
           (enrollmentIsOpen(page_html_closed, datetime.date(2017, 11, 9)) == False)

def testNextBadmintonDate():
    next_badminton_date_1 = nextBadmintonDate(datetime.date(2017, 11, 7))
    next_badminton_date_2 = nextBadmintonDate(datetime.date(2017, 11, 9))
    return (next_badminton_date_1.weekday() == wednesday) and \
           (next_badminton_date_2.weekday() == wednesday) and \
           (next_badminton_date_1.day == 8) and \
           (next_badminton_date_2.day == 15)

# Run tests
if (testEnrollmentIsOpen()):
    print("Unit test enrollmentIsOpen passed")
else:
    print("Unit test enrollmentIsOpen failed")

if (testNextBadmintonDate()):
    print("Unit test nextBadmintonDate passed")
else:
    print("Unit test nextBadmintonDate failed")
