"""Translators for french and english languages"""
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core.api_exception import ApiException
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


def englishToFrench(englishText):
    """Translate english text to french"""

    try:
        translation = language_translator.translate(
                text=[englishText],
                model_id='en-fr'
            ).get_result()
    except ApiException:
        return ''

    french_text = ''
    try:
        french_text = translation['translations'][0]['translation']
    except KeyError:
        pass
    except IndexError:
        pass

    return french_text


def frenchToEnglish(frenchText):
    """Translate french text to english"""

    try:
        translation = language_translator.translate(
                text=[frenchText],
                model_id='fr-en'
            ).get_result()
    except ApiException:
        return ''

    english_text = ''
    try:
        english_text = translation['translations'][0]['translation']
    except KeyError:
        pass
    except IndexError:
        pass

    return english_text
