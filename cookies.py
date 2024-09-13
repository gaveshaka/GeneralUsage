'''
This script shows different cookie-objects within the browser object in requests module
each code snippet is separated by a #=======

'''
import requests

my_browser=requests.session()
print(f"The 'type' of 'my_browser' object is  {type(my_browser)}")
print("===================")

print(f"The attributes and methods of my_browser are:\n {dir(my_browser)}")
print("===================")
print(f" The 'type' of 'my_browser.cookies' is : {type(my_browser.cookies)}")
print("===================")
print(f"The attributes and methods of 'my_browser.cookies' are:\n {dir(my_browser.cookies)}")
print("===================")
print(f" The 'type' of 'my_browser.cookies._cookies' is : {type(my_browser.cookies._cookies)}")
print("===================")
print(f"The attributes and methods of 'my_browser.cookies._cookies' are:\n {dir(my_browser.cookies._cookies)}")
print("===================")
print(f" Printing keys  of 'my_browser.cookies._cookies' are:\n {dir(my_browser.cookies._cookies.values())}")


#================
import requests
response_object1=None
my_browser=None
my_browser=requests.session()
response_object1=my_browser.get("https://bing.com")
print(f" The 'type' of 'my_browser.cookies' is : {type(my_browser.cookies)} and its keys are")
print(my_browser.cookies.keys())
 
print("\n")
print(f"\nThe 'type' of 'my_browser.cookies._cookies' is : {type(my_browser.cookies._cookies)} and its keys are")
print(my_browser.cookies._cookies.keys())
 
print("\n")
my_browser.cookies._cookies['.bing.com'].values()

#==========================

import requests
response_object1=None
my_browser=None
my_browser=requests.session()
response_object1=my_browser.get("https://sans.org")
print(my_browser.cookies)
print("\n\n\n")
print(my_browser.cookies._cookies)
print("\n\n\n")
print(my_browser.cookies._cookies['.sans.org']['/'])
print("\n\n\n\n")
print(my_browser.cookies._cookies['.sans.org']['/'].keys())

#================================
