#!//Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import os

os.environ["FAV_SPORT"] = input("What is your favorite sport? ")
os.environ["FAV_TEAM"] = input("What is your favorite team? ")
os.environ["FAV_PLAYER"] = input("Who is your favorite player? ")

print(os.getenv("FAV_SPORT"))
print(os.getenv("FAV_TEAM"))
print(os.getenv("FAV_PLAYER"))