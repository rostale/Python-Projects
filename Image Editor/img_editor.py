from PIL import Image
import os

# image_process is the name of the directory where the images that are supposed to be edited are stored.
inPath = r"C:\Users\xyz\OneDrive\Desktop\image_process"
# final is the name of directory where images after getting edited are stored.
outPath = r"C:\Users\xyz\OneDrive\Desktop\final"

# using for loop to iterate through differrent image files.
for imagePath in os.listdir(inPath):
    inputPath = os.path.join(inPath, imagePath)
    img = Image.open((inputPath), mode="r").convert('RGB').rotate(270).resize((720, 1080))
    fullOutPath = os.path.join(outPath, 'edited_'+imagePath)
    img.save(fullOutPath)
    name = fullOutPath[38:-1]
    # prints the name of the image file after editing.
    print("The name of the edited image is %s" % (name, ))
    # prints the location of the image file after editing.
    print("The location of the edited image is %s" % (fullOutPath, ))      
