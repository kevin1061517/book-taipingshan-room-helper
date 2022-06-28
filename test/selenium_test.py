from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

import time

def action_chains_clicks_test():
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s)
    browser.implicitly_wait(10) #隱式等待是一個全局配置，設置後所有元素都會給定這一個時間直到元素出現，等待規定時間沒出現就報錯
    browser.maximize_window()
    browser.get("http://sahitest.com/demo/clicks.htm")

    click_btn = browser.find_element(By.XPATH, '/html/body/form/input[3]')
    double_click_btn = browser.find_element(By.XPATH, '/html/body/form/input[2]')
    right_click_btn = browser.find_element(By.XPATH, '/html/body/form/input[4]')

    ActionChains(browser).click(click_btn).double_click(double_click_btn).context_click(right_click_btn).perform()

    text_value = browser.find_element(By.NAME, 't2').get_attribute('value')
    print(text_value)

    time.sleep(20)
    browser.quit()

# 滑鼠相關事件，可透過 ActionChains 完成簡單的事件處理動作
# ref: https://blog.csdn.net/huilan_same/article/details/52305176
def action_chains_mouseover_test():
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s)
    browser.implicitly_wait(10)  # 隱式等待是一個全局配置，設置後所有元素都會給定這一個時間直到元素出現，等待規定時間沒出現就報錯
    browser.maximize_window()
    browser.get("http://sahitest.com/demo/mouseover.htm")

    write = browser.find_element(By.XPATH, '/html/body/form/input[1]')
    blank = browser.find_element(By.XPATH, '/html/body/form/input[2]')

    result = browser.find_element(By.NAME, 't1')

    action = ActionChains(browser)
    action.move_to_element(write).perform()
    # print(result.get_attribute('value'))

    # action.move_to_element(blank).perform() #同下
    action.move_by_offset(10, 50).perform() #context_click()來看，前次 write 會在該元素的正中央
    print(result.get_attribute('value'))

    action.move_to_element_with_offset(blank, 10, -40).perform() #移動到距離 blank 元素(10, -40)的點，所以可以移到 write
    print(result.get_attribute('value'))

    time.sleep(20)
    browser.quit()

def action_chains_drag_test():
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s)
    browser.maximize_window()
    browser.get('http://sahitest.com/demo/dragDropMooTools.htm')

    dragger = browser.find_element(By.ID, 'dragger')
    item1 = browser.find_element(By.XPATH, '/html/body/div[2]')
    item2 = browser.find_element(By.XPATH, '/html/body/div[3]')
    item3 = browser.find_element(By.XPATH, '/html/body/div[4]')
    item4 = browser.find_element(By.XPATH, '/html/body/div[5]')

    action = ActionChains(browser)
    action.drag_and_drop(dragger, item1).perform() #拖曳到某座標然後鬆開
    time.sleep(2)
    action.click_and_hold(dragger).release(item2).perform() #點滑鼠左鍵並不鬆開，release到某元素鬆開左鍵
    time.sleep(2)
    action.click_and_hold(dragger).move_to_element(item3).release().perform()
    time.sleep(2)
    # action.drag_and_drop_by_offset(dragger, 400, 150).perform()
    action.click_and_hold(dragger).move_by_offset(400, 150).release().perform()#與前句相同，移動到指定座標
    time.sleep(2)
    browser.quit()

def action_chains_keypress_test():
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s)
    browser.maximize_window()
    browser.get('http://sahitest.com/demo/keypress.htm')

    key_up_radio = browser.find_element(By.ID, 'r1')
    key_down_radio = browser.find_element(By.ID, 'r2')
    key_press_radio = browser.find_element(By.ID, 'r3')

    result_text = browser.find_element(By.XPATH, '/html/body/form/input[1]')
    enter_text = browser.find_element(By.XPATH, '/html/body/form/input[2]')

    #監測 key_down
    key_down_radio.click()
    ActionChains(browser).key_down(Keys.CONTROL, enter_text).key_up(Keys.CONTROL).perform()
    print(result_text.get_attribute('value'))
    time.sleep(5)

    #監測 key_up
    key_up_radio.click()
    enter_text.click()
    ActionChains(browser).key_down(Keys.SHIFT).key_up(Keys.SHIFT).perform()
    print(result_text.get_attribute('value'))
    time.sleep(5)

    #監測 key_press
    key_press_radio.click()
    enter_text.click()
    ActionChains(browser).send_keys('a').perform()
    print(result_text.get_attribute('value'))

    time.sleep(30)
    browser.quit()

# key_down 按下鍵盤某個鍵 / key_up 鬆掉鍵盤上某個鍵
def action_chains_combo_keypress_test():
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s)
    browser.maximize_window()
    browser.get('https://sahitest.com/demo/label.htm')

    username_1 = browser.find_element(By.XPATH, '/html/body/label[1]/input')
    username_2 = browser.find_element(By.XPATH, '/html/body/label[2]/table/tbody/tr/td[2]/input')

    action = ActionChains(browser)
    username_1.click()
    action.send_keys('Test Keys').perform()
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform() #等同於 ctrl + a
    action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform() #等同於 ctrl + c
    time.sleep(5)

    action.key_down(Keys.CONTROL, username_2).send_keys('v').key_up(Keys.CONTROL).perform() # ctrl + v
    time.sleep(5)

    print(username_1.get_attribute('value'))
    print(username_2.get_attribute('value'))

    browser.quit()

def start_browser():
    options = Options()
    options.add_argument("--disable-notifications") #取消網頁中的彈出視窗

    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s, options=options)
    browser.get("https://shopee.tw/")

    try:
        # ===========等待直到某個元素被渲染===========
        # 會等待10秒來找到並返回元素，否則會拋 TimeoutException
        # element = WebDriverWait(browser, 10).until(lambda browser: browser.find_element(By.CSS_SELECTOR, '.shopee-popup__close-btn'))
        # print(element)
        # WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.ID, "myDynamicElement")))
        # browser.maximize_window()
        # WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located(
        #     By.XPATH('//*[@id="main"]/div/div[2]/div[2]/shopee-banner-popup-stateful//div/div/div/div/div')))
        # ===========END 等待直到某個元素被渲染===========

        login_btn = browser.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[1]/div/ul/a[3]')
        print(login_btn, login_btn.size, login_btn.location)
        login_btn.click()
        #https://stackoverflow.com/questions/57741875/selenium-common-exceptions-elementclickinterceptedexception-message-element-cl
        browser.execute_script("arguments[0].click();", login_btn)
        # browser.execute_script("arguments[0].click();arguments[1].click();", userName, password)

        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(100)
        # with open('test.txt', 'w', encoding='utf-8') as f:
        #     f.write(browser.page_source)
    except:
        print('Unable to locate element')
    finally:
        browser.quit()

if __name__ == '__main__':
    action_chains_combo_keypress_test()