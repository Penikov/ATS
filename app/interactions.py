from app.launch import Exe


class Welcome_screen:

    """The class that helps to interact with Audacity 'How to get help' screen"""

    def __init__(self, exe):
        self.exe = exe
        self.win = self.exe['Audacity']
        self.welcome = self.win['Welcome to Audacity!']

    def click_checkbox(self):
        win = self.exe['Audacity']
        welcome = win['Welcome to Audacity!']
        return welcome.child_window(title="Don't show this again at start up").click()

    def click_ok_button(self):
        win = self.exe['Audacity']
        welcome = win['Welcome to Audacity!']
        return welcome.child_window(title='OK').click()

    def close(self):
        return self.welcome.child_window(title='Close').click()


class Audacity:
    def __init__(self, exe):
        self.exe = exe
        self.win = self.exe['Audacity']

    def close_button(self):
        return self.win.child_window(title='Close').click()




"""This section is using just for easy testing of new elements right in the IDE"""
if __name__ == '__main__':
    Audacity(Exe().run_max())
    pass











