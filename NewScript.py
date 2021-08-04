#
# Copyright 2021
#
# Written by Azura4k
# www.github.com/Azura4k
# Version 2.0
# Import csv json, and post library
from requests.structures import CaseInsensitiveDict
import csv
import glob
import os
import json

# Class for holding data collected into one unit


class Mp3Data:
    def __init__(self):
        self.Key = str()
        self.HttpStatus = int()
        self.downloadSize = int()
        self.requestorIP = str()


def main():
    # Put filename and location here.
    PresentCSVs = glob.glob(r"*.csv")
    for index in range(0, len(PresentCSVs)):
        DataLocation = PresentCSVs[index].replace("[", "")
        DataLocation = PresentCSVs[index].replace("]", "")
        # Load all relevent data into list
        Mp3Stats = []

        # This will parse through and load all relevent data into class, then into lists.
        with open(DataLocation, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Parses only for mp3s, Once it ends, load information into class, and then load class into the List for later parsing
                if str(row['key']).endswith('.mp3'):
                    # Load data into class
                    Data = Mp3Data()
                    Data.Key = str(row['key'])
                    Data.HttpStatus = int(row['httpstatus'])

                    # To prevent error from adaptation
                    # Test and see if bytes equal nothing, if so, set equal to zero for no server confusion :)
                    if row['bytessent'] == "":
                        Data.downloadSize = 0
                    else:
                        Data.downloadSize = int(row['bytessent'])
                    Data.requestorIP = str(row['requester'])

                    # Insert into list Key, Increment count (For later), HTTP Status, Bytesent, and Bytes over 10,000
                    Mp3Stats.append([Data.Key, Data.HttpStatus,
                                    Data.downloadSize, Data.requestorIP])

        # Packaging and API Sendout
        # Output Final Stats to JSON Text
        json_text = json.dumps(Mp3Stats)
        import requests
        url = "http://example.com"
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "binder 33234321"
        headers["Content-Type"] = "application/json"
        resp = requests.post(url, headers=headers, data=json_text)

        # Delete File
        os.remove(DataLocation)
        print(resp.status_code)


# Calling Main
main()
