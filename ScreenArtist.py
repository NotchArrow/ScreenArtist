import pygame  # canvas
import pyautogui  # mouse location and pixel color
import shutil  # file management
import os  # file management
import datetime  # datestamp for fileversions
import random  # randomdrawing
from ScreenArtistConfig import *  # settings from config

sysDrawingX = 0
sysDrawingY = 0

timeLapse = False
timeLapseHotkey = timeLapseHotkey.lower()
if timeLapseHotkey == "space":
	timeLapseHotkey = "SPACE"

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ScreenArtist")
clock = pygame.time.Clock()

screen.fill(backgroundColor)

# load from file/start new
listToSave = []
try:
	
	file = open(loadFile, "r")
	pixel_array = pygame.PixelArray(screen)

	for item in file.readlines():
		if "pixel_array" in item:

			exec(item)
			listToSave.append(item.replace("pixel_array", ""))

		else:

			exec("pixel_array" + item)
			listToSave.append(item)

except:
	pass


# main loop
running = True
while running:

	# prevents pygame window hangup
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == getattr(pygame, "K_" + timeLapseHotkey):
				timeLapse = True

	# mouse drawing
	if drawing:
		try:

			# adding pixel to array
			pixel_array = pygame.PixelArray(screen)
			x, y = pyautogui.position()

			relX = -brushSize
			while relX <= brushSize:

				relY = -brushSize
				while relY <= brushSize:

					color = pyautogui.pixel(x + relX, y + relY)
					pixel_array[x + relX, y + relY] = color

					# saving to a list
					if saving:

						thingToSave = '[' + str(x + relX) + ', ' + str(y + relY) + ']  = ' + str( color)
						thingToSavePos = '[' + str(x + relX) + ', ' + str(y + relY) + ']'

						# replacing duplicate pixel locations in the list
						for text in listToSave:
							if thingToSavePos in text:

								listToSave[listToSave.index(text)] = thingToSave
								break

						else:

							listToSave.append(thingToSave)

					relY += 1

				relX += 1

			pixel_array.close()

		except:
			pass


	# drawing pixels in random locations
	if randomDrawing:
		try:

			# adding pixel to array
			pixel_array = pygame.PixelArray(screen)
			x = random.randint(0, SCREEN_WIDTH)
			y = random.randint(0, SCREEN_HEIGHT)

			relX = -brushSize
			while relX <= brushSize:

				relY = -brushSize
				while relY <= brushSize:

					color = pyautogui.pixel(x + relX, y + relY)
					pixel_array[x + relX, y + relY] = color

					# saving to a list
					if saving:

						thingToSave = '[' + str(x + relX) + ', ' + str(y + relY) + ']  = ' + str( color)
						thingToSavePos = '[' + str(x + relX) + ', ' + str(y + relY) + ']'

						# replacing duplicate pixel locations in the list
						for text in listToSave:
							if thingToSavePos in text:

								listToSave[listToSave.index(text)] = thingToSave
								break

						else:

							listToSave.append(thingToSave)

					relY += 1

				relX += 1

			pixel_array.close()

		except:
			pass


	# drawing pixels in rows
	if systematicDrawing:
		try:

			# x and y calculations
			if sysDrawingDirection == 'horizontal':
				if sysDrawingY >= SCREEN_HEIGHT:
					sysDrawingY = 0
					sysDrawingX += 1
				else:
					sysDrawingY += 1
					if sysDrawingY > SCREEN_HEIGHT:
						sysDrawingY = 0

			else:
				if sysDrawingX >= SCREEN_WIDTH:
					sysDrawingX = 0
					sysDrawingY += 1
				else:
					sysDrawingX += 1
					if sysDrawingX > SCREEN_WIDTH:
						sysDrawingX = 0

			# adding pixel to array
			pixel_array = pygame.PixelArray(screen)
			x = sysDrawingX
			y = sysDrawingY

			relX = -brushSize
			while relX <= brushSize:

				relY = -brushSize
				while relY <= brushSize:

					color = pyautogui.pixel(x + relX, y + relY)
					pixel_array[x + relX, y + relY] = color

					# saving to a list
					if saving:

						thingToSave = '[' + str(x + relX) + ', ' + str(y + relY) + ']  = ' + str( color)
						thingToSavePos = '[' + str(x + relX) + ', ' + str(y + relY) + ']'

						# replacing duplicate pixel locations in the list
						for text in listToSave:
							if thingToSavePos in text:

								listToSave[listToSave.index(text)] = thingToSave
								break

						else:

							listToSave.append(thingToSave)

					relY += 1

				relX += 1

			pixel_array.close()

		except:
			pass


	# if a timelapse is being done
	if timeLapse:
		screen.fill(backgroundColor)
		pixel_array = pygame.PixelArray(screen)
		i = 0
		for item in listToSave:
			i += 1
			if "pixel_array" in item:
				exec(item)

			else:
				exec("pixel_array" + item)

			if i >= 25:
				i = 0
				pygame.display.update()
		
	timeLapse = False


	# display refresh
	pygame.display.update()
	clock.tick(refreshRate)


# saving after main loop exit
if saving:

	file = open(saveFile, "w")
	listToSave = list(set(listToSave))
	listToSave.sort()

	for item in listToSave:

		file.write(item)
		file.write('\n')

	file.close()

	# saving multiple versions with time/datestamps
	if saveVersions:

		time = datetime.datetime.now()
		time = str(time.month) + "-" + str(time.day) + "-" + str(time.year) + "_" + str(time.hour) + "-" + str(time.minute) + "-" + str(time.second) + "_"
		os.makedirs("./" + versionsFolder, exist_ok=True)
		shutil.copyfile(saveFile, versionsFolder + "/" + time + saveFile)

pygame.quit()