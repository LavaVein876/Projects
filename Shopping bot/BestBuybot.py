# BestBuy shopping bot by: LavaVein

# from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Creating path for the URl to be launched in Chrome
ser = Service(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
url = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-ti-12gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6462956.p?skuId=6462956"
driver.get(url)
#driver.maximize_window()

# A class for a timeout so that the following elements has loaded before webdriver does the required actions
wait = WebDriverWait(driver, 10)

# Selecting US as the store
click1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[2]/a[2]/img')
click1.click()

buyButton = False

while not buyButton:
    try:  # Checking if buy button is available and if not the page refreshes
        addToCartBtn = driver.find_element(By.XPATH, '/html/body/div[3]/main/div[2]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div/button')
        print("Button isn\'t ready yet.")
        time.sleep(1)
        driver.refresh()
    except:  # If button is available it will be added to the cart
        addToCartBtn = driver.find_element(By.CLASS_NAME, 'add-to-cart-button').click()
        print("Button was clicked\nadding item to cart")
        buyButton = True


# Waiting for the window element to be visible so that it brings us to the cart
goto_cart = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[8]/div/div[1]/div/div/div/div/div[1]/div[3]/a')))
goto_cart.click()

# Waiting for the element to be visible so that it brings us to check out
check_out = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
check_out.click()

# Waiting for the element to be visible so that it continues as a guest
con_guest = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/section/main/div[2]/div[4]/div/div[2]/button')))
con_guest.click()

try:  # tries to select shipping
    switchShipping = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[2]/div[2]/div/div/a')))
    switchShipping.click()

except:
    print("SHIPPING ALREADY SELECTED OR IS NOT AVAILABLE")

finally:  # Following lines of code will be for the shipping and contact info
    first_name = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/form/div[1]/div/label/input')))
    first_name = first_name.send_keys("Alrick")

    last_name = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/form/div[2]/div/label/input')
    last_name = last_name.send_keys("Birch")

    address = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/form/div[3]/div[2]/label/div[2]/div/input')
    address = address.send_keys("241-24 148th Ave")

    city = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/form/div[5]/div[1]/div/label/input')
    city = city.send_keys("Queen")

    state = driver.find_element(By.XPATH, '//*[@id="state"]').click()
    state_sel = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/form/div[5]/div[2]/div/label/div[2]/select/option[38]')
    state_sel.click()

    zipcode = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/form/div[6]/div/div[1]/div/label/input')
    zipcode = zipcode.send_keys("11422")

    email = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[2]/label/div/input')
    email = email.send_keys("jonathan@gmail.com")

    phone_number = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[3]/label/div/input')
    phone_number = phone_number.send_keys("646 807 9958")

    check_box1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[4]/span/div/label')
    check_box1.click()

    con_pay_info = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button')
    con_pay_info.click()

    try:  # If alert pops to reconfirm shipping details
        alert = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[1]/div/div/div/div')))
        time.sleep(1.5)
        con_pay_info.click()

    except:
        print("THERE WAS NO ALERT TO RECONFIRM ADDRESS")

    finally:

        # The following lines of code will be the payment info
        card = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div[1]/div/section/div[1]/div/input')))
        card = card.send_keys("4916807182855836")

        exp_date = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div[1]/div/section/div[2]/div[1]/div/div[1]/label/div/div/select').click()
        exp_date_sel = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div[1]/div/section/div[2]/div[1]/div/div[1]/label/div/div/select/option[9]')
        exp_date_sel.click()

        exp_year = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div[1]/div/section/div[2]/div[1]/div/div[2]/label/div/div/select').click()
        exp_year_sel = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div[1]/div/section/div[2]/div[1]/div/div[2]/label/div/div/select/option[5]')
        exp_year_sel.click()

        cvv_code = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div[1]/div/section/div[2]/div[2]/div/div[2]/div/input')
        cvv_code = cvv_code.send_keys("876")

        # These line will be placing the order
        place_order = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[3]/div/div[2]/button')
        place_order.click()
