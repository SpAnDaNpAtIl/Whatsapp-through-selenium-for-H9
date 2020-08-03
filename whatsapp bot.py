import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from database import *



def send_message(number, array):
    try:
        sleep(3)
        browsing_session.switch_to.alert().accept()
    except Exception as e:
        pass
    
    
    user_page_link = 'https://web.whatsapp.com/send?phone=' + str(number) + '&source=&data=#'
    user_page = browsing_session.get(user_page_link)
    sleep(5) #lets pause the code for 5 seconds so that user_page session gets loaded in the meantime
    typing_chat = browsing_session.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') 
    #can try searching tags to chat typing section also.
    for i in array[:len(array)-1]:
        typing_chat.send_keys(i)
        typing_chat.send_keys(Keys.SHIFT, Keys.ENTER)
        
        
    typing_chat.send_keys(array[len(array)-1])
    typing_chat.send_keys(Keys.ENTER)
    
    
    

if __name__ == "__main__":
    browsing_session = webdriver.Chrome() #session created
    browsing_session.get("https://web.whatsapp.com")
    sleep(15) #lets pause the next computing for 15 seconds so that we can log in into whatsapp web
    

    for i in database:
        send_message(i[1], sep_newline)
        
    