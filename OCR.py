import requests


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
    
out = POSTRequest(filename='C:\\1.jpg')
print(out)
