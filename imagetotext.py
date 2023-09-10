from PIL import Image
import pytesseract

# Open an image file (replace 'image.png' with your image file)
image = Image.open('image.png')

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text:")
print(text)
