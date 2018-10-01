# ARGOSQueryTool.py
#
# Description: Parses a line of ARGOS tracking data 
#
# Created by: John Fay (john.fay@duke.edu)
# Created on: Sept, 2018

# Create a variable pointing to the file with no header
fileName = "SaraNoHeader.txt"

# Open the file as a read-only file object
fileObj = open(fileName, 'r')

# Read in all lines in the text file into a list variable
lineStrings = fileObj.readlines()
print("There are {} records in this file".format(len(lineStrings))) 

# Close the file
fileObj.close()

# Create empty dictionaries
dateDict = {}
locationDict = {}
try:
    # Loop with for loop

    for lineString in lineStrings:

        # Use the split command to parse the items in lineString into a list object
        lineData = lineString.split("\t")

        # Assign variables to specfic items in the list
        recordID = lineData[0]              # ARGOS tracking record ID
        obsDateTime = lineData[2]           # Observation date and time (combined)
        obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
        obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
        obsLC = lineData[3]                 # Observation Location Class
        obsLat = lineData[5]                # Observation Latitude
        obsLon = lineData[6]                # Observation Longitude

        # Filter out bad data
        if obsLC in ('1', '2', '3'):

            # Adds values to dictionaries
            dateDict[recordID] = obsDate
            locationDict[recordID] = (obsLon,obsLat)

    print("Finished")

    # Ask for a date
    userDate = input("Enter a date M/D/YYYY:")

    # Check the date
    if not "/" in userDate:
        print("Wrong format")

    # Create empty key list
    keyList=[]

    # Loop through the date dictionary
    for k, v in dateDict.items():
        # See if the date (the value) matches the user date
        if v == userDate:
            keyList.append(k)

    for key in keyList:
        print(locationDict[key])

except Exception as e:
    print(e)