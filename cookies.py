'''
This script shows different cookie-objects within the browser object in requests module
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
