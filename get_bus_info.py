# Importing python libraries
import sys
import json
import urllib2
import csv

if __name__ == '__main__':

    # # Calling BUS MTA API using Key and Bus Number Inputs
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
    print "Bus Line is:  %s" % sys.argv[2]
    print "Number of Active Buses: %d" % len(vehicleMonitoring)

    # Extracting bus and stop location attributes into external csv file
    with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
        writer.writerow(headers)

        for bus in vehicleMonitoring:
            for key in bus:
                if "MonitoredVehicleJourney" in key:
                    busLat = bus[key]['VehicleLocation']['Latitude']
                    busLon = bus[key]['VehicleLocation']['Longitude']
                    try:
                        stopName = bus[key]['MonitoredCall']['StopPointName']
                        stopStatus = (
                            bus[key]['MonitoredCall']['Extensions']
                            ['Distances']['PresentableDistance'])
                    except:
                        stopName = "N/A"
                        stopStatus = "N/A"

                    writer.writerow([busLat, busLon, stopName, stopStatus])
