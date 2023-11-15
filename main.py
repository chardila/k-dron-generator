from PIL import Image, ImageDraw, ImageOps
import os
from itertools import permutations


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
    for cont_i in range(len(images) - 3):
        for cont_j in range(cont_i + 1, len(images) - 2):
            for cont_k in range(cont_j + 1, len(images) - 1):
                for cont_l in range(cont_k + 1, len(images)):
                    # Create a new image with a 2x2 grid
                    combined_width = images[cont_i].width * 2
                    combined_height = images[cont_i].height * 2
                    combined_image = Image.new("RGB", (combined_width, combined_height))

                    # Paste the images into the grid
                    combined_image.paste(images[cont_i], (0, 0))
                    combined_image.paste(images[cont_j], (images[cont_i].width, 0))
                    combined_image.paste(images[cont_k], (0, images[cont_i].height))
                    combined_image.paste(images[cont_l], (images[cont_i].width, images[cont_i].height))

                    combination_name = f"combination_{cont_i}_{cont_j}_{cont_k}_{cont_l}.png"
                    combination_path = os.path.join(output_folder, combination_name)

                    # Save the combined image with a new name to the "output" folder
                    combined_image.save(combination_path)
                    print(f"Creating file: {combination_name}")

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
    for cont_i in range(len(images) - 1):
        for cont_j in range(cont_i + 1, len(images)):
            # Create a new image with a 2x1 grid
            combined_width = max(images[cont_i].width, images[cont_j].width)
            combined_height = images[cont_i].height + images[cont_j].height
            combined_image = Image.new("RGB", (combined_width, combined_height))

            # Paste the images into the grid
            combined_image.paste(images[cont_i], (0, 0))
            combined_image.paste(images[cont_j], (0, images[cont_i].height))

            # Append the combined image to the list
            combinations_2x1.append(combined_image)

    # Create combinations of 2x1 images in a 1x2 grid
    for cont_i in range(len(combinations_2x1) - 1):
        for cont_j in range(cont_i + 1, len(combinations_2x1)):
            # Create a new image with a 1x2 grid
            combined_width = combinations_2x1[cont_i].width + combinations_2x1[cont_j].width
            combined_height = max(combinations_2x1[cont_i].height, combinations_2x1[cont_j].height)
            combined_image = Image.new("RGB", (combined_width, combined_height))

            # Paste the images into the grid
            combined_image.paste(combinations_2x1[cont_i], (0, 0))
            combined_image.paste(combinations_2x1[cont_j], (combinations_2x1[cont_i].width, 0))

            # Save the combined image with a new name to the "output" folder
            combination_name = f"combination_1x2_{cont_i}_{cont_j}.png"
            combination_path = os.path.join(output_folder, combination_name)
            combined_image.save(combination_path)

            print(f"Creating file: {combination_name}")

            # Store the content hash in the dictionary along with the file name

    # Close all opened images
    for image in images:
        image.close()

    for combined_image in combinations_2x1:
        combined_image.close()


def create_permutations():
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

    # Get all permutations of the images
    image_permutations = permutations(images, 4)

    cont = 0
    # Loop through all permutations
    for permutation in list(image_permutations):
        # Create a new image with a 2x2 grid
        combined_width = permutation[0].width * 2
        combined_height = permutation[0].height * 2
        combined_image = Image.new("RGB", (combined_width, combined_height))

        # Paste the images into the grid
        combined_image.paste(permutation[0], (0, 0))
        combined_image.paste(permutation[1], (permutation[0].width, 0))
        combined_image.paste(permutation[2], (0, permutation[0].height))
        combined_image.paste(permutation[3], (permutation[0].width, permutation[0].height))

        # Save the combined image with a new name to the "output" folder
        # combination_name = f"permutation_{file_names.index(permutation[0].filename)}_{file_names.index(permutation[1].filename)}_{file_names.index(permutation[2].filename)}_{file_names.index(permutation[3].filename)}.png"
        combination_name = f"permutation_{cont}.png"
        cont = cont + 1
        print(f"file created: {combination_name}")
        combination_path = os.path.join(output_folder, combination_name)
        combined_image.save(combination_path)

    # Close all opened images
    for image in images:
        image.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_box()
    generate_figures()
    # create_combinations_version2()
    create_permutations()
