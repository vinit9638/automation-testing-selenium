from selenium import webdriver
from selenium.webdriver.common.by import By

# Test case >>> Test script >> Script
# TEst Id 

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
# Link Text locator >> Find elemenet with help of text present in the anchor tag.

# Write a code to check navigation bar
l1 = driver.find_elements(By.TAG_NAME,"li")
# l2 = driver.find_elements(By.TAG_NAME,"a")
l1 = [i.text for i in l1]
print(l1)
l2 = []
for i in l1:
    if i.isupper():
        l2.append(i)
        
for i in l2:
    driver.find_element(By.LINK_TEXT, i).click()
    driver.back()


# back(), Forward(), Refresh()