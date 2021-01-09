import os
import re
import shutil
import webbrowser

siteFolder = input("Please enter folder name where your site files are located:")
siteName = input("Please enter the filename of your stored website files:")
fileType = input("Please enter the file (css, js, etc.):")
fileName = input("Please enter what file to search for fonts:")
fontPathStart = input("Please enter the start for each font link:")
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
path = "/Users/davidborn/Desktop/"+siteFolder+"/"+siteName+"_files/"+fileType+"/"+fileName

linkArray=[]

with open(path, 'r') as cssFile:
    for line in cssFile:
        print(line)
        eotPattern = "[\/()-_%&0-9a-zA-Z \.]+\.eot"
        svgPattern = "[\/()-_%&0-9a-zA-Z \.]+\.svg"
        woffPattern = "[\/()-_%&0-9a-zA-Z \.]+\.woff"
        woff2Pattern = "[\/()-_%&0-9a-zA-Z \.]+\.woff2"
        if re.findall("url"+ eotPattern,line):
            fontPath = re.findall("url"+eotPattern,line)
            linkArray.append(fontPath[0])
        if re.findall("url"+ svgPattern,line):
            fontPath = re.findall("url"+svgPattern,line)
            linkArray.append(fontPath[0])
        if re.findall("url"+ woffPattern,line):
            fontPath = re.findall("url"+woffPattern,line)
            linkArray.append(fontPath[0])
        if re.findall("url"+ woff2Pattern,line):
            fontPath = re.findall("url"+woff2Pattern,line)
            linkArray.append(fontPath[0])

for i in range(len(linkArray)):
    fontPathEnd = linkArray[i]
    linkArray[i] = fontPathEnd.replace('url(',fontPathStart)
    webbrowser.get(chrome_path).open(linkArray[i])

print(linkArray)       


#webbrowser.get(chrome_path).open('youtube.com');
#webbrowser.get(chrome_path).open('https://www.boeing.com/assets/fonts/bcf54343-d033-41ee-bbd7-2b77df3fe7ba.woff');