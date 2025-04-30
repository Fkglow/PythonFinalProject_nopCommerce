from selenium.webdriver.common.action_chains import ActionChains

def scroll_into_view(driver, element):
    ActionChains(driver).move_to_element(element).perform()




