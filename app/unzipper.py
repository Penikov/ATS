from zipfile import ZipFile
from os import listdir
import io
from conf import Conf

zip_dir = Conf.DOWNLOAD_DIR
dest_dir = Conf.EXTRACT_DIR


def unzip():
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


unzip()
