import requests
my_version = "1.00"
my_url = "https://raw.githubusercontent.com/sophia-genetics/uploader/master/wrapper.py"

def get_remote_version():
    url = "https://raw.githubusercontent.com/sophia-genetics/uploader/master/version.txt"
    version_file = requests.get(url)
    version = version_file.text
    return version

def update_self():
    requests.get(my_url)
    me = open(__file__, 'wb')
    me.write()
    me.close()


def main():
    if get_remote_version() > my_version :
        update_self()

if __name__ == "__main__":
    main()
