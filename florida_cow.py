import random
import re
import ssl
import sys
import urllib.request
from datetime import datetime

import cowsay


def google(day, month, gender):
    ssl._create_default_https_context = ssl._create_unverified_context
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-Agent", "MyApp/1.0")]
    urllib.request.install_opener(opener)
    page = urllib.request.urlopen(
        "https://www.google.com/search?&q="
        + str(day)
        + "+"
        + month.lower()
        + "+florida+"
        + gender
    )
    return re.findall(
        r"florida " + gender + r"[^\<]+?\.\.\.", str(page.read()), re.IGNORECASE
    )


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 2:
        day, month = (args[1], args[2]) if args[1].isnumeric() else (args[2], args[1])
        gender = args[3] if len(args) > 3 else "man"
        lines = google(day, month, gender)
        if len(lines) > 0:
            cowsay.cow(month.capitalize() + " " + day + ": " + random.choice(lines))
        else:
            cowsay.cow(
                "It was quiet in Florida on " + month.capitalize() + " " + day + "."
            )
    else:
        print(
            "Enter a date and optionally a gender, e.g. `python florida_cow.py "
            + datetime.today().strftime("%B %d").lower()
            + " woman`!"
        )
