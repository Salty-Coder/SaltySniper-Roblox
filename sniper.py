"""
Program made by Salty-Coder.
Protected by GNU General Public License v3.0
"""

from selenium import webdriver
from random import randint
import random
import time
import winsound
import ctypes
import pygetwindow as gw
import os
import sys
from colorama import Fore
from win10toast import ToastNotifier
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def debug(msg):
    if len(sys.argv) > 1:
        if sys.argv[1] == '--debug':
            print(str(msg))
            return

clear=lambda: os.system('cls')
toaster = ToastNotifier()

options = webdriver.ChromeOptions()

options.add_argument('--headless')


consoletitle = gw.getActiveWindow().title #sniper.py
debug(consoletitle)
console = gw.getWindowsWithTitle(consoletitle)[0]


print(Fore.RED+"""
 ________  ________  ___   _________    ___    ___      ________  ________   ___  ________  _______   ________     
|\   ____\|\   __  \|\  \ |\___   ___\ |\  \  /  /|    |\   ____\|\   ___  \|\  \|\   __  \|\  ___ \ |\   __  \    
\ \  \___|\ \  \|\  \ \  \\|___ \  \_| \ \  \/  / /    \ \  \___|\ \  \\ \  \ \  \ \  \|\  \ \   __/|\ \  \|\  \   
 \ \_____  \ \   __  \ \  \    \ \  \   \ \    / /      \ \_____  \ \  \\ \  \ \  \ \   ____\ \  \_|/_\ \   _  _\  
  \|____|\  \ \  \ \  \ \  \____\ \  \   \/  /  /        \|____|\  \ \  \\ \  \ \  \ \  \___|\ \  \_|\ \ \  \\  \| 
    ____\_\  \ \__\ \__\ \_______\ \__\__/  / /            ____\_\  \ \__\\ \__\ \__\ \__\    \ \_______\ \__\\ _\ 
   |\_________\|__|\|__|\|_______|\|__|\___/ /            |\_________\|__| \|__|\|__|\|__|     \|_______|\|__|\|__|
   \|_________|                       \|___|/             \|_________|                                             
                                                                                                                   
                                                                                                                   """+Fore.RESET)

link = str(input("Link to limited: "))

ddelay = 5
delay = input("Scan delay (default is " + str(ddelay) + "): ")

if delay.isnumeric and len(delay) > 0:
    debug("func")
    delay = int(delay)
debug(delay)
bs = int(input("Are you looking to, 1 - Buy, 2 - Sell?: "))

if bs != 1 and bs != 2:
    print("You must buy or sell!")
    quit()

if bs == 1:
    price = int(input("What is your maximum price to buy at?: "))
if bs == 2:
    price = int(input("What is your minimum price to sell at?: "))

if link:
    

    browser = webdriver.Chrome(r"chromedriver\chromedriver.exe", options=options)
    browser.get(link)

    console.minimize()
    

    limited = browser.find_element(By.CSS_SELECTOR, '#item-container > div.remove-panel.section-content.top-section > div.border-bottom.item-name-container > h2').text

    lowestprice = 999999999999999999999999999999999
    highestprice = -1

    while True:
        element = False
        while element == False:
            debug("none")
            element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#item-details > div.clearfix.price-container > div.price-container-text > div.price-info > div > span.text-robux-lg.wait-for-i18n-format-render'))
            )
        debug("not false")
        currentprice = browser.find_element(By.CSS_SELECTOR, '#item-details > div.clearfix.price-container > div.price-container-text > div.price-info > div > span.text-robux-lg.wait-for-i18n-format-render').text
        debug(currentprice)
        currentprice = currentprice.replace(',', '')

        #----------------------------------
        if bs == 1:
            if int(currentprice) <= price: #currentprice <= desired price
                if int(currentprice) < lowestprice:
                    lowestprice = int(currentprice)
                    toaster.show_toast("Salty Sniper","The price on " + limited + " reached an all-time low at " + str(currentprice) + "!\nGO GRAB IT!", icon_path=None, duration=7, threaded=True)
                    winsound.Beep(540, 2000)
                else:
                    toaster.show_toast("Salty Sniper","The price on " + limited + " has reached your desired buy price at " + str(currentprice) + "!", icon_path=None, duration=5, threaded=True)
                    winsound.Beep(500, 1000)
        #----------------------------------
        #----------------------------------
        if bs == 2:
            if int(currentprice) >= price: #currentprice >= desired price
                if int(currentprice) > highestprice:
                    highestprice = int(currentprice)
                    toaster.show_toast("Salty Sniper","The price on " + limited + " reached an all-time high at " + str(currentprice) + "!\nGO SELL IT!", icon_path=None, duration=7, threaded=True)
                    winsound.Beep(540, 2000)
                else:
                    toaster.show_toast("Salty Sniper","The price on " + limited + " has reached your desired sell price at " + str(currentprice) + "!", icon_path=None, duration=5, threaded=True)
                    winsound.Beep(500, 1000)
        #----------------------------------



        
        time.sleep(delay or ddelay)
        browser.get(link)