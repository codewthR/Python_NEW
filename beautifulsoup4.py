import requests  
import pandas as pd  
from bs4 import BeautifulSoup  
  
# link for extract html data  
def getdata(url):  
    r = requests.get(url)  
    return r.text  
  
htmldata = getdata("https://www.selenium.dev/")  
soup = BeautifulSoup(htmldata, 'html.parser')  
data = ''  
for data in soup.find_all("p"):  
    print(data.get_text())