import os
import requests
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
def minify():
    URL = 'https://cssminifier.com/raw'
    css_name = input('Please enter css file you want to minify: ')
    css_dir = input('In your desktop or your workspace? ')
    if (css_dir == 'desktop'):
        dir_name = input("What's your MS ID? ")
        css_final_dir = '/Users/' + dir_name +'/Desktop/'
    else:
        css_final_dir = '/WORKSPACES/JBOSS_DEVELOPER_STUDIO/EeS/'
    print('Searching ...')
    css_file = find(css_name, css_final_dir)
    if (css_file != None):
        print("Found it!")
    else:
        print("Error: Cannot find file " + css_name)
        exit()
    option = input("Do you want to display the minified version of " + css_name + "? ")
    if (option == 'yes'):
        data = {'input': open(css_file, 'rb').read()}
        response = requests.post(url=URL, data=data).text
        print("\n" + response)
    else:
        exit()

if __name__ == "__main__":
    minify()