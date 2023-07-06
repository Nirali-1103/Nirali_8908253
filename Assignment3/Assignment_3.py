# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Linked in Learning
driver.get("https://www.linkedin.com/learning/")
time.sleep(2)

# Finding the search bar and entering text
search_bar = driver.find_element("xpath","/html/body/header/nav/section/section[3]/form/section/input")
search_bar.send_keys("Python")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(2)

# Verifying that the search results page has loaded
assert "Python" in driver.title

# Selecting a video from the search results
video_link = driver.find_element("xpath","/html/body/div/div[2]/main/section/ul/li[1]/div/a")
video_link.click()

# Waiting for the searched subject details page to load
time.sleep(2)

# Verifying that the text is Python (Programming Language)
video_text = driver.find_element("xpath","/html/body/main/section[1]/div/section[2]/div/ul/li/a")
assert video_text.text == "Python (Programming Language)"

# Verifying that the rating is > 4
rating_video_text = driver.find_element("xpath","/html/body/main/section[1]/div/section[5]/div/div/section/div[1]/h3/span[1]")
assert float(rating_video_text.text) > 4.0

# Closing the webdriver
driver.close()
