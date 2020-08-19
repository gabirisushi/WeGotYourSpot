# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:33:49 2020

@author: udopa
"""

import random
import json
import numpy as np
import datetime


LETTERS = 'ABCDEFGHIJK'
MAX_NUMBER_LOTS = 10
MAX_NUMBER_SPOTS = 10

MAX_NUMBER_BOOKINGS = 30
MAX_COST = 50


def random_date(start, end):
    """
    This function will return a random datetime between two datetime objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


tStart = datetime.datetime(2020, 2, 20, 1, 0)
tEnd = datetime.datetime(2020, 2, 23, 23, 0)

# %%
num_lots = random.randint(1, MAX_NUMBER_LOTS)


for h in range(num_lots):
    location = random.uniform(-180, 180), random.uniform(-90, 90)
    data = []
    num_letters = random.randint(1, len(LETTERS))
    for i in range(num_letters):
        num_spots = random.randint(1, MAX_NUMBER_SPOTS)
        rand_booleans = [bool(x) for x in (np.random.randint(0, 2, size=(7),
                                                             dtype=bool))]
        for j in range(num_spots):
            bookings = []

            for _ in range(random.randint(0, MAX_NUMBER_BOOKINGS)):
                tRand = random_date(tStart, tEnd)
                bookings.append({
                    "from": str(tRand),
                    "to": str(tRand + datetime.timedelta(hours=2))})

            dat = {"name": LETTERS[i] + str(j),
                   'location': location,
                   "type": {
                           "women": rand_booleans[0],
                           "handicap": rand_booleans[1],
                           "pregnant": rand_booleans[2],
                           "family": rand_booleans[3],
                           "luggage": rand_booleans[4],
                           "truck": rand_booleans[5]},
                   "free": rand_booleans[6],
                   'bookings': bookings,
                   'cost': 1+sum(rand_booleans[:-1])*0.2  # charge 20c per attr
                   }

            data.append(dat)

    with open('mock_data/parking{}.json'.format(h), 'w') as json_file:
        json.dump(data, json_file)
