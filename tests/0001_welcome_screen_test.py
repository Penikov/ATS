from app.interactions import Welcome_screen


def test_click_get_help(app):
    """The test checks that the 'how to get help' checkbox is appears at the first startup"""
    Welcome_screen(app).click_checkbox().close()






