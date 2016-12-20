from selenium import webdriver
import os, time

zips = ['28801', 	# asheville, nc
		'94701',	# berkeley, ca
		'80301', 	# boulder, co
		'02108', 	# boston, ma
		'95616',	# davis, ca
		'80123', 	# denver, co
		'32826',  	# orlando, fl
		'04101', 	# portland, me
		'97201', 	# portland, or
		'02901',	# providence, ri
		'94101',	# san francisco, ca
		'90401',	# santa monica, ca
		'98101', 	# seattle, wa
		'98401'		# tacoma, wa
	]

def login(driver):
	
	# username = raw_input("username: ")
	username = 'jdliauw@gmail.com'
	# os.system("stty -echo")
	# password = raw_input("password: ")
	# os.system("stty echo")

	driver.get("http://www.okcupid.com")
	driver.find_element_by_id('open_sign_in_button').click()

	try:
		driver.find_element_by_id('login_username').send_keys(username)
		driver.find_element_by_id('login_password').send_keys(password)
		driver.find_element_by_id('sign_in_button').click()

		time.sleep(1)
		driver.get("https://www.okcupid.com/match")

	except:
		print 'Login failure, exiting\n'

def sort_by_match(driver):
	
	# click dropdown
	css = "[class='match-filters-in-results'] div[class='chosen-container chosen-container-single']"
	driver.find_element_by_css_selector(css).click()

	# sort by match
	css = "[class='chosen-container chosen-container-single chosen-with-drop chosen-container-active'] ul li:nth-child(2)"
	driver.find_element_by_css_selector(css).click()

if __name__ == "__main__":
	driver = webdriver.Firefox()
	login(driver)
	sort_by_match(driver)