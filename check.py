import urllib.request

URL = input("URL to check: ")

if (urllib.request.urlopen(URL).getcode() == 200):
    print("Site is up, site connection code:", urllib.request.urlopen(URL).getcode())
else:
    print(urllib.request.urlopen(URL).getcode())
