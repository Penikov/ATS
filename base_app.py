from app.downloader import Download
from conf import Conf


app = Download(Conf.ARTIFACTS, Conf.BUILD_NAME)
app.unzip()
