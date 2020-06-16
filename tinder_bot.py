from pyotp import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from config import google_username, google_password, google_auth_secret_code

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
    def login(self):
        self.driver.get('https://www.tinder.com/')
        
        sleep(3)
        # if (self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')):
        #     more_opt_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
        #     more_opt_btn.click()
        # fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        # fb_btn.click()
                                                        
        google_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
        google_btn.click()
        # sleep(3)
        ## SWITCHING TO THE LOGIN POPUP 
        main_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        ## FOR FACEBOOK LOGIN
        # email_ip = self.driver.find_element_by_xpath('//*[@id="email"]') 
        # email_ip.send_keys('email_ID')
        # pass_ip = self.driver.find_element_by_xpath('//*[@id="pass"]')
        # pass_ip.send_keys('password')
        # login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]') 
        # login_btn.click()

        ## FOR GOOGLE LOGIN
        email_ip = self.driver.find_element_by_xpath('//*[@id="identifierId"]') 
        email_ip.send_keys(google_username)
        next_btn_1 = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
        next_btn_1.click()
        sleep(1.6)
        pass_ip = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        pass_ip.send_keys(google_password)
        next_btn_2 = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
        next_btn_2.click()

        ## FOR PHONE LOGIN
        # phone_no_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
        # phone_no_btn.click()
        # sleep(1)
        # phone_no_ip = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
        # phone_no_ip.send_keys('phone_number')
        # continue_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        # continue_btn.click()

        ### Using Google Authenticator
        ## FOR GOOGLE
        sleep(1.5)
        auth_ip = self.driver.find_element_by_xpath('//*[@id="totpPin"]')
        totp = TOTP(google_auth_secret_code)
        token = totp.now()
        print (token)
        auth_ip.send_keys(token)
        next_btn_3 = self.driver.find_element_by_xpath('//*[@id="totpNext"]')
        next_btn_3.click()

        # Switch back to main window
        self.driver.switch_to.window(self.driver.window_handles[0])

        sleep(8)
        loc_allow = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
        loc_allow.click()
        notif_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span')
        notif_btn.click()
        if (self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[2]/button')):
            privacy_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[2]/button')
            privacy_btn.click()
            sleep(.7)
            refuse_all_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/div[2]/button')
            refuse_all_btn.click()
            
        

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        from random import random
        left_count, right_count = 0,0
        # sleep(7)
        while True:
            sleep(1)
            try:
                rand = random()
                if not (self.driver.find_elements_by_class_name('recsCardboard__cards') ):
                    self.msg_new_mathces()
                elif rand < .79:
                    self.like()
                    right_count += 1
                    print('{} right swipes have been made'.format(right_count))
                else:
                    self.dislike()
                    left_count += 1
                    print('{} left swipes have been made'.format(left_count))
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except:
                        self.close_out_likes()
                        self.driver.quit()


    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()
    
    def close_out_likes(self):
        out_of_likes_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        out_of_likes_popup.click()

    def msg_new_mathces(self):
        matches = self.driver.find_elements_by_class_name('matchListItem')[1:]
        matches[0].click()
        text_ip = bot.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
        text_ip.send_keys('Hey, 2 truths one lie?')
        send_msg_btn = bot.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button/span')
        send_msg_btn.click()

bot = TinderBot()
bot.login()