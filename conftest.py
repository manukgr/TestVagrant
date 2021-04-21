
def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     dest="browser",
                     # default="chrome",ie,edge,firefox,safari
                     default="chrome",
                     help="Browser. Valid options are firefox, ie and chrome")
    parser.addoption("-L", "--headless",
                     dest="headless",
                     default="n",
                     help="To execute headless browser")
    parser.addoption("-U", "--app_url",
                     dest="url",
                     default="https://ndtv.com/",
                     help="The url of the application")