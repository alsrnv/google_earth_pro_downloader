
import pandas as pd 
import os
import shutil
import config
import logging

CURRENT_PATH = os.getcwd()
IMAGE_PATH = os.path.join(CURRENT_PATH, config.IMAGES_FOLDER)


class ImageCleaner():
	def __init__(self, path_images = IMAGE_PATH):
		self.path_images = path_images

	def group_image(self):
		logging.info('starting grouping images')
		all_files = [file for file in os.listdir(self.path_images) if file.endswith('.jpg')]
		df = pd.DataFrame({'filename': all_files})
		df['file_number'] = df['filename'].apply(lambda x: x.split('_')[1].split('.')[0]).astype(int)
		df['coords'] = df['filename'].apply(lambda x: x.split('_')[0])

		for coord, group in df.groupby('coords'):
			os.mkdir(os.path.join(self.path_images, coord))
		    #moving files to the new directory
			for _, row  in group.iterrows():
				filename = row['filename']
				file_number = row['file_number']
				shutil.move(os.path.join(self.path_images, filename), 
							os.path.join(self.path_images, coord, filename))
				os.rename(os.path.join(self.path_images, coord, filename), 
						  os.path.join(self.path_images, coord, str(file_number) + '.jpg'))

	def delete_duplicates(self):
		logging.info('starting deleting duplicates for each folder')
		folders = list(filter(lambda x: os.path.isdir(os.path.join(self.path_images, x)), 
			 							os.listdir(self.path_images)))

		for folder in folders:
			os.system('image-cleaner {}'.format(os.path.join(self.path_images, folder)))



