# Import Libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from config import link_produk, pin_number, cookiee, chrome_driver
import time
import pyfiglet as f
import requests

# Setting Chrome
my_chrome = Service(chrome_driver)
WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

browser = webdriver.Chrome(service=my_chrome, options=chrome_options)
browser.delete_all_cookies

# Define some methods
def authors():
    style = f.figlet_format("By: Zulfikar")
    print(style)
    print("\033[31m----- \033[93mGithub : \033[92mhttps://github.com/zulfikar4568 \033[31m-----")

def load_cookies():
    browser.get("https://shopee.co.id")
    browser.add_cookie({'name': 'SPC_EC', 'value': cookiee})
    browser.get_cookies()
    time.sleep(1)
    print('\033[32m[+] Driver initialization suksess,...')
def purchase_button():
  try:
    print('\033[32m[+] This is for purchasing an item!')
    # varians = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Merlot')]")))
    # browser.execute_script("arguments[0].click();", varians) bila ada variant tinggal ganti di bagian Merlot
    # beli = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]')))
    # browser.execute_script("arguments[0].click();", beli)
    # print("\033[32m[+] INFO: Barang terbeli! Dalam\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")
    # checkout = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button/span')))
    # browser.execute_script("arguments[0].click();", checkout)
    # print("\033[32m[+] INFO: Barang otw Checkout!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")
    # pesanan = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[2]/div[7]/button')))
    # browser.execute_script("arguments[0].click();", pesanan)
    # print("\033[32m[+] INFO: Pesanan Dibuat!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")
    # bayar = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.ID, 'pay-button'))).click()
    # browser.execute_script("arguments[0].click();", bayar)
    # print("\033[32m[+] INFO: Otw Bayar!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")
    # pin_shopee = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pin-popup"]/div[1]/div[3]/div[1]')))
    # browser.execute_script("arguments[0].click();", pin_shopee)
    # pin_shopee.send_keys(pin_number)
    # print("\033[32m[+] INFO: Uhuiy,..Dapet!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")
  except NoSuchElementException as e:
    print(e)

def main():
  minute = int(time.strftime("%M", time.localtime()))
  authors()
  load_cookies()
  browser.get(link_produk)
  r = requests.get(link_produk)
  if (r.status_code == 200):
    print('\033[32m[+] Success get the Product')
  current_minute = int(input("\033[32m[+] Input the minutes number (1-60) : "))

  while minute != current_minute:
    minute = int(time.strftime("%M", time.localtime()))
    if minute != current_minute :
      browser.refresh()
      print("\033[32m[+] INFO:\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mSabar Belum mulai!")
    else:
        break

  purchase_button()

if __name__ == "__main__":
  main()
