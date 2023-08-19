import os
from bs4 import BeautifulSoup
import requests
import csv
from urllib.request import urlretrieve
from urllib.parse import urljoin
import re
import time

base = 'http://www.knittingonthenet.com/stitches.htm'
imgbase = 'http://www.knittingonthenet.com'

result = requests.get(base)

doc = BeautifulSoup(result.text, 'html.parser')

links = doc.find_all('a', href=re.compile('^/stitches/[^/]+$'))

# #csv info
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_dir, 'image_data.csv')
fieldnames = ['Image Name', 'Page Title']

# #open the csv first
with open(csv_file, 'w', newline='') as file:
     writer = csv.DictWriter(file, fieldnames=fieldnames)
     writer.writeheader()
     
     child_sites = [urljoin(imgbase, link['href']) for link in links if link['href'].startswith('/stitches/')]
     
     for child_site in child_sites:
        if child_site == 'http://www.knittingonthenet.com/stitches/bw.htm':
            continue
        result = requests.get(child_site)
        doc = BeautifulSoup(result.text, 'html.parser')
        print(child_site)

        images = doc.find_all('img')
        for img in images:
            try:
                image_url = img['src']
                full_image_url = urljoin(imgbase, image_url)
                image_name = image_url.split('/')[-1]
                image_path = f"E:\\Documents\\knit_stitch_identifier\\images\\{image_name}"  # Modify the path as per your requirements
                if image_name == 'title.gif':
                        continue
                urlretrieve(full_image_url, image_path)
                print(f"Image saved: {image_path}")
                page_title = doc.title.string.strip() if doc.title else ''
                writer.writerow({'Image Name': image_name, 'Page Title': page_title})
                time.sleep(5)
            except Exception as e:
                 print(f'error for {child_site}')
print(f"CSV file created: {csv_file}")