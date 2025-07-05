# test.py
import cv2
import numpy as np

def cartoonize_image(image_path, output_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur to reduce noise
    gray_blurred = cv2.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(
        gray_blurred, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 11, 7
    )

    # Use bilateral filter for better smoothing
    color = cv2.bilateralFilter(img, d=10, sigmaColor=75, sigmaSpace=75)

    # Sharpen the image (optional for improved effect)
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharpened = cv2.filter2D(color, -1, kernel)

    # Combine edges with the smoothed image
    cartoon = cv2.bitwise_and(sharpened, sharpened, mask=edges)

    # Save the cartoonized image
    cv2.imwrite(output_path, cartoon)

