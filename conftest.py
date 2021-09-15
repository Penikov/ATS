import pytest
from base_app import BaseApp
from app.download import Fetch
from conf import Conf


@pytest.fixture(scope='module')
def fetch():
    dnld = Fetch(Conf.ARTIFACTS, Conf.BUILD_NAME).unzip()
    return dnld



@pytest.fixture(scope='module')
def app():
    exe = BaseApp().launch_latest()
    return exe


