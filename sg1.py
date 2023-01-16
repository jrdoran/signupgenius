# specify the url
# my_url = 'https://www.signupgenius.com/go/70a0e4fa5aa2cabfc1-everglades45#/' 

import time 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#print ("Start : %s" % time.ctime())

import sys
from os import system


  
#url of the page we want to scrape
url = "https://www.signupgenius.com/go/70a0e4fa5aa2cabfc1-everglades45#/"

url ="https://www.signupgenius.com/go/70a0e4fa5aa2cabfc1-everglades48#/"
#print (" ")
print(url)
  
# initiating the webdriver. Parameter includes the path of the webdriver.

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)



#driver = webdriver.Chrome('./chromedriver') 
driver.get(url) 
  
# this is just to ensure that the page is loaded
time.sleep(2) 
  
html = driver.page_source
  
# this renders the JS code and stores all
# of the information in static HTML code.  
# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")


title = soup.select('h1.signup--title-text')[0].text.strip()

print ("Start : %s" % time.ctime() +" ---"+ title )
# <h1 class="signup--title-text ng-binding">Everglades 12/28 or Ezell 12/29 or Rohan 12/30</h1>



all_divs = soup.find('div', {'class' : 'alert alert-danger feedback-error fade-in-up black-shadow-active'})

s =        soup.find('div', {'class' : 'alert alert-danger feedback-error fade-in-up black-shadow-active'})

if s is not None:
    job_profiles = all_divs.find_all('span')

    for job_profile in job_profiles :
        if (job_profile.text == 'This sign up is full and has no more available slots. Please contact the sign up creator for more info.'):
            print('Signup is Full')
    driver.close() # closing the webdriver
else:
    print("Signup is NOT FULL")




exit()
