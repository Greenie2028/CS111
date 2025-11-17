from byuimage import Image

# Returns the absolute value of a number
def abs(num):
    if num < 0:
        return num * -1
    return num

# Dims a provided image by a given percent
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
            
# Makes the provided image grayscale
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

# Applies a sepia filter to an image
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

# Returns a vertically flipped image
def flipped(filename):
    in_img = Image(filename)
    out_img = Image.blank(in_img.width, in_img.height)
    for x in range(in_img.width):
        for y in range(in_img.height):
            pixel = out_img.get_pixel(x,y)
            old_pixel = in_img.get_pixel(x, in_img.height - y - 1)
            pixel.color = old_pixel.color
    return out_img

# Applies a border to an image of the given thickness and color in rgb code
def make_borders(filename,thickness,r,g,b):
    in_img = Image(filename)
    out_img = Image.blank(in_img.width + (2*thickness), in_img.height + (2*thickness))
    for x in range(out_img.width):
        for y in range(out_img.height):
            new_pixel = out_img.get_pixel(x,y)
            if x <= thickness or x >= thickness+in_img.width or y <= thickness or y >= thickness + in_img.height:
                new_pixel.color = (r,g,b)
    for x in range(in_img.width):
        for y in range(in_img.height):
            old_pixel = in_img.get_pixel(x,y)
            new_pixel = out_img.get_pixel(x+thickness,y+thickness)
            new_pixel.color = old_pixel.color
    return out_img


if __name__ == "__main__":
    test_img = make_borders("test_files\\landscape.png",10,0,0,255)
    test_img.show()