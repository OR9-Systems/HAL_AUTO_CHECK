from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import time
from halcion_auto_calulator import loadhalurl, save_to_file
# Assuming the loadhalurl and save_to_file functions are defined elsewhere and imported here

@given('I have opened the webpage')
def open_webpage(context):
    """
    Opens the webpage using the URL from a shortcut file.
    """
    context.ie_options = webdriver.IeOptions()
    context.ie_options.attach_to_edge_chrome = True
    context.ie_options.ignore_zoom_level = True
    context.ie_options.require_window_focus = True
    context.ie_options.edge_executable_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
    context.ie_options.ignore_protected_mode_settings = True

    context.driver = webdriver.Edge(options=context.ie_options)
    halurl = loadhalurl()
    context.driver.get(halurl)
    time.sleep(5)  # Wait for the page to load

@when('I copy text from the webpage')
def copy_text_from_webpage(context):
    """
    Copies text from the webpage using an action chain.
    """
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
    if context.copied_text:
        save_to_file(context.copied_text, filename)
        # Verification step to ensure the file contains the expected text could be added here
    else:
        raise AssertionError("No text was copied from the webpage.")
