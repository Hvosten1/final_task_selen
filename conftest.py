import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
#options.add_argument('headless')
#options.add_argument('window-size=1920x935') # убираем эти два коммента чтобы не видеть каждый раз браузер




@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    #browser.implicitly_wait(3)
    yield browser
    print("\nquit browser..")
    browser.quit()