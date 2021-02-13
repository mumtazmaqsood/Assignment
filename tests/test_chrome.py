from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC






import pytest

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



# ------------comment these 3 lines if you want to run test in browser and uncommet 29---------------
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
# ------------ End comment these 3 lines if you want to run test in browser-------------------------

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
        print("name has been entered")
        driver.find_element_by_xpath("//a[@class='button button-block action']").click()
        print("button clicked")
        time.sleep(2)
        print("button clicked")

# -----------------------Taking Screen Shot-------------------------------------------
        S = lambda X: driver.execute_script("return document.body.parentNode.scroll"+X)
        driver.set_window_size(S('Width'), S('Height'))
        driver.find_element_by_xpath("//div[@class='col-xs-6 center-block']").screenshot('sign-in.png')
        time.sleep(2)
        driver.find_element_by_xpath("//a[@class='button button-block sign-button action']").click()
        time.sleep(2)
# -----------------------End Taking Screen Shot-------------------------------------------

# ----------------Validating text 'Document singed!'-------------------------------------
        timeout = 5
        try:
            element_present = EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Document signed')]"))
            a = WebDriverWait(driver, timeout).until(element_present)
            assert a.text == "Document signed!"

        except TimeoutException:
            print
            "Timed out waiting for page to load"
# ----------------End Validating text 'Document singed!'-------------------------------------


# run test pytest -v for more detail'
#pip install pytest-xdist for parallel testing