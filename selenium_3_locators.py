# ID, Name, CLassname, Tag name, Css, Xpath
from selenium import webdriver
from selenium.webdriver.common.by import By

# By >> Locators 
driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/default.asp")

# return type >> List
a_tag_data = driver.find_elements(By.TAG_NAME,"a")

# 1,10, [i for i in range(1,11)]
a_tag_data = [i.text for i in a_tag_data]
a_tag_data = [i.lower() for i in a_tag_data]
temp = []
for i in a_tag_data:
    if "html" in i:
        temp.append(i)

# l1 = []
# for i in a_tag_data:
#     l1.append(i.text)
print(temp)

