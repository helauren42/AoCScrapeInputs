import requests
import sys
import os
import subprocess
from bs4 import BeautifulSoup

URL = "https://adventofcode.com/"
YEAR = sys.argv[1]
cwd = os.path.curdir
PROJECT_DIR = f"{cwd}/{YEAR}/"

os.system(f"mkdir -p {YEAR}")

def getCookie():
    with open("secrets.txt", "r") as file:
        return file.read()

ID = getCookie().strip()
COOKIE = {"session": ID}

for i in range(1, 26):
    subprocess.run([f"mkdir -p Day{i}"], shell=True, cwd=PROJECT_DIR)
    subprocess.run(["touch script.py main.cpp subject.txt input.txt"], shell=True, cwd=f"{PROJECT_DIR}Day{i}")
    subprocess.run(["if [ ! -s main.cpp ]; then cat ../../draft.cpp > main.cpp; fi "], shell=True, cwd=f"{PROJECT_DIR}Day{i}")
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
