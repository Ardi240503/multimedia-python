from PIL import Image
from PIL import ImageFilter

# Memuat gambar
image = Image.open('image.jpg')

# Menyimpan gambar
cropped_image = image.crop((10, 10, 700, 700))
cropped_image.save('cropped_image.jpg')

resized_image = cropped_image.resize((700, 700))
resized_image.save('resized_image.jpg')

flitered_image =resized_image.filter(ImageFilter.BLUR)
flitered_image.save('filtered_image.jpg')