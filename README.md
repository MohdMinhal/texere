# Texere: A Powerful Image Processing Module

Texere is a Python package designed for Digital Image Processing, offering two primary functions: Text Removal from Images and Edge Marking. Additionally, it provides the capability to generate masks to support further image processing tasks.

## Installation

You can easily install Texere using pip:

```bash
pip install texere
```

## Usage

### Removing Text from Images

```python
from texere.purge import txt

# Replace 'image_path.jpg' with the path to your input image
modified_image, mask = txt('image_path.jpg', pixels=7, threshold=10)

# 'modified_image': image with text removed
# 'mask': binary image indicating text-removed regions
# Further processing using the 'mask' image can be performed
```

### Marking Edges in Images

```python
from texere.edges import mark

# Replace 'image_path.jpg' with the path to your input image
marked_image = mark('image_path.jpg', threshold=70)

# 'marked_image': image with marked edges
# You can further process or visualize the edges as needed
```

## Example

### Removing Text from Images

```python
from texere.purge import txt
import cv2

# Replace 'input_image.jpg' with the path to your input image
modified_image, mask = txt('input_image.jpg', pixels=7, threshold=10)

# Save the modified image
cv2.imwrite('output_image.jpg', modified_image)

# Save the mask as a binary image for potential text area inpainting
cv2.imwrite('mask_image.jpg', mask)
```

### Marking Edges in Images

```python
from texere.edges import mark

# Replace 'input_image.jpg' with the path to your input image
marked_image = mark('input_image.jpg', threshold=70)

# Save the marked image
marked_image.save('marked_image.jpg')
```

## Contributing

Contributions to Texere are encouraged! If you have ideas for improvements, bug fixes, or new features, please open an issue or submit a pull request on GitHub.

## License

Texere is licensed under the MIT License - see the LICENSE file for details.
