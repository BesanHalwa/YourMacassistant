import requests


class OCRSpaceLanguage:
    English = 'eng'

class OCRSpace:
    def __init__(self, api_key, language=OCRSpaceLanguage.English):
        """ ocr.space API wrapper
        :param api_key: API key string
        :param language: document language
        """
        self.api_key = api_key
        self.language = language
        self.payload = {
            'isOverlayRequired': True,
            'apikey': self.api_key,
            'language': self.language,
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

def main():
    obj = OCRSpace(api_key=fdcfa151c288957)
    json_obj = obj.ocr_file('ss.py')

if __name__ == "__main__":
    main()
