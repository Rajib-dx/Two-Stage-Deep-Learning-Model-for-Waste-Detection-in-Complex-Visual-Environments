import tkinter as tk
from tkinter import filedialog
from src.classifier import classifier
from src.detector import detector
from src.camera import capture_image

def get_image_path():
    """Opens a native file explorer pop-up to upload an image."""
    root = tk.Tk()
    root.withdraw()  # Hide the main blank tkinter window
    root.attributes('-topmost', True)  # Force window to top layer
    
    # Open file browser filter for standard image files
    file_path = filedialog.askopenfilename(
        title="Upload Image for Waste Analysis",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp")]
    )
    return file_path

# 1. Trigger the file browser upload window
image = get_image_path()

# 2. Run analysis only if a file was actually chosen
if image:
    is_waste, confidence = classifier(image)

    if is_waste and confidence > 0.88:
        print("\nResult: Waste")
        results = detector(image)
    else:
        print("\nResult: Not Waste")
else:
    print("Execution cancelled. No image was selected.")
