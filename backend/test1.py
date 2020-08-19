# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:51:58 2020

@author: udopa
"""

from main import getParkingLotInfo, getValidParkingSpots
import datetime

search_parameter = {
                "women": True,
                "handicap": False,
                "pregnant": False,
                "family": False,
                "luggage": True,
                "truck": False}

tStart = "18:02:2020 10:30"
tEnd = "18:02:2020 11:30"

tStart = datetime.datetime.strptime("18:02:2020 10:30", "%d:%m:%Y %H:%M")
tEnd = datetime.datetime.strptime("18:02:2020 11:30", "%d:%m:%Y %H:%M")


parking_lot_data = getParkingLotInfo()
valid_parking_spots = getValidParkingSpots(parking_lot_data, 
                                           search_parameter,
                                           tStart,
                                           tEnd)


dictdata = valid_parking_spots.to_dict("index")

datalist = [value for value in dictdata.values()]
