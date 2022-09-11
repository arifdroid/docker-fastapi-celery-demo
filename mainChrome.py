from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def scraping_script():
    websiteUrl = 'https://www.ttbdirect.com/ttb/kdw1.39.1#_frmIBPreLogin'
    options = Options()
    options.headless = True
    # options.add_argument("--window-size=1920,1200")
    DRIVER_PATH = '/Users/arifzamri/chromeDriver/chromedriver'
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
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
        time.sleep(5)
        driver.close()
        driver.quit()


    return 'success'
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
