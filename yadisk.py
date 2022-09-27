import requests
import os

class YaUploader:
    host = 'https://cloud-api.yandex.net'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'content-type': 'application/json', 'Authorization': f'OAuth {self.token}'}


    def get_upload_link(self, path):
        url = f'{self.host}/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': f'/{os.path.basename(path)}', 'overwrite': 'True'}
        response = requests.get(url, headers=headers, params=params)
        return response.json().get('href')

    def get_upload_file(self, path):
        upload_link = self.get_upload_link(path)
        headers = self.get_headers()
        response = requests.put(upload_link, data=open(path, 'rb'), headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')