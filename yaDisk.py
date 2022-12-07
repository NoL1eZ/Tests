import yadisk
import requests



def get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(TOKEN)
        }

def new_folder(path):
    create_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = get_headers()
    params = {'path': path}
    response = requests.put(url=create_url, headers=headers, params=params)
    # print (str(response))
    return str(response)

TOKEN = 'y0_AgAAAAAIYDeqAADLWwAAAADVxBBL3M6zgCrrSR6Grx3WZRBXlBX1Jck'
file_path = 'asdaasdsasaf'


new_folder(file_path)