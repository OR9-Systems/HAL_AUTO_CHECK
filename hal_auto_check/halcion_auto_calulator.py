from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.options import Options
import pyperclip
import time

IMP_LINE = "URL="
SHORTCUT_NAME = "Halcion.url"

def loadhalurl(url=SHORTCUT_NAME):
    """
    Reads the URL from a shortcut file.

    :return: The URL extracted from the file.
    :rtype: str
    """
    with open(url, 'r+') as h_file:
        important_line = [line for line in h_file.readlines() if IMP_LINE in line][0]
    return important_line.strip(IMP_LINE)

def save_to_file(content, filename):
    """
    Saves the given content to a file.

    :param content: The content to be saved.
    :type content: str
    :param filename: The name of the file where the content will be saved.
    :type filename: str
    :return: None
    """
    with open(filename, 'w') as file:
        file.write(content)

def print_action_chain(driver, filename):
    """
    Executes an action chain to copy text and save it to a file.

    :param driver: The Selenium WebDriver instance.
    :param filename: The name of the file to save the copied text.
    :type filename: str
    :return: None
    """
    actions = ActionChains(driver)
    window_handles = driver.window_handles
    halcion_handle = window_handles[-1]
    driver.switch_to.window(halcion_handle)
    print("Switched to Window")
    actions.key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).perform()
    copied_text = pyperclip.paste()
    print(copied_text)
    save_to_file(copied_text, filename)

if __name__ == "__main__":
    edge_options = Options()
    edge_options.use_chromium = True  # Specify using Chromium-based Edge
    # Set the desired page load strategy
    driver = webdriver.Edge(options=edge_options)
    halurl = loadhalurl()
    driver.get(halurl)
    print("Executing Action Chain")
    time.sleep(1)

    while True:
        # Get filename input from user
        filename = input("Enter the filename to save copied text or type 'exit' to quit: ")
        if filename.lower() == 'exit':  # Check if user wants to exit
            print("Exiting the program.")
            break
        print_action_chain(driver, filename)
    driver.quit()
