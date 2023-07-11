# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Linked in Learning
driver.get("https://www.linkedin.com/learning/")
time.sleep(5)

# Finding the search bar and entering text
search_bar = driver.find_element("xpath","/html/body/header/nav/section/section[3]/form/section/input")
search_bar.send_keys("Python")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "Python" in driver.title

# Selecting a video from the search results
video_link = driver.find_element("xpath","/html/body/div/div[2]/main/section/ul/li[1]/div/a")
video_link.click()

# Waiting for the searched subject details page to load
time.sleep(5)

# playing video
play_video = driver.find_element("xpath","/html/body/main/section[1]/section/section/a/span/span")
play_video.click()

# Waiting for the searched subject details page to load
time.sleep(5)

# moving to exercise files details
exercise_files = driver.find_element("xpath","/html/body/main/section[1]/div/div/ul/li[2]/button")
exercise_files.click()

# Waiting for the searched subject details page to load
time.sleep(5)

# Getting back to preview page of course
back_to_preview_page = driver.find_element("xpath","/html/body/main/section[1]/section/section/div/div/div/h2/a")
back_to_preview_page.click()

# Waiting for the searched subject details page to load
time.sleep(2)

# Verifying that the rating is > 4
rating_video_text = driver.find_element("xpath","/html/body/main/section[1]/div/section[5]/div/div/section/div[1]/h3/span[1]")
assert float(rating_video_text.text) > 4.0

# Closing the webdriver
driver.close()
