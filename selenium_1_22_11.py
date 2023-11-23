# import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def login_script(user,password):
    driver.find_element(By.ID, "username").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()

    actual_value = driver.find_element(By.CLASS_NAME,"post-title").text
    actual_value = actual_value.lower()
    # Actual, Expected , Logged in successful
    exp_valu = "success"
    if exp_valu in actual_value:
        status = True
    else:
        status = False
    return status
 


usernames = ["u1","u2","u3"]
passwords = ["p1","p2","p3"]

num = 0
for i in range(len(usernames)):
    login_script(usernames[i],passwords[i])




driver.get("https://practicetestautomation.com/practice-test-login/" )



# id_name = "student"



# def open_url(url):
#     d = webdriver.Chrome()
#     d.get(url)







