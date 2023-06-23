import streamlit as st
st.set_page_config(
    page_title="Webscraping Methods (SELENIUM )",
    page_icon="🕷",

)
st.sidebar.success("develop by : HOSSEIN QASHQAEII 🧛")
st.image("Selenium_Logo.png")
#____________________________________________________________
st.header("Dynamic Scraping Example using Selenium ✔️ ")
code = """
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Selenium options
options = Options()
options.add_argument('--headless')  # Run in headless mode without displaying the browser window

# Set up the WebDriver
selenium_service = Service('path/to/chromedriver')  # Path to the ChromeDriver executable
driver = webdriver.Chrome(service=selenium_service, options=options)

# Navigate to the target URL
driver.get('https://example.com')

# Find and extract specific data using Selenium
title_element = driver.find_element(By.TAG_NAME, 'title')
title = title_element.get_attribute('text')

# Print the extracted data
print('Title:', title)

# Quit the WebDriver
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
st.header("Scraping data from dynamic websites using Selenium ✔️ ")
code = """
from selenium import webdriver

# Set up the Selenium driver (replace 'chromedriver' with the path to your driver)
driver = webdriver.Chrome('chromedriver')

# Navigate to the webpage
driver.get('https://www.example.com')

# Find and extract specific elements using Selenium's methods
title_element = driver.find_element_by_css_selector('h1')
title = title_element.text

# Print the extracted data
print('Title:', title)

# Close the Selenium driver
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
st.header("Scraping data from a JavaScript-rendered page using Selenium: ✔️ ")
code = """
from selenium import webdriver

# Set up the Selenium driver (replace 'chromedriver' with the path to your driver)
driver = webdriver.Chrome('chromedriver')

# Navigate to the webpage
driver.get('https://www.example.com')

# Execute JavaScript to load dynamic content
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# Wait for the content to load
driver.implicitly_wait(10)

# Extract and print the desired data
data_element = driver.find_element_by_css_selector('.data')
data = data_element.text
print('Data:', data)

# Close the Selenium driver
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
st.header("Scraping dynamic content ✔️ ")
code = """
from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the webpage
driver.get('https://www.example.com')

# Find and extract the dynamic content using appropriate selectors
element = driver.find_element_by_css_selector('.class-name')
print(element.text)

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
st.header("Filling out forms and submitting with Selenium ✔️ ")
code = """
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage with the form
driver.get('https://www.example.com')

# Find the input fields and fill them with data
name_input = driver.find_element_by_name('name')
name_input.send_keys('John Doe')

email_input = driver.find_element_by_name('email')
email_input.send_keys('johndoe@example.com')

# Submit the form
submit_button = driver.find_element_by_css_selector('.submit-button')
submit_button.click()

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#_________________________________________________________________
st.header("Handling pop-up windows - Selenium ✔️ ")
code = """
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('https://www.example.com')

# Click a button to open a pop-up window
popup_button = driver.find_element_by_id('popup-button')
popup_button.click()

# Switch to the pop-up window
driver.switch_to.window(driver.window_handles[1])

# Perform actions in the pop-up window
popup_element = driver.find_element_by_css_selector('.popup-element')
print(popup_element.text)

# Close the pop-up window
driver.close()

# Switch back to the main window
driver.switch_to.window(driver.window_handles[0])

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#_________________________________________________________________
st.header("Taking screenshots in  Selenium ✔️ ")
code = """
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('https://www.example.com')

# Take a screenshot of the entire webpage
driver.save_screenshot('screenshot.png')

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#_________________________________________________________________
st.header("Executing JavaScript code: using Selenium ✔️ ")
code = """
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('https://www.example.com')

# Execute JavaScript code to interact with the webpage
driver.execute_script("document.getElementById('element-id').value = 'new value';")

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#_________________________________________________________________
st.header("Scrolling and loading dynamic content in Selenium ✔️ ")
code = """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('https://www.example.com')

# Scroll down to load dynamic content
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Wait for the content to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.dynamic-content')))

# Extract the loaded content
dynamic_content = driver.find_element_by_css_selector('.dynamic-content')
print(dynamic_content.text)

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#_________________________________________________________________
st.header("Handling dropdown menus and selecting options in Selenium ✔️ ")
code = """
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage with the dropdown menu
driver.get('https://www.example.com')

# Find the dropdown menu element
dropdown = Select(driver.find_element_by_id('dropdown-menu'))

# Select an option by value
dropdown.select_by_value('option-value')

