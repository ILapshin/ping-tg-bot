import subprocess
# import os

class Service:

    def __init__(self, url_list: list):
        self.url_list = url_list

    
    def ping_all(self):
        unreacheble_urls = []

        for url in self.url_list:
            command = ['ping', '-c', '1', '-q', url]
            try:
                response = subprocess.call(command)
                if response != 0:
                    unreacheble_urls.append(url)
            except:
                unreacheble_urls.append(url)

        return unreacheble_urls
    