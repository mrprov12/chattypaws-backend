# src/utils/image_processing_utils.py
import cv2


def detect_button_press(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a threshold to get a binary image
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Calculate the area and ignore small contours
        area = cv2.contourArea(contour)
        if area > 1000:
            # Get the bounding box coordinates
            x, y, w, h = cv2.boundingRect(contour)
            # Draw a rectangle around the detected button press
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            return (x, y, w, h)  # Return the bounding box of the button press

    return None
