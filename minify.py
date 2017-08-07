import os
import requests
url = 'https://cssminifier.com/raw' #Calls the minifier url

def find_files(directory): #Function to recursivly loop through all files and minify.
    for filename in os.listdir(directory):
        if (os.path.isdir(os.path.join(directory, filename))): #Checks if the file is directory
            find_files(os.path.join(directory, filename))
        if filename.endswith(".css"): # Checks for css files
            path = os.path.join(directory, filename) # Creates path
            print(path)
            data = {'input': open(path, 'rb').read()} # Packs the css file to a data variable to be sent off to the minifier.
            response = requests.post(url, data=data) # Sends a Post requests, then retrieves the data.

            wr = open(path, 'w') # Opens current local file.
            wr.write(response.text) # Overwrites the local file.
            continue
        else:
            continue

find_files(os.getcwd()) #Calls the function with the current directory
