import json
import requests
import redis
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class Link:
    """ Link metadata  """

    status: int
    fullLink: Optional[str] = None
    date: Optional[str] = None
    shortLink: Optional[str] = None
    title: Optional[str] = None


try:
    conn = redis.Redis(host="localhost", port=6379, db=0)
    conn.acl_whoami()
except redis.ConnectionError as exc:
    raise Exception(f"Error connecting to Redis server: {exc}")


def get_link(link: str, key: str = "8c20a834fa0982f435f85d937a9628da47e8f"):
    """ Getting new (short) link """

    """
	link -- original link (http://example.com.com)
	key -- API service key from cutt.ly. By default, my key is used to generate links, 
	       this method is not very reliable in terms of performance, 
	       but if my key is disabled, I will try to quickly replace it (again, you can use your key) 
	
	"""
    try:
        response = requests.get(
            "https://cutt.ly/api/api.php?key=" + key + "&short=" + link + ""
        )
        seq = json.loads(response.text)
        shortLink = seq["url"]["shortLink"]
        fullLink = seq["url"]["fullLink"]
    except:
        print("[-] An error occured while getting short link!")
    if seq["url"]["status"] == 7:
        result = Link(
            status=seq["url"]["status"],
            fullLink=seq["url"]["fullLink"],
            date=seq["url"]["date"],
            shortLink=seq["url"]["shortLink"],
            title=seq["url"]["title"],
        )
        print("[+] Link successfully formed!")
        print("[*] Your new link:\n" + shortLink + "")
        conn.set(shortLink, fullLink) # Adding link to redis (shortlink -- key)
        return result
    else:
        print(
            "[-] An error occured while getting short link. Error code: "
            + str(seq["url"]["status"])
            + ""
        )
        result = Link(status=seq["url"]["status"])
        return result




