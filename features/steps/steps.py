from behave import *
import time


@given('I visit a URL "{url}"')
def step(context, url):
	# context.browser.maximize_window()
	context.browser.get(url)
	print(context.browser.title)
	time.sleep(10)
	

@then('execute JavaScript function to scroll')
def step(context):
	context.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


@then('capture screenshot of the page')
def step(context):
	context.browser.save_screenshot('test_screenshot.png')
