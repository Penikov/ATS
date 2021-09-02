class Conf(object):

    BUILD_NAME = 'Audacity_Windows_64bit_1188560332_11e3a26'
    with open('C:\\AudacityTestTool\\token.txt', 'r') as t:
        TOKEN = t.read()
    ARTIFACTS = 'https://api.github.com/repos/audacity/audacity/actions/artifacts'
    DOWNLOAD_DIR = 'E:\\AudacityDownloads\\'
    EXTRACT_DIR = 'C:\\AudacityAutomation\\'
    TEST_ARCHIVE = 'testarchive.zip'


