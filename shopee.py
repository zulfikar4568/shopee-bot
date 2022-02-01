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
chrome_options.headless = False
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
prefs = {'profile.default_content_setting_values': {'images': 2,
                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                            'durable_storage': 2}}
chrome_options.add_experimental_option("prefs", prefs)
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
    r = requests.get("https://shopee.co.id")
    if (r.status_code == 200):
      print('\033[32m[+] Inisialisasi Driver sukses!,...')
      
def purchase_button():
  try:
    print('\033[32m[+] GOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW!')
    # Pilih Varian
    # varians = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Merah')]")))
    # browser.execute_script("arguments[0].click();", varians)

    # Klik Tombol Beli
    beli = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[3]/div/div[5]/div/div/button[2]')))
    browser.execute_script("arguments[0].click();", beli)
    print("\033[32m[+] INFO: Barang terbeli! Dalam\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")

    #Klik Tombol Checkout
    checkout = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[3]/div[2]/div[7]/button[4]/span')))
    browser.execute_script("arguments[0].click();", checkout)
    print("\033[32m[+] INFO: Barang otw Checkout!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")

    #Klik Buat Pesanan
    pesanan = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[3]/div[2]/div[4]/div[2]/div[7]/button')))
    browser.execute_script("arguments[0].click();", pesanan)
    print("\033[32m[+] INFO: Pesanan Dibuat!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")

    #Klik Bayar
    bayar = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.ID, 'pay-button'))).click()
    browser.execute_script("arguments[0].click();", bayar)
    print("\033[32m[+] INFO: Otw Bayar!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")

    #Masukan Pin Shopee Pay
    pin_shopee = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pin-popup"]/div[1]/div[3]/div[1]')))
    browser.execute_script("arguments[0].click();", pin_shopee)
    # pin_shopee.send_keys(pin_number)
    print("\033[32m[+] INFO: Uhuiy,..Dapet!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")
  except NoSuchElementException as e:
    print(e)

def main():
  minute = int(time.strftime("%M", time.localtime()))
  authors()
  load_cookies()
  browser.get(link_produk)
  r = requests.get(link_produk)
  if (r.status_code == 200):
    print('\033[32m[+] Berhasil mendapatkan product')
  current_minute = int(input("\033[32m[+] Masukin angkat menitnya (1-59) : "))

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
