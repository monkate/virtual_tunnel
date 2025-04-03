import PIL.Image as Image
import random

# Dimensions of the rectangle image
# number of rows, columns
# 29,1cm x 91cm & 14,7cm x 91cm
N = 14.7
M = 91

# box width and height (in mm)
W = 10
H = 10

width = int(N*W)
height = int(M*H)

# Create a new image with a white background
image = Image.new("RGB", (width, height), "white")

# Access the pixel data of the image
pixels = image.load()

# Iterate over each pixel and set the color
for y in range(0, height, H):
    for x in range(0, int(N)*W, W):
        # Alternate between black and white pixels
        a = random.randint(0, 1)
        if a == 0:
            for dx in range(W):
                for dy in range(H):
                    pixels[x+dx, y+dy] = (0, 0, 0)  # Set pixel to black (RGB: 0, 0, 0)
        else:
            for dx in range(W):
                for dy in range(H):
                    pixels[x+dx, y+dy] = (255, 255, 255)  # Set pixel to white (RGB: 255, 255, 255)

'''
#last 7 lines:
x = 140
for y in range(0, height, H):
    a = random.randint(0, 1)
    if a == 0:
        for dx in range(7):
            for dy in range(H):
                pixels[x+dx, y+dy] = (0, 0, 0)  # Set pixel to black (RGB: 0, 0, 0)
    else:
        for dx in range(7):
            for dy in range(H):
                pixels[x+dx, y+dy] = (255, 255, 255)  # Set pixel to white (RGB: 255, 255, 255)
'''

# Display the image
image.show()