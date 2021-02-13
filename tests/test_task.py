from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
#from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


import pytest

class TestChrome():
    @pytest.fixture()
    def test_setup(self):
        global driver
    # Automatically download latest webdriver and save in cache
    # https://staging.scrive.com/t/9221714692410699950/7348c782641060a9
    #     driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver = webdriver.Ie(IEDriverManager().install())
        # driver = webdriver.Chrome()

        # driver = webdriver.Chrome(ChromeDriverManager().install())

        #driver = webdriver.Chrome(ChromeDriverManager().install())

        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome(executable_path="../../Assignment/driver/chromedriver.exe")
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
        # for screen shot
        # ----------------------------
        S = lambda X: driver.execute_script("return document.body.parentNode.scroll"+X)
        driver.set_window_size(S('Width'), S('Height'))
        driver.find_element_by_xpath("//div[@class='col-xs-6 center-block']").screenshot('sign-in.png')
        time.sleep(2)
        driver.find_element_by_xpath("//a[@class='button button-block sign-button action']").click()
        time.sleep(2)

        print("confirmation done")

        # bodyText = driver.find_element(By.XPATH, "//span[contains(text(),'Document signed')]")
        bodyText = driver.find_element_by_tag_name("h1")
        assert bodyText.text == "Document signed!"
        print("confirmation done")








# class TestFirefox():
#     @pytest.fixture()
#     def test_setup1(self):
#         global driver
#     # Automatically download latest webdriver and save in cache
#     # https://staging.scrive.com/t/9221714692410699950/7348c782641060a9
#     #     driver = webdriver.Chrome(ChromeDriverManager().install())
#         # driver = webdriver.Ie(IEDriverManager().install())
#         # driver = webdriver.Chrome()
#         # driver = webdriver.Chrome(ChromeDriverManager().install())
#         # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#
#         options = FirefoxOptions()
#         options.add_argument("--headless")
#         driver = webdriver.Firefox(options=options)
#
#         driver.implicitly_wait(2)
#         driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")
#         driver.maximize_window()
#         yield
#         driver.close()
#         driver.quit()
#         print("test completed")
#
#     # --------------------End-----------------------------------------------------------------
#
#     def test_enterName1(self, test_setup1):
#
#         driver.find_element_by_xpath("//input[@id='name']").send_keys("test")
#         time.sleep(2)
#         driver.find_element_by_xpath("//a[@class='button button-block action']").click()
#         time.sleep(2)
#         # for screen shot
#         # ----------------------------
#         S = lambda X: driver.execute_script("return document.body.parentNode.scroll"+X)
#         driver.set_window_size(S('Width'), S('Height'))
#         driver.find_element_by_xpath("//div[@class='col-xs-6 center-block']").screenshot('sign-in.png')
#         # time.sleep(4)
#         driver.find_element_by_xpath("//a[@class='button button-block sign-button action']").click()
#         time.sleep(4)
#
#         # bodyText = driver.find_element(By.XPATH, "//span[contains(text(),'Document signed')]")
#         bodyText = driver.find_element_by_tag_name("h1")
#         assert bodyText.text == "Document signed!"
#         # if(bodyText.text == "Document signed!"):
#         #     print("Found")
#         # else:
#         #     print("Not Found")


    # -------------------------------------------------------------------------------------
    # def test_setup(self):
    #     global driver
    # # Automatically download latest webdriver and save in cache
    # # https://staging.scrive.com/t/9221714692410699950/7348c782641060a9
    # #     browserName = "firefox"
    # #     if browserName == "chrome":
    # #         driver = webdriver.Chrome(ChromeDriverManager().install())
    # #     elif browserName == "firefox":
    # #         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # #     elif browserName == "safri":
    # #         driver = webdriver.safari()
    # #     else:
    # #         print("Enter correct borwser name"+browserName)
    # #         raise Exception("Driver is not Found")
    #     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    #     driver.implicitly_wait(2)
    #     driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")
    #     driver.maximize_window()
    #     yield
    #     driver.close()
    #     driver.quit()
    #     print("test completed")
    #
    #
    # # --------------------End-----------------------------------------------------------------
    #
    # def test_enterName(self, test_setup):
    #
    #     driver.find_element_by_xpath("//input[@id='name']").send_keys("test")
    #     time.sleep(2)
    #     driver.find_element_by_xpath("//a[@class='button button-block action']").click()
    #     time.sleep(2)
    #     # for screen shot
    #     # ----------------------------
    #     S = lambda X: driver.execute_script("return document.body.parentNode.scroll"+X)
    #     driver.set_window_size(S('Width'), S('Height'))
    #     driver.find_element_by_xpath("//div[@class='col-xs-6 center-block']").screenshot('sign-in.png')
    #     time.sleep(2)
    #
    #     driver.find_element_by_xpath("//a[@class='button button-block sign-button action']").click()
    #     time.sleep(4)
    #     bodyText = driver.find_element_by_tag_name("h1")
    #     assert bodyText.text == "Document signed!"

# run test pytest -v for more detail'
#pip install pytest-xdist for parallel testing
