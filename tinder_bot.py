from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
    def login(self):
        self.driver.get('https://www.tinder.com/')
        
        sleep(5)
        if (self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')):
            more_opt_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
            more_opt_btn.click()
        # fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        # fb_btn.click()
                                                        
        # google_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
        # google_btn.click()

        ## SWITCHING TO THE LOGIN POPUP 
        # main_window = self.driver.window_handles[0]
        # self.driver.switch_to.window(self.driver.window_handles[1])

        ## FOR FACEBOOK LOGIN
        # email_ip = self.driver.find_element_by_xpath('//*[@id="email"]') 
        # email_ip.send_keys('email_ID')
        # pass_ip = self.driver.find_element_by_xpath('//*[@id="pass"]')
        # pass_ip.send_keys('password')
        # login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]') 
        # login_btn.click()

        ## FOR GOOGLE LOGIN
        # email_ip = self.driver.find_element_by_xpath('//*[@id="identifierId"]') 
        # email_ip.send_keys('vapatwa2004')
        # next_btn_1 = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
        # next_btn_1.click()
        # sleep(3)
        # pass_ip = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        # pass_ip.send_keys('ghostrider007')
        # next_btn_2 = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
        # next_btn_2.click()

        ## FOR PHONE LOGIN
        phone_no_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
        phone_no_btn.click()
        sleep(1)
        phone_no_ip = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
        phone_no_ip.send_keys('9819945941')
        continue_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        continue_btn.click()

bot = TinderBot()
bot.login()