import urllib.request


def main():
    check_site()


def check_site():
    site = "https://" + input("Enter site to check: ")
    try: urllib.request.urlopen(site), print('Connected')
    except urllib.error.URLError as err:
        print(err.reason)


if __name__ == '__main__':
    main()
