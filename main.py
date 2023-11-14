from PIL import Image, ImageDraw, ImageOps


def generate_box(p_color, p_namefile):
    # Set the image size
    image_size = (2000, 2000)

    # Create a black square image
    image = Image.new("RGB", image_size, p_color)

    # Save the image as "figure01.png"
    image.save(p_namefile)


def generate_figures():
    # Set the image02 size
    image_size = (2000, 2000)

    # Create a white square image02
    image02 = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image02)

    # Define the coordinates for the lines
    top_middle = (image_size[0] // 2, 0)
    right_middle = (image_size[0], image_size[1] // 2)
    left_middle = (0, image_size[1] // 2)
    bottom_middle = (image_size[0] // 2, image_size[1])
    bottom_right = (image_size[0], image_size[1])
    bottom_left = (0, image_size[1])
    top_left = (0, 0)
    top_right = (0, image_size[1])

    triangle_coords_bottom = [
        left_middle,
        bottom_left,
        bottom_right,
        right_middle,
        bottom_middle
    ]

    rectangle_coords_bottom= [
        left_middle,
        right_middle,
        bottom_right,
        bottom_left
    ]

    triangle_coords_top_left = [
        left_middle,
        top_middle,
        top_left,
    ]

    triangle_coords_top_right = [
        right_middle,
        top_middle,
        top_right,
    ]

    # Draw triangles in the corners
    draw.polygon(triangle_coords_bottom, fill="black")

    # Save the image02
    image02.save("figure02.png")

    # Invert the colors (swap black and white)
    inverted_image12 = ImageOps.invert(image02)
    inverted_image12.save("figure12.png")

    # Rotate the image02 90 degrees to the left
    rotated_image05 = image02.rotate(90, expand=True)
    rotated_image05.save("figure05.png")

    inverted_image11 = ImageOps.invert(rotated_image05)
    inverted_image11.save("figure11.png")

    rotated_image04 = rotated_image05.rotate(90, expand=True)
    rotated_image04.save("figure04.png")

    inverted_image10 = ImageOps.invert(rotated_image04)
    inverted_image10.save("figure10.png")

    rotated_image03 = rotated_image04.rotate(90, expand=True)
    rotated_image03.save("figure03.png")

    inverted_image13 = ImageOps.invert(rotated_image03)
    inverted_image13.save("figure13.png")

    #Another draws
    # Create a white square image06
    image06 = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image06)

    # Draw rectangles in the corners
    draw.polygon(rectangle_coords_bottom, fill="black")

    # Save the image06
    image06.save("figure06.png")

    inverted_image08 = ImageOps.invert(image06)
    inverted_image08.save("figure08.png")

    rotated_image09 = image06.rotate(90, expand=True)
    rotated_image09.save("figure09.png")

    inverted_image07 = ImageOps.invert(rotated_image09)
    inverted_image07.save("figure07.png")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_box("black", "figure14.png")
    generate_box("white", "figure01.png")

    generate_figures()
