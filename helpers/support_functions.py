from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scroll_into_view(driver, element):
    ActionChains(driver).move_to_element(element).perform()

def wait_5s_until_element_is_visible(driver, element_locator: tuple[str,str]):
    return WebDriverWait(driver, 5).until(EC.visibility_of_element_located(element_locator))

def wait_5s_until_element_is_no_longer_visible(driver, element_locator: tuple[str,str]):
    return WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(element_locator))




