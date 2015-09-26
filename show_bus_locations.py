import sys
import json
import urllib2

if __name__ == '__main__':
    url = 'http://api.prod.obanyc.com/api/siri/\
vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&\
LineRef=%s' % (sys.argv[1], sys.argv[2])

    request = urllib2.urlopen(url)
    busData = json.load(request)

    vehicleMonitoring = (
        busData['Siri']['ServiceDelivery']
        ['VehicleMonitoringDelivery'][0]['VehicleActivity'])

    print "Bus Line is:  %s" % sys.argv[2]
    print "Number of Active Buses: %d" % len(vehicleMonitoring)

    busLoc = []

    for bus in vehicleMonitoring:
        for key in bus:
            if "MonitoredVehicleJourney" in key:
                busLoc.append(bus[key]['VehicleLocation'])

    for i in range(len(busLoc)):
        busLat = busLoc[i]['Latitude']
        busLon = busLoc[i]['Longitude']
        print(
            'Bus %d is at latitude %s and longitude %s' %
            (i, busLat, busLon))
