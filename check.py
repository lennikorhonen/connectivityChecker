import urllib.request
import time
import schedule


def main():
    print('Startting...')
    check_connection()
    schedule.every(5).minutes.do(check_connection)
    while True:
        schedule.run_pending()
        time.sleep(5)


def check_connection():
    print(read_file())
    check = read_file()

    for site in check:
        if urllib.request.urlopen(site).getcode() == 200:
            print(site, ':', urllib.request.urlopen(site).getcode())
        else:
            print(site, ': Not up, error code:',
                  urllib.request.urlopen(site).getcode())


def read_file():
    with open('./sites.txt', encoding='utf=8') as URL:
        return URL.read().splitlines()


if __name__ == '__main__':
    main()
