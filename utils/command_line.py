import sys


def get_browser():
    if "--browser" in sys.argv:
        return sys.argv[sys.argv.index("--browser") + 1]
    else:
        return "chrome"


def headless():
    if "--headless" in sys.argv:
        return sys.argv[sys.argv.index("--headless") + 1]
    else:
        return "n"


def get_url():
    if "--url" in sys.argv:
        return sys.argv[sys.argv.index("--url") + 1]
    else:
        return "https://ndtv.com"
