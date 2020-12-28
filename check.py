import urllib.request

def main():
    print(check_connection())
    check = check_connection()

    for site in check:
        if urllib.request.urlopen(site).getcode() == 200:
            print(site,':', urllib.request.urlopen(site).getcode())
        else:
            print('Not up')


def check_connection():
    with open('./sites.txt', encoding='utf=8') as URL:
        return URL.read().splitlines()

if __name__ == '__main__':
    main()
