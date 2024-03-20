# simple chatter!
# do read the readme, it explains a lot of what you'll need and what's going on here

# imports
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located as appeared
from selenium.webdriver.firefox.options import Options

# headless firefox
oppy=Options()
oppy.add_argument('-headless')
browser=webdriver.Firefox(options=oppy)
browser.get('https://you.com/?chatMode=default')
query_number=0

# query, answer fetch, and self-delete
def query(message):
    global query_number
    browser.find_element('xpath','//*[@id="search-input-textarea"]').send_keys(message+"\ue006")
    query_number+=1
def answer():
    p = f"/html/body/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[{2*query_number}]/div/div[2]"
    pb = r"/html/body/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/button"
    wait(browser,10).until(appeared(['xpath',pb]))
    wait(browser,60).until_not(appeared(['xpath',pb]))
    return browser.find_element('xpath',p).text
def __del__():
    browser.quit()

# looooop
while True:
    query(input('::: '))
    print(f'--> {answer()}')

# TODO develop tkinter ui
