from PIL import Image

img = Image.open("../assets/profile.png")

rgb_image = img.convert("RGB")

# Resize the image
resized_image = rgb_image.resize((600, 400))

resized_image.save("resized_profile.png")


# Resize the image while maintaining the aspect ratio
img.thumbnail((600, 400))

# Save the resized image to a file
img.save("thumbnail_image.png")