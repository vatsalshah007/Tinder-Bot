# Tinder-Bot
This tinder bot automatically likes the profiles on your behalf.


**NOTE: This bot only works over __Chrome web-browser__.**

To run 

First download the Chromedriver, unzip and  move to your desired location (Windows)

Then install Selenium using:
- `pip install selenium`

To Login using Google Account, replace:

```
fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
fb_btn.click()
```

with 

```
google_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
google_btn.click()
```
and 
 
```
## FOR FACEBOOK LOGIN
email_ip = self.driver.find_element_by_xpath('//*[@id="email"]') 
email_ip.send_keys('email_ID')
pass_ip = self.driver.find_element_by_xpath('//*[@id="pass"]')
pass_ip.send_keys('password')
login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]') 
login_btn.click()
```

with

```
## FOR GOOGLE LOGIN
email_ip = self.driver.find_element_by_xpath('//*[@id="identifierId"]') 
email_ip.send_keys('vapatwa2004')
next_btn_1 = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
next_btn_1.click()
sleep(3)
pass_ip = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
pass_ip.send_keys('ghostrider007')
next_btn_2 = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
next_btn_2.click()
```       

To Login using Phone number, replace FB Login code from above with

```
## FOR PHONE LOGIN
phone_no_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
phone_no_btn.click()
sleep(1)
phone_no_ip = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
phone_no_ip.send_keys('9819945941')
continue_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
continue_btn.click()
```

and remove

```
## SWITCHING TO THE LOGIN POPUP 
main_window = self.driver.window_handles[0]
self.driver.switch_to.window(self.driver.window_handles[1])
```
**If you do not use 2FA on your account then comment the following code:**
```
sleep(1.5) 
gauth_btn = bot.driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[2]/div')
gauth_btn.click()
sleep(1.5)
auth_ip = bot.driver.find_element_by_xpath('//*[@id="totpPin"]')
totp = TOTP('secret code')
token = totp.now()
print (token)
auth_ip.send_keys(token)
next_btn_3 = bot.driver.find_element_by_xpath('//*[@id="totpNext"]')
next_btn_3.click()
```

