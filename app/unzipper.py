from zipfile import ZipFile
from os import listdir
import io

zip_dir = 'e:\Audacity_releases\Journaling\\'
dest_dir = 'c:\Audacity_journaling\\'


def unzip_archive():
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

                print('Well done!')


unzip_archive()
