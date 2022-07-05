import requests
import base64
import streamlit as st
from devtools import debug

URL = "http://127.0.0.1:8000"
headers = {'Bypass-Tunnel-Reminder': "go",
           'mode': 'no-cors'}

def check_if_valid_backend(url):
    try:
        resp = requests.get(url, timeout=5, headers=headers)
        return resp.status_code == 200
    except requests.exceptions.Timeout:
        return False

def call_dalle(url, chap, num_images=1):
    data = {"text": chap[0]["summary_text"], "num_images": num_images}
    resp = requests.post(url + "/dalle", headers=headers, json=data)
    if resp.status_code == 200:
        return resp
 
def create_and_show_images(chap_sum, num_images):
    valid = check_if_valid_backend(URL)
    if not valid:
        st.write("Backend service is not running")
    else:
        for ind, chap in enumerate(chap_sum):
            resp = call_dalle(URL, chap, num_images)
            if resp is not None:
                #debug(resp.json())
                for data in resp.json()['generatedImgs']:
                    img_data = base64.b64decode(data)
                    st.write(f"Chapter {ind}")
                    st.image(img_data)
