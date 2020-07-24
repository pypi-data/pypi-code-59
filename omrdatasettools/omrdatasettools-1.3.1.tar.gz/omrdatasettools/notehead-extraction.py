import numpy as np
from PIL import Image, ImageDraw
from PIL import ImageFilter
from scipy import ndimage
from skimage.measure import regionprops

image = Image.open("notehead_masks.jpg")

kernel = (0, 0, 0, 0, 0,
          0, -1, 1, -1, 0,
          0, 1, 3, 1, 0,
          0, -1, 1, -1, 0,
          0, 0, 0, 0, 0)

dilation_img = image.filter(ImageFilter.MinFilter(5))
# dilation_img.show()

erosion_img = dilation_img.filter(ImageFilter.MaxFilter(5))
# plt.imshow(erosion_img)
# plt.show()

# Remove objects that are too small
# smooth the image (to remove small objects)
imgf = ndimage.gaussian_filter(erosion_img, 2)
threshold = 50

# find connected components
labeled, nr_objects = ndimage.label(imgf > threshold)
print("Number of objects is {}".format(nr_objects))

proposals = regionprops(labeled)

output_image = Image.open("notehead_masks.jpg").convert("RGB")
image_draw = ImageDraw.Draw(output_image)

widths = [p.bbox[3] - p.bbox[1] for p in proposals]
heights = [p.bbox[2] - p.bbox[0] for p in proposals]
median_width = np.median(np.array(widths))
print(median_width)
median_height = np.median(np.array(heights))
print(median_height)

for proprosal in proposals:
    y0, x0, y1, x1 = proprosal.bbox
    width = x1 - x0
    height = y1 - y0
    if width > median_width + 5 or height > median_height + 5:
        continue  # Skip too big objects
    if width < median_width - 5 or height < median_height - 5:
        continue  # Skip too small objects
    image_draw.rectangle((x0, y0, x1, y1), width=3, outline="red")

# plt.imshow(output_image)
# plt.show()
output_image.save("output.png")
