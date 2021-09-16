import pytest
from base_app import BaseApp
from app.download import Fetch
from app.interactions import Audacity

from conf import Conf


@pytest.fixture(scope='module')
def fetch():
    dnld = Fetch(Conf.ARTIFACTS, Conf.BUILD_NAME).unzip()
    return dnld


@pytest.fixture(scope='module')
def app():
    """This fixture opens a new instance of BaseApp class, which runs Audacity"""
    exe = BaseApp().launch_latest()
    return exe


@pytest.fixture(scope='function')
def close_audacity(app):
    """This fixture is closing Audacity"""
    yield
    Audacity(app).close_button()







