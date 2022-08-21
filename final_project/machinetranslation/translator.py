import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    """Function to translate english to french"""	
    french_text = language_translator.translate(
        text = english_text,
        model_id='en-fr').get_result()
    result = french_text['translations'][0]['translation']
    return result

def frenchToEnglish(french_text):
    """Function to translate french to english"""
    english_text = language_translator.translate(
        text = french_text,
        model_id='fr-en').get_result()
    result = english_text['translations'][0]['translation']
    return result