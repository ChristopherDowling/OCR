import requests
import os
import datetime
import sys
import zipfile
import shutil

def POSTRequest(filename, overlay=False, apikey='621cb55b5d88957', language='eng'):
    payload = {'isOverlayREquired': overlay,
               'detectOrientation': 'False',
               'apikey': apikey,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
        return r.content.decode()

def cleanup(line):
    # messy and arbitrary but it's not like I'm going to train an AI to fix mistakes
    #print('in:  ' + line)
    line = line.replace('TO:,', '')
    line = line.replace('\' ', '')
    line = line.replace(': ', '')
    line = line.replace('; ', '')
    line = line.replace('cvca ', 'CVG2 ')
    line = line.replace('CVG20? ', 'CVG2 06 ')
    line = line.replace('TUSI ', 'TUS1 ')
    line = line.replace('TUS106', 'TUS1 06')
    line = line.replace('LEXI ', 'LEX1 ')
    line = line.replace('AMAZO\\I', 'AMAZON')
    line = line.replace('3LVC', 'BLVD')
    #print('out: ' + line)
    return line

### Start
print('Processing file ... Please Wait ...')
# Drag + Drop a zip file on to the .bat
# .bat pipes zip file path to .py
for arg in sys.argv[1:]:
    if arg.endswith('.zip') == False: # Exit if a zip file wan't specified as an argument
        print('Error: Please use a .zip file')
        sys.exit()

# delete any old folders by the same name (makes it easier for testing)
zippedfile = arg
folder = arg[:-4] + '/'
if os.path.exists(folder):
    shutil.rmtree(folder)

# unzip the folder
print('Unzipping ' + zippedfile)
print('Unzipping to ' + folder)
zipfile.ZipFile(zippedfile, 'r').extractall(folder)

# makes a list of all the files in the folder
os.mkdir(folder + '/out')
files = []
for r, d, f in os.walk(folder):
    for file in f:
        files.append(os.path.join(r, file))

# rotates the files
i = 0
print('Pre-processing text ... ')
for f in files:
    ext = f[-4:]
    os.system('magick convert -rotate 90 "' + f + '" ' + folder + 'out/' + str(i).zfill(2) + ext)
    i = i + 1

# Sends them to the OCR scanning program online
text = []
for r, d, f in os.walk(folder + 'out/'):
    for file in f:
        print('Attempting to OCR: ' + folder + 'out/' + file)
        responce = POSTRequest(folder + 'out/' + file)
        #print(responce)
        text.append(responce)

# Processess text
print('Processing text ...')

if os.path.exists('out.csv'):
    os.remove('out.csv')
output = open('out.csv', 'w+')

# temporary, used to fish for errors
if os.path.exists('out.txt'):
    os.remove('out.txt')
tmpoutput = open('out.txt', 'w+')

now = datetime.datetime.now()

for line in text:
    namestart = line.find('"ParsedText":"')
    nameend = line.find('\\r\\n')
    name = line[namestart+14:nameend]
    
    addressstart = line.find('SHIP ')
    addressend = line.find('UPS GROUND')
    address = line[addressstart+5:addressend]

    out = now.strftime("%m/%d/%Y") + ',' + name + ',7676 WOODBINE AVENUE,MARKHAM,ON,L3R 2N2,' + address.replace('\\r\\n', ',') + '\n'
    tmpoutput.write(out)
    
    out = cleanup(out)
    output.write(out)

    
    
output.close()
tmpoutput.close()

# Cleanup
# shutil.rmtree(folder)
