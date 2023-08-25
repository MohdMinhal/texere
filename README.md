# Texere: Text Removal from Images

Texere is a Python package that provides functionality for removing text from images, along with the option to generate a mask for further processing.

## Installation

You can install Texere using pip:

```
pip install texere
```

# Usage: 
```
from texere.purge import txt

modified_image, mask = txt('image_path.jpg')

# 'modified_image' contains the image with text removed
# 'mask' is a binary image indicating the regions where text was removed
# Further processing using the 'mask' image can be done here
```

# Example:
```
from texere.purge import txt

# Replace 'input_image.jpg' with the path to your input image
modified_image, mask = txt('input_image.jpg')

# Save the modified image
cv2.imwrite('output_image.jpg', modified_image)

# Save the mask as a binary image
cv2.imwrite('mask_image.jpg', mask)
```
# Contributing:
Contributions to Texere are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request on GitHub.

# License:
This project is licensed under the MIT License - see the LICENSE file for details.
