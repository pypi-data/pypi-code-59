import urllib.request
import logging
import os
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

log_file = os.path.join(os.path.normpath(os.path.expanduser('~/Documents/')), 'uraiko.log')

file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

err_instruction =  "Something is wrong, please check '" + str(log_file) + "'"
err_notice = "Please talk to the dev if you think this is a mistake."

def url_check(url):
    logger.info("Checking: " + str(url))
    header = "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'"
    try:
        if url[:4] != "http":
            logger.info("[!] No protocol specified.")
            url = "http://" + url
            logger.info("[+] Going with HTTP")
            logger.info("Checking: " + str(url))
        req = urllib.request.Request(url, headers={'User-Agent': header})
        u = urllib.request.urlopen(req)
        if url != u.geturl():
            logger.info("[!] " + url + " redirected to "+u.geturl())
            url = u.geturl()
            logger.info("Checking: " + str(url))
    except urllib.error.HTTPError as e:
        if e.code == 403:
            logger.error("Got 403! Website seems to be behind a WAF.")
    except urllib.error.URLError:
        if url[:5] == "https":
            logger.info("[!] Couldn't connect over HTTPS.")
            logger.info("[+] Trying with HTTP")
            url = "http://" + url[8:]
            logger.info("Checking: " + str(url))
            try:
                url_check(url)
            except urllib.error.URLError:
                logger.error("Couldn't open url, please make sure to type a valid and publicly accessible url")
                logger.info(err_notice)
                sys.exit(err_instruction)
        else:
            logger.error("Couldn't open url, please make sure to type a valid and publicly accessible url")
            logger.info(err_notice)
            sys.exit(err_instruction)
    except ValueError:
        logger.error("Invalid url! Please type in correct url")
        logger.info(err_notice)
        sys.exit(err_instruction)
    return url