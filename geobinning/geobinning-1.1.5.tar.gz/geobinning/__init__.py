# __init__.py

# Version of the realpython-reader package
def geobin(geojson,points,property_id):
    import matplotlib.path as mpltPath
    import numpy as np
    import pandas as pd
    pset = property_id.split()

    id = [];bins = []
    for i,feature in enumerate(geojson['features']):
        coords = feature['geometry']['coordinates'][0]
        if (len(coords)>2):
            path = mpltPath.Path(coords)
            inside = path.contains_points(points)
            cnt = np.count_nonzero(inside)
            if len(pset)==2:
                id.append(feature[pset[0]][pset[1]])
            elif len(pset)==1:
                id.append(feature[pset[0]])
            else:
                pass;
            bins.append(cnt)
    return pd.DataFrame(list(zip(id, bins)),columns=[property_id,'bins'])

def randomPoints(geojson,NumPoints):
    return 'poop'

def mergeGeometries(geojson,NumPoints):
    # Merge the set of geometries into a single ID to allow for combined binning and display.  Either you can generate a totally new (merged) set or just
    # make an new property
    return 'poop'
