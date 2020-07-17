def url_download(url: str, download_path: str, retry: int=3) -> bool:
    from urllib import request
    import time
    size = 1024 * 16
    try_time = 0
    while try_time < retry:
        try:
            r = request.urlopen(url, timeout=120)
            with open(download_path, 'wb') as f:
                while True:
                    chunk = r.read(size)
                    if not chunk:
                        f.flush()
                        break
                    f.write(chunk)
            return True
        except Exception as e:
            print(e)
            try_time += 1
            time.sleep(1)
    return False

