import tkinter as tk
from PIL import Image, ImageTk
import requests
import io

#  Function to get a link to a random fox image
def get_random_fox_image_url():
    response = requests.get('https://randomfox.ca/floof/')
    data = response.json()
    return data['image']

# # Function to update the image in the GUI
def update_image():
    # Get a new link to the image
    image_url = get_random_fox_image_url()
    # # Load the image by URL
    response = requests.get(image_url)
    image_data = io.BytesIO(response.content)
    pil_image = Image.open(image_data)
    
    #  Convert the image for use in tkinter
    global photo  # To prevent the image from being deleted by the garbage
    photo = ImageTk.PhotoImage(pil_image)
    
    #  Update the image label
    image_label.config(image=photo)

# Create the main window
root = tk.Tk()
root.title("Генератор картинок лисичек")

# Create an empty label for the image (will be filled during the first update)
image_label = tk.Label(root)
image_label.pack(pady=10)

# Initialize the first image
update_image()

# Create a button to update the image
button = tk.Button(root, text="Следующая лисичка", command=update_image)
button.pack(pady=5)

# Start the main event loop
root.mainloop()
