import colorgram as co

rgb_colors = []
colors = co.extract('Image.jpg', 6)
print(colors)  # the extract function would simply extract the color
# the colors are extracted in a format of alist which is stored
# in colors variable and can b used to iterate through each.
# It can give us two types of colors one is rgb and other is hsl.

# Now, we are gonna write a for loop that taps into each of these colors.
# by, appending

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)  # He, by naming it rgb we are commanding that we need
    # only the rgb part of our returned list.

print(rgb_colors)
