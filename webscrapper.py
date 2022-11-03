from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com.my/maps/@2.2373723,102.1114167,11z")
sleep(2)

def searchplace():
	place = driver.find_element_by_class_name("tactile-searchbox-input")
	place.send_keys("Malacca")
	submit = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
	submit.click()
searchplace()

def directions():
	sleep(5)
	directions = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/button")
	directions.click()
directions()

def find():
	sleep(3)
	find = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
	find.send_keys("Johor Bahru")
	sleep(3)
	search = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
	search.click()
find()

def kilometers():
	sleep(3)
	totalKilometers = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div/div[1]/div[1]/div[2]/div")
	print("Total Kilometers: ", totalKilometers.text)
	sleep(4)
	bus = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div/div[1]/div[1]/div[1]/span[1]")
	print("Bus travel: ", bus.text)
	sleep(3)
	train = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[3]/div/div[2]/div[1]/div")
	print("Train travel: ", train.text)
	sleep(4)
kilometers()