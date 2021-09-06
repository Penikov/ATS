class Conf(object):

    BUILD_NAME = 'Audacity_Windows_64bit_1197865240_a06cab7'
    with open('C:\\AudacityTestTool\\token.txt', 'r') as t:
        TOKEN = t.read()
    ARTIFACTS = 'https://api.github.com/repos/audacity/audacity/actions/artifacts'
    DOWNLOAD_DIR = 'E:\\AudacityDownloads\\'
    EXTRACT_DIR = 'C:\\AudacityAutomation\\'
    TEST_ARCHIVE = 'testarchive.zip'


    # Results per page (max 100)
    # Github API Default: 30
    PAGE_SIZE = '100'

    # Page number of the results to fetch.
    # Github Default: 1
    PAGE = '1'
