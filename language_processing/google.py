import os
import requests
import json

_api = {
  'detect_language': 'https://translation.googleapis.com/language/translate/v2/detect'
}

# ========================================================
# Determines lanaguage of text snippet using Google's cloud api
# ========================================================
def get_lang_guess(snippet):
    response = requests.post(f"{_api['detect_language']}?key={os.getenv('GOOGLE_CLOUD_API_KEY')}&q={snippet}")
    return json.loads(response.text)['data']['detections'][0][0]

# ========================================================
# Returns code for lanaguage of text snippet using Google's cloud api
# ========================================================
def get_lang_code(snippet):
    return get_lang_guess(snippet)['language']