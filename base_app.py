from app.download import Fetch
from conf import Conf
from app.interactions import Welcome_screen


app = Fetch(Conf.ARTIFACTS, Conf.BUILD_NAME)
app.unzip()
Welcome_screen().click_checkbox().close()
