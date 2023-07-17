import requests
from bs4 import BeautifulSoup
import lxml
import smtplib 

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "Your Username or Gmail"
MY_PASSWORD = "Your Password"


headers = {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

response  = requests.get(url = "", headers=headers)
content = response.text 

soup = BeautifulSoup(content, 'html.parser')

value= []

prices = soup.select("span", class_="a-price aok-align-center")

# print(prices)

for price in prices:
    x = price.get_text().split(".")
    # print(x[0])
    value.append(x[0])
print(value[0])
val = int(float(value[0]))
    

if(val < 1500):
    with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"The Airpod 141 price is less than 1100 and the current price is {val}"
        )

