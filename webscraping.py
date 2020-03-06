import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
from unicodedata import normalize
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os

def webautomation():
    print("Amazon Devices & Accessories = 1")
    print("Apps for Android = 2")
    print("Audible Audiobooks = 3")
    print("Automotive = 4")
    print("Baby = 5")
    print("Beauty & Personal Care = 6")
    print("Books = 7")
    print("Clothing & Accessories = 8")
    print("Electronics = 9")
    print("Gift Cards = 10")
    print("Grocery & Gourmet Food = 11")
    print("Handmade Products = 12")
    print("Health & Personal Care = 13")
    print("Home = 14")
    print("Industrial & Scientific = 15")
    print("Jewelry = 16")
    print("Kindle Store = 17")
    print("Livres en francais = 18")
    print("Luggage & Bags = 19")
    print("Movies & TV Shows = 20")
    print("Music = 21")
    print("Musical Instruments, Stage & Studio = 22")
    print("Office Products = 23")
    print("Patio, Lawn & Garden = 24")
    print("Pet Supplies = 25")
    print("Shoes & Handbags = 26")
    print("Software = 27")
    print("Sports & Outdoors = 28")
    print("Tools & Home Improvement = 29")
    print("Toys & Games = 30")
    print("Video = 31")
    print("Video Games = 32")
    print("Watches = 33")
    print("")

    x = int(input("Please enter the category: "))

    browser = webdriver.Chrome('/usr/local/bin/chromedriver')
    browser.maximize_window()
    browser.get('https://www.amazon.ca')
    ##search = browser.find_elements_by_id('twotabsearchtextbox')[0]
    ##search.send_keys(x)
    ##time.sleep(2)
    ##search.send_keys(Keys.ENTER)
    bestseller = browser.find_elements_by_xpath('//*[@id="nav-xshop"]/a[1]')[0]
    bestseller.click()
    time.sleep(1)
    androidapps = browser.find_elements_by_xpath('//*[@id="zg_browseRoot"]/ul/li[%d]/a' % (x))[0]
    androidapps.click()


def createcsv():

    messagebox.showinfo("Starting...", "The program is starting to create the CSV file")

    urls = ['https://www.amazon.ca/Best-Sellers/zgbs/amazon-devices/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Appstore-Android/zgbs/mobile-apps/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers/zgbs/audible/ref=zg_bs_nav_0','https://www.amazon.ca/Best-Sellers-Automotive/zgbs/automotive/ref=zg_bs_nav_0','https://www.amazon.ca/Best-Sellers-Baby/zgbs/baby/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Beauty/zgbs/beauty/ref=zg_bs_nav_0','https://www.amazon.ca/Best-Sellers-Books/zgbs/books/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Clothing-Accessories/zgbs/apparel/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Gift-Cards/zgbs/gift-cards/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Grocery/zgbs/grocery/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Handmade/zgbs/handmade/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Health-Personal-Care/zgbs/hpc/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Home-Kitchen/zgbs/kitchen/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Industrial-Scientific/zgbs/industrial/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Jewelry/zgbs/jewelry/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Kindle-Store/zgbs/digital-text/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Livres-Fran-ccedil-ais/zgbs/books-en-francais/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Luggage-Bags/zgbs/luggage/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-DVD/zgbs/dvd/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Music/zgbs/music/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Musical-Instruments-Stage-Studio/zgbs/musical-instruments/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Office-Products/zgbs/office/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Patio-Lawn-Garden/zgbs/lawn-garden/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Pet-Supplies/zgbs/pet-supplies/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Shoes-Handbags/zgbs/shoes/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Software/zgbs/software/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Sports-Outdoors/zgbs/sports/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Tools-Home-Improvement/zgbs/hi/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Toys-Games/zgbs/toys/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Video/zgbs/video/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Computer-Video-Games/zgbs/videogames/ref=zg_bs_nav_0', 'https://www.amazon.ca/Best-Sellers-Watches/zgbs/watch/ref=zg_bs_nav_0']
    
    count = 0
    while(count < len(urls)):
        if(count == 16):
            messagebox.showinfo("Still Processing", "We are still processing the data!!!")
        product = []
        prices = []
        ratings = []

        url = urls[count]

        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')

        if(url == 'https://www.amazon.ca/Best-Sellers/zgbs/audible/ref=zg_bs_nav_0'):
            data = soup.findAll('a',attrs={'class' : 'a-link-normal'})
            price = soup.findAll('span', attrs={'class' : 'a-size-base a-color-price'})
            rate = soup.findAll('span', attrs={'class' : 'a-icon-alt'})
            category = soup.findAll('span', attrs={'class' : 'zg_selected'})
        else:
            data = soup.findAll('a',attrs={'class' : 'a-link-normal'})
            price = soup.findAll('span', attrs={'class' : 'p13n-sc-price'})
            rate = soup.findAll('span', attrs={'class' : 'a-icon-alt'})
            category = soup.findAll('span', attrs={'class' : 'zg_selected'})



        for d in category:
            categoryname = d.get_text().strip()

        for a in data:
            for img in a.find_all('img', alt=True):
                product.append(img['alt'])

        for a in rate:
            ratings.append(a.get_text())


        for i in price:
            prices.append(normalize("NFKD", i.text))



        with open('index.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(" ")

            a = []
            a.append("Products category: %s" %(categoryname))
            a.append("Price")
            a.append("Ratings")
            writer.writerow(a)

            i = 0
            while(i < 10):
                writer.writerow([product[i], prices[i], ratings[i]])
                i = i+1

        count = count+1
    
    
    messagebox.showinfo("CSV is DONE!", "Your CSV file is done and it is now in the same directory as the program")
    

root = tk.Tk()

cnvs = tk.Canvas(root, height=500, width=500, bg='red')
cnvs.pack()

frame = tk.Frame(root, bg='white')
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

sel = tk.Button(frame, text="Open Website", padx = 10, pady = 30, command=webautomation)
bs = tk.Button(frame, text="Create CSV", padx = 10, pady = 30, command=createcsv)


sel.pack()
bs.pack()

root.mainloop()