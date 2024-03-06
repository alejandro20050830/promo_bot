from deep_translator import GoogleTranslator
info='‼️La verificación en dos pasos está habilitada y se requiere una contraseña.Agreguela de la siguiente manera:\n\n• <b>Ejemplo</b>:\n\nSu contraseña es <b>123456</b>, luego ingrese <b>mypass123456</b>\n\n🧩 Por favor, introduzca su contraseña:'
def translate_(text,to_lenguage='spanish'):


    try:
        translated = GoogleTranslator(source='auto', target=to_lenguage).translate(text)
    
        return translated
    
    except Exception as e:
        print(e)
        return text
    
#print(translate(info,'english'))



def translate(text, to_language='spanish'):
    try:
        words_to_exclude = ['mycode', 'mypass']
        words = text.split(' ')
        for i in range(len(words)):
            word_=words[i].split('\n')
            for w in word_:           
                if ('/' in w and ('</' not in w or w.count('/')>1)) or 'http' in w or '@' in w:
                    print(w)
                    words_to_exclude.append(w.replace('\n',''))  
                               
        translated_text=GoogleTranslator(source='auto', target=to_language).translate(text)
        for exc in words_to_exclude:
            exc_trans=GoogleTranslator(source='auto', target=to_language).translate(exc)
            translated_text=translated_text.replace(exc_trans,exc)
              
        return translated_text
    except Exception as e:
        print(e)
        return text
    
print(translate('🧩 連結帳戶'))