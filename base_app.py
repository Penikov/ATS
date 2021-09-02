from app.download import Fetch
from conf import Conf
from app.launch import Launch


app = Fetch(Conf.ARTIFACTS, Conf.BUILD_NAME)
app.unzip()
Launch(Conf.EXTRACT_DIR).run_max()
