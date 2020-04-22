# Sierpinski carpet generator, in Python using Numpy and Pillow.
# Written by Nathan Reed, June 2014.
# This code is released into the public domain.

import numpy as np
from PIL import Image
# загальна кількість разів повторення процесу
numLevels = 7

# розмір зображення
imageSize = 3**numLevels

# створення образу
img = np.empty([imageSize, imageSize, 3], dtype=np.uint8)

# заповнення білого кольору
img.fill(255)
color = np.array([0, 0, 0], dtype = np.uint8)

for level in range(0, numLevels + 1):
	stepSize = 3**(numLevels - level)
	for x in range(0, 3**level):

		# перевірка центральної площі
		if x % 3 == 1:
			for y in range(0, 3**level):
				if y % 3 == 1:
					# змінює свій колір
					img[y*stepSize:(y+1)*stepSize, x*stepSize:(x+1)*stepSize] = color

	# збереження створеного зображення
	outputFilename = "sierpinski%d.png" % level
	Image.fromarray(img).save(outputFilename)
	# відображення його в консолі
	print('Wrote %s' % outputFilename)
