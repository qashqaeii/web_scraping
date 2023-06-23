import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Webscraping Methods",
    page_icon="🕷",

)
st.sidebar.success("develop by : HOSSEIN QASHQAEII 🧛")
st.title("WebScraping Roadmap")
st.image("main.png")

st.header("Understand the website")
st.write(" Familiarize yourself with the website you want to scrape. Identify the structure, layout, and the data you want to extract. Determine if the website allows scraping by checking its terms of service or robots.txt file")

st.header("Choose a programming language")
st.write("Select a programming language that is suitable for web scraping. Python is a popular choice due to its rich ecosystem of libraries like BeautifulSoup and Scrapy.")

st.header("Set up your development environment")
st.write("Install the necessary tools and libraries for web scraping. For Python, you can use pip to install libraries like BeautifulSoup, Requests, and Selenium.")

st.header("Inspect the HTML structure")
st.write("Use your web browser's developer tools to inspect the HTML structure of the website. This will help you identify the elements and attributes containing the data you want to extract.")

st.header("Choose a scraping approach")
st.write("Depending on the website's structure and complexity, you can choose between two main approaches:")
col1,col2 = st.columns(2)
with col1:
    st.title("Static scraping")
    st.write("If the data is present in the HTML source code and doesn't require interaction with JavaScript, you can use libraries like BeautifulSoup or lxml to parse the HTML and extract the desired information.")
with col2:
    st.title("Dynamic scraping")
    st.write("If the website heavily relies on JavaScript to load or modify content, you may need to use tools like Selenium or Puppeteer. These tools allow you to automate browser actions and extract data from dynamically generated content.")



#______________________________________________________________
