from byuimage import Image

def iron_puzzle(filename):
    my_img = Image(filename)
    # Iterates through each pixel in the picture
    for x in range(my_img.width):
        for y in range(my_img.height):
            # Gets the pixel and sets red and green to 0 and multiples blue by 10
            pixel = my_img.get_pixel(x,y)
            pixel.color = (0,0,pixel.blue*10)
    return my_img
def west_puzzle(filename):
    my_img = Image(filename)
    # Iterates through each pixel in the picture
    for x in range(my_img.width):
        for y in range(my_img.height):
            # Gets the pixel and sets red and green to 0 and multiples blue by 16 if blue is less than 16, otherwise makes it black
            pixel = my_img.get_pixel(x,y)
            if pixel.blue < 16:
                pixel.color = (0,0,pixel.blue*16)
            else:
                pixel.color = (0,0,0)
    return my_img


def darken(filename, percent):
    my_img = Image(filename)
    # Percent that the image will be darkened by
    darken_amount = 1.0 - percent
    for x in range(my_img.width):
        for y in range(my_img.height):
            pixel = my_img.get_pixel(x,y)
            # Setting the image to a dark color
            pixel.red *= darken_amount
            pixel.green *= darken_amount
            pixel.blue *= darken_amount
    return my_img
            

def grayscale(filename):
    my_img = Image(filename)
    # Loop through image
    for x in range(my_img.width):
        for y in range(my_img.height):
            pixel = my_img.get_pixel(x,y)
            # Takes the average integer to make the image grayscale
            average = (pixel.red + pixel.green + pixel.blue) // 3
            # Setting the image grayscale
            pixel.color = (average, average, average)
    return my_img

def sepia(filename):
    my_img = Image(filename)
    for x in range(my_img.width):
        for y in range(my_img.height):
            pixel = my_img.get_pixel(x,y)
            # Setting the new color values
            true_red = int(0.393*pixel.red + 0.769*pixel.green + 0.189*pixel.blue)
            true_green = int(0.349*pixel.red + 0.686*pixel.green + 0.168*pixel.blue)
            true_blue = int(0.272*pixel.red + 0.534*pixel.green + 0.131*pixel.blue)
            # Maxing the colors at 255
            if true_red > 255:
                true_red = 255
            if true_green > 255:
                true_green = 255
            if true_blue > 255:
                true_blue = 255
            # Setting the pixel color
            pixel.color = (true_red, true_green, true_blue)
    return my_img


def create_left_border(filename, weight):
    my_img = Image(filename)
    # New output image
    new_img = Image.blank(my_img.width + weight, my_img.height)
    for x in range(new_img.width):
        for y in range(new_img.height):
            pixel = new_img.get_pixel(x,y)
            # Creating the border
            if x < weight:
                pixel.color = (0,0,255)
            # Copying over the old image
            else:
                old_pixel = my_img.get_pixel(x-weight, y)
                pixel.color = old_pixel.color
    return new_img


###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def create_stripes(filename):
    """*** YOUR CODE HERE ***"""


def copper_puzzle(filename):
    """*** YOUR CODE HERE ***"""
