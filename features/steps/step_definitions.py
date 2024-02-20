from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.edge.options import Options
import pyperclip
import threading
import os
from hal_auto_check.halcion_auto_calulator import  save_to_file, loadhalurl
# Assuming the loadhalurl and save_to_file functions are defined elsewhere and imported here
script_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
URL=os.path.join(script_dir, 'test-website.url')
PAGE_OPENED = False


def timeout_error():
    """
    Function to be called when the timeout is reached.
    """
    raise WebDriverException("Page load timed out after 10 seconds")

def wait_for_page_load(driver,url,timeout):
    """
    Function to wait for the page to load within a specified timeout.
    """
    print(f"Loading Url :{url}")
    driver.set_page_load_timeout(timeout)
    timer = threading.Timer(timeout, timeout_error)
    try:
        timer.start()
        driver.get(url)  # Wait for the page to load within the specified timeout
    finally:
        timer.cancel()


@given('I have opened the webpage')
def open_webpage(context):
    """
    Opens the webpage using the URL from a shortcut file.
    """
    edge_options = Options()
    edge_options.use_chromium = True  # Specify using Chromium-based Edge
    # Set the desired page load strategy

    driver = webdriver.Edge(options=context.edge_options)
    halurl = loadhalurl(URL)
    try:
        wait_for_page_load(driver, halurl,10)
    except TimeoutException:
        # Fail the step if a TimeoutException is caught
        assert False, "Failed to load the webpage within the specified timeout."
    except Exception as e:
        # Fail the step for any other exceptions
        assert False, f"An error occurred while opening the webpage: {str(e)}"
    #time.sleep(5)  # Wait for the page to load

@when('I copy text from the webpage')
def copy_text_from_webpage(context):
    """
    Copies text from the webpage using an action chain.
    """
    if not PAGE_OPENED:
        raise Exception("Webpage was not successfully opened. Skipping scenario.")
    context.copied_text = ""
    try:
        actions = ActionChains(context.driver)
        actions.key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).perform()
        context.copied_text = pyperclip.paste()
    except Exception as e:
        print(f"Error copying text: {e}")

@then('I should be able to save the text to a "{filename}" file')
def save_text_to_file(context, filename):
    """
    Saves the copied text to a specified file.
    """
    if not PAGE_OPENED:
        raise Exception("Webpage was not successfully opened. Skipping scenario.")
    
    if context.copied_text:
        save_to_file(context.copied_text, filename)
        # Verification step to ensure the file contains the expected text could be added here
    else:
        raise AssertionError("No text was copied from the webpage.")
