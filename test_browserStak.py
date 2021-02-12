from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
import time
import urllib3


desired_cap = {
 'os_version': '10',
 'resolution': '1920x1080',
 'browser': 'IE',
 'browser_version': '11.0',
 'os': 'Windows',
 'browserstack.debug' : 'true',
 'name': 'BStack-[Python] Sample Test', # test name
 'build': 'BStack Build Number 1' # CI/CD job or build name
}


class TestChrome():
    @pytest.fixture()
    def test_setup(self):
        global driver
        urllib3.disable_warnings()
        driver = webdriver.Remote(
        command_executor='https://mumtaz7:rjpGcuyfNym5RuHgmcih@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=desired_cap)
        driver.implicitly_wait(2)
        driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("test completed")

    # --------------------End-----------------------------------------------------------------

    def test_enterName(self, test_setup):

        driver.find_element_by_xpath("//input[@id='name']").send_keys("test")
        time.sleep(2)
        driver.find_element_by_xpath("//a[@class='button button-block action']").click()
        time.sleep(2)
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)
        # Switch to window and search course
        handles = driver.window_handles
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                break



        # for screen shot
        # ----------------------------
        # S = lambda X: driver.execute_script("return document.body.parentNode.scroll"+X)
        # driver.set_window_size(S('Width'), S('Height'))
        # driver.find_element_by_xpath("//div[@class='col-xs-6 center-block']").screenshot('sign-in1.png')

