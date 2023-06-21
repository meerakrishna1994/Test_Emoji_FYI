from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

# your device
desired_caps = {
    'platformName': 'Mac',
    'platformVersion': '13.2.1 (22D68)',
    'app': '/Users/meerakrishna/Documents/EmojiPicker/build/appEmojiSelector.app',
}
# Connect to the Appium Server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Wait for the application to launch
time.sleep(5)
# Wait smiley element to be present
smiley_element = None
max_wait_time = 10
wait_interval = 1
current_wait_time = 0
while current_wait_time < max_wait_time:
    try:
        smiley_element = driver.find_element('id', 'emoji_id')
        break
    except:
        time.sleep(wait_interval)
        current_wait_time += wait_interval

if smiley_element is not None:

    # click action on smiley
    action = TouchAction(driver)
    action.tap(element=smiley_element).perform()


    time.sleep(3)

# Close Application
driver.quit()
