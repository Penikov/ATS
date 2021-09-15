import requests
from zipfile import ZipFile
from os import listdir
from conf import Conf
import io

token = Conf.TOKEN
headers = {'Content-type': 'application/vnd.github.v3+json',
           'Authorization': Conf.TOKEN}
zip_dir = Conf.DOWNLOAD_DIR
dest_dir = Conf.EXTRACT_DIR


class Fetch:

    """ Class with method to unzip a downloaded Audacity build

    artifacts: A string, the method of GitHub API, which returns a list of actions of repository.

    file: A string, the filename of the Audacity build, which you would like to download and test.

    unzip: A method, which only extract files into the directory. You can point path to the destination directory
    in /conf.py

    Please note: __init__ method uses GitHub API endpoint that requires authorization. 'Download' class
    uses authorization with personal token. So you need to get one to successful download.

    The token has stored in a simple .txt file.
    Please note: The GitHub API requires token in specific format. You should write your token in a file that way:
    token [your personal token here]

    """


    def __init__(self, artifacts, file):
        self.artifacts = artifacts
        self.file = file

        f = ''
        r = requests.get(self.artifacts + '?per_page=' + Conf.PAGE_SIZE + '&' + '&page=' + Conf.PAGE, allow_redirects=True, headers=headers)
        artifact = r.json()['artifacts']
        print('Searching the file in the array.')
        for i in artifact:
            if self.file == i['name']:
                f = i['archive_download_url']
        print('Downloading...')
        f = requests.get(f, allow_redirects=True, headers=headers)
        new_file = Conf.DOWNLOAD_DIR + Conf.TEST_ARCHIVE
        open(new_file, 'wb').write(f.content),
        print('The build has been downloaded')

    def unzip(self):
        arr = zip_dir + str(listdir(zip_dir)[-1])
        print(arr)

        with ZipFile(arr) as z:
            nested_z = z.namelist()[0]
            print(nested_z)
            with z.open(nested_z) as z2:
                z2_filedata = io.BytesIO(z2.read())
                with ZipFile(z2_filedata) as nested_z2:
                    z2_files = nested_z2.namelist()
                    print(z2_files[2])
                    for i in z2_files:
                        nested_z2.extract(i, dest_dir)
                        print(i)

                    print('Well done! All files have extracted')



if __name__ == '__main__':
    Fetch(Conf.ARTIFACTS, Conf.BUILD_NAME).unzip()
