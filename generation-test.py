# Python code for Mandelbrot Fractal 
  
# Import necessary libraries 
from PIL import Image 
from numpy import array
  
# setting the width of the output image as 1024 
WIDTH = 720
  
# a function to return a tuple of colors 
# as integer value of rgb 
def rgb_conv(i): 
    color = 255 * array((i/(31*(i**0.075)), 0.5, 1.0))
    return tuple(color.astype(int)) 
  
# function defining a mandelbrot 
def mandelbrot(x, y): 
    c0 = complex(x, y) 
    c = 0.4
    for i in range(1, 150): 
        if abs(c) > 2: 
            return rgb_conv(i) 
        c = c * c + c0 
    return (0, 0, 0) 
  
# creating the new image in RGB mode 
img = Image.new('RGB', (WIDTH, int(WIDTH * (9/16)))) 
pixels = img.load() 
  
for x in range(img.size[0]): 
  
    # displaying the progress as percentage 
    print("%.2f %%" % (x / WIDTH * 100.0))  
    for y in range(img.size[1]): 
        pixels[x, y] = mandelbrot((x - (0.75 * WIDTH)) / (WIDTH / 4), 
                                      (y - (WIDTH / 3.5625)) / (WIDTH / 4)) 
  
# to display the created fractal after  
# completing the given number of iterations
img.save("./mandelbrot_mod.jpg")
img.show()