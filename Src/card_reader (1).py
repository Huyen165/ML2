import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pytesseract

from PIL import Image

# %% Image processing


def resize(img, scale=50):
    # Scale should be in range of 10% - 25%
    new_w = int(img.shape[1] * scale / 100)
    new_h = int(img.shape[0] * scale / 100)
    dim = (new_w, new_h)
    resized_img = cv2.resize(img, dim)  # , interpolation = cv2.INTER_AREA)

    return resized_img


def edge_detection(img, thresh_lower=50, thresh_upper=200):
    # Grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Gaussian blur
    blurred_img = cv2.GaussianBlur(gray_img, (3, 3), 0)

    # Edge detection
    edge_img = cv2.Canny(blurred_img, thresh_lower, thresh_upper)

    return edge_img


def extract_contour(img):
    # Find contours
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
    dilated_img = cv2.dilate(img, kernel)
    contours, hierarchy = cv2.findContours(
        dilated_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(clone_resized_img, contours, -1, (0, 255, 0), 1)

    # Get the largest contour
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt = contours[max_index]

    return cnt


def approx_contour(img, cnt):
    # Bounding quadrangle
    hull = cv2.convexHull(cnt)

    # Approx
    approximations = cv2.approxPolyDP(
        hull, 0.02 * cv2.arcLength(hull, True), closed=True)
    cv2.drawContours(img, [approximations], 0, (255, 0, 255), 2)

    return approximations


def deskew(img, approximations):
    ROI = approximations.reshape(4, 2)

    rect = np.zeros((4, 2), dtype='float32')

    s = np.sum(ROI, axis=1)
    rect[0] = ROI[np.argmin(s)]  # [T]op [l]eft corner (denoted as tl)
    rect[2] = ROI[np.argmax(s)]  # [B]ottom [r]ight corner (denoted as br)

    diff = np.diff(ROI, axis=1)
    rect[1] = ROI[np.argmin(diff)]  # [T]op [r]ight corner (denoted as tr)
    rect[3] = ROI[np.argmax(diff)]  # [B]ottom [l]eft corner (denoted as bl)

    # Calculate the width and the height of the original document
    (tl, tr, br, bl) = rect

    width1 = np.sqrt((tl[0] - tr[0])**2 + (tl[1] - tr[1])**2)
    width2 = np.sqrt((bl[0] - br[0])**2 + (bl[1] - br[1])**2)
    original_width = max(int(width1), int(width2))

    height1 = np.sqrt((tl[0] - bl[0])**2 + (tl[1] - bl[1])**2)
    height2 = np.sqrt((tr[0] - br[0])**2 + (tr[1] - br[1])**2)
    original_height = max(int(height1), int(height2))

    # Calculate new rectangle coordinate for the perspective transform
    new_rect = np.array([
        [0, 0],
        [original_width-1, 0],
        [original_width-1, original_height-1],
        [0, original_height-1]], dtype="float32")

    # Calculate the transform matrix
    matrix = cv2.getPerspectiveTransform(rect, new_rect)

    # Do the perspective transform and crop
    deskew_img = cv2.warpPerspective(
        img, matrix, (original_width, original_height))

    return deskew_img

# %% OCR


def OCR_engine(img):
    # Tesseract installation path
    pytesseract.pytesseract.tesseract_cmd = r'F:/Machine Learning/OCCR/tesseract.exe'

    # Call the API
    text = pytesseract.image_to_string(img, lang='eng+vie')

    return text

# %% Main function


if __name__ == "__main__":
    # Input data
    folder_path = "F:/Machine Learning/OCCR/ImgData"
    image_name = 'test6.jpg'  # 'LX_41.jpg'
    img_path = os.path.join(folder_path, image_name)

    # Read the original image
    original_img = cv2.imread(img_path)

    # Resize
    resized_img = resize(original_img, 50)
    cv2.imshow('Resized', resized_img)

    # Make a copy of the resized image
    clone_resized_img = resized_img.copy()

    # Edge detection
    edge_img = edge_detection(resized_img, 20, 200)
    cv2.imshow('Edge detection', edge_img)

    # Contours
    cnt = extract_contour(edge_img)
    approximations = approx_contour(resized_img, cnt)
    cv2.imshow('Approximation', resized_img)

    # Create a blank image if there is no proper deskew found
    deskew_img = np.zeros(
        shape=[resized_img.shape[0], resized_img.shape[1], 3], dtype=np.uint8)

    try:
        # Deskew
        deskew_img = deskew(resized_img, approximations)
    except:
        pass

    cv2.imshow('Deskew', deskew_img)

    # Empty string to store the OCR result
    text = ''

    try:
        # OCR with Tesseract API
        text = OCR_engine(deskew_img)

    except:
        pass

    print(text)

    cv2.waitKey()