# Select an option by visible text
dropdown.select_by_visible_text('Option Text')

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#_________________________________________________________________
st.header("Capturing network traffic in Selenium ✔️ ")
code = """
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Start capturing network traffic
driver.get('chrome://net-export')
driver.execute_script("chrome.netExport.startExport({\"captureMode\":\"all\"});")

# Navigate to the webpage
driver.get('https://www.example.com')

# Perform scraping actions

# Stop capturing network traffic
driver.execute_script("chrome.netExport.stopExport();")

# Retrieve the exported network traffic log
net_log = driver.execute_script("return chrome.netExport.getHar();")

# Process the network log data as per your requirement

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#_________________________________________________________________
st.header("Interacting with forms in Selenium ✔️ ")
code = """
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage with a form
driver.get('https://www.example.com')

# Fill in a text input field
text_input = driver.find_element_by_id('input-field')
text_input.send_keys('Hello, World!')

# Submit the form
submit_button = driver.find_element_by_css_selector('button[type="submit"]')
submit_button.click()

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#_________________________________________________________________
st.header("Extracting data from a table in Selenium ✔️ ")
code = """
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage with a table
driver.get('https://www.example.com')

# Find the table element
table = driver.find_element(By.CSS_SELECTOR, 'table')

# Iterate over the rows of the table
rows = table.find_elements(By.TAG_NAME, 'tr')
for row in rows:
    # Extract data from each cell in the row
    cells = row.find_elements(By.TAG_NAME, 'td')
    for cell in cells:
        print(cell.text)

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#_________________________________________________________________
st.header("Scraping dynamic content with scrolling in Selenium ✔️ ")
code = """
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage with dynamic content
driver.get('https://www.example.com')

# Scroll down to load more content
driver.find_element_by_tag_name('body').send_keys(Keys.END)

# Continue scrolling until all content is loaded
while True:
    # Scroll down
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    
    # Check if all content is loaded
    if is_all_content_loaded():
        break

# Extract the desired data from the page

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________

#_________________________________________________________________
st.header("Handling file downloads in Selenium ✔️ ")
code = """
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage with a file download
driver.get('https://www.example.com')

# Find the download link
download_link = driver.find_element_by_link_text('Download File')

# Get the download URL
download_url = download_link.get_attribute('href')

# Download the file using a HTTP library (e.g., requests)

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________

#_________________________________________________________________
st.header("Automating login and authentication in Selenium ✔️ ")
code = """
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get('https://www.example.com/login')

# Fill in the login form
username_input = driver.find_element_by_id('username')
password_input = driver.find_element_by_id('password')

username_input.send_keys('your_username')
password_input.send_keys('your_password')

# Submit the login form
submit_button = driver.find_element_by_css_selector('button[type="submit"]')
submit_button.click()

# Wait for the authentication process to complete

# Continue scraping or interacting with authenticated content

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#_________________________________________________________________
st.header("Scraping images from a website in Selenium ✔️ ")
code = """
from selenium import webdriver
import urllib.request

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage with images
driver.get('https://www.example.com')

# Find all image elements on the page
images = driver.find_elements_by_tag_name('img')

# Download and save each image
for image in images:
    image_url = image.get_attribute('src')
    urllib.request.urlretrieve(image_url, 'image.jpg')

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#_________________________________________________________________
st.header("Handling JavaScript alerts in Selenium ✔️ ")
code = """
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage with a JavaScript alert
driver.get('https://www.example.com')

# Trigger the JavaScript alert
alert_button = driver.find_element_by_id('alert-button')
alert_button.click()

# Switch to the alert and accept it
alert = driver.switch_to.alert
alert.accept()

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#_________________________________________________________________
st.header("Capturing screenshots of web pages in Selenium ✔️ ")
code = """
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage to capture
driver.get('https://www.example.com')

# Capture a screenshot of the entire page
driver.save_screenshot('screenshot.png')

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
#_________________________________________________________________
st.header("Interacting with checkboxes in Selenium ✔️ ")
code = """
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage with checkboxes
driver.get('https://www.example.com')

# Find the checkbox element
checkbox = driver.find_element_by_id('checkbox')

# Check the checkbox if it is unchecked
if not checkbox.is_selected():
    checkbox.click()

# Uncheck the checkbox if it is checked
if checkbox.is_selected():
    checkbox.click()

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
st.header("Scraping data using XPath expressions in Selenium ✔️ ")
code = """
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage with the data
driver.get('https://www.example.com')

# Find elements using XPath
elements = driver.find_elements_by_xpath('//xpath_expression')

# Extract data from the elements
for element in elements:
    print(element.text)

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
st.header("Waiting for elements to load: in Selenium ✔️ ")
code = """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('https://www.example.com')

# Wait for an element to be visible
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'element-id'))
)

# Perform actions on the element
# ...

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
st.header("Scrolling to load dynamic content: in Selenium ✔️ ")
code = """
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('https://www.example.com')

# Scroll down to load dynamic content
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# Close the browser
driver.quit()

"""
st.code(code,language="python")
st.markdown("---")
#_________________________________________________________________
