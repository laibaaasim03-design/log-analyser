print("Hello, log analyser!")
with open("/workspaces/log-analyser/data/OpenSSH_2k.log") as file:
    lines = file.readlines()

# for Pas in lines:
#     if "Failed password" in Pas:
#         print(Pas)

count = 0

for Pas in lines:
    if "Failed password" in Pas:
        count = count + 1

print(count)