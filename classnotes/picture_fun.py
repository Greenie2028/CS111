from byuimage import Image
def is_green(r,g,b):
    # Threshold 50 green and 20 more than other blue, red
    # 20 more than others
    threshold = 50
    bigger_by = 20
    if g > threshold and g > r +bigger_by and g > b + bigger_by:
        return True
    else:
        return False
my_img = Image("man.png")
for x in range(my_img.width):
    for y in range(my_img.height):
        pixel = my_img.get_pixel(x,y)
        if is_green(pixel.red, pixel.green, pixel.blue):
            pixel.color = (255,255,255)
my_img.show()