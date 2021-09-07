from app.launch import Launch


class Welcome_screen:
    def __init__(self):
        self.exe = Launch().run_max()
        self.win = self.exe['Audacity']
        self.welcome = self.win['Welcome to Audacity!']

    def click_checkbox(self):
        win = self.exe['Audacity']
        welcome = win['Welcome to Audacity!']
        return welcome.window(title="Don't show this again at start up").click()

    def click_ok_button(self):
        win = self.exe['Audacity']
        welcome = win['Welcome to Audacity!']
        return welcome.window(title='OK').click()

    def close(self):
        return self.welcome.window(title='Close').click()












