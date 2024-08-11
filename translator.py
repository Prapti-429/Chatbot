# translator.py

from langdetect import detect
from googletrans import Translator

# Initialize the translator
translator = Translator()

def detect_language(text):
    """
    Detect the language of the provided text.
    
    Parameters:
        text (str): The text whose language is to be detected.
        
    Returns:
        str: The detected language code (e.g., 'en' for English).
    """
    try:
        return detect(text)
    except Exception as e:
        print(f"Error detecting language: {e}")
        return 'en'

def translate_to_english(text):
    """
    Translate the provided text to English.
    
    Parameters:
        text (str): The text to be translated to English.
        
    Returns:
        str: The translated text in English.
    """
    try:
        translated = translator.translate(text, src='auto', dest='en')
        return translated.text
    except Exception as e:
        print(f"Error translating to English: {e}")
        return text

def translate_to_original(text, dest_language):
    """
    Translate the provided text back to the original language.
    
    Parameters:
        text (str): The text to be translated back to the original language.
        dest_language (str): The original language code (e.g., 'fr' for French).
        
    Returns:
        str: The translated text in the original language.
    """
    try:
        if dest_language == 'en':
            return text
        translated = translator.translate(text, src='en', dest=dest_language)
        return translated.text
    except Exception as e:
        print(f"Error translating to original language: {e}")
        return text
