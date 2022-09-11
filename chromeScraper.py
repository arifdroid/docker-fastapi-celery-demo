from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def scraping_script():
    websiteUrl = 'https://www.ttbdirect.com/ttb/kdw1.39.1#_frmIBPreLogin'
    options = Options()
    options.headless = True
    print("scraping 1")
    # options.add_argument("--window-size=1920,1200")
    # DRIVER_PATH = '/Users/arifzamri/chromeDriver/chromedriver'
    try:
        driver = webdriver.Remote(command_executor='http://chrome:4444/wd/hub',
                                  desired_capabilities=DesiredCapabilities.CHROME)
        print("scraping 2")
        driver.get(websiteUrl)
        driver.implicitly_wait(10)
        user = driver.find_element(By.ID, "frmIBPreLogin_txtUserId")
        user.click()
        user.send_keys("Phanphailin2")
        pw = driver.find_element(By.ID, "frmIBPreLogin_txtPassword")
        pw.click()
        pw.send_keys("ABC123def")
        time.sleep(3)
        button = driver.find_element(By.ID, "frmIBPreLogin_btnLogIn")
        button.click()
        time.sleep(5)
        button2 = driver.find_element(
            By.ID, "frmIBPostLoginDashboard_link867777585898847")
        button2.click()
        time.sleep(2)
        button3 = driver.find_element(
            By.ID, "frmIBAccntSummary_lnkFullStatement")
        button3.click()
        try:
            alert = Alert(driver)
            alert.accept()
            print("got alert, no data")
            time.sleep(5)
            driver.close()
            driver.quit()

        except:
            print("No alert,data is here")
            time.sleep(2)
            button4 = driver.find_element(By.ID, "frmIBAccntFullStatement_btncsv")
            button4.click()
            print("data dowmloaded")
            time.sleep(3)
            button5 = driver.find_element(By.ID, "hbxIBPostLogin_lnkLogOut")
            button5.click()
            print("logut from web")
            time.sleep(5)
            driver.close()
            driver.quit()

        return 'success'

    except:
        return 'error driver'

# """
#         exist, error = self.check_existence(element_type = "ID",
#                     id_ = "frmIBPreLogin_imgReloadCaptcha_span",
#                     repeated_times=60, sleepTime=0.5)
#         self.driver.save_screenshot("ss2.png")
#         import codecs
#         print(self.driver.current_url)
#         n = "PageSave3.html"
#         f = codecs.open(n, "w", "utf−8")
#         h = self.driver.page_source
#         f.write(h)
#         self.driver.save_screenshot("ss3.png")
#         print("END HERER")
#         time.sleep(30)
#         """
# time.sleep(15)
# print(driver.page_source)
# driver.quit()
