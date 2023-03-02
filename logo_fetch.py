import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def web_logo(url, name_log):
        name_log = f"{name_log}.jpg"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
           logo_img = max(soup.find_all('img'), key=lambda img: (img.get('height'), img.get('width'))) # Find the <img> tag with the highest height and width attributes
        except:
           logo_img = max(soup.find_all('img'), key=lambda img: (int(img.get('height') or 0), int(img.get('width') or 0)))
        if logo_img is not None:
            logo_url = logo_img.get('src') # Extract the logo URL from the src attribute
            if not logo_url.startswith('http'): # If the URL is relative, make it absolute using the original URL
                parsed_url = urlparse(url)
                logo_url = f"{parsed_url.scheme}://{parsed_url.netloc}/{logo_url.lstrip('/')}"

            response = requests.get(logo_url)
            logo_data = response.content

            # Save the logo data to a file
            with open(f"./Assets/{name_log}", 'wb') as f:
                f.write(logo_data)
            print(logo_url)
        else:
            print('No logo found.')


import requests
from bs4 import BeautifulSoup
import tkinter as tk
from PIL import ImageTk, Image
from io import BytesIO
def web_2(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the <img> tag with the highest height and width attributes
    logo_img = max(soup.find_all('img'), key=lambda img: (int(img.get('height') or 0), int(img.get('width') or 0)))
    if logo_img is not None:
        # Extract the logo URL from the src attribute
        logo_url = logo_img.get('src')
        # If the URL is relative, make it absolute using the original URL
        if not logo_url.startswith('http'):
            logo_url = f"{url}/{logo_url.lstrip('/')}"
        # Send a GET request to the logo URL and create an Image object from the response content
        response = requests.get(logo_url)
        img = Image.open(BytesIO(response.content))
        img_tk = ImageTk.PhotoImage(img)
        return img_tk
    else:
        print('No logo found.')