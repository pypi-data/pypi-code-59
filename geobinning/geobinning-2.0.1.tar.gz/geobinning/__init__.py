def geobin(polygons,points):
    import matplotlib.path as mpltPath
    import numpy as np
    import pandas as pd

    bins = []
    for poly in polygons:
        if (len(poly)>2):
            path = mpltPath.Path(poly)
            inside = path.contains_points(points)
            cnt = np.count_nonzero(inside)
            bins.append(cnt)
    return bins
