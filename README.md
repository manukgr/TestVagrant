# TestVagrant
TestVagrant Coding Challenge

Steps to Execute 
---------
SETUP
---------
Prerequisites
-------------

a) Install Python `3.6.x`

b) Add Python `3.6.x` to your PATH environment variable

c) If you do not have it already, get pip

(**NOTE**: Most recent Python distributions come with pip)

d) `pip install -r requirements.txt` to install dependencies
    
    **Note:** Command may be ``pip3`` instead of ``pip`` depending on the system.
e) Get setup with your browser driver. If you don't know how to, please try:

   > For Chrome: https://sites.google.com/a/chromium.org/chromedriver/getting-started

   > For Firefox: https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver	#Note: Check firefox version & selenium version compatibility before downloading geckodriver.
   
   > For IE: https://support.microsoft.com/en-us/help/2990999/webdriver-support-for-internet-explorer-11
   
   > For Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   
   > For Safari: https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari


__If your setup goes well__, you should be able to run a simple test with this command:

`python3 -m pytest -n {concurrent_tests} {test_class_path} -k {test_case_name}`

-------------------
Framework Structure
-------------------
Directory structure of our current Templates

    <TestVagrant>/
    └──    
        ├── endpoints:              <API endoints and related classes>
        |
        ├── locator:                <For all configurations and locator files>
        |   
        ├── page_objects:           <Contains our Base Page,different Page Objects,DriverFactory, PageFactory>
      
        ├── testdata:               <Directory to keep or generate test data>
      
        ├── tests          <Tests to be added here>
    
        |    
        ├── utils:                  <All utility modules >
        |
        ├── .gitignore
        ├── conftest.py
        ├── README.md
        ├── requirement.txt

## TODO
1. Add support for other browsers
2. Add command line arguments support
3. Add Dynamic locators support
4. More tests
5. Autorun on Circle CI : Done
6. Using python magic methods
7. Add allure report with screenshots and steps