from bs4 import BeautifulSoup
import requests
import os
import csv
from datetime import datetime

filename = 'product.csv'

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

base_path = os.path.dirname(os.path.abspath(__file__))
filepath  = os.path.join(base_path, filename)

source = requests.get('https://www.amazon.in/Redragon-K673-Mechanical-Dedicated-Absorbing/dp/B0CDX5XGLK/?_encoding=UTF8&pd_rd_w=DJszn&content-id=amzn1.sym.1cde463e-0316-4b4b-a52e-a6bd52339fb2&pf_rd_p=1cde463e-0316-4b4b-a52e-a6bd52339fb2&pf_rd_r=ZSH28A6H0P026CTJCXZ9&pd_rd_wg=TiYFp&pd_rd_r=4b878286-a104-4ffa-bc67-16cbaec28a79&ref_=pd_hp_d_atf_dealz_cs&th=1').text
soup = BeautifulSoup(source, 'lxml')

product = soup.find('span', class_ = 'a-size-large product-title-word-break')
d  = product.text


symbol =  soup.find('span', class_ = 'a-price-symbol')
s = symbol.text

price  = soup.find('span', class_= 'a-price-whole')
p  = price.text
p = p.replace('.', '')
headers = ['product', 'price', 'timestamp']

file_exists = os.path.exists(filepath)

with open(filepath, 'a', newline='') as products:
    writer = csv.DictWriter(products, fieldnames=headers)
    if not file_exists:
        writer.writeheader()
    writer.writerow({"product": d, "price": p, "timestamp": timestamp})

with open(filepath) as products:
        reader = csv.DictReader(products, delimiter='\t')
        
        for line in reader:
                print(line)
