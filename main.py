import urllib.request
import os
os.system("bash banner.sh")
def wallpaper(): #wallpaper set 
     os.system(f"termux-wallpaper  -f 'image.jpg' ")
     #=========================
def cheak():
    if (os.path.exists("image.jpg")):
        os.system("rm -rf image.jpg")
        print("deelet susses image.jpg")
        #========================
def download_image(url, file_path):
    with urllib.request.urlopen(url) as response, open(file_path, 'wb') as out_file:
        data = response.read()
        out_file.write(data)

# Example usage:
cheak()
uri = input("enter url image :-")
url = (f"{uri}")
file_path = 'image.jpg'
download_image(url, file_path)
wallpaper()