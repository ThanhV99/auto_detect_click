import pyautogui
import numpy as np

def click():
    # Define the region (left, top, width, height)
    region = (0, 0, 500, 500)
    image_path = 'test.JPG'  # Path to the image you want to detect
    
    
    location = pyautogui.locateOnScreen(image_path, region=region, confidence=0.9)
    if location:
        print(f"Image found at {location}")
        print(location)
    else:
        print("Image not found in the region")

if __name__ == "__main__":
    click()