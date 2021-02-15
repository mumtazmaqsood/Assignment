# Assignment

    Description: 
      Test cases has been written according to requirement and also build CI by using Github actions on ubuntu 
      server and also showing test coverge results and Allure Reports integrated.
      Test cases are running both with headless on Chrome & Firefox and also integrated with BrowserStack(IE11).
  
    Tests Files (For code review):
      tests
        -- test_browserStak.py
        -- test_chrome.py
        -- test_firefox.py
  
    Test can run on local machine on window 10 by installing required software (python3.7, pycharm) & packages  
        
    Install packages
    python -m pip install --upgrade pip
    pip install selenium
    pip install webdriver-manager
    pip install pytest
    pip install pytest-html
    pip install pytest-cov
    pip install pytest-xdist
    pip install coverage
    pip install pytest-cov
 

  # Run Test
  py.test tests/ -v -s --cov --alluredir=./reports



  # Test Case
    Create a selenium test using Python that does the following:
    1- Go to https://staging.scrive.com/t/9221714692410699950/7348c782641060a9
    2- Fill in the full name in the document.
    3- Click on Next
    4- There should be a confirmation modal (the one that has text "by clicking the button you will..."). 
    Take a screenshot of this confirmation modal and try to make it only show what is actually visible in
    the modal (not the whole web page).
    5- Sign the document
    6- Verify that there is a text “Document Signed” on the screen.



    Make the test runnable on both Firefox and Chrome -------------------------- Done 
    Make the test runnable on IE11 on Browserstack ----------------------------- Done
    Document how to run the test on Ubuntu ------------------------------------- Build CI by using GitHub action 

# Test Result
    Test results avaliable in 

    1- Repo Actions
        -- All workflows and check all results and test cases coverage 
    
    2- Allure Report is avaliable on localhost, need to configure and installed on local 
    computer and then avaliable on http://192.168.99.1:59313/index.html 
    this report is showing all testing activities and capturing, displaying captured images with description


# Results Screenshot github Action    
![action_result](https://user-images.githubusercontent.com/18198800/107922596-8860d600-6f70-11eb-83dd-f63a60ece10a.png)

# Results Screenshot Allure Reporting

![graph](https://user-images.githubusercontent.com/18198800/107924739-bf84b680-6f73-11eb-8c47-040be5813e6e.png)
![mainpage](https://user-images.githubusercontent.com/18198800/107924891-f65acc80-6f73-11eb-8dc5-e76da2e6b053.png)
![entername](https://user-images.githubusercontent.com/18198800/107924881-f4910900-6f73-11eb-9145-76a8fadd3c38.png)
![nextbtn](https://user-images.githubusercontent.com/18198800/107924892-f6f36300-6f73-11eb-87cf-0aff4b9de5f3.png)
![sign](https://user-images.githubusercontent.com/18198800/107924894-f8249000-6f73-11eb-8c2a-44de68afcf7a.png)
![assert](https://user-images.githubusercontent.com/18198800/107924880-f3f87280-6f73-11eb-94d5-5590206c3a81.png)






