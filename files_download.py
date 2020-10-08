from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import pandas
project_folder_path = os.getcwd()
ChromeOptions = Options()
content_folder = "Videos_For_Upload"
content_folder_path = os.path.join(project_folder_path, content_folder)
ChromeOptions.add_experimental_option("prefs", {"download.default_directory": content_folder_path })
driver_path = os.path.join(project_folder_path, r"Chrome_Drivers\chromedriver.exe")


driver = webdriver.Chrome(executable_path = driver_path, chrome_options = ChromeOptions)

driver.get("https://yandex.ru/")

#
# import pandas as pd
#
# file = pd.read_csv(r"csv\first.csv")
# file_2 = file[file["IsVideo"] == "Yes"]
# video_urls = file_2['PostUrl']

# def download_video(url, driver):
download_site_url = "https://instadownloader.co/ru/"
driver.get(download_site_url)
form_path = "/html/body/div/div[1]/div[2]/div[1]/div/div[1]/form/div[1]/input"
driver.find_element_by_xpath(form_path).send_keys("https://www.instagram.com/p/B97F6dMHfrz")
download_button = "/html/body/div/div[1]/div[2]/div[1]/div/div[1]/form/div[2]/button"
driver.find_element_by_xpath(download_button).click()
time.sleep(3)
download_first_video = "/html/body/div/div/div/div[2]/div/div/a[4]"
driver.find_element_by_xpath(download_first_video).click()
# time.sleep(4)

# download_video(video_urls[0], driver)

# driver.quit()




# for i in video_urls:
#     print(i)
