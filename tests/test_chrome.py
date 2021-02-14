from allure_commons.types import AttachmentType
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure





import pytest
@allure.severity(allure.severity_level.NORMAL)
class TestChrome():
    @pytest.fixture()
    def test_setup(self):
        global driver
    # Automatically download latest webdriver and save in cache
    # https://staging.scrive.com/t/9221714692410699950/7348c782641060a9
        # driver = webdriver.Ie(IEDriverManager().install())


# ------------comment below line if you want to run test headless mode
# -------------and uncomment lines 36,37,38 -------------------------
        # driver = webdriver.Chrome(ChromeDriverManager().install())

# ------------ End comment below line if you want to run test headless mode-------------------------


# ------------ End comment below line if you want to run test headless mode-------------------------

# ------------comment these 3 lines if you want to run test in browser and uncommet 29---------------
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
# ------------ End comment these 3 lines if you want to run test in browser-------------------------

        driver.implicitly_wait(2)
        print("Chrome Testing Started")
        driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")
        allure.attach(driver.get_screenshot_as_png(), name="URL", attachment_type= AttachmentType.PNG)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("test completed")

# --------------------End-----------------------------------------------------------------

    def test_enterName(self, test_setup):
        # Enter Full name
        driver.find_element_by_xpath("//input[@id='name']").send_keys("Dan")
        allure.attach(driver.get_screenshot_as_png(), name="Enter Name", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        print("Name entered")
        driver.find_element_by_xpath("//a[@class='button button-block action']").click()
        allure.attach(driver.get_screenshot_as_png(), name="Next Button Clicked", attachment_type=AttachmentType.PNG)
        print("Next Button clicked")
        time.sleep(2)


# -----------------------Taking Screen Shot-------------------------------------------
#         S = lambda X: driver.execute_script("return document.body.parentNode.scroll"+X)
#         driver.set_window_size(S('Width'), S('Height'))
        driver.find_element_by_xpath("//div[@class='col-xs-6 center-block']").screenshot('sign-chrome.png')
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name="ScreenShot taken", attachment_type=AttachmentType.PNG)
        print("Screenshot taken ")
        driver.find_element_by_xpath("//a[@class='button button-block sign-button action']").click()
        allure.attach(driver.get_screenshot_as_png(), name="Sign", attachment_type=AttachmentType.PNG)
        time.sleep(2)
        print("Sign button clicked")
# -----------------------End Taking Screen Shot-------------------------------------------

# ----------------Validating text 'Document singed!'-------------------------------------
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
# ----------------End Validating text 'Document singed!'-------------------------------------


# run test pytest -v for more detail'
#pip install pytest-xdist for parallel testing
# run: py.test tests/ -v -s --cov --cov-report=html

# Allure reports
# py.test tests/test_chrome.py -v -s --alluredir=./reports
# then C:\Allure\bin>allure serve F:\scrive\Assignment\reports