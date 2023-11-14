from PIL import Image, ImageDraw, ImageOps
import os


def generate_box():
    # Set the image size
    image_size = (200, 200)

    # Create a black square image
    image01 = Image.new("RGB", image_size, "white")

    # Save the image as "figure01.png"
    image01.save("figure01.png")

    # Invert the colors (swap black and white)
    inverted_image14 = ImageOps.invert(image01)
    inverted_image14.save("figure14.png")


def generate_figures():
    # Set the image size
    image_size = (200, 200)

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
        rotated_image = image.rotate(90 * (i + 1), expand=True)
        rotated_image.save(f"figure0{i + 3}.png")
        inverted_image = ImageOps.invert(rotated_image)
        inverted_image.save(f"figure1{i + 1}.png")

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


def create_combinations():
    # Get the current working directory as the folder path
    base_folder = os.getcwd()

    # Create the "output" folder if it doesn't exist
    output_folder = os.path.join(base_folder, "output")
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of file names in the specified folder
    file_names = [filename for filename in os.listdir(base_folder) if
                  filename.startswith("figure") and filename.endswith(".png")]

    # Open all images and store them in a list
    images = [Image.open(os.path.join(base_folder, file_name)) for file_name in file_names]

    # Loop through all combinations of 4 files
    for i in range(len(images) - 3):
        for j in range(i + 1, len(images) - 2):
            for k in range(j + 1, len(images) - 1):
                for l in range(k + 1, len(images)):
                    # Create a new image with a 2x2 grid
                    combined_width = images[i].width * 2
                    combined_height = images[i].height * 2
                    combined_image = Image.new("RGB", (combined_width, combined_height))

                    # Paste the images into the grid
                    combined_image.paste(images[i], (0, 0))
                    combined_image.paste(images[j], (images[i].width, 0))
                    combined_image.paste(images[k], (0, images[i].height))
                    combined_image.paste(images[l], (images[i].width, images[i].height))

                    # Save the combined image with a new name to the "output" folder
                    combination_name = f"combination_{i}_{j}_{k}_{l}.png"
                    combination_path = os.path.join(output_folder, combination_name)
                    combined_image.save(combination_path)
    # Close all opened images
    for image in images:
        image.close()


def create_combinations_version2():
    # Get the current working directory as the base folder path
    base_folder = os.getcwd()

    # Create the "output" folder if it doesn't exist
    output_folder = os.path.join(base_folder, "output")
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of file names in the specified folder
    file_names = [filename for filename in os.listdir(base_folder) if
                  filename.startswith("figure") and filename.endswith(".png")]

    # Open all images and store them in a list
    images = [Image.open(os.path.join(base_folder, file_name)) for file_name in file_names]

    # Create a list to store the images for 2x1 combinations
    combinations_2x1 = []

    # Create combinations of 2 files in a 2x1 grid
    for i in range(len(images) - 1):
        for j in range(i + 1, len(images)):
            # Create a new image with a 2x1 grid
            combined_width = max(images[i].width, images[j].width)
            combined_height = images[i].height + images[j].height
            combined_image = Image.new("RGB", (combined_width, combined_height))

            # Paste the images into the grid
            combined_image.paste(images[i], (0, 0))
            combined_image.paste(images[j], (0, images[i].height))

            # Append the combined image to the list
            combinations_2x1.append(combined_image)

    # Create combinations of 2x1 images in a 1x2 grid
    for i in range(len(combinations_2x1) - 1):
        for j in range(i + 1, len(combinations_2x1)):
            # Create a new image with a 1x2 grid
            combined_width = combinations_2x1[i].width + combinations_2x1[j].width
            combined_height = max(combinations_2x1[i].height, combinations_2x1[j].height)
            combined_image = Image.new("RGB", (combined_width, combined_height))

            # Paste the images into the grid
            combined_image.paste(combinations_2x1[i], (0, 0))
            combined_image.paste(combinations_2x1[j], (combinations_2x1[i].width, 0))

            # Save the combined image with a new name to the "output" folder
            combination_name = f"combination_1x2_{i}_{j}.png"
            combination_path = os.path.join(output_folder, combination_name)
            combined_image.save(combination_path)

    # Close all opened images
    for image in images:
        image.close()

    for combined_image in combinations_2x1:
        combined_image.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_box()
    generate_figures()
    create_combinations_version2()
