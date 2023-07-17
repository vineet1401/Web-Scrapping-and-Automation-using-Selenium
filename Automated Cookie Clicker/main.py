from selenium.webdriver.common.by import By
import time
from selenium import webdriver

source_path = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome("")

driver.get(source_path)

cookie = driver.find_element(By.ID, "cookie")

ids = driver.find_elements(By.CSS_SELECTOR, "store div")
id = [id.get_attribute("id") for id in ids]


timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    #every 5 Seconds
    if(time.time() > timeout):

        # convert b in integar price
        store_item_prices = driver.find_elements(By.CSS_SELECTOR, "store  b")
        item_price = []
        for item in store_item_prices:
            price = item.text
            if(price != ""):
                item_price.append(int(price.split("-")[1].strip().replace(",", "")))

        # create dictionary of store items and ids
        cookie_dict = {}
        for n in range(len(item_price)):
            cookie_dict[item_price[n]] = id[n]

        # get current cookie count
        money = driver.find_element(By.ID, "money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_dict.items():
            if cookie_count > cost:
                 affordable_upgrades[cost] = id 

        #Purchase the most expensive affordable upgrade
        if(len(affordable_upgrades) > 0):
            highest_price_affordable_upgrade = max(affordable_upgrades)
        else:
            continue
        # print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()
        
        #Add another 5 seconds until the next check
        timeout = time.time() + 5

    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break

