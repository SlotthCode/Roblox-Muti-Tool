#Imports
import requests, threading
import time
from time import sleep

with open('cookies.txt', 'r') as cookies:
    cookies1 = cookies.read().splitlines()
	



#start of code
print("  _____  _     _        ____        _     ______    _                _ ")
print(" |  __ \| |   | |      |  _ \      | |   |  ____|  (_)              | |")
print(" | |__) | |__ | |_  __ | |_) | ___ | |_  | |__ _ __ _  ___ _ __   __| |")
print(" |  _  /| '_ \| \ \/ / |  _ < / _ \| __| |  __| '__| |/ _ \ '_ \ / _` |")
print(" | | \ \| |_) | |>  <  | |_) | (_) | |_  | |  | |  | |  __/ | | | (_| |")
print(" |_|  \_\_.__/|_/_/\_\ |____/ \___/ \__| |_|  |_|  |_|\___|_| |_|\__,_|")
print("Made by Slotth")
print("---------------------------------------")




print("1 Bot Friend")

choice = input("Pick a Tool > ")

if choice == "1":
	userId = input("userID= ")

def add_user(cookie, userId):
try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
            session.post(f'https://friends.roblox.com/v1/users/{userId}/request-friendship')
    except Exception as e:
        print("An error has occured! You might not have cookies {}".format(e))
        pass
			
sleep(1.0)

print("Bot Friends")

for x in cookies1:
	threading.Thread(target=add_user, args=(x, userId,)).start()
	#end
