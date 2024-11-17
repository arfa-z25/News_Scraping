import requests
import streamlit as st
from bs4 import BeautifulSoup

# CSS for background styling
background_image_css = """
<style>
.stApp {
   background: linear-gradient(orange, rgb(1.2 , 0.1 , 0.1), rgb(1,1,1));
   background-size: cover;
   background-repeat: no-repeat;
   background-attachment: fixed;
}


</style>
"""

# Title HTML
title_text = """
<h1 style="color: white; text-align: center; font-family: 'Arial', sans-serif; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
    BBC NEWS 
</h1>
"""

# Render custom HTML and CSS in Streamlit
st.markdown(title_text, unsafe_allow_html=True)
st.markdown(background_image_css, unsafe_allow_html=True)

# Fetch data from the BBC News website
url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Create category selection section
category_section = """
<div style="margin-bottom: 10px;">
    <h4 style="color: white; margin-left: -35%;">Latest News Articles</h4>
</div>
"""
st.markdown(category_section, unsafe_allow_html=True)

















# Extract headlines, descriptions, images, and publish dates
Headline = [h.get_text(strip=True) for h in soup.find_all('h2', {'data-testid': 'card-headline'})]
DESC = [d.get_text(strip=True) for d in soup.find_all('p', {'data-testid': 'card-description'})]
publish_date = [p.get_text(strip=True) for p in soup.find_all('span', {'data-testid': 'card-metadata-lastupdated'})]

# Extract images
pictures_list = []
images = soup.find_all('img')

# Collecting image URLs
for image in images:
    img_url = image.get('src')
    if img_url and not img_url.startswith('http'):
        img_url = 'https://www.bbc.com/' + img_url
    pictures_list.append(img_url)



    
# Make sure all lists are of the same length
num_articles = min(len(Headline), len(DESC), len(pictures_list), len(publish_date))

# Generate HTML for news article cards
page_struc = f""" 

<html>
<div style="display : flex ; flex-direction:row; gap : 5px ; flex-wrap:wrap;   color:white ; width:80rem ; margin-left:-40% ; padding:4%">
<div style="display : flex ; flex-direction : column ; gap : 10px ; width:24% ; height:auto ; border:2px solid grey ; border-radius:5px ; padding:2% ; box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[0]} alt="article_1">
 <h3>{Headline[0]}</h3>
 <p>{DESC[0]}</p>
 <p style="color : grey">{publish_date[0]}</p>
 

</div>

<div style="display : flex ; flex-direction : column ; gap : 10px ;width:39% ; height:auto; border:2px solid grey ; border-radius:5px;padding:2% ; margin-left:5% ; margin-right:3% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[1]} alt="article_1">
 <h3>{Headline[1]}</h3>
 <p>{DESC[1]}</p>
 <p style="color : grey">{publish_date[1]}</p>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:24% ; height:auto ; border:2px solid grey ; border-radius:5px ; padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[2]} alt="article_1">
 <h3>{Headline[2]}</h3>
 <p>{DESC[2]}</p>
 <p style="color : grey">{publish_date[2]}</p>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:37% ; height:auto ; border:2px solid grey; border-radius:5px ; padding:2%  ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[3]} alt="article_1">
 <h3>{Headline[3]}</h3>
 <p>{DESC[3]}</p>
 <p style="color : grey">{publish_date[3]}</p>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:23% ; height:auto; border:2px solid grey ; border-radius:5px ; padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[4]} alt="article_1">
 <h3>{Headline[4]}</h3>
 <p>{DESC[4]}</p>
 <p style="color : grey">{publish_date[4]}</p>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:35% ; height:auto ; border:2px solid grey ; border-radius:5px ; padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[5]} alt="article_1">
 <h3>{Headline[5]}</h3>
 <p>{DESC[5]}</p>
 <p style="color : grey">{publish_date[5]}</p>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:25% ; height:auto ; border:2px solid grey ; border-radius:5px ; padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[6]} alt="article_1">
 <h3>{Headline[6]}</h3>
 <p>{DESC[6]}</p>
 <p style="color : grey">{publish_date[6]}</p>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:41% ; height:auto ; border:2px solid grey ; border-radius:5px;padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[7]} alt="article_1">
 <h3>{Headline[7]}</h3>
 <p>{DESC[7]}</p>
 <p style="color : grey">{publish_date[7]}</p>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:26% ; height:auto ; border:2px solid grey; border-radius:5px ; padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[8]} alt="article_1">
 <h3>{Headline[8]}</h3>
 <p>{DESC[8]}</p>
 <p style="color : grey">{publish_date[8]}</p>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:42% ; height:auto ; border:2px solid grey ; border-radius:5px  ;padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[9]} alt="article_1">
 <h3>{Headline[9]}</h3>
 <p>{DESC[9]}</p>
 <p style="color : grey">{publish_date[9]}</p>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:30% ; height:auto ; border:2px solid grey ; border-radius:5px  ;padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[10]} alt="article_1">
 <h3>{Headline[10]}</h3>
 <p>{DESC[10]}</p>
 <p style="color : grey">{publish_date[10]}</p>
 

</div>

<div style="display : flex ; flex-direction : column ; gap : 10px;width:26% ; height:auto ; border:2px solid grey ; border-radius:5px  ;padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[11]} alt="article_1">
 <h3>{Headline[11]}</h3>
 <p>{DESC[11]}</p>
 <p style="color : grey">{publish_date[11]}</p>
 

</div>



</div>
</html>

"""

st.markdown(page_struc , unsafe_allow_html=True)

