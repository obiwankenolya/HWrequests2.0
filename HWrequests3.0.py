import os
import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text, to_file, from_lang, to_lang='ru'):

    with open(text) as f:
        text = f.read()
        params = {
            'key': API_KEY,
            'text': text,
            'lang': f'{from_lang}-{to_lang}'
            }
        response = requests.get(URL, params=params)
        translation = response.json()['text'][0]

        file_path = os.path.join('translations', to_file)

    with open(file_path, 'w') as f:
        f.write(translation)

    return translation


translate_it('ES.txt', 'translation es.txt', 'es', to_lang='ru')
