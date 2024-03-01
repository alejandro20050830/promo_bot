from deep_translator import GoogleTranslator

def translate(text,to_lenguage='spanish'):
    try:
        translated = GoogleTranslator(source='auto', target=to_lenguage).translate(text)
    
        return translated
    
    except Exception as e:
        print(e)
        return text
    
