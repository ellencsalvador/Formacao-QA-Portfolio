# ...existing code...
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    opts = Options()
    # opts.add_argument("--headless=new")  # opcional
    opts.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    context.driver.implicitly_wait(3)

def after_all(context):
    try:
        context.driver.quit()
    except Exception:
        pass
# ...existing code...