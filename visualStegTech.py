from PIL import Image,ImageChops,ImageEnhance
'''Overlays two or more images up to a max of 6 using PILs ImageChops.add function'''
def OverlayAdd():
    im1 = Image.open('image1.png')
    im2 = Image.open('image2.png')
    im3 = Image.open('image3.png')
    im4 = Image.open('image4.png')
    im5 = Image.open('image5.png')
    im6 = Image.open('image6.png')
    images = [im1, im2, im3, im4, im5, im6]
'''Superimposes two or more images up to a max of 6 using PIL's ImageChops.multiply function'''
def OverlayMultiply(im1, im2, im3="", im4="", im5="", im6=""):
    pass
'''Runs.add on all the frames of a video at 30fps thats no longer then 60 seconds'''
def overlayVideo(video):
    pass
'''converts image into a base64 string and then converts that string into plain text'''
def decodeBase64(img,base64Str):
    pass
'''increases the brightness of an image'''
def brighten(img):
    pass