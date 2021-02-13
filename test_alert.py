from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException




# Automatically download latest webdriver and save in cache
# https://staging.scrive.com/t/9221714692410699950/7348c782641060a9
# driver = webdriver.Ie(IEDriverManager().install())

# driver = webdriver.Chrome(executable_path="../Assignment/driver/chromedriver.exe")
driver = webdriver.Chrome()
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.implicitly_wait(2)
driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")
driver.maximize_window()

# --------------------End-----------------------------------------------------------------

driver.find_element_by_xpath("//input[@id='name']").send_keys("test")
time.sleep(2)
driver.find_element_by_xpath("//a[@class='button button-block action']").click()
time.sleep(2)
# getAll_button = driver.find_elements(By.XPATH, '//a')
# print(getAll_button)
# for i in range(len(getAll_button)-1):
#      getAll_button1 = driver.find_elements(By.XPATH, '//a')
#      # print(f"button1 title: {getAll_button1.text}: index:{i}")
#      if(i == 1):
#          driver.find_elements(By.XPATH, '//a')[1].click()
#          # print("xpath",getAll_button1[1].text)
#          # driver.find_elements(By.XPATH, '//a')[i].click()
#          time.sleep(2)



# for index in range(len(getAll_button)):
#     print(driver.find_element(By.TAG_NAME, "a")[index])


S = lambda X: driver.execute_script("return document.body.parentNode.scroll"+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_xpath("//div[@class='col-xs-6 center-block']").screenshot('sign-in1.png')
time.sleep(2)
# aler = driver.switch_to.window()
# print(aler)

# for screen shot
# ----------------------------

# --------------Dynamic Browser------------------------
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

# -----------------------------------------------------



driver.close()
driver.quit()
print("test completed")