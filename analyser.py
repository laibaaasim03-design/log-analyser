# print("Hello, log analyser!")
with open("/workspaces/log-analyser/data/OpenSSH_2k.log") as file:
    lines = file.readlines()

# for Pas in lines:
#     if "Failed password" in Pas:
#         print(Pas)

# count = 0

# for Pas in lines:
#     if "Failed password" in Pas:
#         count = count + 1

# print(count)

import re

ip = re.findall(r"\d+\.\d+\.\d+\.\d+", lines[5])

ips = []

for Pas in lines:
    if "Failed password" in Pas:
        found = re.findall(r"\d+\.\d+\.\d+\.\d+", Pas)
        ips.append(found[0])

print(len(ips))
print(ips[0])