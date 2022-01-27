import pygame
import sys
from settings import *

class Stacker:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH * BLOCK_SIZE, HEIGHT * BLOCK_SIZE))
		pygame.display.set_caption("Stacker")
		self.RUNNING = False
		self.grid = [[0 for cell in range(WIDTH)] for row in range(HEIGHT)]

	def run(self):
		self.RUNNING = True
		while self.RUNNING:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit

			self.draw()
			pygame.display.flip()

	def draw(self):
		self.screen.fill("#8F282B")
		self.draw_grid_lines()

	def draw_grid_lines(self):
		for col_index in range(WIDTH):
			if col_index != 0:
				pygame.draw.line(self.screen,"#943437", (col_index * BLOCK_SIZE, 0), (col_index * BLOCK_SIZE, HEIGHT * BLOCK_SIZE,), width = 5)

		for row_index in range(HEIGHT):
			if row_index in [0,1,4,5]:
				pygame.draw.line(self.screen,"#EDEDED", (0, row_index * BLOCK_SIZE), (WIDTH * BLOCK_SIZE, row_index * BLOCK_SIZE), width = 7)
			elif row_index != 0:
				pygame.draw.line(self.screen,"#943437", (0, row_index * BLOCK_SIZE), (WIDTH * BLOCK_SIZE, row_index * BLOCK_SIZE), width = 5)

		





