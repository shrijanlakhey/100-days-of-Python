from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from os import getenv

load_dotenv()
MY_EMAIL = getenv("EMAIL")
MY_PASSWORD = getenv("PASSWORD")


url = "https://www.amazon.com/All-new-Kindle-Paperwhite-GB-adjustable/dp/B09RD7XM9X"

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    # note: only by adding cookie, I could extract the price from the website
    "Cookie": 'session-id=131-2408207-6799903; ubid-main=130-9616858-1608009; sp-cdn="L5Z9:NP"; aws-ubid-main=857-4708800-2567641; aws-userInfo-signed=eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJ1cy1lYXN0LTEiLCJhbGciOiJFUzM4NCIsImtpZCI6IjJmY2QzOWEwLWE1YzYtNDQyYy04MTJiLWRjMWQxYjcyZDIzYyJ9.eyJzdWIiOiIiLCJzaWduaW5UeXBlIjoiUFVCTElDIiwiaXNzIjoiaHR0cDpcL1wvc2lnbmluLmF3cy5hbWF6b24uY29tXC9zaWduaW4iLCJrZXliYXNlIjoiczhrbFlcL3BnV0ZtUk9FTk9jRG8zTGVqY1wveXlmMWd2UFZ2cFVudWh5ZVpBPSIsImFybiI6ImFybjphd3M6aWFtOjozNzM5NTM0NzA4MjY6cm9vdCIsInVzZXJuYW1lIjoiU2hyaWphbiUyMExha2hleSJ9.9Jf6utG--70dsw_XBURuA_evpzc9-hSIkvMBqZ5UuSrHusmv87ne_jyRqFgSz5mhXYD3mpZdKPJUSqjQ2jvRFOCQLtnQkoq4MgAbYOLBfoXdMGTGIZJhJuSISBvLolo9; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A373953470826%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22Shrijan%2520Lakhey%22%2C%22keybase%22%3A%22s8klY%2FpgWFmROENOcDo3Lejc%2Fyyf1gvPVvpUnuhyeZA%5Cu003d%22%2C%22issuer%22%3A%22http%3A%2F%2Fsignin.aws.amazon.com%2Fsignin%22%2C%22signinType%22%3A%22PUBLIC%22%7D; regStatus=pre-register; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1704892788876-738106.48_0; skin=noskin; i18n-prefs=USD; AMCVS_7742037254C95E840A4C98A6%40AdobeOrg=1; s_cc=true; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19733%7CMCMID%7C36292064747254582554581393252449389410%7CMCAID%7CNONE%7CMCOPTOUT-1704979738s%7CNONE%7CvVersion%7C4.4.0; id_pkel=n0; x-main="1YGXfamOyXKkXuQY3QtfSUgiLts4wyIRQDXjx@KuA6@HdZle5iIaWJaMRwxvnY9p"; at-main=Atza|IwEBIEjL8q-pifD1PWCUgZ6uqih6wviRw4gog0C_XAcV12z9wTVXB3cjfAxE6LstPQ6snJ4m-4vObgvWEieGoLD4b5uyKfT-4hXzGu81Og7rjQlW47RPS8tcIOcAM0a6ofK5DfiojucDHFMmelRs9plfeog8vdLnT6P76dSHWNHS33u7FkPR_Sc-uSxFXAzd00PePgeo5gQtoLo4yIGDpEO1vwnBHhz_maUSHx6rEL023hfKjw; sess-at-main="tPcXRynXaUSGdfjmX2xVzxBhWpW1p/6nxBvYlFx+vHM="; sst-main=Sst1|PQGmFnuOUg3cWu6OHStZg_tjCW2YwbaQXtgXPajBA-iaSr17sj3ITLuzNGIm1cqJkeb9OGMW1OYVAUeG5M0GcFxN9Y-EwOc0miuODR7NMvzcpFmC0XhdsyI47l5wFjbq7oEyNEoOwW75DNqPHaudwUOrBs8KL9bznSoUPCqnrUljV6FOnW2eAdrvaU80rX4z6ekuKVtjVq0ZK95uqhixfGTVIrs_mdD6M-HdY5fSp8ZsgrybL51XYEZPjx_Vgbhwz1qA1e6RAV4ofYKZyfcOx4DB4n1UjgVGYKh-NORE1oEPPHA; _rails-root_session=cGlpQ1VPakxYR2FRYVRuZ3pKTGZWZHduUU9kS2lXR2FXbW9xQmVFNndlTmF0SEhDRXgwZkNjb25NUGp4N1pCdm13ektxTnh2bjVVTjI4NGxVVFpDSFI4N2FDNGNmdHBvMmpDdDh5YU43UTU2KzQwVkZ1WnRLL01Kb3gyd0tmYTdObW81S2NlM203K3NVV0dFeE9wRGFZYkxQTHNwUFV2MkRWN2Fqc04wQjJVbWEvUjV6dkxMWmdMWkRia1Voa2tmLS0yd2NpNHpqOUlHUnN2UHRJVXVhbERBPT0%3D--4adebf55695703eb3e07109a0aec70ff7f7b9d70; s_fid=6041C071944D7B97-0B1706EFAFE7FEA5; s_sq=amazdiusprod%3D%2526pid%253Dhttps%25253A%25252F%25252Faffiliate-program.amazon.com%25252Fassoc_credentials%25252Fhome%25253Fopenid.assoc_handle%25253Damzn_associates_us%252526openid.claimed_id%25253Dhttps%2525253A%2525252F%2525252Fwww.amazon.com%2525252Fap%2525252Fid%2525252Famzn1.account.AFASKYDNN34Z4HFALLFYGZFGJQLA%252526openid.identity%25253Dhttps%2525253A%2525252F%2525252Fwww.amazon.com%2525252Fap%2525252Fid%2526oid%253Dhttps%25253A%25252F%25252Faffiliate-program.amazon.com%25252Fhome%2526ot%253DA%26amazditemplate%3D%2526pid%253Dhttps%25253A%25252F%25252Faffiliate-program.amazon.com%25252Fassoc_credentials%25252Fhome%25253Fopenid.assoc_handle%25253Damzn_associates_us%252526openid.claimed_id%25253Dhttps%2525253A%2525252F%2525252Fwww.amazon.com%2525252Fap%2525252Fid%2525252Famzn1.account.AFASKYDNN34Z4HFALLFYGZFGJQLA%252526openid.identity%25253Dhttps%2525253A%2525252F%2525252Fwww.amazon.com%2525252Fap%2525252Fid%2526oid%253Dhttps%25253A%25252F%25252Faffiliate-program.amazon.com%25252Fhome%2526ot%253DA; session-id-time=2082787201l; session-token=DcARFp4dOCqlTAvw0sbddgEMJ2VKnA2OFltfTTBtug89uaiufqb4FHCxOmJmN+ahWREnhA58UGuV5ks8btvrdph4EmY9kyksdGWJCsWOSMUZ0CUgFlPrbh9rgh/xgluTUscoFndgWtbiW/ja66pkawqsixg7d2BskCZ6b0ap2am6Qt/hCsbE4w1wDW1+4/xAclBot0beGYsC9PI8Rb/qTwpIbY80aIUoK5gMgTnicRK+3Y9BmLYmei4CeEm+6cR0be1urZP3cXMkkIQE+FpRbQ6mW2gaptmvQ12P7TOXAeGjQY0Xl2sYy6HqGioCbMq5o4IcFGF7arvnbEOfQCaEDgoeXR/XBaMI4PXcBVEMC+EaSme0OygWsA==; csm-hit=tb:s-8PEFJCM1Q39HHKR1XX1W|1704974104332&t:1704974107198&adb:adblk_yes',
}

response = requests.get(url=url, headers=headers)
product_data = response.content

soup = BeautifulSoup(product_data, "lxml")

# scraping the price of the product and converting it to float type
product_price = soup.select_one(selector=".a-offscreen").getText()
price_in_flaot = float(product_price.split("$")[1])

# scraping the title of the product and
product_title = soup.find(id="productTitle").getText().strip()

BUY_PRICE = 170

# sending email if the price of the product is less the buy price
if price_in_flaot < BUY_PRICE:
    sender_email = MY_EMAIL
    receiver_email = "lakheyshrijan@gmail.com"
    subject = "Amazon Price Alert!!!"
    body = f"{product_title} is now ${price_in_flaot}\n{url}"

    # Create the MIMEText object and set the character encoding to UTF-8
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = MY_EMAIL
    msg["To"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            sender_email,
            receiver_email,
            msg.as_string(),
        )
