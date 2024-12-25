import cv2
import numpy as np
import pyautogui
from logzero import logger

def click():
    region = (0, 0, 900, 600)
    image_path = "test.JPG"
    is_clicked = False
    
    # Load the target image
    template = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    h, w = template.shape[:2]

    while True:
        # Capture the screen region
        screenshot = pyautogui.screenshot(region=region)
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Perform template matching
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

        # Find the best match
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val > 0.8:  # Adjust confidence threshold as needed
            if not is_clicked:
                logger.debug(f"Image found with confidence {max_val} at position {max_loc}")
                logger.debug(f"min loc: {min_loc}")
                logger.debug("Clicking...")
                is_clicked = True
                
            # Draw a rectangle around the detected object
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)
        else:
            is_clicked = False

        # Display the result
        cv2.imshow("Detection", screenshot)

        # Check for key presses
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('w'):
            logger.debug("Refreshing click action...")
            is_clicked = False

    cv2.destroyAllWindows()

if __name__ == "__main__":
    click()