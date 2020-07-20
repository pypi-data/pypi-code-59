import os
import pickle
import time
import urllib.parse
import requests

from .auth import SnooNotesAuth
from .errors import RequestFailedError

class SnooNotes(SnooNotesAuth):
    def __init__(self, username, user_key):
        super().__init__(username, user_key)
        # Create a cache directory
        if not os.path.exists("./caches"):
            os.mkdir("./caches/")

    def _endpoint_url(self, endpoint):
        """Internal helper function to generate url from an endpoint"""
        return urllib.parse.urljoin(self.base_url, endpoint)

    def _authed_request(self, request_type, endpoint, data=None):
        """Internal helper function that performs the request after authenticating as the user"""
        try:
            if self.access_token is not None:
                pass
        except AttributeError:
            # Missing the token in the auth class, grab a new token.
            self.get_access_token()
        
        # Optionally refresh_access_tokens.
        # Should return without refresh in case of a valid token (<3600s of last access)
        self.refresh_access_token()

        if request_type == "POST" and data is None:
            print("No data provided for POST")
            return

        if request_type == "POST":
            r = requests.post(url=self._endpoint_url(endpoint), headers={
                "Authorization": f"{self.token_type} {self.access_token}"
            }, json=data)
            if r.ok:
                if r.content:
                    return r.json()
                else:
                    return
            else:
                raise RequestFailedError(f"{request_type} request returned a non-ok code: {r.status_code}")
        elif request_type == "GET":
            r = requests.get(url=self._endpoint_url(endpoint), headers={
                "Authorization": f"{self.token_type} {self.access_token}"
            })
            if r.ok:
                return r.json()
            else:
                raise RequestFailedError(f"{request_type} request returned a non-ok code: {r.status_code}")
        elif request_type == "DELETE":
            r = requests.delete(self._endpoint_url(endpoint), headers={
                "Authorization": f"{self.token_type} {self.access_token}"
            })
            if r.ok:
                return
            else:
                raise RequestFailedError(f"{request_type} request returned a non-ok code: {r.status_code}")

    def add_note_for_user(self, username, note_type, subreddit, message, url):
        """Add a Snoonote to the `username` under the specific `subreddit`.

        :param username: User to add note for
        :param note_type: ID that identifies a particular note type on a subreddit. `get_notes_for_subreddit` function
        :param subreddit: Subreddit under which the note should be added
        :param message: The content of the note
        :param url: The url to the reddit comment/post
        """
        self._authed_request("POST", "/api/note", data={
            "NoteTypeID": note_type,
            "SubName": subreddit,
            "Message": message, 
            "AppliesToUsername": username,
            "Url": url
        })
        pass

    def get_notes_for_user(self, usernames):
        """Returns a dict with the usernames passed and the Snoonotes they have.

        :param usernames: `String` or a list of `Strings` that represent the Reddit usernames to query for.
        """
        if isinstance(usernames, str):
            usernames = [usernames]
        return self._authed_request("POST", "/api/Note/GetNotes", data=usernames)

    def delete_note_for_user(self, username, note_id):
        """ Deletes a note given a `note_id` for a given `user`
        
        :param username: Username of the user to remove a note for
        :param note_id: id of the note to remove.
        """
        return self._authed_request("DELETE", f"/api/Note?id={note_id}")

    def get_notes_for_subreddit(self, subreddit, use_cache=True):
        """Return usernotes supported by a subreddit. Also caches the data for a day to prevent repeated calls to the API. Should therefore be very fast for repeated access.
   
        :param subreddit: Subreddit for which the notes are returned
        :param use_cache: Set to `False` to manually prevent cache use.
        """
        if use_cache:
            if os.path.exists(f"./caches/{subreddit}"):
                with open(f"./caches/{subreddit}", "rb") as sub_notes_cache:
                    cache = pickle.load(sub_notes_cache)
                if time.time() - int(cache.pop("LastCache")) > 86400:
                    print("Last cache older than a day. Not using cache.")
                    data = self._authed_request("GET", f"restapi/Subreddit/{subreddit}")[0]
                    data["LastCache"] = round(time.time())
                    with open(f"./caches/{subreddit}", "wb") as sub_notes_cache:
                        pickle.dump(data, sub_notes_cache)
                    del data["LastCache"]
                    return data
                else:
                    return cache
        data = self._authed_request("GET", f"restapi/Subreddit/{subreddit}")[0]
        data["LastCache"] = round(time.time())
        with open(f"./caches/{subreddit}", "wb") as sub_notes_cache:
            pickle.dump(data, sub_notes_cache)
        del data["LastCache"]
        return data
