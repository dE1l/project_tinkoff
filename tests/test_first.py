import pytest

from utils.project_data import base_headers


def test_header(api):
    resp = api.get('headers')
    assert resp.status_code == 200
    assert resp.json()
    assert 'headers' in resp.json()
    assert resp.json()['headers'] == base_headers


@pytest.mark.parametrize("status_code", [200, 201, 400, 403, 404, 500])
def test_status(api, status_code):
    resp = api.get('status', status_code)
    assert status_code == resp.status_code


@pytest.mark.parametrize("redirect_count", [1, 3])
def test_redirect(api, redirect_count):
    resp = api.get('redirect', redirect_count)
    assert resp.status_code == 200
    assert len(resp.history) == redirect_count
