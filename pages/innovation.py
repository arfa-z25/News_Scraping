import streamlit as st
import requests
from bs4 import BeautifulSoup

background_image_css = """
<style>
.stApp {
  background-image: linear-gradient(120deg, #e0c3fc 0%, #8ec5fc 100%);
}


</style>
"""

# Title HTML
title_text = """
<h1 style="color: black; text-align: center; font-family: 'Arial', sans-serif; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
    News Related To Innovation
</h1>
"""

# Render custom HTML and CSS in Streamlit
st.markdown(title_text, unsafe_allow_html=True)
st.markdown(background_image_css, unsafe_allow_html=True)













# Fetch data from the BBC News website
url = "https://www.bbc.com/innovation"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract headlines, descriptions, images, and publish dates
Headline = [h.get_text(strip=True) for h in soup.find_all('h2', {'data-testid': 'card-headline'})]
DESC = [d.get_text(strip=True) for d in soup.find_all('p', {'data-testid': 'card-description'})]
publish_date = [p.get_text(strip=True) for p in soup.find_all('span', {'data-testid': 'card-metadata-lastupdated'})]

# Extract images
pictures_list = []
    
    # Find all images with the class 'img_ad'
img_tags = soup.find_all('img', class_="sc-a34861b-0 efFcac")

    # Collect image URLs
for image in img_tags:
        img_url = image.get('src')
        
        if img_url:
            # Handle relative URLs by appending the base URL
            if not img_url.startswith('http'):
                img_url = 'https://www.bbc.com/' + img_url
            
            pictures_list.append(img_url)
    

a_tags = soup.find_all('a', {'data-testid' : 'internal-link'})

# Create a list to store the 'href' values
hrefs = []

# Loop through each <a> tag and get the 'href' attribute
for a in a_tags:
    href = a.get('href')
    if href:
        # Check if the 'href' starts with 'http', if not, prepend the base URL
        if not href.startswith('http'):
            href = 'https://www.bbc.com' + href
        # Append the full URL to the list
        hrefs.append(href)



