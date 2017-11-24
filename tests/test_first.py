import http
import logging
import logging.config
from logger import logger_conf

import requests
import pytest

import http.client as http_client
http_client.HTTPConnection.debuglevel = 1
# logging.config.fileConfig('../logging.conf',
#                           defaults={'logfilename': 'httpbin',
#                                     'consoleHandlerLevel': 'DEBUG'},
#                           disable_existing_loggers=False)
logging.config.dictConfig(logger_conf())


logger = logging.getLogger('requests.packages.urllib3')
#logging.config.fileConfig('../logger.py')

# logging.basicConfig(level=logging.DEBUG)
# logging.config.dictConfig(DEFAULT_LOGGING)
# logger = logging.getLogger('main')



base_url = 'https://httpbin.org'

base_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "close",
    "Cookie": "_gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1; _gauges_unique_hour=1",
    "Host": "httpbin.org",
    "Referer": "https://httpbin.org/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "X-Compress": "null"
}


def get(*args, headers=base_headers):
    url = '/'.join(str(arg) for arg in args)
    resp = requests.get(f"{base_url}/{url}", headers=headers)
    logger.info(f'Response content: {resp.content}')
    return resp


def test_header():
    resp = get('headers')
    assert resp.status_code == 200
    assert resp.json()
    assert 'headers' in resp.json()
    assert resp.json()['headers'] == base_headers


@pytest.mark.parametrize("status_code", [200, 201, 400, 403, 404, 500])
def test_status(status_code):
    resp = get('status', status_code)
    assert status_code == resp.status_code


@pytest.mark.parametrize("redirect_count", [1, 3])
def test_redirect(redirect_count):
    resp = get('redirect', redirect_count)
    assert resp.status_code == 200
    assert len(resp.history) == redirect_count
