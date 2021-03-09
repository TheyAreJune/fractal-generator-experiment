from PIL import Image 
from numpy import array 
import colorsys 
  
# a function to return a tuple of colors 
# as integer value of rgb 
def rgb_conv(i): 
    color = 255 * array(colorsys.hsv_to_rgb(i/255, 1.0, 1.0)) 
    return tuple(color.astype(int)) 


print(colorsys.hsv_to_rgb(255, 1.0, 1.0))