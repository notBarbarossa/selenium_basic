from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from user_agent import generate_user_agent
import time

useragent = generate_user_agent(device_type="desktop")

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent}")
options.add_argument("--disable-blink-features=AutomationControlled")

url = "https://www.instagram.com/"

driver_service = Service(executable_path="D:\PyCharm\PROJECTS\smth\Chromedriver\chromedriver.exe")
driver = webdriver.Chrome(
    service=driver_service,
    options=options
)

try:
    driver.get(url=url)
    time.sleep(2)

    username_input = driver.find_element("name", "username")
    username_input.clear()
    username_input.send_keys("asd")
    time.sleep(2)

    password_input = driver.find_element("name", "password")
    password_input.clear()
    password_input.send_keys("123asd")
    time.sleep(3)
    password_input.send_keys(Keys.ENTER)
    time.sleep(3)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
