from PIL import Image, ImageDraw, ImageOps


def generate_box():
    # Set the image size
    image_size = (2000, 2000)

    # Create a black square image
    image01 = Image.new("RGB", image_size, "white")

    # Save the image as "figure01.png"
    image01.save("figure01.png")

    # Invert the colors (swap black and white)
    inverted_image14 = ImageOps.invert(image01)
    inverted_image14.save("figure14.png")

def generate_figures():
    # Set the image size
    image_size = (2000, 2000)

    # Create a white square image
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    # Define the coordinates for the lines
    right_middle = (image_size[0], image_size[1] // 2)
    left_middle = (0, image_size[1] // 2)
    bottom_middle = (image_size[0] // 2, image_size[1])
    bottom_right = (image_size[0], image_size[1])
    bottom_left = (0, image_size[1])

    triangle_coords_bottom = [
        left_middle,
        bottom_left,
        bottom_right,
        right_middle,
        bottom_middle
    ]

    rectangle_coords_bottom = [
        left_middle,
        right_middle,
        bottom_right,
        bottom_left
    ]

    # Draw triangles in the corners
    draw.polygon(triangle_coords_bottom, fill="black")

    # Save the image
    image.save("figure02.png")

    # Invert the colors (swap black and white)
    inverted_image = ImageOps.invert(image)
    inverted_image.save("figure12.png")

    # Rotate and save the images
    for i in range(3):
        rotated_image = image.rotate(90 * (i+1), expand=True)
        rotated_image.save(f"figure0{i+3}.png")
        inverted_image = ImageOps.invert(rotated_image)
        inverted_image.save(f"figure1{i+1}.png")

    # Another draws
    # Create a white square image
    image06 = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image06)

    # Draw rectangles in the corners
    draw.polygon(rectangle_coords_bottom, fill="black")

    # Save the image
    image06.save("figure06.png")

    # Invert the colors (swap black and white)
    inverted_image08 = ImageOps.invert(image06)
    inverted_image08.save("figure08.png")

    # Rotate and save the image
    rotated_image09 = image06.rotate(90, expand=True)
    rotated_image09.save("figure09.png")

    inverted_image07 = ImageOps.invert(rotated_image09)
    inverted_image07.save("figure07.png")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_box()
    generate_figures()
