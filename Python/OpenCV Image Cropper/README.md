# Drinks Classifier Image Cropper

A utility for cropping and managing images for the Drinks Classifier project. Efficiently handle and process your images without the hassle of manual editing.

## 🚀 Usage

Navigate to the main directory:

\```bash
cd ~/Desktop/Drinks_Classifier
\```

Start the cropper:

\```bash
python your_script_name.py
\```

### 🎨 Key Shortcuts:

- **d**: Delete the current image.
- **s**: Save the cropped version of the current image.
- **i**: Ignore the current image and move to the next.
- **q**: Gracefully quit the program.

> 📌 **Note**: The utility smartly remembers the images you've ignored or deleted. So, the next time you run it, you won't revisit them.

### 📢 Outputs

Your terminal will keep you informed:

- 📥 `Image saved at [path/to/image]`
- 🚫 `Image ignored.`
- 🗑️ `Image deleted from [path/to/image]`

A detailed log is maintained for every action, making sure you're always informed of past operations.

## ⚠️ Important Points

1. 🔄 Cropped images directly overwrite the originals. Always backup if you need the raw files.
2. 📜 Every session appends to the log file, providing a cumulative history.

## Contribution

Feel free to contribute, report bugs, or suggest features. Every bit of help is appreciated!
