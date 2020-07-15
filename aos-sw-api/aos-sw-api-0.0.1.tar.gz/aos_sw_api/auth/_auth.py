from typing import Union

import httpx

from aos_sw_api._validate import validate_201, validate_204


class Auth:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return AuthSync(session=session, **kwargs)
        elif isinstance(session, httpx.AsyncClient):
            return AuthAsync(session=session, **kwargs)


class BaseAuth:

    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient], username: str, password: str):
        self._session = session
        self._auth_base_url = "login-sessions"
        self._user_data = dict(userName=username, password=password)


class AuthSync(BaseAuth):

    def __init__(self, session: httpx.Client, username: str, password: str):
        super().__init__(session=session, username=username, password=password)

    def login(self, cookie: Union[str, None]) -> None:
        if cookie is not None:
            self._session.headers["cookie"] = cookie
        else:
            r = self._session.post(url=self._auth_base_url, json=self._user_data)
            validate_201(r)
            self._session.headers["cookie"] = r.json()['cookie']

    def logout(self) -> None:
        r = self._session.delete(self._auth_base_url)
        validate_204(r)


class AuthAsync(BaseAuth):

    def __init__(self, session: httpx.AsyncClient, username: str, password: str):
        super().__init__(session=session, username=username, password=password)

    async def login(self, cookie: Union[str, None]) -> None:
        if cookie is not None:
            self._session.headers["cookie"] = cookie
        else:
            r = await self._session.post(url=self._auth_base_url, json=self._user_data)
            validate_201(r)
            self._session.headers["cookie"] = r.json()['cookie']

    async def logout(self) -> None:
        r = await self._session.delete(self._auth_base_url)
        validate_204(r)
