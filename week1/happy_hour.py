#!/bin/python3

import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samuel L. Jackson",
          "Leonardo"]

random_bar = random.choice(bars)
random_person = random.choice(people)
random_person2 = random.choice(people)

while random_person == random_person2:
    random_person2 = random.choice(people)

print(f"How about you go to {random_bar} with {random_person} and {random_person2}")
