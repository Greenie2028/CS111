from byuimage import Image; import sys

# Darkens the image by a given percent
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
    my_img.save(sys.argv[3])

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
    my_img.save(sys.argv[3])

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
    my_img.save(sys.argv[3])

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
    out_img.save(sys.argv[3])

# Returns a vertically flipped image
def flipped(filename):
    in_img = Image(filename)
    out_img = Image.blank(in_img.width, in_img.height)
    for x in range(in_img.width):
        for y in range(in_img.height):
            pixel = out_img.get_pixel(x,y)
            old_pixel = in_img.get_pixel(x, in_img.height - y - 1)
            pixel.color = old_pixel.color
    out_img.save(sys.argv[3])

def mirrored(filename):
    in_img = Image(filename)
    out_img = Image.blank(in_img.width, in_img.height)
    for y in range(in_img.height):
        for x in range(in_img.width):
            pixel = out_img.get_pixel(x,y)
            old_pixel = in_img.get_pixel(in_img.width-x-1,y)
            pixel.color = old_pixel.color
    out_img.save(sys.argv[3])

def collage(img_name1,img_name2,img_name3,img_name4,width:int):
    img1 = Image(img_name1)
    img2 = Image(img_name2)
    img3 = Image(img_name3)
    img4 = Image(img_name4)
    output_img = Image.blank(2*img1.width + 3*width, 2*img1.height + 3*width)
    for x in range(output_img.width):
        for y in range(output_img.height):
            new_pixel = output_img.get_pixel(x,y)
            if x < width or width+img1.width <= x < 2*width+img1.width or 2*(width+img1.width) <= x:
                new_pixel.color = (0,0,0)
            elif y < width or width+img1.height <= y < 2*width+img1.height or 2*(width+img1.height) <= y:
                new_pixel.color = (0,0,0)
            elif x >= width and x < width+img1.width and y >= width and y < width+img1.height:
                old_pixel = img1.get_pixel(x-width,y-width)
                new_pixel.color = old_pixel.color
            elif x >= 2*width+img1.width and x < 2*(width+img1.width) and y >= width and y < width+img1.height:
                old_pixel = img2.get_pixel(x-(2*width+img1.width), y-width)
                new_pixel.color = old_pixel.color
            elif x >= width and x < width+img1.width and y >= 2*width+img1.height and y < 2*(width+img1.height):
                old_pixel = img3.get_pixel(x-width,y-2*width-img1.height)
                new_pixel.color = old_pixel.color
            elif x >= 2*width+img1.width and x < 2*(width+img1.width) and y >= 2*width+img1.height and y < 2*(width+img1.height):
                old_pixel = img4.get_pixel(x-(2*width+img1.width),y-2*width-img1.height)
                new_pixel.color = old_pixel.color
    output_img.save(sys.argv[6])

def detect_green(pixel,threshold,factor):
  average = (pixel.red + pixel.green + pixel.blue) / 3
  if pixel.green >= factor * average and pixel.green >  threshold:
    return True
  else:
    return False
  
def greenscreen(fore_img_name, back_img_name,threshold,factor):
    fore_img = Image(fore_img_name)
    back_img = Image(back_img_name)
    output_img = Image.blank(fore_img.width,fore_img.height)
    for x in range(output_img.width):
        for y in range(output_img.height):
            old_pixel = fore_img.get_pixel(x,y)
            new_pixel = output_img.get_pixel(x,y)
            if detect_green(old_pixel,threshold,factor):
                new_pixel.color = back_img.get_pixel(x,y).color
            else:
                new_pixel.color = fore_img.get_pixel(x,y).color
    output_img.save(sys.argv[4])

# Checks if the given arguments are valid
def validate_commands(commands):
    # Displays the Image
    flag = commands[0]
    if flag == '-d' and len(commands) > 1:
        Image(commands[1]).show()
        return True
    if flag == "-k" and len(commands) > 3:
        darken(commands[1],float(commands[3]))
        return True
    if flag == '-s' and len(commands) > 2:
        sepia(commands[1])
        return True
    if flag == '-g' and len(commands) > 2:
        grayscale(commands[1])
        return True
    if flag == '-b' and len(commands) > 6:
        make_borders(commands[1],int(commands[3]),int(commands[4]),int(commands[5]),int(commands[6]))
        return True
    if flag == '-f' and len(commands) > 2:
        flipped(commands[1])
        return True
    if flag == '-m' and len(commands) > 2:
        mirrored(commands[1])
        return True
    if flag == '-c' and len(commands) > 6:
        collage(commands[1],commands[2],commands[3],commands[4],int(commands[6]))
        return True
    if flag == '-y' and len(commands) > 5:
        greenscreen(commands[1],commands[2],int(commands[4]),float(commands[5]))
        return True
    return False


def main():
    commands = sys.argv[1:]
    validate_commands(commands)

    
if __name__ == "__main__":
    main()