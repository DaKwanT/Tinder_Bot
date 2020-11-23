from selenium import webdriver
from time import sleep

from secrets import username, password

class tinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):

        self.driver.get('https://tinder.com/')

        sleep(8)
        
        fb_btn = self.driver.find_elements_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/div[2]/button', '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()
        
        fb_login = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_login.click()
        
        #Switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

       

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        p_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        p_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]') 
        login_btn.click()

        self.driver.switch_to_window(base_window)

        sleep(3)

        popup_loc = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        popup_loc.click()

        popup_notif = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_notif.click()

        
  
    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()
        

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()
        
        

    def auto_swipe(self):
        while True:
            sleep(0.5)

            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_noLikes()


                    
    def close_popup(self):
        popup_addHome = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_addHome.click()
    
    def close_noLikes(self):
        noThanks_btn = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        noThanks_btn.click()


        



bot = tinderBot()
bot.login()
sleep(10)
bot.auto_swipe()






  