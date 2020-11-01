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
            jobs = requests.get("https://jobs.github.com/positions.json?description=python&full_time=true&").json()
            res = []
            i = 0

            for job in jobs:
                tmp = {}
                job["location"] = "Paris France"
                job["description"] = job["description"].replace("<a>", "")
                job["description"] = job["description"].replace("</a>", "")
                job["description"] = job["description"].replace("<p>", "")
                job["description"] = job["description"].replace("</p>", "")

                tmp["Company"] = job["company"]
                tmp["JobName"] = job["title"]
                tmp["JobDescription"] = job["description"] 
                tmp["location"] = "Paris France"
                tmp["Salary"] = "unknow"
                res.append(tmp)
                i += 1
                if (i > 50) : break
            return {"status" : "ok", "jobs" : res}
        except:
            return {"status" : "ko"}

if __name__ == "__main__":

    try :
        APP.run(host="0.0.0.0", port=80, debug=True)
    except Exception as e:
        print(str(e))
        pass
