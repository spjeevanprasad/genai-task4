from PIL import Image, ImageFilter

# Load input image
image = Image.open("input.png")

# Apply transformation (simulate image-to-image translation)
output = image.convert("L")  # convert to grayscale
output = output.filter(ImageFilter.DETAIL)

# Save output
output.save("output.png")

print("Image processed and saved as output.png")