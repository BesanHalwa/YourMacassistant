"""
api key : 6802d02f-7b72-4b97-ba8d-9f314b0eba35

"""

import os
import json
import requests

# dense cap
def dense_cap(image_path, number_of_detections=4):
    import requests
    r = requests.post(
        "https://api.deepai.org/api/densecap",
        files={
            'image': open(image_path, 'rb'),
        },
        headers={'api-key': '6802d02f-7b72-4b97-ba8d-9f314b0eba35'}
    )
    print(r.json())
    captions = r.json()
    for i in range(number_of_detections):
        cap = "there is " + captions['output']['captions'][i]['caption']
        os.system("say " + cap)

def scene_cap(image_path, number_of_detections=1):
    r = requests.post(
    "https://api.deepai.org/api/places",
    files={
        'image': open(image_path, 'rb'),
    },
    headers={'api-key': '6802d02f-7b72-4b97-ba8d-9f314b0eba35'}
    )
    print(r.json())
    captions = r.json()
    for i in range(number_of_detections):
        cap = "You are looking at" + captions['output']['places'][i]['name']
        os.system("say " + cap)
