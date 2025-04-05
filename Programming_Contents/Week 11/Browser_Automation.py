from selenium import webdriver

def get_default_edge_options():
    options = webdriver.EdgeOptions()
    options.add_argument("--no-sandbox")
    options.add_experimental_option("detach", True)
    return options

options = get_default_edge_options()
browser = webdriver.Edge(options=options)

browser.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")