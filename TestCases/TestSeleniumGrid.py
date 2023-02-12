from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time,os,shutil
from jproperties import Properties

def test_seleniumgrid():
    configs = Properties()
    with open(os.path.abspath(os.path.join(os.getcwd(), os.pardir,'settings.properties')), 'rb') as config_file:
        configs.load(config_file)
    if configs.get('BROWSER_NAME')=='firefox':
        browser_options=FirefoxOptions()
        browser_options.add_argument('ignore-certificate-errors')
    else:
        browser_options=ChromeOptions()
        browser_options.add_argument('ignore-certificate-errors')

    # desired_capabilities = {'browserName': "chrome", 'javascriptEnabled': True,'acceptInsecureCerts':True}
    driver = webdriver.Remote(command_executor='https://localhost:4444/wd/hub',options=browser_options)
    driver.get("https://www.whatismybrowser.com/")
    driver.maximize_window()
    time.sleep(5)
    print("browser opened")
    print(os.getcwd())
    if os.path.exists(os.path.join(os.getcwd(),'output')):
        shutil.rmtree(os.path.join(os.getcwd(),'output'))

    os.mkdir('output')
    driver.save_screenshot('output/screen.png')
    driver.close()