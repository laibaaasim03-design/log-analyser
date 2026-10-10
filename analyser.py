print("Hello, log analyser!")
with open("/workspaces/log-analyser/data/OpenSSH_2k.log") as file:
    lines = file.readlines()

print(len(lines))
