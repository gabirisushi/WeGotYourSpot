# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:10:42 2020

@author: udopa
"""


import requests
import datetime
import random
# api-endpoint
URL = "http://localhost:9000/"

# r1 = requests.get(url=URL)

# r = requests.get(url=URL + '/api/v1/resources/books?id=2')
#

# %Create Profile


def createProfile(name, pw="pass1"):
    req = requests.post(url=URL+'create_profile',
                        headers={"Content-Type": "application/json"},
                        json={"name": name, "password": pw})
    print(req.content)


# %List Profiles
def listProfiles():
    req = requests.get(url=URL+'list_profiles')
    print(req.content)


# %Login
def login(name, pw="pass1"):
    req = requests.post(url=URL+'login',
                        headers={"Content-Type": "application/json"},
                        json={"name": name, "password": pw})
    print(req.content)


# % Update Profile
def configureProfile(name, user_data):
    req = requests.post(url=URL+'configure_profile',
                        headers={"Content-Type": "application/json"},
                        json={"name": name,
                              "update_data": user_data
                              }
                        )
    print(req.content)


# % Search
def search(name, tStart, tEnd):
    req = requests.post(
        url=URL+'search', headers={"Content-Type": "application/json"},
        json={"name": name,
              "from": tStart,
              "to": tEnd
              })
    print(req.content)
    return req.content


# %
def book(name, parking_slot, tStart, tEnd):
    req = requests.post(
        url=URL+'book', headers={"Content-Type": "application/json"},
        json={"name": name,
              "parking_slot": parking_slot,
              "from": tStart,
              "to": tEnd
              })
    print(req.content)


def listBookings(name):
    req = requests.post(
        url=URL+'listBookings', headers={"Content-Type": "application/json"},
        json={"name": name
              })
    print(req.content)


def book_randomly(username):
    def random_date(start, end):
        """
        This function will return a random datetime between two datetimes.
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        return start + datetime.timedelta(seconds=random_second)

    tStartRANDOM = datetime.datetime(2020, 2, 20, 1, 0)
    tEndRANDOM = datetime.datetime(2020, 2, 23, 23, 0)
    MAX_NUMBER_BOOKINGS = 5
    for _ in range(random.randint(0, MAX_NUMBER_BOOKINGS)):
        tRand = random_date(tStartRANDOM, tEndRANDOM)

        parking_slot = "parking{}_{}{}".format(
            random.randint(0, 10),
            "ABCDEFGHIJK"[random.randint(0, 8)],
            random.randint(0, 10))
        book(username, parking_slot, tRand.strftime("%d:%m:%Y %H:%M"),
             (tRand + datetime.timedelta(hours=2)).strftime("%d:%m:%Y %H:%M"))

# %% MAIN


if __name__ == "__main__":

    parking_slot = "parking0_F1"
    tStart = "18:02:2020 10:30"
    tEnd = "18:02:2020 11:30"

    # tStart = "2020-02-18 11:30:00"
    # tEnd = "2020-02-18 13:30:00"

    for i in range(10):
        username = "max.mustermann+{:02}@bosch.io".format(i)
        PASSWORD = "BoschIO"
        profile_data = {
            "payment": {"id": "604622304587956804", "auth": "5264"},
            "license_plate": ["B-IO2019"],
            "type": {
                "women": True,
                "handicap": False,
                "pregnant": False,
                "family": False,
                "luggage": True,
                "truck": False}
            }

        createProfile(username, PASSWORD)
        login(username, PASSWORD)
        configureProfile(username, profile_data)
        book_randomly(username)

    data = search(username, tStart, tEnd)
    book(username, parking_slot, tStart, tEnd)
    listBookings(username)


# %%

