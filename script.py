from notifier_botty import login_to_chegg, refresh_chegg, telegram_bot_sendtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timedelta
import pytz
import requests

username = "rahulchegg5@gmail.com"
password = "Author@05"
user_bot_chatID = '1155462778'
account_name = "Rahul"
accept_option = True
start_time = 0                   #Stating time. Default 0. In 24 hour format
end_time = 25                    #Stating time. Default 25. In 24 hour format




flag_login = True
user_bot_token = '8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM'  #Chegg notifier bot


# Set up the Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

while flag_login:
   flag_login = login_to_chegg(username,password,driver,account_name)
   
refresh_chegg(driver,accept_option,start_time,end_time,user_bot_token,user_bot_chatID,account_name)
