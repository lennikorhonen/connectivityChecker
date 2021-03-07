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

    try:
        for site in check:
            print(site, "status code:", urllib.request.urlopen(site).getcode())
    except urllib.error.URLError as e:
        print(site, "error reason:", e.reason)



def read_file():
    with open('./sites.txt', encoding='utf=8') as URL:
        return URL.read().splitlines()


if __name__ == '__main__':
    main()
