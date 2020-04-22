import requests
my_version = "1.01"
my_url = "https://raw.githubusercontent.com/sophia-genetics/uploader/master/wrapper.py"
my_name = "wrapper2.py"
def get_remote_version():
    url = "https://raw.githubusercontent.com/sophia-genetics/uploader/master/version.txt"
    version_file = requests.get(url)
    version = version_file.text
    return version

def update_self():
    new_self = requests.get(my_url)
    me = open(my_name, 'wb')
    me.write(new_self.content)
    me.close()


def main():
    if get_remote_version() > my_version :
        update_self()

if __name__ == "__main__":
    main()
