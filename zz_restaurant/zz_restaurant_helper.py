from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
from personal import Personal

personal = Personal('方楷文', '0912345678', 'F129123456', '1995-07-30', 'kevin1061517@gmail.com')
personal.to_string()

def launch_browser():
    target_url = 'https://inline.app/booking/-MH9cm9freYOfdgFI1hj:inline-live-1/-MH9cmKqsdXvWHuA2sUw?language=zh-tw'
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s)

    while True:
        current_time = time.localtime()
        print("Current Time =", time.strftime("%H:%M:%S", current_time))
        if time.strftime("%H:%M:%S", current_time) == '16:00:01':
            break

    browser.get(target_url)
    browser.implicitly_wait(1)

    # Party size
    adult_picker_select = Select(browser.find_element(By.ID, 'adult-picker'))
    adult_picker_select.select_by_value('2')

    # Dining date
    date_select = browser.find_element(By.ID, 'date-picker')
    browser.execute_script("arguments[0].click();", date_select)
    browser.implicitly_wait(1)
    print('prepare date picker')

    # Date picker choose
    target_date_picker = browser.find_element(By.CSS_SELECTOR, '.sc-bdvvtL.DiIbn div[data-date="2022-07-12"]')
    browser.execute_script("arguments[0].click();", target_date_picker)
    browser.implicitly_wait(1)

    # Time picker choose
    target_datetime_choose = browser.find_element(By.CSS_SELECTOR, 'button[data-cy="book-now-time-slot-box-22-30"]')
    browser.execute_script("arguments[0].click();", target_datetime_choose)

    browser.implicitly_wait(1)
    reserve_button = browser.find_element(By.CSS_SELECTOR, '#book-now-action-bar button[data-cy="book-now-action-button"]')
    browser.execute_script("arguments[0].click();", reserve_button)

    # contact info
    browser.implicitly_wait(1)
    # Name
    name_textfield = browser.find_element(By.ID, 'name')
    name_textfield.send_keys(personal.name)
    # Gender
    male_radio_btn = browser.find_element(By.ID, 'gender-male')
    browser.execute_script("arguments[0].click();", male_radio_btn)
    # mobile phone number
    phone_textfield = browser.find_element(By.ID, 'phone')
    phone_textfield.send_keys(personal.cell_phone)
    # Email
    email_textfield = browser.find_element(By.ID, 'email')
    email_textfield.send_keys(personal.email)
    # Occasion
    purpose_checkbox = browser.find_element(By.CSS_SELECTOR, 'div[value="約會"]')
    browser.execute_script("arguments[0].click();", purpose_checkbox)
    # Confirm checkbox
    read_radio_btn = browser.find_element(By.ID, 'privacy-policy')
    browser.execute_script("arguments[0].click();", read_radio_btn)
    # Submit reservation
    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    browser.execute_script("arguments[0].click();", submit_btn)

    time.sleep(200)

if __name__ == '__main__':
    launch_browser()

# def launch_browser_test():
#     target_url = 'https://inline.app/booking/-M3EeVvJKvBxkhOv34U9:inline-live-1?language=zh-tw'
#     s = Service(ChromeDriverManager().install())
#     browser = webdriver.Chrome(service=s)
#
#     while True:
#         current_time = time.localtime()
#         print("Current Time =", time.strftime("%H:%M:%S", current_time))
#         if time.strftime("%H:%M:%S", current_time) == '10:27:00':
#             break
#
#     browser.get(target_url)
#
#     browser.implicitly_wait(1)
#     adult_picker_select = Select(browser.find_element(By.ID, 'adult-picker'))
#     adult_picker_select.select_by_value('4')
#
#     # WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "date-picker"))).click().send_keys('01/15/2021')
#     date_select = browser.find_element(By.ID, 'date-picker')
#     browser.execute_script("arguments[0].click();", date_select)
#     # date_select.click()
#     # select by visible text
#     # select.select_by_visible_text('Banana')
#     print('prepare date picker')
#     browser.implicitly_wait(1)
#
#     target_date_picker = browser.find_element(By.CSS_SELECTOR, '.sc-bdvvtL.DiIbn div[data-date="2022-07-09"]')
#     browser.execute_script("arguments[0].click();", target_date_picker)
#     browser.implicitly_wait(1)
#
#
#     target_date_choose = browser.find_element(By.CSS_SELECTOR, 'div[data-key="-M3EeiiaH1mtp12EYHOf"] button[aria-label="2022-07-09 11:00"]')
#     browser.execute_script("arguments[0].click();", target_date_choose)
#
#     time.sleep(200)