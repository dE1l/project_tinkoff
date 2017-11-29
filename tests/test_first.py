import pytest

from utils.project_data import base_headers
from utils.base import is_json


def test_header(api):
    """
    Send get request by 'headers' method, check headers and compare it with base_headers of project

    :param api: main base fixture
    :return: None
    """
    resp = api.get('headers')
    assert resp.status_code == 200
    assert is_json(resp.content)
    resp_json = resp.json()
    assert 'headers' in resp_json
    assert resp_json['headers'] == base_headers


@pytest.mark.parametrize("status_code", [200, 201, 400, 403, 404, 500])
def test_status(api, status_code):
    """
    Send get request by 'status' method and check status_code

    :param api: main base fixture
    :param status_code: send request with this status code and check it
    :return: None
    """
    resp = api.get('status', status_code)
    assert status_code == resp.status_code


@pytest.mark.parametrize("redirect_count", [1, 3])
def test_redirect(api, redirect_count):
    """
    Send get request by 'redirect' method and check redirect count

    :param api: main base fixture
    :param redirect_count: send request with this redirect count and check it
    :return: None
    """
    resp = api.get('redirect', redirect_count)
    assert resp.status_code == 200
    assert len(resp.history) == redirect_count


def test_log_assert_false(api):
    assert False
