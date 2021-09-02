from app.download import Fetch
from conf import Conf


app = Fetch(Conf.ARTIFACTS, Conf.BUILD_NAME)
app.unzip()
