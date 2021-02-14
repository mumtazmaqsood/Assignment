import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
import time
import urllib3
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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


class TestBrowserStack_IE11():
    @pytest.fixture()
    def test_setup(self):
        global driver
        urllib3.disable_warnings()
        driver = webdriver.Remote(
        command_executor='https://mumtaz7:rjpGcuyfNym5RuHgmcih@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=desired_cap)
        driver.implicitly_wait(2)
        driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")
        allure.attach(driver.get_screenshot_as_png(), name="URL", attachment_type=AttachmentType.PNG)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("test completed")

    # --------------------End-----------------------------------------------------------------

    def test_enterName1(self, test_setup):

        driver.find_element_by_xpath("//input[@id='name']").send_keys("Danial")
        allure.attach(driver.get_screenshot_as_png(), name="Enter Name", attachment_type=AttachmentType.PNG)
        print("Name entered")
        time.sleep(2)
        driver.find_element_by_xpath("//a[@class='button button-block action']").click()
        allure.attach(driver.get_screenshot_as_png(), name="Next Button Clicked", attachment_type=AttachmentType.PNG)
        print("Next Button clicked")
        time.sleep(2)
        # for screen shot
        # ----------------------------
        # driver.find_element_by_xpath("//div[@class='col-xs-6 center-block']").screenshot('browserStack.png')
        # time.sleep(4)
        # allure.attach(driver.get_screenshot_as_png(), name="ScreenShot taken", attachment_type=AttachmentType.PNG)
        # print("Screenshot taken ")
        driver.find_element_by_xpath("//a[@class='button button-block sign-button action']").click()
        allure.attach(driver.get_screenshot_as_png(), name="Sign", attachment_type=AttachmentType.PNG)
        print("Sign button clicked")
        timeout = 5
        try:
            element_present = EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Document signed')]"))
            a = WebDriverWait(driver, timeout).until(element_present)
            assert a.text == "Document signed!"
            allure.attach(driver.get_screenshot_as_png(), name="text validation", attachment_type=AttachmentType.PNG)
            print(f"{a.text}:present")

        except TimeoutException:
            print
            "Timed out waiting for page to load"