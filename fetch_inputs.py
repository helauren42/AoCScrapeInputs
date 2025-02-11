import requests
import sys
import os
import subprocess

URL = "https://adventofcode.com/"
YEAR = int(sys.argv[1])
PROJECT_DIR = f"{os.path.expanduser("~")}/Projects/AVC/{YEAR}/"

os.system(f"mkdir -p {str(YEAR)}")

def getCookie():
    with open("secrets.txt", "r") as file:
        return file.read()

ID = getCookie().strip()
COOKIE = {"session": ID}

for i in range(1, 26):
    response = requests.get(f"{URL}{YEAR}/day/{i}/input", cookies=COOKIE)
    print(f"{URL}{YEAR}/day/{i}/input")
    text = response.content.decode('utf-8')
    subprocess.run([f"mkdir -p Day{i}"], shell=True, cwd=PROJECT_DIR)
    subprocess.run(["touch script.py input.txt"], shell=True, cwd=f"{PROJECT_DIR}Day{i}")
    with open(f"{PROJECT_DIR}Day{i}/input.txt", "w") as file:
        file.write(text)
