from PIL import Image
im = Image.open("钛合金狗眼.jpg")
print(im.size)

x,y = im.size

im.thumbnail((x//2,y//2))
im.save("new.jpg",'JPEG')