import os
import shutil
import glob
import random


def create_test_closed(source, destination, percent):
    # Create destination directory if it doesn't exist
    if not os.path.exists(destination):
        os.makedirs(destination)

    # Use os.scandir() instead of os.walk()
    with os.scandir(source) as entries:
        files_closed = [entry.name for entry in entries if entry.is_file()]

    file_count_closed = len(files_closed)

    # Check if the percent value is within the valid range [0, 100]
    if 0 <= percent <= 100:
        percentage = int(file_count_closed * (percent / 100))
        to_move = random.sample(files_closed, min(percentage, file_count_closed))

        for file_name in to_move:
            file_path = os.path.join(source, file_name)
            shutil.move(file_path, destination)

        print(f"Moved {len(to_move)} images to the destination successfully.")
    else:
        print("Invalid percentage value. Please provide a value between 0 and 100.")


def create_test_open(source, destination, percent):
    # Create destination directory if it doesn't exist
    if not os.path.exists(destination):
        os.makedirs(destination)

    # Use os.scandir() instead of os.walk()
    with os.scandir(source) as entries:
        files_open = [entry.name for entry in entries if entry.is_file()]

    file_count_open = len(files_open)

    # Check if the percent value is within the valid range [0, 100]
    if 0 <= percent <= 100:
        percentage = int(file_count_open * (percent / 100))
        to_move = random.sample(files_open, min(percentage, file_count_open))

        for file_name in to_move:
            file_path = os.path.join(source, file_name)
            shutil.move(file_path, destination)

        print(f"Moved {len(to_move)} images to the destination successfully.")
    else:
        print("Invalid percentage value. Please provide a value between 0 and 100.")


# Example usage
create_test_closed('dataset/train/Closed', 'dataset/test/Closed', 20)  # for 20%
create_test_open('dataset/train/Open', 'dataset/test/Open', 20)  # for 20%
