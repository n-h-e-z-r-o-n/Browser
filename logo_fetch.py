import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def web_logo(url, name_log):
        name_log = f"{name_log}.png"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        logo_img = max(soup.find_all('img'), key=lambda img: (img.get('height'), img.get('width'))) # Find the <img> tag with the highest height and width attributes
        if logo_img is not None:
            logo_url = logo_img.get('src') # Extract the logo URL from the src attribute
            if not logo_url.startswith('http'): # If the URL is relative, make it absolute using the original URL
                parsed_url = urlparse(url)
                logo_url = f"{parsed_url.scheme}://{parsed_url.netloc}/{logo_url.lstrip('/')}"

            response = requests.get(logo_url)
            logo_data = response.content

            # Save the logo data to a file
            with open(name_log, 'wb') as f:
                f.write(logo_data)
            print(logo_url)
        else:
            print('No logo found.')

url = 'https://www.google.com'
web_logo(url, "string")