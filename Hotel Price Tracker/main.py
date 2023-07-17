from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service


TRAVEL_URL = "https://www.oyorooms.com/"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScxs64sDSkU61LhKjV3GVmaOMlpHzS9eygBh0i8oBpzzJZ95w/viewform?usp=sf_link"

area = input("Enter the area you want to: ")

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(TRAVEL_URL)

search_bar = driver.find_element(By.XPATH, '//*[@id="autoComplete__home"]')
search_bar.send_keys(area)
driver.implicitly_wait(5)
first_suggestion = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div[3]/div/div[1]/div/div[1]/div/span/div/div/div[1]/div/div[2]/span')
first_suggestion.click()
driver.implicitly_wait(2)
search_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div[3]/div/div[1]/div/div[4]/button')
search_btn.click()

# driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div[3]/div/div/div/div[1]/div/div/form/div/div').click()
driver.implicitly_wait(5)


Hotel_names = driver.find_elements(By.CLASS_NAME, "listingHotelDescription__hotelName")
Hotel_links = driver.find_elements(By.CLASS_NAME, "c-nn640c")
Hotel_prices = driver.find_elements(By.CLASS_NAME, "listingPrice__finalPrice")



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(FORM_URL)


for i in range(len(Hotel_names)):
    location = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    location.send_keys(area)
    name.send_keys(Hotel_names[i].text)
    driver.implicitly_wait(1)
    price.send_keys(Hotel_prices[i].text)
    driver.implicitly_wait(1)
    link.send_keys(Hotel_links[i].get_attribute("href"))
    submit.click()
    driver.implicitly_wait(2)
    submit_another = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another.click()
    driver.implicitly_wait(5)


driver.quit()