structure_page = f""" 

<html>
<div style="display : flex ; flex-direction:row; gap : 5px ; flex-wrap:wrap;   color:black ; width:80rem ; margin-left:-40% ; padding:4%">
<div style="display : flex ; flex-direction : column ; gap : 10px ; width:53% ; height:auto ; border:2px solid grey ; border-radius:5px ; padding:2% ; box-shadow: 2px 2px 5px black;" >
 <img src = {pictures_list[0]} alt="article_1">
 <h3>{Headline[0]}</h3>
 <p>{DESC[0]}</p>
 <div style="display : flex ; flex-direction:row ;">
 <p style="color : grey">{publish_date[0]}</p>
 <a href={hrefs[4]} 
       style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; text-decoration: none; color: white; background-color: black; border-radius: 5px; border: none; transition: background-color 0.3s ease; margin-left:9%">
        Read More
    </a>
    </div>
 

</div>

<div style="display : flex ; flex-direction : column ; gap : 10px ;width:35% ; height:auto; border:2px solid grey ; border-radius:5px;padding:2% ;    box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[1]} alt="article_1">
 <h3>{Headline[1]}</h3>
 <p>{DESC[1]}</p>
<div style="display : flex ; flex-direction:row ;">
 <p style="color : grey">{publish_date[1]}</p>
 <a href={hrefs[5]} 
       style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; text-decoration: none; color: white; background-color: black; border-radius: 5px; border: none; transition: background-color 0.3s ease; margin-left:9%">
        Read More
    </a>
    </div>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:29% ; height:auto ; border:2px solid grey ; border-radius:5px ; padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[2]} alt="article_1">
 <h3>{Headline[2]}</h3>
 <p>{DESC[2]}</p>
 <div style="display : flex ; flex-direction:row ;">
 <p style="color : grey">{publish_date[2]}</p>
 <a href={hrefs[6]} 
       style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; text-decoration: none; color: white; background-color: black; border-radius: 5px; border: none; transition: background-color 0.3s ease; margin-left:9%">
        Read More
    </a>
    </div>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:37% ; height:auto ; border:2px solid grey; border-radius:5px ; padding:2%  ;  box-shadow: 2px 2px 5px black;" >
 <img src = {pictures_list[3]} alt="article_1">
 <h3>{Headline[3]}</h3>
 <p>{DESC[3]}</p>
 <div style="display : flex ; flex-direction:row ;">
 <p style="color : grey">{publish_date[3]}</p>
 <a href={hrefs[7]} 
       style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; text-decoration: none; color: white; background-color: black; border-radius: 5px; border: none; transition: background-color 0.3s ease; margin-left:9%">
        Read More
    </a>
    </div>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:23% ; height:auto; border:2px solid grey ; border-radius:5px ; padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[4]} alt="article_1">
 <h3>{Headline[4]}</h3>
 <p>{DESC[4]}</p>
<div style="display : flex ; flex-direction:row ;">
 <p style="color : grey">{publish_date[4]}</p>
 <a href={hrefs[8]} 
       style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; text-decoration: none; color: white; background-color: black; border-radius: 5px; border: none; transition: background-color 0.3s ease; margin-left:9%">
        Read More
    </a>
    </div>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:35% ; height:auto ; border:2px solid grey ; border-radius:5px ; padding:2% ;  box-shadow: 2px 2px 5px black;" >
 <img src = {pictures_list[5]} alt="article_1">
 <h3>{Headline[5]}</h3>
 <p>{DESC[5]}</p>
 <div style="display : flex ; flex-direction:row ;">
 <p style="color : grey">{publish_date[5]}</p>
 <a href={hrefs[9]} 
       style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; text-decoration: none; color: white; background-color: black; border-radius: 5px; border: none; transition: background-color 0.3s ease; margin-left:9%">
        Read More
    </a>
    </div>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:25% ; height:auto ; border:2px solid grey ; border-radius:5px ; padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[6]} alt="article_1">
 <h3>{Headline[6]}</h3>
 <p>{DESC[6]}</p>
 <div style="display : flex ; flex-direction:row ;">
 <p style="color : grey">{publish_date[6]}</p>
 <a href={hrefs[10]} 
       style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; text-decoration: none; color: white; background-color: black; border-radius: 5px; border: none; transition: background-color 0.3s ease; margin-left:9%">
        Read More
    </a>
    </div>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:30% ; height:auto ; border:2px solid grey ; border-radius:5px;padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[7]} alt="article_1">
 <h3>{Headline[7]}</h3>
 <p>{DESC[7]}</p>
<div style="display : flex ; flex-direction:row ;">
 <p style="color : grey">{publish_date[7]}</p>
 <a href={hrefs[11]} 
       style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; text-decoration: none; color: white; background-color: black; border-radius: 5px; border: none; transition: background-color 0.3s ease; margin-left:9%">
        Read More
    </a>
    </div>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:26% ; height:auto ; border:2px solid grey; border-radius:5px ; padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[8]} alt="article_1">
 <h3>{Headline[8]}</h3>
 <p>{DESC[8]}</p>
<div style="display : flex ; flex-direction:row ;">
 <p style="color : grey">{publish_date[8]}</p>
 <a href={hrefs[12]} 
       style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; text-decoration: none; color: white; background-color: black; border-radius: 5px; border: none; transition: background-color 0.3s ease; margin-left:9%">
        Read More
    </a>
    </div>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:37% ; height:auto ; border:2px solid grey ; border-radius:5px  ;padding:2% ;  box-shadow: 2px 2px 5px black;" >
 <img src = {pictures_list[9]} alt="article_1">
 <h3>{Headline[9]}</h3>
 <p>{DESC[9]}</p>
<div style="display : flex ; flex-direction:row ;">
 <p style="color : grey">{publish_date[9]}</p>
 <a href={hrefs[13]} 
       style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; text-decoration: none; color: white; background-color: black; border-radius: 5px; border: none; transition: background-color 0.3s ease; margin-left:9%">
        Read More
    </a>
    </div>
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:30% ; height:auto ; border:2px solid grey ; border-radius:5px  ;padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[10]} alt="article_1">
 <h3>{Headline[10]}</h3>
 <p>{DESC[10]}</p>
<div style="display : flex ; flex-direction:row ;">
 <p style="color : grey">{publish_date[10]}</p>
 <a href={hrefs[14]} 
       style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; text-decoration: none; color: white; background-color: black; border-radius: 5px; border: none; transition: background-color 0.3s ease; margin-left:9%">
        Read More
    </a>
    </div>
 

</div>

<div style="display : flex ; flex-direction : column ; gap : 10px;width:35% ; height:auto ; border:2px solid grey ; border-radius:5px  ;padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[11]} alt="article_1">
 <h3>{Headline[11]}</h3>
 <p>{DESC[11]}</p>
<div style="display : flex ; flex-direction:row ;">
 <p style="color : grey">{publish_date[11]}</p>
 <a href={hrefs[15]} 
       style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; text-decoration: none; color: white; background-color: black; border-radius: 5px; border: none; transition: background-color 0.3s ease; margin-left:9%">
        Read More
    </a>
    </div>
 
 
 

</div>
<div style="display : flex ; flex-direction : column ; gap : 10px;width:35% ; height:auto ; border:2px solid grey ; border-radius:5px  ;padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[12]} alt="article_1">
 <h3>{Headline[12]}</h3>
 <p>{DESC[12]}</p>
<div style="display : flex ; flex-direction:row ;">
 <p style="color : grey">{publish_date[12]}</p>
 <a href={hrefs[16]} 
       style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; text-decoration: none; color: white; background-color: black; border-radius: 5px; border: none; transition: background-color 0.3s ease; margin-left:9%">
        Read More
    </a>
    </div>
 
 </div>
 
 <div style="display : flex ; flex-direction : column ; gap : 10px;width:25% ; height:auto ; border:2px solid grey ; border-radius:5px  ;padding:2% ;  box-shadow: 2px 2px 5px grey;" >
 <img src = {pictures_list[13]} alt="article_1">
 <h3>{Headline[13]}</h3>
 <p>{DESC[13]}</p>
 <div style="display : flex ; flex-direction:row ;">
 <p style="color : grey">{publish_date[13]}</p>
 <a href={hrefs[17]} 
       style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; text-decoration: none; color: white; background-color: black; border-radius: 5px; border: none; transition: background-color 0.3s ease; margin-left:9%">
        Read More
    </a>
    </div></div>



</div>
</html>"""

st.markdown(structure_page , unsafe_allow_html=True)






