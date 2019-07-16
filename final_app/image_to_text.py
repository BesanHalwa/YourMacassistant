import requests
import json
import cv2

api_key='fdcfa151c288957'

class OCRSpace:
    def __init__(self, api_key):
        """ ocr.space API wrapper
        :param api_key: API key string
        :param language: document language
        """
        self.api_key = api_key
        self.payload = {

            'apikey': self.api_key,
            'language': 'eng',
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

    def ocr_url(self, url):
        """ OCR.space API request with remote file
        :param url: Image url
        :return: Result in JSON format.
        """
        data = self.payload
        data['url'] = url
        r = requests.post(
            'https://api.ocr.space/parse/image',
            data=data,
        )
        return r.json()

def text_from_image(image):
    obj = OCRSpace(api_key='fdcfa151c288957')
    json_obj = obj.ocr_file(image)
    data = json_obj['ParsedResults']
    text = data[0]['ParsedText']
    return text
