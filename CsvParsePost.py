#
# Copyright 2021
#
# Written by Azura4k
# www.github.com/Azura4k

# Import csv json, and post library
import csv
import json
# Put filename and location here.
DataLocation = 'data.csv'

# Class for holding data collected into one unit


class Mp3Data:
    def __init__(self):
        self.Key = str()
        self.HttpStatus = str()
        self.bytesent = str()
        self.BytesSentOver10000 = str()


def main():
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
                Data.HttpStatus = str(row['httpstatus'])
                Data.bytesent = str(row['bytessent'])
                # Test and see if bytes equal nothing, if so, set equal to zero for no server confusion :)
                if Data.bytesent == "":
                    Data.bytesent = "0"
                # Test if value amount of byte sent is longer then or equal to 5 (10,000). If so, set Bytes over 10,000 equal to 1
                if len(Data.bytesent) >= 5:
                    Data.BytesSentOver10000 = "Bytes Sent Over 10,000"
                # Insert into list Key, Increment count (For later), HTTP Status, Bytesent, and Bytes over 10,000
                Mp3Stats.append([Data.Key, 1, Data.HttpStatus,
                                Data.bytesent, Data.BytesSentOver10000])
    # This will parse through all the filtered data to ensure no duplicates
    # Sorts List in Alphebetical and numerical for alg to grab duplicates correctly
    Mp3Stats = sorted(Mp3Stats, key=lambda x: (x[0], x[1], x[2], x[3], x[4]))
    Mp3FinalStats = []
    # Counter for second list
    i2 = 0
    # Just so python wont give me an error
    Mp3FinalStats.append("Test")
    # Parse through data to calculate requests, only similar
    for i in range(0, len(Mp3Stats)):
        if Mp3Stats[i][0] == Mp3FinalStats[i2][0] and Mp3Stats[i][2] == Mp3FinalStats[i2][2] and Mp3Stats[i][3] == Mp3FinalStats[i2][3] and Mp3Stats[i][4] == Mp3FinalStats[i2][4]:
            # Adds to count per duplicate amount
            Mp3FinalStats[i2][1] += 1
        else:
            # Append the missing stat to the final list and add one to counter
            Mp3FinalStats.append(Mp3Stats[i])
            i2 += 1
    # Removes the "Test" placeholder
    Mp3FinalStats.remove("Test")

# For testing and debugging
#   for i in range(0, len(Mp3Stats)):
#        print(Mp3Stats[i])
#    print("Separate Data")
#    for i in range(0, len(Mp3FinalStats)):
#        print(Mp3FinalStats[i])

    # Output Final Stats to JSON Text
    json_text = json.dumps(Mp3FinalStats)
    print(json_text)

 # Calling Main
main()
