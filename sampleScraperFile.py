from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def download_scraping_script_demo():
    websiteUrl = 'https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html'
    options = Options()
    options.headless = True
    print("scraping demo 1")
    # options.add_argument("--window-size=1920,1200")
    # DRIVER_PATH = '/Users/arifzamri/chromeDriver/chromedriver'
    try:
        driver = webdriver.Remote(command_executor='http://chrome:4444/wd/hub',
                                  desired_capabilities=DesiredCapabilities.CHROME)
        print("scraping demo 2")
        driver.get(websiteUrl)
        driver.implicitly_wait(10)
        button4 = driver.find_element(By.LINK_TEXT, "addresses.csv")
        button4.click()
        return 'downloaded file'
    except:
        print("scraping fail")
        return 'scraping fail'    

    