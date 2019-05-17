
import config
import pyautogui
import os
import time
import logging
try:
	import httplib
except:
	import http.client as httplib


CURRENT_PATH = os.getcwd()


def have_internet():
	"""Checking internet connection"""
	conn = httplib.HTTPConnection("www.google.com", timeout=5)
	try:
		conn.request("HEAD", "/")
		conn.close()
		return True
	except:
		conn.close()
		return False



class ImageSet():
	def __init__(self, coordinates):
		self.coordinates = coordinates
		self.save_mode_active = False
		self.history_mode_active = False

	def click_on_button(self, position):
		pyautogui.moveTo(position[0], position[1])
		pyautogui.click(position[0], position[1])

	def start_searching(self, text):
		pyautogui.click( config.GOOGLE_EARTH_INT['searchField'][0], 
						 config.GOOGLE_EARTH_INT['searchField'][1])
		#delete existing text in a field
		pyautogui.hotkey('command','a');pyautogui.hotkey('backspace')
		pyautogui.typewrite(text)

		pyautogui.moveTo(config.GOOGLE_EARTH_INT['searchButton'][0], 
						 config.GOOGLE_EARTH_INT['searchButton'][1])

		pyautogui.press('enter')

		#unpinning a yellow clip
		self.click_on_button(config.GOOGLE_EARTH_INT['pinCheck'])

	def open_history_panel(self):
		#open history frame
		if self.history_mode_active == False:
			self.click_on_button(config.GOOGLE_EARTH_INT['historyButton'])
			self.history_mode_active = True
		else:
			pass

	def open_save_panel(self):
		#open save frame
		if self.save_mode_active == False:
			self.click_on_button(config.GOOGLE_EARTH_INT['saveImageButton'])
			self.save_mode_active = True
		else:
			pass

	def save_image(self, image_name):
		self.click_on_button(config.GOOGLE_EARTH_INT['saveImageFile'])
		self.click_on_button(config.GOOGLE_EARTH_INT['cancelSaveButton'])

		#click on save button again
		while not have_internet():
			time.sleep(10)
		self.click_on_button(config.GOOGLE_EARTH_INT['saveImageFile'])
		pyautogui.typewrite(image_name)

		self.click_on_button(config.GOOGLE_EARTH_INT['saveFinalButton'])

	def check_is_file_exist(self, file_name):
		path = os.path.join(CURRENT_PATH, config.IMAGES_FOLDER, file_name + '.jpg')
		return os.path.exists(path)

	def start_downloading(self):

		while not have_internet():
			time.sleep(10)

		self.start_searching(self.coordinates)
		
		self.open_history_panel()
		self.open_save_panel()

		#saving initial photo
		self.save_image(image_name = self.coordinates + '_0')
		time.sleep(5)

		for step in range(1, config.HISTORY_STEPS + 1):
			new_image_file = self.coordinates + '_' + str(step)

			while not have_internet():
				time.sleep(10)

			self.click_on_button(config.GOOGLE_EARTH_INT['moveBackHistory'])
			time.sleep(3)
			self.save_image(image_name = new_image_file)

			while not self.check_is_file_exist(file_name = new_image_file):
				time.sleep(2)
			
			time.sleep(7)



		self.click_on_button(config.GOOGLE_EARTH_INT['saveImageButton'])
		self.save_mode_active == False
		self.click_on_button(config.GOOGLE_EARTH_INT['historyButton'])
		self.history_mode_active = False
		time.sleep(5)






