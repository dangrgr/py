import requests

# # Session
# s = requests.Session()

# userName = {'userName': 'John99'} 
# location = {'location': 'NewYork'}

# setCookieUrl = 'https://httpbin.org/cookies/set'
# getCookiesUrl = 'https://httpbin.org/cookies'

# s.get(setCookieUrl, params=userName)
# s.get(setCookieUrl, params=location)

# r = s.get(getCookiesUrl)
# print(r.text)



# # history / redirects
# r = requests.get('http://github.com', allow_redirects=False)
# # history shows redirect from http to https with 301
# print(r.history) # History is empty if using allow_redirects=False
# print(r.url)



# # Handle status codes / Timeouts
# r = requests.get("https://httpbin.org/status/200", timeout=0.01)
# r.raise_for_status()



# # cookies
# url = 'https://httpbin.org/cookies'

# cookies = {'location': 'New York'}
# r = requests.get(url, cookies=cookies)
# print(r.text)

# r2 = requests.get('https://google.com')
# print(r2.cookies['1P_JAR'])

# requestsJar = requests.cookies.RequestsCookieJar()
# requestsJar.set("userId", "John99", domain="httpbin.org", path="/cookies")
# requestsJar.set("cartItem", "laptop", domain="httpbin.org", path="/cart")
# r3 = requests.get(url, cookies=requestsJar)
# print(r3.text)



# # Post headers
# headers = {'content-type': 'multipart/form-data'}
# r = requests.post('https://httpbin.org/post', headers=headers)
# print(r.headers['content-type'])



# # POST JSON       
# data = {'firstName': 'John'}
# r = requests.post('http://httpbin.org/post', json=data)
# print(r.text)


# # GET JSON
# data = {'firstName': 'John'}
# r = requests.get('https://api.github.com/events', json=data)
# events = r.json()
# print(events[0]['id'])


# # Uploading a File
# url = 'https://httpbin.org/post'
# #files = {'file': open('py/playground/USCarBrands.csv', 'rb')}
# files = [
#     ('copy1', ('USCarBrands.csv', open('py/playground/USCarBrands.csv', 'rb'), 'csv')),
#     ('copy2', ('USCarBrands.csv', open('py/playground/USCarBrands.csv', 'rb'), 'csv'))
# ]

# r = requests.post(url, files=files)
# print(r.status_code)
# print(r.text)

