from toripchanger import TorIpChanger

print('''
  ,d                           
  88                           
MM88MMM ,adPPYba,  8b,dPPYba,  
  88   a8"     "8a 88P'   "Y8  
  88   8b       d8 88          
  88,  "8a,   ,a8" 88          
  "Y888 `"YbbdP"'  88 

          TOR Changer IP
''')

tor_ip_changer = TorIpChanger(tor_password='my password', tor_port=9051, local_http_proxy='127.0.0.1:8118')
tor_ip_changer.get_new_ip()
