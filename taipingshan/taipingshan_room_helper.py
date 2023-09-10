from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from taipingshan.personal import Personal
import time

target_date = '2022-03-25'
target_time = '08:00'
# order_day order_holiday
day_flag = 'order_holiday'
calendar_item_selector = f'span.{day_flag} a[onclick="dateCheck(\'{target_date}\')"]'
target_url = 'https://tpsr.forest.gov.tw/TPSOrder/wSite/index.do?action=indexPage&mp=1'
personal = Personal('Kevin', '0912345678', 'F129123456', '1995-07-30', 'kevin1234567@gmail.com')
personal.to_string()


def start_booking_room():
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s)
    browser.get(target_url)

    # close announce window
    close_announce_btn = browser.find_element(By.XPATH, '//*[@id="show"]/div[1]/a/img')
    close_announce_btn.click()

    captcha_code = input('input Captcha code: ')

    # [Root] Step1. Start script and input the captcha code on screen at 7:59:30
    time_textfield = browser.find_element(By.ID, 'nowTime')

    while time_textfield.text[-8:-3] != target_time:
        print('WAIT! Now time: ' + time_textfield.text[-8:])
        pass

    # [Root]. when timer reach 8:00, captcha code textfield will be fill in directly
    captcha_code_textfield = browser.find_element(By.ID, 'captcha')
    captcha_code_textfield.send_keys(captcha_code)

    book_room_btn = browser.find_element(By.XPATH, '//*[@id="signForm"]/div[2]/input[1]')
    book_room_btn.click()

    # [step1. Room] click double room button
    double_book_room_btn = browser.find_element(By.XPATH, '/html/body/div/div[2]/div[3]/ul/li[1]/form/input[1]')
    double_book_room_btn.click()

    # [step2. Date] choose target date
    WebDriverWait(browser, 30).until(lambda d: d.execute_script("return jQuery.active == 0"))
    print('css selector: ' + calendar_item_selector)
    target_date_btn = browser.find_element(By.CSS_SELECTOR, calendar_item_selector)
    target_date_btn.click()

    # [step3. Order] fill in cellphone number
    WebDriverWait(browser, 20).until(lambda d: d.execute_script("return jQuery.active == 0"))
    cell_phone_textfield = browser.find_element(By.XPATH, '//*[@id="htx_iphone"]')
    cell_phone_textfield.send_keys(personal.cell_phone)

    agree_check_box = browser.find_element(By.XPATH, '//*[@id="agree"]')
    agree_check_box.click()

    confirm_order_btn = browser.find_element(By.XPATH, '//*[@id="form1"]/div[2]/input[1]')
    confirm_order_btn.click()

    # [step4. Personal] fill out personal information
    WebDriverWait(browser, 10).until(lambda d: d.execute_script("return jQuery.active == 0"))
    identification_number_textfield = browser.find_element(By.XPATH, '//*[@id="htx_idnumber"]')
    identification_number_textfield.send_keys(personal.identification_num)

    name_textfield = browser.find_element(By.XPATH, '//*[@id="htx_name"]')
    name_textfield.send_keys(personal.name)

    birthday_textfield = browser.find_element(By.XPATH, '//*[@id="htx_birthday_display"]')
    birthday_textfield.send_keys(personal.birthday)

    mail_textfield = browser.find_element(By.XPATH, '//*[@id="htx_email"]')
    mail_textfield.send_keys(personal.email)

    confirm_personal_information_btn = browser.find_element(By.XPATH, '//*[@id="form1"]/div[2]/input[1]')
    confirm_personal_information_btn.click()

    time.sleep(200)


if __name__ == '__main__':
    start_booking_room()
