def check_exact(placename, match_list):
    """Find Geonames entries that have an exact match place name.

    When multiple hits come back for a query, this looks to see if any of them have
    an exact place name match in the `alternative_names` field. If only one does,
    it returns that one. Otherwise it returns None.
    """
    exact_matches = []
    for m in match_list:
        all_names = m['alternativenames']
        all_names.append(m['name'])
        if placename in all_names:
            exact_matches.append(m)
    if len(exact_matches) == 1:
        return exact_matches[0]
    else:
        None

def check_editdist(placename, matchlist, threshold=2):
    """
    If an 
    
    Returns
    ---------
    tuple, the edit distance and the actual match
    """
    min_dists = []
    avg_dists = []
    for m in matchlist:
        all_names = m['alternativenames'] 
        all_names.extend([m['asciiname'], m['name']])

        ds = [editdistance.eval(placename, i)  for i in all_names]
        min_dists.append(np.min(ds))
        avg_dists.append(np.mean(ds))

    if np.sum([i <= threshold for i in min_dists]) == 1:
        dist = round(np.min(min_dists), 2)
        m = matchlist[np.argmin(min_dists)]
        reason = "CAUTION: Single edit distance match." 
        info = "One entry of {0} within minimum edit distance of {1}".format(len(matchlist), dist)
        return m, reason, info
    elif np.sum([i <= threshold for i in min_dists]) > 1:
        dist = round(np.min(min_dists), 2)
        m = matchlist[np.argmin(avg_dists)]
        reason = "CAUTION: Best of several edit distance matches."
        info = "{0} entries within minimum edit distance. Picking closest average distance: {1}.".format(len(matchlist), round(np.min(avg_dists), 2))
        return m, reason, info
    else:
        return None, None, None
                                                                    


def lookup_city(city, country="SYR", adm1=None):
    """
    Return the "best" Geonames entry for a city name.

    Queries the ES-Geonames gazetteer for the the given city, province, and Syria,
    and uses a set of  rules to determine the best result to return. If adm1 is supplied,
    only results from that governorate will be returned. 
    
    This code was modified from Halterman's (2019) Syria casualties working paper.

    Parameters
    ----------
    placename: str
      The name of the city to look up
    country: str
      The three character country code (iso3c)
    adm1: str
      (Optional) the name of the state/governorate/province

    Returns
    -------
    match: dict or list
      The single entry from Geonames that best matches the query, or [] if no match at all.
    """
    adm_limit = None
    if adm1:
        adm_res = geo.query_geonames_country(placename=adm1, 
                                             country=country,
                                             filter_params={"feature_code": "ADM1"})
        adm_res = adm_res['hits']['hits']
        if len(adm_res) == 1:
            adm1 = adm_res[0]['admin1_code']
            adm_limit = {"admin1_code" : adm1}
    res = geo.query_geonames_country(city, country, adm_limit)
    res = res['hits']['hits']
    #print(res)
    if re.search("[Uu]niversity|[Gg]overnorate", city):
        if len(res) == 1:
            reason = "Single fuzzy match for university/governorate."
            info = "{0} total results of all types".format(len(res))
            return {"geo" : res[0],
                    "query" : city,
                    "info" : info,
                    "reason" : reason}
    
    # look for a city first
    match = [i for i in res if i['feature_code'] in ['PPL', 'PPLA', 'PPLC', 'PPLA2', 'PPLA3', 'PPLA3']]
    if match:
        if len(match) == 1:
            return {"geo" : match[0],
                    "query" : city,
                    "info" : "{0} total results of all types".format(len(res)),
                    "reason" : "Single elasticsearch match for city."}
        # if there's more than one match:
        m = check_exact(city, match)
        if m:
            return {"geo" : m,
                    "query" : city,
                        "info": "{0} elasticsearch matches for cities out of {1} total results of all types".format(len(match), len(res)),
                    "reason" : "Exact name match for city."}
        # check the editdistance
        m, reason, info = check_editdist(city, match)
        if m:
            return {"geo" : m,
                    "query" : city,
                    "info": info,
                    "reason" : reason}
            
    # if there's no city match, look for a neighborhood
    match = [i for i in res if i['feature_code'] in ['PPLX', 'LCTY', 'PPLL', 'AREA']]
    if match:
        #print("neighborhood")
        # if there's just a single match, we're done
        if len(match) == 1:
            reason = "Single elasticsearch match for neighborhood."
            info = "{0} total results of all types".format(len(res))
            return {"geo" : match[0],
                "query" : city,
                    "info" : info,
                "reason" : reason}
        # if there are multiple matches, look for exact matches
        else:
            m = check_exact(city, match)
            if m:
                reason = "Exact place name match for neighborhood." 
                info = "{0} elasticsearch matches out of {1} total results of all types".format(len(match), len(res))
                return {"geo" : m,
                        "query" : city,
                        "info" : info,
                        "reason" : reason}
            
                
            m, reason, info = check_editdist(city, match)
            if m:
                return {"geo" : m,
                    "query" : city,
                    "info": info,
                    "reason" : reason}

    #print(res)
    if len(res) == 1:
        reason = "CAUTION: One fuzzy match, not a city-type location."
        return {"geo" : res[0],
                "query" : city,
                "reason" : reason,
                "info" :  "{0} total results of all types.".format(len(res))}
    
    
    
    if len(res) == 0:
        reason = "FAILURE: No fuzzy match for city or neighborhood."
    else:
        reason = "FAILURE: Too many matches for city or neighborhood, none exact."
    return {"geo" : None,
                "query" : city,
                "reason" : reason,
                "info" :  "{0} total results of all types.".format(len(res))}


#lookup_city("Bstn al Qsr")
#lookup_city("Hama")
lookup_city("Rukn al-Din")
