from PIL import Image

filename = "../assets/profile.png"
filename = "/Users/girish/Desktop/workspace/GirishCodeAlchemy/alchemy/alchemy-useful-packages/usefulpackages.png"
sizes = (500, 500)
img = Image.open(filename)
rgb_image = img.convert("RGB")

# Resize the image
resized_image = rgb_image.resize(sizes)

resized_image.save("resized_profile.png")


# Resize the image while maintaining the aspect ratio
img.thumbnail(sizes)

# Save the resized image to a file
img.save("thumbnail_image.png")