# -*- coding: utf-8 -*-
import urllib, json
#Εισάγει ο χρήστης μια ημερομηνία με την μορφή dd-mm-yyyy
date1 = raw_input("Insert a date in form dd-mm-yyyy:")
url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/ %s.json" %(date1)
#Σύνδεση με την ιστοσελίδα του οπαπ
response = urllib.urlopen(url)
#Μετατροπή των δεδομένων σε μορφή json
data = json.loads(response.read())
#Παίρνει μόνο τις λίστες με τους αριθμούς και συγκεκριμένα
#την πρώτη από όλες προκειμένου να τις ενώσει όλες μαζί
c1=(data["draws"]["draw"][0]["results"])
#Ένωση όλων των λιστών σε μία
for i in range(1,157):
    c1=c1+(data["draws"]["draw"][i]["results"])
#Μετράει πόσες φορές εμφανίζεται ο κάθε αριθμός μέσα στην λίστα και
#παράλληλα εκτυπώνει με την μορφή αριθμός:πλήθος εμφανίσεων
for j in range(1,81):
    print j ,":", c1.count (j)
