#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
## EPITECH PROJECT, 2020
## WorshopHub
## File description:
## worker
##

import json
import os
import requests
import random
import sys

from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin

APP = Flask(__name__)
CORS(APP)

@APP.route('/getGithubJob', methods=["GET"])
@cross_origin()
def getGithubJob():
    try:
        departure = request.POST.get("Adresse", None).replace(" ", "%20")
        jsonDeparture = requests.get("https://api-adresse.data.gouv.fr/search/?q=" + departure + "&type=housenumber&autocomplete=1").json()
        cordinateDeparture = jsonDeparture["features"][0]["geometry"]["coordinates"]
        link = "https://www.openstreetmap.org/export/embed.html?bbox=" + str(cordinateDeparture[0]) + "%2C" + str(cordinateDeparture[1]) + \
            "%2C" + str(cordinateDeparture[0]) + "%2C" + str(cordinateDeparture[1]) + "&amp;layer=mapnik"
        return JsonResponse({"status" : "ok", "link" : link})
    except Exception as e:
        print(e)
        return {"status" : "ko"}

if __name__ == "__main__":

    try :
        APP.run(host="0.0.0.0", port=80, debug=True)
    except Exception as e:
        print(str(e))
        pass
