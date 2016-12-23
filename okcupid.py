from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import os, time

"""
- Parse matches for all > 90%
- Place cookie so don't login every time
"""

def login():
	
	# username = raw_input("username: ")
	username = 'jdliauw@gmail.com'
	os.system("stty -echo")
	password = raw_input("password: ")
	os.system("stty echo")
	print '\n'

	driver = webdriver.Firefox()
	driver.get("http://www.okcupid.com")
	driver.find_element_by_id('open_sign_in_button').click()
	driver.find_element_by_id('login_username').send_keys(username)
	driver.find_element_by_id('login_password').send_keys(password)
	driver.find_element_by_id('sign_in_button').click()

	time.sleep(1)
	driver.get("https://www.okcupid.com/match")

	return driver

def sort_by_match(driver):
	
	# click dropdown
	css = "[class='match-filters-in-results'] div[class='chosen-container chosen-container-single']"
	driver.find_element_by_css_selector(css).click()

	# sort by match
	css = "[class='chosen-container chosen-container-single chosen-with-drop chosen-container-active'] ul li:nth-child(2)"
	driver.find_element_by_css_selector(css).click()

	driver.find_element_by_css_selector("span[class='order-by-label']").click()
	driver.get("https://www.okcupid.com/match")

def select_city(driver, zip):

	css = "span[class='filter-wrapper filter-location-locale']"
	driver.find_element_by_css_selector(css).click()
	
	css = "div[class='clear-location-search'] button"
	driver.find_element_by_css_selector(css).click()
 
	xpath = "//span[text()='More options']"
	driver.find_element_by_xpath(xpath).click()

	time.sleep(1)
	css = "div[class='okinput'] input"
	driver.find_element_by_css_selector(css).click()

	css = "input[name='lquery']"
	driver.find_element_by_css_selector(css).send_keys(zip)

	time.sleep(1)
	css = "span[class='filter-wrapper filter-location-locale']"

def count_matches(driver):
	
	time.sleep(1)

	images = driver.find_elements_by_css_selector("span[class='fadein-image image_wrapper loaded'] img")
	print 'len images:', len(images)

	for image in images:
		print image.get_attribute('src')

	ages = driver.find_elements_by_css_selector("span[class='age']")
	print 'len ages:', len(ages)

	for age in ages:
		print age.text

	# percentages = driver.find_elements_by_css_selector("div[class='match-results-cards'] div")
	percentages = driver.find_elements_by_css_selector("span[class='percentage']")
	print 'len percentages (x2):', len(percentages)

	for percent in percentages:
		print int(percent.text.replace('%', ''))

def cycle_cities(driver):

	zips = ["28801", 	# asheville, nc
		"94701",		# berkeley, ca
		"80301", 		# boulder, co
		"02108", 		# boston, ma
		"95616",		# davis, ca
		"80123", 		# denver, co
		"32826",  		# orlando, fl
		"04101", 		# portland, me
		"97201", 		# portland, or
		"02901",		# providence, ri
		"94101",		# san francisco, ca
		"90401",		# santa monica, ca
		"98101", 		# seattle, wa
		"98401"			# tacoma, wa
	]

	for zip in zips:
		select_city(driver, zip)
		time.sleep(1)

if __name__ == "__main__":
	driver = login()
	sort_by_match(driver)
	count_matches(driver)