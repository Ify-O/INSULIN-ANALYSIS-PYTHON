import json
def readJsonFile(fileName):
    data=""
    try:  #try/except block to make this function more reliable
        with open('files/Insulin.json') as json_file:   #open returns a file handler to the files/insulin.json file.
            data = json.load(json_file)  #json.load reads the JSON file and returns the content as a Python dictionary.
    except IOError:
        print("Could not read file")
    return data
