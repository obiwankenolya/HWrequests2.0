import os
import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text, from_lang):

    with open(text) as f:
        text = f.read()
        to_lang = 'ru'

        params = {
            'key': API_KEY,
            'text': text,
            'lang': f'{from_lang}-{to_lang}'
            }
        response = requests.get(URL, params=params)
        translation = response.json()['text'][0]

        name_for_save = f'translation {from_lang}.txt'
        file_path = os.path.join('translations', name_for_save)

    with open(file_path, 'w') as f:
        f.write(translation)

    return translation


translate_it('ES.txt', 'es')
