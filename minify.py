import os
import requests
css = 'https://cssminifier.com/raw' #Calls the minifier url
js = 'https://javascript-minifier.com/raw'

def minifyCode(url, path):
    print(path)
    data = {'input': open(path, 'rb').read()} # Packs the css file to a data variable to be sent off to the minifier.
    response = requests.post(url, data=data) # Sends a Post requests, then retrieves the data.

    wr = open(path, 'w') # Opens current local file.
    wr.write(response.text) # Overwrites the local file.

def find_files(directory): #Function to recursivly loop through all files and minify.
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename) # Creates path

        if (os.path.isdir(path)): #Checks if the file is directory
            find_files(path)
        if filename.endswith(".css"): # Checks for css files
            minifyCode(css, path)
            continue
        elif filename.endswith(".js"): # Checks for css files
            minifyCode(js, path)
            continue
        else:
            continue

find_files(os.getcwd()) #Calls the function with the current directory
