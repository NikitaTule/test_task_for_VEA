
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from datetime import datetime
from my_config import MY_ABSOLUTE_PATH_TO_THE_SCREENSHOT_FILE

# “function”-один раз для тестового метода
# “class”-один раз для класса
# “module”-один раз для модуля
# “session”-один раз для всех тестов, запущенных в данной сессии



@pytest.fixture
def chrome_options():
    """ Опции для хрома """
    options_chrome = ChromeOptions()
    options_chrome.add_experimental_option('excludeSwitches', ['enable-logging'])
    options_chrome.add_argument('--headless')
    options_chrome.add_argument('--no-sandbox')
    options_chrome.add_argument('--log-level=SEVERE')
    return options_chrome


@pytest.fixture
def firefox_options():
    """ Опции для фокса """
    options_firefox = FirefoxOptions()
    options_firefox.add_argument('--headless')
    return options_firefox


def current_date_and_time() -> str:
    """ Текушая дата и время """
    date_time = str(f"({datetime.now().day}." + f"{datetime.now().month}."
                    + f"{datetime.now().year}_" + f"{datetime.now().hour};"
                    + f"{datetime.now().minute})")
    return date_time


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """ Хук для проверки упавшего теста """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(params=["Chrome"])  # "Chrome", "Firefox"
def driver_init(request, chrome_options, firefox_options):
    if request.param == "Chrome":
        driver_name = "Chrome"
        name_test = request.function.__name__
        print(f"\nstart chrome browser for ...{name_test}")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    if request.param == "Firefox":
        driver_name = "Firefox"
        name_test = request.function.__name__
        print(f"\nstart firefox browser for ...{name_test}")
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

    yield driver
    if request.node.rep_call.failed:
        name_test = request.function.__name__
        all_name = driver_name + "_" + name_test + current_date_and_time()
        name_screenshot = all_name.replace(" ", "")
        """ Необходимо указать собственный абсолютный путь к файлу со скриншотами """
        driver.save_screenshot(f'{MY_ABSOLUTE_PATH_TO_THE_SCREENSHOT_FILE}\\{name_screenshot}' + '.png')
        print(f'Текущий URL => {driver.current_url}' == "url")
        driver.quit()
    driver.quit()
    print(f"\nquit browser..{driver_name}")


