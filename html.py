import os
import requests
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
def minify():
    URL = 'https://html-minifier.com/raw'
    html_name = input('Please enter html file you want to minify: ')
    html_dir = input('In your desktop or your workspace? ')
    if (html_dir == 'desktop'):
        dir_name = input("What's your MS ID? ")
        html_final_dir = '/Users/' + dir_name +'/Desktop/'
    else:
        html_final_dir = '/WORKSPACES/'
    print('Searching ...')
    html_file = find(html_name,  html_final_dir)
    if (html_file != None):
        print("Found it!")
    else:
        print("Error: Cannot find file " + html_name)
        exit()
    option = input("Do you want to display the minified version of " + html_name + "? ")
    if (option == 'yes'):
        data = {'input': open(html_file, 'rb').read()}
        response = requests.post(url=URL, data=data).text
        print("\n" + response)
    else:
        exit()

if __name__ == "__main__":
    minify()