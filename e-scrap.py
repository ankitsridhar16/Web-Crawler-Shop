import requests
from bs4 import BeautifulSoup
import time
import sys

print("""\
                                                    
  ______ ________________  ______ ______ ___.__. 
 /  ___// ___\_  __ \__  \ \____ \\____ <   |  | 
 \___ \\  \___|  | \// __ \|  |_> >  |_> >___  | 
/____  >\___  >__|  (____  /   __/|   __// ____| 
     \/     \/           \/|__|   |__|   \/      
    """)

print("""\
       __          _____             __           _______      ___   
  / /  __ __  / ___ \__ _  ____ / /__ _______/_  / _ \___ <  /___
 / _ \/ // / / / _ `/  ' \/ __//  '_// __/ _ \/ / // / _ \/ / __/
/_.__/\_, /  \ \_,_/_/_/_/_/__/_/\_\/_/ / .__/_/\___/_//_/_/\__/ 
     /___/    \___/       /___/        /_/                     
""")
animation = "|/-\\"

for i in range(100):
    time.sleep(0.01)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
    #print("Welcome to scrappy by mr-kryp70n1c")
print("Welcome to scrappy by ankit") 

for i in range(100):
    time.sleep(0.01)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()


def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 48 <= ord(c) <= 57)
    return ''.join(stripped)


q = input("Enter product code to Search the product")

## flipkart scrapping ##
fliplink = "https://www.flipkart.com/search?q="+q+"&otracker==search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
r = requests.get(fliplink)
soup = BeautifulSoup(r.content,"lxml")
price = soup.find_all("div",{"class":"_1vC4OE"})
if price:
    fp = price[0].text
    fp = strip_non_ascii(fp)
    print("Flipkart Price: "+fp)
else:
    print("Flipkart do not sell this product")
##amazon scrapping ##
amazonlink = "https://www.amazon.in/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords="+q+"&rh=i%3Aaps%2Ck%3A"+q
#amazonlink = "https://www.amazon.in/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords="+"klv-40w562d&rh"+"=i%3Aaps%2Ck%3A"+"klv-40w562d"
r = requests.get(amazonlink)
soup = BeautifulSoup(r.content,"lxml")
price = soup.find("span",{"class":"a-size-base a-color-price s-price a-text-bold"})
if price:
    ap = price.text
    ap = strip_non_ascii(ap)
    print("Amazon Price: "+ap)
else:
    print("Amazon do not sell this product")
    ap = -1;


##sanpdeal scrapping##
link = "https://www.snapdeal.com/search?keyword="+q+"&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=1&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy"
r = requests.get(link)
soup = BeautifulSoup(r.content,"lxml")
price = soup.find_all("span",{"class":"lfloat product-price"})
if price:
    sp = price[0].text
    sp = strip_non_ascii(sp)
    print("Snapdeal Price :"+fp)
else:
    print("Snapdeal does not sell this product")
    sp= -1;