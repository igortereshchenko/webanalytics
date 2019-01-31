import time
from random import randint
from urllib.parse import urlparse

from urllib3 import ProxyManager, make_headers, PoolManager, disable_warnings
from selenium import webdriver
import os

from Requests.Response import Response

disable_warnings()

from Requests.RequesterException import RequesterException


# https://urllib3.readthedocs.io/en/latest/user-guide.html

class Requester:
    """
    Class to perform https/http request
    """

    def __init__(self, url, retries=4, timeout=30, sleep_time=10, proxy=None, run_html=False):
        """
        :param url: server url
        :param retries: you can control the retries using the retries parameter to request
        :param timeout: Timeouts allow you to control how long requests are allowed to run before being aborted
        :param sleep_time: Average waiting time before next retry
        :param proxy: proxy server
        :param run_html: open url in selenium (True/False)
        """

        self.__url = url
        self.__retries = retries
        self.__timeout = timeout
        self.__sleep_time = sleep_time
        self.__run_html = run_html

        if (self.__run_html):
            # TODO load driver depend on OS type
            dir_path = os.path.dirname(os.path.realpath(__file__))
            chromedriver = os.path.join(dir_path, 'drivers', 'chromedriver_win')

            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('window-size=1200x600')  # optional
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)

            self.__browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)


        if proxy:
            # TODO make proxy authorization
            # default_headers = make_headers(proxy_basic_auth='myusername:mypassword')
            self.__http = PoolManager()
        else:
            self.__http = PoolManager()

    def __del__(self):
        if (self.__run_html):

            self.__browser.close()


    def make_get_request(self, parameters=None):
        """
        Perform GET request with parameters

        :param parameters: dictionary {key:value}
        :return: Response class
        """

        status = None
        html_content = None

        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

        for counter in range(self.__retries):
            try:

                # http request
                response = self.__http.request('GET', self.__url, headers=headers, fields=parameters, timeout=self.__timeout)

                status = response.status
                html_content = response.data

                # Success
                if response.status == 200:
                    if (self.__run_html):
                        self.__browser.get("data:text/html;charset=utf-8,{html_content}".format(html_content=html_content))
                        html_content = self.__browser.page_source

                    break

            except Exception as e:

                if counter == self.__retries - 1:
                    raise RequesterException("Retries {0} overlimit".format(self.__retries), self.__url)
                else:
                    # wait a random amount of time between requests to avoid bot detection
                    random_delta = randint(1, self.__sleep_time)
                    time.sleep(self.__sleep_time * counter+random_delta)

        return Response(status=status, data=html_content)

    def get_url_root(self):
        return '{}://{}'.format(urlparse(self.__url).scheme, urlparse(self.__url).netloc)




