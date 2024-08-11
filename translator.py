# translator.py

from deep_translator import GoogleTranslator
from langdetect import detect

def detect_language(text):
    """Detect the language of the input text."""
    return detect(text)

def translate_to_english(text):
    """Translate the text to English."""
    return GoogleTranslator(source='auto', target='en').translate(text)

def translate_to_original(text, target_language):
    """Translate the text back to the original language."""
    return GoogleTranslator(source='en', target=target_language).translate(text)
