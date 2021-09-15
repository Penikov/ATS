from app.download import Fetch
from app.launch import Exe
from conf import Conf


class BaseApp:
    def __init__(self):
        self.conf = Conf

    def fetch(self):
        file = Fetch(Conf.BUILD_NAME, Conf.EXTRACT_DIR)
        return file

    def unzip(self):
        extract = self.fetch()
        return extract

    def launch_latest(self):
        start = Exe().run_max()
        return start



if __name__ == '__main__':
    BaseApp().fetch()
    BaseApp().unzip()
    BaseApp().launch_latest()
