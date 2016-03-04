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
if followers1[-1] =="K":
    fl1=float(followers1[:-1])*1000
    fs1=int(fl1)
if followers1[-1] =="M":
    fl1=float(followers1[:-1])*1000000
    fs1=int(fl1)
if followers2[-1] =="K":
    fl2=float(followers2[:-1])*1000
    fs2=int(fl2)
if followers2[-1] =="M":
    fl2=float(followers2[:-1])*1000000
    fs2=int(fl2)

score1 = 0
score2 = 0
#Συγκρίνει τα twetts του ενός προφίλ με τα twetts του άλλου και αντίστοιχα αυξάνει το σκορ
if (tw1!=0 and tw2!=0):
    if tw1 >tw2:
        score1 = score1+1
    elif tw1 < tw2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0
elif (tw1==0 and  tw2!=0):
    if twetts1 >tw2:
        score1 = score1+1
    elif twetts1 < tw2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0
elif (tw1!=0 and tw2==0):
    if tw1 >twetts2:
        score1 = score1+1
    elif tw1 < twetts2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0
elif (tw1==0 and tw2==0):
    if tweets1 > twetts2:
        score1 = score1+1
    elif tweets1 < twetts2:
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
if (fs1!=0 and fs2!=0):
    if fs1 >fs2:
        score1 = score1+1
    elif fs1 < fs2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0
elif (fs1==0 and fs2!=0):
    if followers1 >fs2:
        score1 = score1+1
    elif followers1 < fs2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0
elif (fs1!=0 and fs2==0):
    if fs1 >followers2:
        score1 = score1+1
    elif fs1 < followers2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0
elif (fs1==0 and fs2==0):
    if followers1 >followers2:
        score1 = score1+1
    elif followers1 < followers2:
        score2 = score2+1
    else:
        score1 = score1+0
        score2 = score2+0

#Συγκρίνει τα likes του ενός προφίλ με τα likes του άλλου και αντίστοιχα αυξάνει το σκορ
if likes1 > likes2:
   score1 = score1+1
elif likes1 < likes2:
    score2 = score2+1
else:
    score1 = score1+0
    score2 = score2+0

#Εμφανίζει το τελικό σκορ μεταξύ των δύο προφίλ
print "Score",score1 ,"-", score2
