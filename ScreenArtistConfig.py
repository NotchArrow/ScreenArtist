# Drawing Settings

brushSize = 0  # Brush size, 0 is 1 pixel, 1 is 2x2, 2 is 3x3, etc.
drawing = True  # Whether drawing with your mouse is enabled

randomDrawing = False  # If pixels should be drawn in random locations on the screen, independent of the mouse

systematicDrawing = False  # If pixels should be drawn in rows
sysDrawingDirection = 'vertical'  # 'horizontal', 'vertical', defaults to vertical

refreshRate = 60  # How many times per second new pixels are drawn, Affects performance and how quickly the image changes


# File Settings

saving = True  # If the program should save
saveFile = "Save1.txt"  # Relative filepath of the savefile
loadFile = "Save1.txt"  # Relative filepath of the loadfile, Leaving blank will result in a new drawing

saveVersions = True  # If you want to save versions with timestamps as a timeline, Saving must be enabled
versionsFolder = "PreviousVersions"  # Relative filepath of the folder to put these versions in


# Canvas Settings

backgroundColor = (0, 0, 0)  # Background color, RGB value

SCREEN_WIDTH = 1820  # Width of canvas window in pixels
SCREEN_HEIGHT = 980  # Height of canvas window in pixels