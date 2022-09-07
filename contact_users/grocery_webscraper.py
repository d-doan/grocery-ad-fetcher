from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlretrieve
from datetime import date, timedelta
import os

# prob should chuck each grocery store in its own class so then can do it all in one file

def download_file(download_url, store_name, date, file_type):
    file_location = 'contact_users\\static\\contact_users\\Weekly_ads' + '\\' + date + '\\' + store_name + '.' + file_type
    urlretrieve(download_url, file_location)
    
def get_last_wednesday():
    todays_date = date.today()
    date_offset = (todays_date.weekday() -2) % 7
    return todays_date - timedelta(days=date_offset)

class Hmart:
    driver = webdriver.Chrome(executable_path="C:/Users/dando/Downloads/chromedriver_win32/chromedriver.exe")
    # implicit wait applied
    driver.implicitly_wait(5)
    driver.get("https://www.hmart.com/weekly-sales-and-events/california/")

    image_class = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[2]/div/div[3]/div[2]/div/div[1]/div[1]/img[1]')
    hmart_weekly_ad = image_class.get_attribute('src')

    last_wednesday = str(get_last_wednesday())
    del_wed = str(get_last_wednesday() - timedelta(7))
    
    dir_name = 'contact_users\\static\\contact_users\\Weekly_ads' + '\\' + last_wednesday
    prev_dir_name = 'contact_users\\static\\contact_users\\Weekly_ads' + '\\' + del_wed + '\\Hmart.jpg'

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        download_file(hmart_weekly_ad, "Hmart", last_wednesday, "jpg")
    else:
        download_file(hmart_weekly_ad, "Hmart", last_wednesday, "jpg")
        
    if os.path.exists(prev_dir_name):
        os.remove(prev_dir_name)


class Ralphs:
    driver = webdriver.Chrome(executable_path="C:/Users/dando/Downloads/chromedriver_win32/chromedriver.exe")
    # implicit wait applied
    driver.implicitly_wait(5)
    driver.get("https://www.ralphs.com/weeklyad")

    # finds html element containing advertisement
    pdf_class = driver.find_element(By.LINK_TEXT, 'Download PDF')
    ralphs_weekly_ad = pdf_class.get_attribute('href')
    
    last_wednesday = str(get_last_wednesday())
    del_wed = str(get_last_wednesday() - timedelta(7))
    
    dir_name = 'contact_users\\static\\contact_users\\Weekly_ads' + '\\' + last_wednesday
    prev_dir_name = 'contact_users\\static\\contact_users\\Weekly_ads' + '\\' + del_wed + '\\Ralphs.pdf'


    # checks if weekly directory exists yet, if not then make it
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        download_file(ralphs_weekly_ad, "Ralphs", last_wednesday, "pdf")
    else:
        download_file(ralphs_weekly_ad, "Ralphs", last_wednesday, "pdf")

    if os.path.exists(prev_dir_name):
        os.remove(prev_dir_name)