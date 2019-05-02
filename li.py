from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.parse
import time

class LinkedIn:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        driver = self.driver
        driver.get("https://www.linkedin.com/uas/login?trk=guest_homepage-basic_nav-header-signin")
        driver.find_element_by_id("username").send_keys(self.username)
        driver.find_element_by_id("password").send_keys(self.password)
        driver.find_element_by_css_selector(".btn__primary--large.from__button--floating").click()

    def message(self):

        driver = self.driver

        query = input("Search for? ")
        search = urllib.parse.quote(query)

        website = ("https://www.linkedin.com/search/results/people/?facetNetwork=%5B%22F%22%5D&keywords=" + search + "&origin=FACETED_SEARCH")

        driver.get(website)

        driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/2);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, 0);")

        names = driver.find_elements_by_css_selector(".name.actor-name")
        occs = driver.find_elements_by_css_selector(".subline-level-1.t-14")
        message_buttons = driver.find_elements_by_css_selector(".search-result__actions--primary")

        first_names = []
        count = 0

        for name in names:
            name = name.text
            first_names.append(name[0:name.index(" ")])

        for i in range(len(first_names)):
            message_buttons[i].click()
            script = "Hi " + first_names[i] + ", I see that you are a " + occs[i].text + " I would love to discuss your career further"
            driver.find_element_by_css_selector(".msg-form__contenteditable").send_keys(script)
            if count == 0:
                time.sleep(1.5)
            else:
                time.sleep(.3)
            driver.find_element_by_css_selector(".msg-overlay-bubble-header__control.js-msg-close").click()
            driver.find_element_by_css_selector(".mlA.mr3.artdeco-button").click()
            count+=1


if __name__ == "__main__":

    username = "USERNAME"
    password = "PASSWORD"

    ig = LinkedIn(username, password)
    ig.login()
    ig.message()
