# print("Hello, log analyser!")
# Opened the log file
with open("/workspaces/log-analyser/data/OpenSSH_2k.log") as file:
    lines = file.readlines()

# Check the lines in log file and check which lines have failed password in them
# for Pas in lines:
#     if "Failed password" in Pas:
#         print(Pas)

# Count the total number of failed password lines
# count = 0

# for Pas in lines:
#     if "Failed password" in Pas:
#         count = count + 1

# print(count)

#Find the IP addresses of those lines which have failed password in them and store it in "ips"
    import re

ip = re.findall(r"\d+\.\d+\.\d+\.\d+", lines[5])

ips = []

for Pas in lines:
    if "Failed password" in Pas:
        found = re.findall(r"\d+\.\d+\.\d+\.\d+", Pas)
        ips.append(found[0])

# print(len(ips))
# print(ips[0])

#Finding the biggest attacker by tally marks 
from collections import Counter
counts = Counter(ips)
# print(counts.most_common(5))

#Checking which IP has been attacked above a number of 20
# for ip, number in counts.items():
#     if number > 20:
#         print("ALERT:", ip, "had", number, "failed logins")

import sqlite3

#Creating the database and the table
conn = sqlite3.connect("logins.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS failed_logins (ip TEXT)")

#Clearing old rows so there aren't duplicates each time the code is run
cur.execute("DELETE FROM failed_logins")

#Saving every IP into the table
for ip in ips:
    cur.execute("INSERT INTO failed_logins (ip) VALUES (?)", (ip,))

conn.commit()

#Asking the database that which 6 IPs has failed the most?
cur.execute("SELECT ip, COUNT(*) FROM failed_logins GROUP BY ip ORDER BY COUNT(*) DESC LIMIT 6")
rows = cur.fetchall()
print(rows)

conn.close()