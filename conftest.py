import io

import pytest
import allure
from logger import logger_conf
import logging.config

from utils.project_data import base_url
from application import Application

def pytest_addoption(parser):
    parser.addoption("--base_url", action="store",
                     default=base_url,
                     help="base server https://URL")


def pytest_runtest_call(__multicall__):
    try:
        __multicall__.execute()
    except KeyboardInterrupt:
        raise
    except:
        logging.exception('pytest_runtest_call caught exception:')
        raise


@pytest.fixture(scope="session")
def optns(request):
    ops = {}
    ops['base_url'] = request.config.getoption("--base_url")
    return ops


@pytest.fixture(scope="session")
def api(optns, request):
    """
    :param optns:
    :param request:
    :return:
    """
    allure.environment(report='Allure report', server=optns['base_url'])
    return Application(optns)


# @pytest.fixture(scope="function")
# def log(request):
#     log_capture_string = io.StringIO()
#     return logging.config.dictConfig(log_test(log_capture_string))

# def attach_screenshot(screenshot_file_name='screenshot %s' % datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
#     return allure.attach(screenshot_file_name, driver.get_screenshot_as_png(), type=AttachmentType.PNG)


# def attach_console_log():
#     return allure.attach('console.log', str(driver.get_log('browser')))