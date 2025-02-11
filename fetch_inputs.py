import requests
import sys
import os
import subprocess
from bs4 import BeautifulSoup

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
    subprocess.run([f"mkdir -p Day{i}"], shell=True, cwd=PROJECT_DIR)
    subprocess.run(["touch script.py subject.txt input.txt"], shell=True, cwd=f"{PROJECT_DIR}Day{i}")

    # fetching subjects
    response = requests.get(f"{URL}{YEAR}/day/{i}", cookies=COOKIE)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text()
    start = text.find("--- Day ")
    end = text.find("To begin, get your puzzle input.")
    with open(f"{PROJECT_DIR}Day{i}/subject.txt", "w") as file:
        file.write(text)

    # fetching input texts
    response = requests.get(f"{URL}{YEAR}/day/{i}/input", cookies=COOKIE)
    text = response.content.decode('utf-8')
    with open(f"{PROJECT_DIR}Day{i}/input.txt", "w") as file:
        file.write(text)
