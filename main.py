from selenium import webdriver
from time import sleep

PATH = r"C:\Program Files (x86)\chromedriver.exe"
my_username = 'runbypython'
my_pw = 'python37'
my_search = 'cars'

class InstaBot:
    def __init__(self, username, pw):
        # Initialize chrome webdriver
        self.driver = webdriver.Chrome(PATH)
 
        # Open up instagram
        self.driver.get("https://instagram.com")
        sleep(2)

        # Input user info
        username_bar = self.driver.find_element_by_xpath("//input[@name=\"username\"]")
        password_bar = self.driver.find_element_by_xpath("//input[@name=\"password\"]")
        submit_button = self.driver.find_element_by_xpath('//button[@type="submit"]')
        username_bar.send_keys(username)
        password_bar.send_keys(pw)
        submit_button.click()
        sleep(4)

        # Click through pop up window after logging in
        pop_up_window = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
        pop_up_window.click()
        sleep(2)


    def like_pictures(self, search):
        # Input your search key into search bar
        search_bar = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        search_bar.send_keys(search)
        sleep(2)
        
        # Click the tag that pops up for your search key
        tag = self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(search))
        tag.click()
        sleep(2)
       
        # Scroll through page so pictures load
        for i in range(1,3):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Javascript for scrolling
            sleep(2)
        
        # Gather the links of each post in view
        hrefs = self.driver.find_elements_by_tag_name('a')
        post_links = []
        for i in hrefs:
            href = i.get_attribute('href')
            if "/p" not in href:
                continue
            # print links to each post
            print(href) 
            post_links.append(href)

        # Like the post by going to links of each post just gathered
        for post_link in post_links:
            self.driver.get(post_link)
            like_button = self.driver.find_element_by_class_name("_8-yf5")
            like_button.click()
            # sleep for 20 seconds to avoid liking too many posts too fast i.e. instagram noticing suspicious activity
            sleep(20)  
        
my_bot = InstaBot(my_username, my_pw)
my_bot.like_pictures(my_search)