#!/usr/bin/python
# -*- coding: utf-8 -*-
original = raw_input("Please insert a date with the form dd/mm/yyyy:")
s = str(original)
date, month, year = s.split('/')
#Έλεγχος αν η ημερομηνία, ο μήνας και το έτος είναι σωστά
while((int(month) < 01 or int(month) > 12) or (int(year) < 1600 or int(year) > 2799)):
    if int(month) < 01 and int(month) > 12:
        month1 = raw_input("Please insert a month  (01-12):")
        month = str(month1)
    if int(year) < 1600 and int(year) > 2799:
        year1 = raw_input("Please insert a year (1600-2799):")
        year = str(year1)
if int(month)==01 or int(month)==03 or int(month)==05 or int(month)==07 or int(month)==07 +1 or int(month)==10 or int(month)==12:
    while(int(date)<01 or int(date)>31):
        print "The %s month has range(01-31)" % (month)
        date1 = raw_input("Please insert a date (01-31):")
        date = str(date1)

elif int(month)==04 or int(month)==06 or int(month)==07+2 or int(month)==11:
    while(int(date)<01 or int(date)>30):
        print "The %s month has range(01-30)" % (month)
        date1= raw_input("Please insert a date (01-30):")
        date = str(date1)

else:
    if int(year)%4==0:
        while(int(date)<01 or int(date)>29):
            print "The %s month has range(01-29)" % (month)
            date1 = raw_input("Please insert a date (01-29):")
            date = str(date1)

    else:
        while(int(date)<01 or int(date)>28):
            print "The %s has month range(01-28)" % (month)
            date1 = raw_input("Please insert a date (01-28):")
            date = str(date1)

#Βρίσκει τον κωδικό του μήνα που έχει δώσει ο χρήστης
if int(month) == 01:
    codeofmonth = 1
elif int(month) == 02:
    codeofmonth = 4
elif int(month) == 03:
    codeofmonth = 4
elif int(month) == 04:
    codeofmonth = 0
elif int(month) == 05:
    codeofmonth = 2
elif int(month) == 06:
    codeofmonth = 5
elif int(month) == 07:
    codeofmonth = 0
elif int(month) == 07 +1:
    codeofmonth = 3
elif int(month) == 07 +2:
    codeofmonth = 6
elif int(month) == 10:
    codeofmonth = 1
elif int(month) == 11:
    codeofmonth = 4
else:
    codeofmonth = 6
#Βρίσκει τι κωδικό έχει ο αιώνας μέσα
#στο οποίο βρίσκεται το έτος που έχει δώσει ο χρήστης
if int(year) >= 1600 and int(year) <= 1699:
    codeofcentury = 6
elif int(year) >= 1700 and int(year) <= 1799:
    codeofcentury = 4
elif int(year) >= 1800 and int(year) <= 1899:
    codeofcentury = 2
elif int(year) >= 1900 and int(year) <= 1999:
    codeofcentury = 0
elif int(year) >= 2000 and int(year) <= 2099:
    codeofcentury = 6
elif int(year) >= 2100 and int(year) <= 2199:
    codeofcentury = 4
elif int(year) >= 2200 and int(year) <= 2299:
    codeofcentury = 2
elif int(year) >= 2300 and int(year) <= 2399:
    codeofcentury = 0
elif int(year) >= 2400 and int(year) <= 2499:
    codeofcentury = 6
elif int(year) >= 2500 and int(year) <= 2599:
    codeofcentury = 4
elif int(year) >= 2600 and int(year) <= 2699:
    codeofcentury = 2
else:
    if int(year) >= 2700 and int(year) <= 2799:
        codeofcentury = 0

#Βρίσκει το τελευταίο και το προτελευταίο ψηφίο του έτους
yearlast = int(year) % 10
yeartempt = int(year) / 10
yearprelast = yeartempt % 10
#Υπολογίζει τον κωδικό του έτους
codeofyear = (codeofcentury + (yearprelast * 10 + yearlast) + (yearprelast * 10 + yearlast) / 4) % 7
#Υπολογίζει τον κωδικό της ημέρας
codeofday = (codeofmonth + codeofyear + int(date))%7
#Ελέγχει αν το έτος είναι δίσεκτο
#Αν είναι τότε αφαιρεί 1 μέρα μόνο
#αν ο μήνας είναι ο Ιανουάριος ή ο Φεβρουάριος
if int(year)%4 == 0:
    if int(month) == 01 or int(month) == 02:
        codeofday=codeofday-1
if codeofday == 1:
    print "Sunday"
elif codeofday == 2:
    print "Monday"
elif codeofday == 3:
    print "Tuesday"
elif codeofday == 4:
    print "Wednesday"
elif codeofday == 5:
    print "Thursday"
elif codeofday == 6:
    print "Friday"
else:
    print "Saturday"
