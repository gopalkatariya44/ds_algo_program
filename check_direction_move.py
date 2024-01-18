import numpy as np
import cv2


def calculate_image_similarity(img1, img2):
    img1 = np.array(img1)
    img2 = np.array(img2)

    # Calculate the absolute difference between the two images
    diff = np.abs(img1 - img2)

    # Calculate the sum of the absolute differences
    similarity_score = np.sum(diff)

    return similarity_score


def calculate_movement_direction(img1, img2):
    similarity_score = calculate_image_similarity(img1, img2)

    # Determine the movement direction based on the similarity score
    if similarity_score == 0:
        direction = "No movement"
    else:
        direction = "Movement detected"

    return direction, similarity_score


def find_movement_direction(img1, img2):
    result = cv2.matchTemplate(np.array(img1).astype(np.float32), np.array(img2).astype(np.float32), cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)

    # Calculate the movement direction
    movement_direction = (max_loc[0] - len(img1[0]) // 2, max_loc[1] - len(img1) // 2)

    # Calculate the number of points
    num_points = np.sum(np.array(img1) & np.array(img2))

    # Calculate the angle in degrees
    angle = np.arctan2(movement_direction[1], movement_direction[0]) * (180 / np.pi)

    return movement_direction, num_points, angle


if __name__ == '__main__':
    # img1 = [[-9, 1, 0, -4, 0, -4, 1, 2],
    #         [0, 1, 1, 0, 2, -9, -4, 8],
    #         [0, 0, 0, 0, 3, 1, 0, 1],
    #         [0, 2, 6, 0, 4, 1, 0, 4],
    #         [0, 0, 0, 7, 8, 9, 1, -2],
    #         [1, 0, -1, 1, 0, 0, 1, 0],
    #         [2, 1, 2, 1, 0, 1, 0, 0],
    #         [5, 0, 3, 1, 0, 1, 7, -7],
    #         [-8, 0, 2, 4, 5, 1, 8, 0]]
    #
    # img2 = [[1, 2, 0, -4, 0, -4, 1, 2],
    #         [1, 3, 1, 0, 2, -9, -4, 8],
    #         [1, 1, 0, 0, 3, 1, 0, 1],
    #         [1, 1, 6, 0, 4, 1, 0, 4],
    #         [4, 1, 0, 7, 8, 9, 1, -2],
    #         [6, 1, -1, 1, 0, 0, 1, 0],
    #         [1, 6, 2, 1, 0, 1, 0, 0],
    #         [0, -1, -3, 2, 1, 4, 9, 7],
    #         [-4, 1, 3, 5, 7, 2, 9, 1]]
    img1 = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

    img2 = [[1, 1, 1, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1]]

    direction, points, angle = find_movement_direction(img1, img2)

    print(f"Movement Direction: {direction}")
    print(f"Number of Points: {points}")
    print(f"Angle: {angle} degrees")
