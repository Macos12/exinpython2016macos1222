# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
#Εισάγει ο χρήστης δύο ονόματα του twitter
firstacc = raw_input("Please insert the name of twitter account:")
secondacc = raw_input("Please insert the name of another twitter account:")
#Κάνει την ίδια διαδικασία και για τα δύο account
for i in range(2):
    #Μπαίνει στο πρώτο account
    if i==0:
        #Συνδέεται με το twitter
        Base_URL="https://twitter.com/"+firstacc
        r = requests.get(Base_URL)
        #Μπαίνει στο κώδικα html του twitter
        soup = BeautifulSoup(r.content, "lxml")
        #Βρίσκει τις ετικέτες tweets,following,followers,likes από τον κώδικα της σελιδας
        twetts1 = soup.find("div", class_="ProfileCanopy-nav").find("ul", class_="ProfileNav-list").find("li", class_="ProfileNav-item ProfileNav-item--tweets is-active").find("span", class_="ProfileNav-value").text
        following1 = soup.find("div", class_="ProfileCanopy-nav").find("ul", class_="ProfileNav-list").find("li", class_="ProfileNav-item ProfileNav-item--following").find("span", class_="ProfileNav-value").text
        followers1 = soup.find("div", class_="ProfileCanopy-nav").find("ul", class_="ProfileNav-list").find("li", class_="ProfileNav-item ProfileNav-item--followers").find("span", class_="ProfileNav-value").text
        likes1 = soup.find("div", class_="ProfileCanopy-nav").find("ul", class_="ProfileNav-list").find("li", class_="ProfileNav-item ProfileNav-item--favorites").find("span", class_="ProfileNav-value").text
    else:
        #Κάνει την ίδια διαδικασία που περιγράφεται παραπάνω
        Base_URL="https://twitter.com/"+secondacc
        r = requests.get(Base_URL)
        soup = BeautifulSoup(r.content, "lxml")
        twetts2 = soup.find("div", class_="ProfileCanopy-nav").find("ul", class_="ProfileNav-list").find("li", class_="ProfileNav-item ProfileNav-item--tweets is-active").find("span", class_="ProfileNav-value").text
        following2 = soup.find("div", class_="ProfileCanopy-nav").find("ul", class_="ProfileNav-list").find("li", class_="ProfileNav-item ProfileNav-item--following").find("span", class_="ProfileNav-value").text
        followers2 = soup.find("div", class_="ProfileCanopy-nav").find("ul", class_="ProfileNav-list").find("li", class_="ProfileNav-item ProfileNav-item--followers").find("span", class_="ProfileNav-value").text
        likes2 = soup.find("div", class_="ProfileCanopy-nav").find("ul", class_="ProfileNav-list").find("li", class_="ProfileNav-item ProfileNav-item--favorites").find("span", class_="ProfileNav-value").text

#Βρίσκει αν ο αριθμός περιέχει στο τέλος του Κ ή Μ (χιλίαδες ή εκατομμύρια αντίστοιχα)
tw1=0
tw2=0
fl1=0
fl2=0
lks1=0
lks2=0
if twetts1[-1] =="K":
    ts1=float(twetts1[:-1])*1000
    tw1=int(ts1)
if twetts1[-1] =="M":
    ts1=float(twetts1[:-1])*1000000
    tw1=int(ts1)
if twetts2[-1] =="K":
    ts2=float(twetts2[:-1])*1000
    tw2=int(ts2)
if twetts2[-1] =="M":
    ts2=float(twetts2[:-1])*1000000
    tw2=int(ts2)
if followers1[-1] =="K":
    fs1=float(followers1[:-1])*1000
    fl1=int(fs1)
if followers1[-1] =="M":
    fs1=float(followers1[:-1])*1000000
    fl1=int(fs1)
if followers2[-1] =="K":
    fs2=float(followers2[:-1])*1000
    fl2=int(fs2)
if followers2[-1] =="M":
    fs2=float(followers2[:-1])*1000000
    fl2=int(fs2)
if likes1[-1] =="K":
    ls1=float(likes1[:-1])*1000
    lks1=int(ls1)
if likes1[-1] =="M":
    ls1=float(likes1[:-1])*1000000
    lks1=int(ls1)
if likes2[-1] =="K":
    ls2=float(likes2[:-1])*1000
    lks2=int(ls2)
if likes2[-1] =="M":
    ls2=float(likes2[:-1])*1000000
    lks2=int(ls2)


score1 = 0
score2 = 0
#Συγκρίνει τα twetts του ενός προφίλ με τα twetts του άλλου και αντίστοιχα αυξάνει το σκορ
if (tw1!=0 and tw2!=0):
    if tw1 > tw2:
        score1 = score1+1
    elif tw1 < tw2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0
elif (tw1==0 and  tw2!=0):
    if twetts1 > tw2:
        score1 = score1+1
    elif twetts1 < tw2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0
elif (tw1!=0 and tw2==0):
    if tw1 > twetts2:
        score1 = score1+1
    elif tw1 < twetts2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0
elif (tw1==0 and tw2==0):
    if twetts1 > twetts2:
        score1 = score1+1
    elif twetts1 < twetts2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0

#Συγκρίνει τα following του ενός προφίλ με τα following του άλλου και αντίστοιχα αυξάνει το σκορ
if following1 > following2:
    score1 = score1+1
elif following1 < following2:
    score2 = score2+1
else:
    score1 = score1+0
    score2 = score2+0

#Συγκρίνει τα followers του ενός προφίλ με τα followers του άλλου και αντίστοιχα αυξάνει το σκορ
if (fl1!=0 and fl2!=0):
    if fl1 >fl2:
        score1 = score1+1
    elif fl1 < fl2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0
elif (fl1==0 and fl2!=0):
    if followers1 >fl2:
        score1 = score1+1
    elif followers1 < fl2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0
elif (fl1!=0 and fl2==0):
    if fl1 >followers2:
        score1 = score1+1
    elif fl1 < followers2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0
elif (fl1==0 and fl2==0):
    if followers1 >followers2:
        score1 = score1+1
    elif followers1 < followers2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0

#Συγκρίνει τα likes του ενός προφίλ με τα likes του άλλου και αντίστοιχα αυξάνει το σκορ
if (lks1!=0 and lks2!=0):
    if lks1 > lks2:
        score1 = score1+1
    elif lks1 < lks2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0
elif (lks1==0 and lks2!=0):
    if likes1 > lks2:
        score1 = score1+1
    elif likes1 < lks2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0
elif (lks1!=0 and lks2==0):
    if lks1 > likes2:
        score1 = score1+1
    elif lks1 < likes2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0
elif (lks1==0 and lks2==0):
    if likes1 > likes2:
        score1 = score1+1
    elif likes1 < likes2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0


#Εμφανίζει το τελικό σκορ μεταξύ των δύο προφίλ
print "Score",score1 ,"-", score2
