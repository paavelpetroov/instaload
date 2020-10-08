from selenium import webdriver
import time
import os

# USING FULL X-PATH

project_folder_path = os.getcwd()
content_folder = "Videos_For_Upload"
content_folder_path = os.path.join(project_folder_path, content_folder)
driver_path = os.path.join(project_folder_path, r"Chrome_Drivers\chromedriver.exe")

# ENTRANCE AND AUTHORIZATION

driver = webdriver.Chrome(driver_path)
driver.maximize_window()


start_url = "https://business.facebook.com/creatorstudio?tab=instagram_content_posts&mode=instagram&collection_id=all_pages&content_table=INSTAGRAM_POSTS"
driver.get(start_url)


authorization_form = "//*[@id='u_0_0']/div[1]/div[3]/a"
driver.find_element_by_xpath(authorization_form).click()

login = "------------"
password = "-------"

driver.find_element_by_name("email").send_keys(login)
driver.find_element_by_name("pass").send_keys(password)
driver.find_element_by_id("loginbutton").click()

driver.get(start_url)
time.sleep(2)

instagram_part = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/a"
driver.find_element_by_xpath(instagram_part).click()
time.sleep(2)

publication_creating_button = "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div/ul/li[1]/div/div"
driver.find_element_by_xpath(publication_creating_button).click()
time.sleep(2)
# START POST UPLOADING
# /html/body/div[8]/div/div/div/div/div/a/div/input

add_content_button = "/html/body/div[6]/div/div/div/div[2]/div[1]/div/div[5]/div/div/div/span"
driver.find_element_by_xpath(add_content_button).click()

file_upload = "/html/body/div[7]/div/div/div/div/div/a/div/input"
video_name = "cat.jpg"
video_path = os.path.join(content_folder_path, video_name)


driver.find_element_by_xpath(file_upload).send_keys(video_path)

# ===============================================================================================

# def authorization(driver):
#     start_url = "https://business.facebook.com/creatorstudio?tab=instagram_content_posts&mode=instagram&collection_id=all_pages&content_table=INSTAGRAM_POSTS"
#     driver.get(start_url)
#
#
#     authorization_form = "//*[@id='u_0_0']/div[1]/div[3]/a"
#     driver.find_element_by_xpath(authorization_form).click()
#
#     login = "pahan.1100@mail.ru"
#     password = "577914tyu"
#
#     driver.find_element_by_name("email").send_keys(login)
#     driver.find_element_by_name("pass").send_keys(password)
#     driver.find_element_by_id("loginbutton").click()
#
#     driver.get(start_url)
#
#     return True
#
#
# def uploading_form_open(driver):
#
#     instagram_part = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/a"
#     driver.find_element_by_xpath(instagram_part).click()
#     time.sleep(2)
#
#     publication_creating_button = "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div/ul/li[1]/div/div"
#     driver.find_element_by_xpath(publication_creating_button).click()
#     time.sleep(2)
#
# def main():
#     project_folder_path = os.getcwd()
#     content_folder = "Videos_For_Upload"
#     content_folder_path = os.path.join(project_folder_path, content_folder)
#     driver_path = os.path.join(project_folder_path, r"Chrome_Drivers\chromedriver.exe")
#
#     driver = webdriver.Chrome(driver_path)
#     driver.maximize_window()
#
#     authorization(driver)
#
#     uploading_form_open(driver)
#
# if __name__ == "__main__":
#     main()
