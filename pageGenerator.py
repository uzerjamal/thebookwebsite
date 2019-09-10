import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

baseUrl = 'http://manojpurohitcsharp.blogspot.in/'
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
        <script src="js/jquery.js"></script> 
        <script> 
            $(function(){
                $("#menuHere").load("menu.html"); 
            });
        </script> 
    </head>

    <body>
      <div id="menuHere"></div>
      <div class="content">
'''

bottomHtml = '''
</div>
</body>
</html>
'''

menuLinks = ''

menuTop = '''
<div class="menu">
    <img src = "images/Csharp.png" height = "200" width = "200" style="padding-inline-start: 20px">
    <ul>
'''

menuBottom = '''
    </ul>
</div>>
'''

print('SCROLLING TO THE BOTTOM OF THE PAGE!')
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
print('FINISHED SCROLLING!')

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

print('SAVING POSTS...')

for li in soup.ol:
    title = ((((li.h1.a.text).strip()).replace(':', ' ')).replace(' ', '-')).replace('#', 'S')
    contentDiv = li.find('div', class_='article-content entry-content')
    with open(title + '.html', 'w+', encoding="utf-8") as f:
        f.write(titleOpenHtml + title + titleCloseHtml + topHtml + str(contentDiv) + bottomHtml)
        f.close()
    print('Created ' + title + '.html')
    menuLinks = '\n' + '<li><a href="' + title + '.html' + '">' + title.replace('-', ' ') + '</a></li>' + menuLinks

print('SAVED POSTS!')
print('CREATING MENU...')
with open('menu.html', 'w+', encoding="utf-8") as f:
    f.write(menuTop + menuLinks + menuBottom)
    f.close()
print('CREATED MENU!')
print('DONE!')
driver.close()