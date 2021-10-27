import time

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class Credentials(object):
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password


def doAuth():
    loginButton = driver.find_element(By.CSS_SELECTOR, "button.ph-login")
    loginButton.send_keys(Keys.RETURN)

    WebDriverWait(driver, 5).until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe.ag-popup__frame__layout__iframe")
        )
    )  # Wait until the auth pop-up appears

    usernameInput = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[name='username']")
        )
    )  # Wait until the email input field is finally loaded
    usernameInput.send_keys(credentials.username)

    clickAuthContinueButton()

    passwordInput = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[name='password']")
        )
    )  # Wait until the password input field is finally loaded
    passwordInput.send_keys(credentials.password)

    clickAuthContinueButton()
    driver.switch_to.default_content()  # Switch back to the main content instead of auth pop-up


def clickAuthContinueButton():
    continueButton = driver.find_element(By.CSS_SELECTOR, "button.base-0-2-79.primary-0-2-93")
    continueButton.click()


def sendMessage():
    sendTo = "lab_lubich_selenium@mail.ru"
    subject = "Selenium lab"
    message = "'This is the test message...'"

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.sidebar")
        )
    )  # Wait until the main page with sidebar finally loaded

    composeButton = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.compose-button")
        )
    )
    composeButton.click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.compose-app")
        )
    )

    sendToInputField = driver.find_element(By.CSS_SELECTOR, "input.container--H9L5q")
    sendToInputField.send_keys(sendTo)

    subjectInputField = driver.find_element(By.CSS_SELECTOR, "input[name='Subject']")
    subjectInputField.send_keys(subject)

    driver.execute_script("window.container = document.getElementsByClassName('cke_editable')[0]")
    driver.execute_script("window.messageContent = window.container.innerHTML")
    driver.execute_script("window.container.innerHTML=" + message + " + window.messageContent")

    sendMessageButton = driver.find_element(By.CSS_SELECTOR, "span[data-title-shortcut='Ctrl+Enter']")
    sendMessageButton.click()


def makeLogout():
    driver.find_element(By.CSS_SELECTOR, "div.ph-project__account").click()

    logoutButton = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a[tabindex='0']")
        )
    )
    logoutButton.click()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    credentials = Credentials(
        url="https://mail.ru/",
        username="lab_lubich_selenium@mail.ru",
        password="lrR1EaP1-sce"
    )
    driver.get(credentials.url)

    try:
        doAuth()
        sendMessage()
        time.sleep(2)
        makeLogout()
    except TimeoutError:
        driver.quit()
    finally:
        time.sleep(5)

    driver.close()
