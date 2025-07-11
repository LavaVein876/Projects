from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from user_information import username, password
import time

# The lines below contains the url, the wait variable which is used for timeouts and it also has the path of the driver
ser = Service(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
url = "https://www.instagram.com/"
driver.get(url)
wait = WebDriverWait(driver, 10)

# These lines will input the username of the Instagram account
username0 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/main/article/div[2]'
                                                                   '/div[1]/div/form/div/div[1]/div/label/input')))
username0 = username0.send_keys(username)

# These lines will input the password of the user's account
password0 = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]'
                                          '/div/label/input')
password0 = password0.send_keys(password)

# This will click the login button
login = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]'
                                      '/button/div').click()

# These lines will bring us to the user's account and select the following tab
profile_tab = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div'
                                                                     '/div[3]/div/div[6]/div[1]/span/img'))).click()
profile = driver.find_element(By.XPATH,
                              '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]'
                              '/div[2]/a[1]/div').click()
following_tab = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/main/div/header/'
                                                                       'section/ul/li[3]/a/div'))).click()

time.sleep(15)

# This variable will be used to carry out all mouse like actions
action = ActionChains(driver)

# This loop will iterate through the following tabs to retrieve the users
for i in range(270):
    scroll1 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div/div[3]')))
    action.move_to_element(scroll1)
    action.click_and_hold(scroll1).send_keys(Keys.END).perform()
    time.sleep(0.9)

# These lines will take the names of the following tab users and store it in a list
list1 = []
persons_from_following_tab = driver.find_elements(By.CLASS_NAME, 'notranslate')
for following in persons_from_following_tab:
    list1.append(following.get_attribute('title'))

# These lines will close the following tab, refresh the page and open the followers tab
close_following_persons_tab = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[1]/div/div[3]/div'
                                                            '/button').click()
for n in range(2):
    time.sleep(2)
    driver.refresh()

time.sleep(20)
followers_tab = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/main/div/header/'
                                                                       'section/ul/li[2]/a/div'))).click()

# This loop will iterate through the followers tabs to retrieve the users
for j in range(270):
    scroll2 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div/div[2]')))
    action.move_to_element(scroll2)
    action.click_and_hold(scroll2).send_keys(Keys.END).perform()
    time.sleep(0.9)

# These lines will take the names of the followers tab users and store it in a list
list2 = []
persons_from_followers_tab = driver.find_elements(By.CLASS_NAME, 'notranslate')
for followers in persons_from_followers_tab:
    list2.append(followers.get_attribute('title'))

# This line will close the followers tab
close_followers_persons_tab = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[1]/div/div[3]/div'
                                                            '/button').click()

# This variable will compare the 2 lists and output the users who aren't following back
non_followers = list(set(list1) - set(list2))

# This is a whitelist of users who you don't want to be unfollowed
try:
    non_followers.remove("champagnepapi")
    non_followers.remove("pajamabillionaire")
    non_followers.remove("alstonbillionaire")
except ValueError:
    print("user was not found in the list")

non_followers.sort()
time.sleep(20)
print(non_followers, "\n")

# The following lines will determine if the user would like to unfollow the users and carry it out if so
ques = input("Would you like to unfollow the users? ").lower()
if ques in ["yes", "y"]:
    for user in non_followers[0:15]:
        search = wait.until((EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')))).send_keys(user)
        try:
            select_user = wait.until(
                (EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/nav/div'
                                                             '[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div')))).click()
        except TimeoutError:
            print("User's account no longer exist")
            driver.refresh()

        time.sleep(1)
        try:
            tab = wait.until((EC.visibility_of_element_located((By.XPATH, "//button[@class='_5f5mN    -fzfL     _6VtSN     yZn4P   ']")))).click()
        except TimeoutError:
            print("Already unfollowed user")

        time.sleep(1)
        unfollow = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'aOOlW'))).click()
        time.sleep(4)
        driver.refresh()
        time.sleep(1)
    print("The users has now been unfollowed")
else:
    print("Have a good day")