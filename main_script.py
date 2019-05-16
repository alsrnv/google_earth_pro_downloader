
import config
from google_earth_pro import ImageSet
from image_cleaner import ImageCleaner
import time
import pyautogui
import logging
import pandas as pd

logging.basicConfig(filename='log.log',level=logging.INFO, filemode='w', 
	                format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

all_coords = pd.read_csv('data/all_coordinates.csv')

time.sleep(5)
pyautogui.PAUSE = 3

#COORD_EXAMPLE = ['55.6062,37.6620', '55.83433,37.95648']
COORD_EXAMPLE = ['55.403809, 37.536859']

for coord in COORD_EXAMPLE:
	ImageSet(coord).start_downloading()

# for _, row in all_coords.iloc[:,:50].iterrows():
# 	logging.info('Starting {} {}'.format(row['coordinates'], row['name']))
# 	ImageSet(row['coordinates']).start_downloading()



# obj = ImageCleaner()
# obj.group_image()
# obj.delete_duplicates()



logging.info('done')