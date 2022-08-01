import os
import sys

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Edit these to match your credentials
USERNAME = os.environ.get('BROWSERSTACK_USERNAME') or  "ssl_QXfg6H"
BROWSERSTACK_ACCESS_KEY = os.environ.get('BROWSERSTACK_ACCESS_KEY') or "zagQyVouKXjd39mfZqoT"

desired_cap = {

        "browserName": "chrome",
        "browserVersion": "103.0",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "Parallel Test 1",  # test name
        "buildName": "soorya build",  # Your tests will be organized within this build
    }

if not (USERNAME and BROWSERSTACK_ACCESS_KEY):
    raise Exception("Please provide your BrowserStack username and access key")

def test_run():
    url = "https://%s:%s@hub.browserstack.com/wd/hub" %(
        USERNAME, BROWSERSTACK_ACCESS_KEY
    )


    def get_browser_option(browser):
        switcher = {
            "chrome": ChromeOptions(),
        }

    options = webdriver.ChromeOptions()
    options.set_capability("browserName", desired_cap["browserName"].lower())
    options.set_capability("bstack:options", desired_cap)

    #    driver = webdriver.Remote(command_executor=url, desired_capabilities=DesiredCapabilities.FIREFOX)
    driver = webdriver.Remote(command_executor=url, options=options)
    driver.get('http://www.google.com')
    print(driver.title)

    if not "Google" in driver.title:
        raise Exception("Are you not on google? How come!")
        elem = driver.find_element_by_name("q")
        elem.send_keys("selenium")
        elem.submit()
        driver.quit()