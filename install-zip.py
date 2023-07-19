import requests
import os
import zipfile
import sys
from time import sleep
from zipfile import ZipFile

def DownloadFile(url):
    local_filename = url.split('/')[-1] + ".zip"
    try:
        print('Requesting uri data...')
        r = requests.get(url)
        if r.status_code == 200:
            print('Creating new zip file...')
            f = open(local_filename, 'wb')
            print('Writing requested data to file...')
            for chunk in r.iter_content(chunk_size=512 * 1024): 
                if chunk:
                    f.write(chunk)
            f.close()
            
            InstallZipFile(local_filename)
        else:
            print("Couldn't download file!")
    except Exception as e:
        print(e)
        print('Invalid URI!')
    return 

def InstallZipFile(filename):
    if zipfile.is_zipfile(filename):
        print('Extracting zip file...')
        zip_ref = ZipFile(filename)
        extracted = zip_ref.namelist()
        zip_ref.extractall()
        url = '"' + os.getcwd() + '\\' + extracted[0].replace('/', '\\') + '"'
        trying = True
        while trying:
            try:
                print('Trying to remove ' + filename + '...')
                print('Installed in dir: ' + url)
                os.remove(filename)
                trying = False
            except:
                return
    else:
        print('File is not a zip!')

DownloadFile(sys.argv[1])