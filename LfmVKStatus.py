import pylast
import os
import vk_api
from time import sleep

VK = VKTOKEN
LASTFM_API_KEY = LASTKEY
LASTFM_API_SECRET = LASTSECRET
network = pylast.LastFMNetwork(api_key=LASTFM_API_KEY, api_secret=LASTFM_API_SECRET)
api = vk_api.VkApi(token=VK).get_api()
user=USERNAME


def main():
    try:
        user: pylast.User = network.get_user(user)
        track: pylast.Track = user.get_now_playing()
    except Exception as e: 
        user: pylast.User = network.get_user(user)
        track = " "     
    return track 
    
def get_status():
    usr_id=VKUSERID #numbers, not strings
    status=api.users.get(user_id=usr_id, fields='status')
    return status
    
def set_status():
    track=main()
    api.status.set(text=f"{track}")

if __name__ == "__main__":
   
   while True:     
       while True: 
           catch_status = get_status()
           current_track = main()
           current_status = catch_status[0]["status"]
           if f"{current_track}" == current_status: 
               sleep(3)
               break
           else: 
               set_status()
               break 

           
