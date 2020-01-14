import praw
import os
import requests
import sys

## TODO
##   Figure out Gifs

def download(link):
    try:
        # Print to console
        print('Title: ' + link.title)
        print('    '+link.url + '\n')

        # Get info about links 
        imgTitle = link.title
        imgTitle = sanatize(imgTitle)
        image = requests.get(link.url)
        
        # Get right extension
        linkType = link.url
        linkType = getExtension(linkType)

        # Quit if no extension
        if linkType == 'NA':
            exit

        # Download \ Save image   
        with open(account+'\\'+imgTitle+linkType, 'wb') as pic:
            pic.write(image.content)            
        
    except AttributeError:
        print('Attribute Error - Possibly a comment')

    except OSError:
        print('OSError')

def saved():
    saved = reddit.user.me().saved(limit=None)
    # Create folder if it does not exist
    if not os.path.isdir(account):
        print('Creating folder ' + account)
        os.mkdir(account)

    for link in saved:
        download(link)

def hidden():
    hidden = reddit.user.me().hidden(limit=None)
    # Create folder if it does not exist
    if not os.path.isdir(account):
        print('Creating folder ' + account)
        os.mkdir(account)
        
    for link in hidden:
        download(link)

def sanatize(title):
    if '\\' in title:
        title = title.replace('\\', ' ')
    elif '/' in title:
        title = title.replace('/', ' ')
    elif ':' in title:
        title = title.replace(':', ' ')
    elif '*' in title:
        title = title.replace('*', '')
    elif '?' in title:
        title = title.replace('?', '')
    elif '"' in title:
        title = title.replace('"', '\'')
    elif '<' in title:
        title = title.replace('<', ' ')
    elif '>' in title:
        title = title.replace('>', ' ')
    elif '|' in title:
        title = title.replace('|', ' ')
    return title

def getExtension(linkType):
    if '.jpg' in linkType:
        return '.jpg'
    elif 'gfycat' in linkType:
        return 'NA'
    elif '.png' in linkType:
        return '.png'
    elif '.gifv' in linkType:
        return '.gifv'
    else:
        return 'NA'
    

# Determines which account to grab info from
account = input("Which account to use? ")
reddit = praw.Reddit(account)

if reddit.read_only:
    print("this is a read only account")
else:
    print("This is an authorized account")
choice = input(
    '''Download Saved: 1
Download Hidden: 2
Option: ''')
if choice == '1':
    saved()
elif choice == '2':
    hidden()

os.system('cls')
