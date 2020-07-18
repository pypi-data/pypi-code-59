def image_url(url):
    from requests import get

    response = get("https://images.google.com/searchbyimage", params={
        "image_url": url
    })

    response.raise_for_status()
    return response.headers.get("Location")
