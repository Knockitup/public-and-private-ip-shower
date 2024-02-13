import socket
from requests import get
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Private IP:" + IPAddr)
ip = get('https://api.ipify.org').content.decode('utf8')
print('Public IP: {}'.format(ip))
from requests import get
