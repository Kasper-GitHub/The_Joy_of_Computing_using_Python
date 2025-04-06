from selenium import webdriver

def get_default_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_experimental_option("detach", True)
    return options

options = get_default_chrome_options()
browser = webdriver.Chrome(options=options)

browser.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

browser.find_element_by_id('first')
browser.click()