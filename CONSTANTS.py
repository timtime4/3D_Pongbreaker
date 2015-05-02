# Tim Pusateri
# Jon Richelsen
# CSE30332
# Final Project: PyGame + Twisted
# 3D_Pongbreaker
#
# FUTURE IMPROVEMENTS
# Have number of brick rows and columns be determined by brick position file

# colors
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY =  (100, 100, 100)
COLOR_BLACK = (0,   0,   0)
COLOR_RED =   (175, 0,   0)
COLOR_GREEN = (0,   255, 0)
COLOR_BLUE =  (0,   0,   175)

# screen
SCREEN_WIDTH = 800  # pixels
SCREEN_HEIGHT = 800 # pixels
SCREEN_CENTER_X = SCREEN_WIDTH / 2 # pixels
SCREEN_CENTER_Y = SCREEN_HEIGHT / 2 # pixels
SCALING_FACTOR = 0.9995 # 'a' in 'y = a^x', where x is distance from screen (pixels) and y is scaling factor
FRAMERATE = 10 # frames/second

# hallway
HALLWAY_DEPTH = 3200 # pixels
HALLWAY_COLOR = COLOR_BLACK
HALLWAY_EDGE_THICK = 1 # pixels
HALLWAY_EDGE_COLOR = COLOR_GREEN

# wall
WALL_WIDTH = SCREEN_WIDTH * pow(SCALING_FACTOR, HALLWAY_DEPTH) # pixels
WALL_HEIGHT = SCREEN_HEIGHT * pow(SCALING_FACTOR, HALLWAY_DEPTH) # pixels
WALL_TL = (SCREEN_WIDTH - WALL_WIDTH) / 2, (SCREEN_HEIGHT - WALL_HEIGHT) / 2 # pixels
WALL_TR = (SCREEN_WIDTH - WALL_WIDTH) / 2 + WALL_WIDTH, (SCREEN_HEIGHT - WALL_HEIGHT) / 2 # pixels
WALL_BL = (SCREEN_WIDTH - WALL_WIDTH) / 2, (SCREEN_HEIGHT - WALL_HEIGHT) / 2 + WALL_HEIGHT # pixels
WALL_BR = (SCREEN_WIDTH - WALL_WIDTH) / 2 + WALL_WIDTH, (SCREEN_HEIGHT - WALL_HEIGHT) / 2 + WALL_HEIGHT # pixels

# brick
N_BRICK_ROWS = 8
N_BRICK_COLUMNS = 8
BRICK_WIDTH = SCREEN_WIDTH / N_BRICK_COLUMNS # pixels
BRICK_HEIGHT = SCREEN_HEIGHT / N_BRICK_ROWS # pixels
BRICK_PLANE = HALLWAY_DEPTH / 2 # pixels
BRICK_COLORS = {
	'R': COLOR_RED,
	'B': COLOR_BLUE
}
BRICK_POS_FN = 'test_brick_pos.txt'

# paddle
PADDLE_SCALING = 10
PADDLE_WIDTH = SCREEN_WIDTH / PADDLE_SCALING # pixels
PADDLE_HEIGHT = SCREEN_HEIGHT / PADDLE_SCALING # pixels
PADDLE_BUFFER = HALLWAY_DEPTH / 50 # pixels
PADDLE_COLOR = COLOR_WHITE
PADDLE_ALPHA = 100

# ball
BALL_SCALING = 20
BALL_RADIUS = min(SCREEN_WIDTH, SCREEN_HEIGHT) / BALL_SCALING / 2 # pixels
BALL_INIT_SPEED = 500 / FRAMERATE # pixels/second / frames/second = pixels/frame
BALL_COLOR = COLOR_WHITE
