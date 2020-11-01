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

@APP.route('/getGeoPos', methods=["GET"])
@cross_origin()
def getGeoPos():
    """
    ICI
    """

if __name__ == "__main__":

    try :
        APP.run(host="0.0.0.0", port=80, debug=True)
    except Exception as e:
        print(str(e))
        pass
