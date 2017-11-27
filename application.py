import logging
import logging.config

import requests
from utils.project_data import base_headers
import http.client as http_client
from logger import logger_conf


class Application(object):
    def __init__(self, optns):
        self.base_url = optns['base_url']

    @property
    def logger(self):
        http_client.HTTPConnection.debuglevel = 1

        # logging.config.fileConfig('../logging.conf',
        #                           defaults={'logfilename': 'httpbin',
        #                                     'consoleHandlerLevel': 'DEBUG'},
        #                           disable_existing_loggers=False)

        logging.config.dictConfig(logger_conf())
        return logging.getLogger('requests.packages.urllib3')

    def get(self, *args, headers=base_headers):
        """
        :param args:
        :param headers:
        :return:
        """
        url = '/'.join(str(arg) for arg in args)
        resp = requests.get(f"{self.base_url}/{url}", headers=headers)
        self.logger.info(f'Response content: {resp.content}')
        return resp

    @property
    def session(self):
        """
        :return: requests.Session() instance
        """
        session = requests.Session()
        session.verify = False
        # self.session.auth = HTTPBasicAuth(optns['username'], optns['password'])
        session.encoding = 'utf-8'
        return session
