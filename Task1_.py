# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 08:28:35 2019

@author: Hassan
"""

import time
import urllib.request as r
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-L", "--URL", required=True, help="Your Url")
opener = r.build_opener()

def getNextURL(URL): #Finds the first link/title
    infile = opener.open(URL)
    page = infile.read()
                        #Find the first <p> tag for the main body
    mainP = page[page.find('<p>'.encode(encoding='utf-8',\
                errors='strict')):page.find('<p>'.encode(encoding='utf-8',\
                errors='strict'))+500]
                        #Find the first href for the link
    newPage = mainP[mainP.find('<a href="/wiki/'.encode(encoding='utf-8',\
                    errors='strict'))+15:mainP.find('"'.encode(encoding='utf-8',\
                    errors='strict'),mainP.find('<a href="/wiki/'.encode(encoding='utf-8',\
                    errors='strict'))+15)] 
    return newPage

def main():  # The MAIN function
    args = vars(parser.parse_args())
    URL = args["URL"]
    counter = 0
    start_time = time.time()
    newPage = getNextURL(URL)
    if newPage.decode(encoding='utf-8', errors='strict') == 'Philosophy':
        counter += 1
        print(newPage.decode(encoding='utf-8', errors='strict'))
    while newPage.decode(encoding='utf-8', errors='strict') != 'Philosophy':
        #print(URL)
                #Creates the next link to go to based upon the first link
         URL = 'http://en.wikipedia.org/w/index.php?title=' + newPage.decode(encoding='utf-8',
                                                                             errors='strict') 
         time.sleep(.5)
         newPage = getNextURL(URL)
         print (newPage.decode(encoding='utf-8', errors='strict'))
         counter +=1
        
         
    t = time.time()-start_time
    print(counter) 
    print(t)
    
if __name__ == "__main__":
    main()