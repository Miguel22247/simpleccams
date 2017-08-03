import requests
from squawklist import squawklist

url = 'https://api.ivao.aero/getdata/whazzup/whazzup.txt'

assigned_squawk = dict()
online = dict()

def download_whazzup():
    """ Downloads whazzup file from IVAO and returns it as a string """

    whazzup = requests.get(url)

    return whazzup.text

def parse_whazzup(data):
    """ Takes a string of whazzup data and parses it to create a dictionary
    containing the callsign and its squawk code """

    output = dict()
    for line in data.splitlines():
        if 'PILOT' in line:
            line = line.split(':')
            output[line[0]] = line[17]

    return output

def used_squawks(data):
    """ Creates a list of squawks currently in use """

    data = list(set(data.values()))

    return data

def assign_squawk(callsign):
    """ Assigns a unique squawk code """
    online = parse_whazzup(download_whazzup())
    for squawk in squawklist:
        if squawk not in assigned_squawk.values():
            if squawk not in used_squawks(online):
                assigned_squawk[callsign] = squawk
                break

if __name__ == '__main__':
    main()
