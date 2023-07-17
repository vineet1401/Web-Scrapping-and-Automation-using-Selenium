from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

USERNAME = "Your Username or Gmail"
PASSWORD = "Your Password"



# driver = webdriver.Chrome("D:\CODING MATERIAL\HTML ANS CSS\WEB SCRAPPING\SELENIUM WEBDRIVER\chromedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.linkedin.com/home")
username = driver.find_element(By.XPATH, '//*[@id="session_key"]')
username.send_keys(USERNAME)
driver.implicitly_wait(2)
password = driver.find_element(By.XPATH, '//*[@id="session_password"]')
password.send_keys(PASSWORD)
login = driver.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
login.click()
driver.implicitly_wait(3)




linkedin_jobs_url = "https://www.linkedin.com/jobs/search/?currentJobId=3348298644&f_AL=true&f_E=1%2C2&f_WT=2&geoId=90009642&keywords=python%20developer&location=Pune%2FPimpri-Chinchwad%20Area&refresh=true"
driver.get(linkedin_jobs_url)


all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    driver.implicitly_wait(2)

    #Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        driver.implicitly_wait(5)
        
        # #If phone field is empty, then fill your phone number.
        # phone = driver.find_element_by_class_name("fb-single-line-text__input")
        # if phone.text == "":
        #     phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        #If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            driver.implicitly_wait(2)
            discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
    
        #Once application completed, close the pop-up window.
        driver.implicitly_wait(2)
        close_button = driver.find_element(By.CLASS_NAME,   "artdeco-modal__dismiss")
        close_button.click()

    #If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

driver.implicitly_wait(5)
driver.quit()