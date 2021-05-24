from geopy.distance import distance

import ggps
import h3

print('Start')

infile = 'input/39970665555.tcx'
handler = ggps.TcxHandler()
handler.parse(infile)
trackpoints = handler.trackpoints
print(len(trackpoints))

prevPoint = (float(trackpoints[0].get("latitudedegrees")), float(trackpoints[0].get("longitudedegrees")))
prevCumMeters = float(trackpoints[0].get('distancemeters'))

for t in trackpoints[6:]:
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
