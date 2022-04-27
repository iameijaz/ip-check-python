'''
CODE FOR CHECKING YOUR IP ADDRESS
AUTHOR: IJAZ AHMED (VBT)
'''

# Check my IP Address

import requests 


def get_ip():
    res=requests.get('http://ip.jsontest.com')
    ip=res.text.split('"')[3].split('"')[0]


    #print(f"MY IP ADDRESS IS: {ip}")
    return ip

if __name__ == "__main__":
    print(f"My IP ADDRESS IS: {get_ip()}")
