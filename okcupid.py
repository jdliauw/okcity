from selenium import webdriver
import time

zips = [ 	'28801', 	# asheville, nc
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

def login():
	driver = webdriver.Firefox()
	driver.get("http://www.okcupid.com")
	driver.find_element_by_id('open_sign_in_button').click()

	username = 'jdliauw@gmail.com'
	password = ''

	try:
		driver.find_element_by_id('login_username').send_keys(username)
		driver.find_element_by_id('login_password').send_keys(password)
		driver.find_element_by_id('sign_in_button').click()
	except:
		print 'Login failure, exiting\n'

	# move within try after match_page functions properly
	match_page(driver)

def match_page(driver):
	time.sleep(1)
	driver.get("https://www.okcupid.com/match")
	
	try:
		driver.find_element_by_class_name('chosen-single').click()
	except:
		print 'failed'

	# driver.find_element_by_id('chosen-id-8pjq-1').click()



login()