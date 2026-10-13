# log-analyser

## Tool and its features
What is this tool and what does it do?
This is an SSH server log which helps in finding failed login attempts & which IP addresses has been attacked the most. It's similar to brute-force attack, the same IP failing again & again, and saves the results to three different places; database, CSV file & an HTML report. 

## How it works
Reads the log which have 2k lines, 
Finds the lines which say "Failed password",
Extract IPs from each failed password line using a regex, 
Count the failed logins for each IP, 
Flags those IPs which has too many number of failures(highest 286)
Stores the IPs in a SQLite database and uses SQL to find the top attackers, 
Writes the results to a CSV & HTML file with CSS styling done.

## Tools used
Python 3 (re, sqlite3, csv, collections), 
SQL (SQLite), 
HTML & CSS
Git/Github & Github Codespaces
Data was the OpenSSH sample log from the Loghub dataset.

## Results
What did you find? Which IP attacked the most, and how many times?
The sample log has 520 "Failed password" lines. The top attacker was 183.62.140.253 with 286 failed logins (about 55%), then 187.141.143.180 (80) and 103.99.0.122 (46). The top 5 IPs made about 88% of all failed logins, which points to automated bots.

## How to run it
What command do you type?
Put the log file in `data/`, then ran:
                `python analyser.py`
This creates `logins.db`, `report.csv` and `report.html`. To view the report in a browser, ran `python -m http.server 8000` and opened `report.html`.
No extra installs were needed.

- **FileNotFoundError:** I typed `OpenSSH_2K.log` with a capital K, but the file name has a lowercase k. File names are case-sensitive.
- **Search found nothing:** I searched for "Failed Password" but the log says "Failed password". String matching is case-sensitive too.
- **Counting the wrong list:** `Counter(lines)` gave every line a count of 1, because I needed to count the extracted IPs. I also mixed up the loop names `ips` and `ip`, which gave the wrong output.
- **Indentation error in the HTML report:** the `for` line was outside the `with open(...)` block, so Python closed the file early and gave "I/O operation on closed file".

## Known limitation
The log sometimes writes "message repeated 5 times" instead of 5 separate lines, so my counts are a bit lower than the real number of failures.

## Ethical note
I only analysed a public sample log dataset. Nothing here is meant for attacking real systems.
