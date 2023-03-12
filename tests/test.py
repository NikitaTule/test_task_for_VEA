from pages.base_page import BasePage


def test_yandex_create_folder_and_file(driver_init):
    BASE_URL: str = 'https://passport.yandex.ru/'
    password: str = "Ont8x$oHR2xP@f}"
    login: str = "my.test.accaunt"
    base_page = BasePage(driver_init)
    base_page.open_site(BASE_URL)
