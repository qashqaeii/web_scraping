import streamlit as st


st.set_page_config(
    page_title="Webscraping Methods ( REQUEST )",
    page_icon="🕷",

)
st.sidebar.success("develop by : HOSSEIN QASHQAEII 🧛")
st.image("request.png")
st.header("HTTP request and retrieve data from a web page:")

code = '''
import requests

# Send a GET request to a URL
url = 'https://www.example.com'
response = requests.get(url)

# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    # Get the content of the response
    content = response.content

    # Print the content
    print(content)
else:
    print('Error:', response.status_code)

'''
st.code(code, language="python")

#___________________________________
st.write("""
In this example, we import the requests library and use the get() function to send a GET request to the specified URL (https://www.example.com). We store the response in the response variable.

We then check the status code of the response using response.status_code. If the status code is 200 (indicating a successful request), we can access the content of the response using response.content. In this example, we simply print the content to the console.

If the status code is not 200, we print an error message along with the actual status code.

You can modify the code to suit your specific needs, such as adding headers, handling different request methods (e.g., POST), passing parameters, or parsing the retrieved content using libraries like BeautifulSoup.

Remember to install the requests library before running this code by executing pip install requests in your terminal or command prompt.
""")

st.header("Sending a GET request and retrieving JSON data")

code = '''
import requests

url = 'https://api.example.com/data'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)


'''
st.code(code, language="python")
#___________________________________
#___________________________________

st.header("Sending a POST request with JSON payload:")

code = '''
import requests

url = 'https://api.example.com/submit'
data = {'name': 'John', 'age': 30}
response = requests.post(url, json=data)

if response.status_code == 200:
    print('Request successful')
else:
    print('Error:', response.status_code)


'''
st.code(code, language="python")
#___________________________________
#___________________________________

st.header("Sending a request with headers")

code = '''
import requests

url = 'https://api.example.com/data'
headers = {'User-Agent': 'My User Agent'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)


'''
st.code(code, language="python")
#___________________________________
#___________________________________
st.header("Sending a request with custom headers:")

code = '''
import requests

url = 'https://api.example.com/data'
headers = {'Authorization': 'Bearer your_token', 'User-Agent': 'MyApp/1.0'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)


'''
st.code(code, language="python")
#___________________________________
#___________________________________

st.header("Sending a request with query parameters")

code = '''
import requests

url = 'https://api.example.com/data'
params = {'category': 'books', 'limit': 10}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)


'''
st.code(code, language="python")
#___________________________________
#___________________________________

st.header("Handling request timeouts:")

code = '''
import requests

url = 'https://api.example.com/data'
try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print('Error:', response.status_code)
except requests.Timeout:
    print('Request timed out')


'''
st.code(code, language="python")
#___________________________________
#___________________________________

st.header("Sending a request with cookies:")

code = '''
import requests

url = 'https://api.example.com/data'
cookies = {'session_id': '1234567890'}
response = requests.get(url, cookies=cookies)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)


'''
st.code(code, language="python")
#___________________________________
#___________________________________

st.header("Uploading a file with a POST request:")

code = '''
import requests

url = 'https://api.example.com/upload'
file_path = '/path/to/file.txt'
with open(file_path, 'rb') as file:
    files = {'file': file}
    response = requests.post(url, files=files)

if response.status_code == 200:
    print('File uploaded successfully')
else:
    print('Error:', response.status_code)


'''
st.code(code, language="python")
#___________________________________

#___________________________________

st.header("Sending a request with custom authentication:")

code = '''
import requests
from requests.auth import HTTPBasicAuth

url = 'https://api.example.com/data'
auth = HTTPBasicAuth('username', 'password')
response = requests.get(url, auth=auth)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)


'''
st.code(code, language="python")
#___________________________________

#___________________________________

st.header("Sending a request with a custom timeout for connection and read:")

code = '''
import requests

url = 'https://api.example.com/data'
timeout = (3, 10)  # 3 seconds for connection, 10 seconds for read
response = requests.get(url, timeout=timeout)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)


'''
st.code(code, language="python")
#___________________________________

#___________________________________

st.header("Sending a POST request with JSON data:")

code = '''
import requests

url = 'https://api.example.com/data'
data = {'name': 'John', 'age': 30}
response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print('Error:', response.status_code)


'''
st.code(code, language="python")
#___________________________________

st.header("Sending a PUT request with form data:")

code = '''
import requests

url = 'https://api.example.com/user/1'
data = {'name': 'John', 'age': 30}
response = requests.put(url, data=data)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print('Error:', response.status_code)


'''
st.code(code, language="python")
#___________________________________

#___________________________________

st.header("Sending a POST request with JSON payload:")

code = '''
import requests
import json

url = 'https://api.example.com/data'
payload = {'name': 'John Doe', 'age': 25}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)


'''
st.code(code, language="python")
#___________________________________

st.header("Sending a request with query parameters:")

code = '''
import requests

url = 'https://api.example.com/search'
params = {'q': 'python', 'limit': 10}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)


'''
st.code(code, language="python")
