from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

target_url = 'https://event.mi.com/tw/2022618'

def launch_browser():
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s)

    # while True:
    #     current_time = time.localtime()
    #     print("Current Time =", time.strftime("%H:%M:%S", current_time))
    #     if time.strftime("%H:%M:%S", current_time) != '18:48:00':
    #         break

    browser.get(target_url)
    book_room_btn = browser.find_element(By.XPATH, '//*[@id="1861_192_0"]/div/div/a')
    book_room_btn.click()

    time.sleep(200)

if __name__ == '__main__':
    launch_browser()