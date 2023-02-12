from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time,os,shutil

def test_seleniumgrid():
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    desired_capabilities = {'browserName': "chrome", 'javascriptEnabled': True,'acceptInsecureCerts':True}
    driver = webdriver.Remote(command_executor='https://localhost:4444/wd/hub',desired_capabilities=desired_capabilities)
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