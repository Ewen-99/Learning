import requests

### no parameter
api = "https://api.thecatapi.com/v1/images/search"
response = requests.get(api)
print(response.text)

### get: with parameter
api = "https://httpbin.org/get"
query_params = {'name': 'Alice', 'age': '30'}
response = requests.get(api, params = query_params)
print(response.url)
print(response.text)

### post
api = "https://httpbin.org/get"
post_data = {'name': 'Alice', 'age': '30'}
response = requests.post(api, data = post_data)

### check status codes
response = requests.get(api)

# Check if the response.status_code is equal to the requests.codes value for "200 OK"
if (response.status_code == requests.codes.ok):
  print('The server responded succesfully!')
  
# Or if the request was not successful because the API did not exist
elif (response.status_code == requests.codes.not_found):
  print('Oops, that API could not be found!')

### headers
response = requests.get(api)
print(response.headers['content-type'])
print(response.headers['accept'])