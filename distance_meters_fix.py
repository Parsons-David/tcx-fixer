from geopy.distance import distance

import xml.etree.ElementTree as ET
import h3

print('Start')

tree = ET.parse('input/39970665555.tcx')
root = tree.getroot()
print(root)
activities = list(root)[0]
print(activities)
activity = list(activities)[0]
print(activity)
lap = list(activity)[1]
print(lap)
track = list(lap)[5]
print(track)
trackpoints = list(track)
print(trackpoints)


prevPoint = (float(trackpoints[0].get("Position").get("LatitudeDegrees")), float(trackpoints[0].get("Position").get("LongitudeDegrees")))
prevCumMeters = float(trackpoints[0].get('DistanceMeters'))

for t in trackpoints:
    currPoint = (float(t.get("latitudedegrees")), float(t.get("longitudedegrees")))
    currCumMeters = float(t.get('distancemeters'))

    print(f"Cumulative Distance - {t.get('distancemeters')}")

    if currCumMeters == '0.0' or currCumMeters < prevCumMeters:
        distanceBetweenPoints = h3.point_dist(prevPoint, currPoint, unit='m')
        print(f"Distance Between Points - {distanceBetweenPoints}")
        t.set('distancemeters', str(prevCumMeters + distanceBetweenPoints))
        print(t.get('time'))
        print(f"Cumulative Distance - {t.get('distancemeters')}")

    prevPoint = currPoint
    prevCumMeters = float(t.get('distancemeters'))

print(trackpoints[-1].get('distancemeters'))

print('Complete')
