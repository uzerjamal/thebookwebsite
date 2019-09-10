import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

baseUrl = 'https://manojpurohitcsharp2019.blogspot.com/'
driver = webdriver.Firefox()
driver.get(baseUrl)
time.sleep(10)
titleOpenHtml = '''
<html>
    <head>
        <title>
'''

titleCloseHtml = '''
</title>
'''

topHtml = '''
<link rel="stylesheet" href="css/style.css">
<meta charset="UTF-8">
        <script src="js/jquery.js"></script> 
        <script> 
            $(function(){
                $("#menuHere").load("menu.html"); 
                $("#headerHere").load("header.html");
            });
        </script> 
    </head>

    <body>
      <div id="headerHere"></div>
      <div id="menuHere"></div>
      <div class="content">
'''

bottomHtml = '''
</div>
</body>
</html>
'''

print('SCROLLING TO THE BOTTOM OF THE PAGE!')
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(3)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    # break condition
    if new_height == last_height:
        break
    last_height = new_height
print('FINISHED SCROLLING!')

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

print('SAVING POSTS...')

for li in soup.ol:
    title = (((li.h1.a.text).strip()).replace(':', ' ')).replace(' ', '-')
    contentDiv = li.find('div', class_='article-content entry-content')
    with open(title + '.html', 'w+') as f:
        f.write(titleOpenHtml + title + titleCloseHtml + topHtml + str(contentDiv) + bottomHtml)
        f.close()
    print('Created ' + title + '.html')

print('SAVED POSTS!')
