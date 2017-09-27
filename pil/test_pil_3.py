# test_pil_3.py
# coding: utf-8
'''
gaosi ...
'''
from PIL import Image, ImageFilter

class MyGaussianBlur(ImageFilter.Filter):
    name = "GaussianBlur"

    def __init__(self, radius=2, bounds=None):
        self.radius = radius
        self.bounds = bounds

    def filter(self, image):
        if self.bounds:
            clips = image.crop(self.bounds).gaussian_blur(self.radius)
            image.paste(clips, self.bounds)
            return image
        else:
            return image.gaussian_blur(self.radius)
if __name__ == '__main__':

	simg = 'demo.jpg'
	dimg = 'demo_blur.jpg'
	image = Image.open(simg)
	image = image.filter(MyGaussianBlur(radius=30))
	image.save(dimg)
	print dimg, 'success'