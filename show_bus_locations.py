# Importing python libraries
import sys
import json
import urllib2

if __name__ == '__main__':

    # Calling BUS MTA API using Key and Bus Number Inputs
    url = 'http://api.prod.obanyc.com/api/siri/\
vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&\
LineRef=%s' % (sys.argv[1], sys.argv[2])

    request = urllib2.urlopen(url)
    busData = json.load(request)

    # Parsing through lists and dictionaries in the input json file
    try:
        vehicleMonitoring = (
            busData['Siri']['ServiceDelivery']
            ['VehicleMonitoringDelivery'][0]['VehicleActivity'])
    except KeyError:
        print "Error: No such route"
        sys.exit()

    # Printing the Bus Line and # Active Buses output
    print "Bus Line is: %s" % sys.argv[2]
    print "Number of Active Buses: %d" % len(vehicleMonitoring)

    # Creating an empty list to store active buses location attributes
    busLoc = []

    for bus in vehicleMonitoring:
        for key in bus:
            if "MonitoredVehicleJourney" in key:
                busLoc.append(bus[key]['VehicleLocation'])

    # Printing the output of Bus Location list object through iterations
    for i in range(len(busLoc)):
        busLat = busLoc[i]['Latitude']
        busLon = busLoc[i]['Longitude']
        print(
            'Bus %d is at latitude %s and longitude %s' %
            (i, busLat, busLon))
