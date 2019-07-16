import requests

English = 'eng'

self.api_key = fdcfa151c288957
self.language = language
self.payload = {
    'isOverlayRequired': True,
    'apikey': self.api_key,
    'language': self
    }

def ocr_file(self, filename):
    """ OCR.space API request with local file
    :param filename: Your file path & name
    :return: Result in JSON format
    """
    with open(filename, 'rb') as f:
        r = requests.post(
            'https://api.ocr.space/parse/image',
            files={filename: f},
            data=self.payload,
        )
    return r.json()
