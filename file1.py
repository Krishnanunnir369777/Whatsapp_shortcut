from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime as dt
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")

contact =str(input("Enter the name of recipient:"))
text = str(input("Enter the message:"))
print("Enter the time details")
thour=int(input("Hour:"))
tmin=int(input("Minute:"))
n=int(input("Enter number of spams:"))
while True:
    if (thour<=dt.now().hour):
        if (tmin<=int(dt.now().minute)):
            inp_xpath_search = "//input[@title='Search or start new chat']"
            input_box_search = WebDriverWait(driver,100).until(lambda driver: driver.find_element('xpath','''//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p'''))
            input_box_search.click()
            time.sleep(2)
            input_box_search.send_keys(contact)
            time.sleep(2)
            input_box_search.send_keys(Keys.ENTER)

            for i in range(n):
                input_box = driver.find_element('xpath','''//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p''')
                input_box.send_keys(text+ Keys.ENTER )

            A=input("Press any key :")
            driver.quit()

    else:
        pass
