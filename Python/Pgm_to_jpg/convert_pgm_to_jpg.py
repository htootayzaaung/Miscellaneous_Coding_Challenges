import os
from PIL import Image

# Use the current directory as source and output directory
directory = os.getcwd()

for filename in os.listdir(directory):
    if filename.endswith('.pgm'):
        filepath = os.path.join(directory, filename)
        
        # Open the image
        with Image.open(filepath) as img:
            # Convert and save as JPG with maximum quality
            output_filename = os.path.join(directory, filename.split('.')[0] + '.jpg')
            img.save(output_filename, 'JPEG', quality=100)
            print(f"Converted {filename} to JPG format with maximum quality.")
            
        # Delete the original .pgm file
        os.remove(filepath)
        print(f"Deleted {filename}.")

print("Conversion and cleanup completed!")
