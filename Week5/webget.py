import os.path
import urllib.parse
import urllib.request
import os
import urllib.request as req
from urllib.parse import urlparse

def download(url, to=None):
    """Download a remote file specified by a URL to a 
    local directory.

    :param url: str
        URL pointing to a remote file.
        
    :param to: str
        Local path, absolute or relative, with a filename 
        to the file storing the contents of the remote file.
    """
    with req.urlopen(url) as response:
        data = response.readlines()

    filename = os.path.basename(url)
    if to is not None:
        filename = to
    with open(filename, 'wb') as f:
        f.writelines(data)

if __name__ == "__main__":
    url = 'https://admin.opendata.dk/dataset/0cd08120-3fb4-4ab9-8b8b-2817ca190e2f/resource/6c5badab-8d8d-40cc-a382-50bdcfb77317/download/udlansdatacodes.csv'
    download(url, './my_modules/petererdejlig.csv')