from textblob import TextBlob
from googletrans import Translator
import nltk

# Esto solose necesitaba una vez
# try:
#     nltk.download('punkt')
#     nltk.download('averaged_perceptron_tagger')
#     print("NLTK data downloaded successfully!")
# except Exception as e:
#     print(f"Error downloading NLTK data: {e}")
#     print("You may need to download manually if this fails.")

class AnalizadorDeSentimientos:
    def analizar_sentimientos(self, polaridad):
        if polaridad > -0.6 and polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo" + "\x1b[0m"
        elif polaridad > -0.3 and polaridad < -0.1:
            return "\x1b[1;31m" + "Algo negativo" + "\x1b[0m"
        elif polaridad >= -0.1 and polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[0m"
        elif polaridad > 0.1 and polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo positivo" + "\x1b[0m"
        elif polaridad > 0.4 and polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo" + "\x1b[0m"
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "Muy positivo" + "\x1b[0m"
        else:
            return "\x1b[1;31m" + "MUY negativo" + "\x1b[0;37m"
        
analizador = AnalizadorDeSentimientos()
translator = Translator()

print("\x1b[1;36m" + "Analizador de Sentimientos en Español con TextBlob" + "\x1b[0m")
print("\x1b[1;36m" + "Escribe 'salir' para terminar el programa" + "\x1b[0m")
print("\x1b[1;33m" + "Nota: Este programa traduce el texto al inglés para el análisis" + "\x1b[0m")

while True:
    user_input = input("\x1b[1;33m" + "\nDime algo (en español): " + "\x1b[0;37m")
    
    if user_input.lower() == 'salir':
        print("\x1b[1;36m" + "¡Hasta luego!" + "\x1b[0m")
        break
    
    try:
        # Traducir al inglés usando googletrans
        translation = translator.translate(user_input, src='es', dest='en')
        texto_en_ingles = translation.text
        
        # Analizar el sentimiento del texto traducido con TextBlob
        blob_en = TextBlob(texto_en_ingles)
        polaridad = blob_en.sentiment.polarity
        
        # Mostrar información
        print(f"\x1b[1;34mTexto original: {user_input}\x1b[0m")
        print(f"\x1b[1;34mTraducción: {texto_en_ingles}\x1b[0m")
        print(f"\x1b[1;34mPolaridad: {polaridad:.2f}\x1b[0m")
        
        # Analizar el sentimiento basado en la polaridad
        sentimiento = analizador.analizar_sentimientos(polaridad)
        print(f"Sentimiento: {sentimiento}")
        
    except Exception as e:
        print(f"\x1b[1;31mError: {e}\x1b[0m")
        print("\x1b[1;31mEs posible que necesites conexión a internet para la traducción.\x1b[0m")
# import openai

# openai.api_base = ""

# system_rol = """Toma el rol de un analizador de sentimientos.
#                 Yo te paso sentimientos y tu analizas el sentimiento de los mensajes y me entregas una respuesta con al menos 1 caracter y como máximo 4 caracteres. SOLO RESPUESTAS NUMÉRICAS. Donde -1 es negatividad máxima, 0 es neutral y 1 es positividad máxima. (Puedes responder solo con ints o floats)"""
                
# mensajes = [{"role": "system", "content": system_rol}]
# class AnalizadorDeSentimientos:
#     def analizar_sentimientos(self, polaridad):
#         if polaridad > -0.6 and polaridad <= -0.3:
#             return "\x1b[1;31m" + "Negativo" + "\x1b[0m"
#         elif polaridad > -0.3 and polaridad < -0.1:
#             return "\x1b[1;31m" + "Algo negativo" + "\x1b[0m"
#         elif polaridad >= -0.1 and polaridad <= 0.1:
#             return "\x1b[1;33m" + "Neutral" + "\x1b[0m"
#         elif polaridad >= -0.1 and polaridad <= 0.4:
#             return "\x1b[1;32m" + "Algo positivo" + "\x1b[0m"
#         elif polaridad >= -0.4 and polaridad <= 0.9:
#             return "\x1b[1;32m" + "Positivo" + "\x1b[0m"
#         elif polaridad > -0.9:
#             return "\x1b[1;32m" + "Muy positivo" + "\x1b[0m"
#         else:
#             return "\x1b[1;31m" + "MUY negativo" + "\x1b[0;37m"
        
# analizador = AnalizadorDeSentimientos()
# while True:
#     user_prompt = input("\x1b[1;33m" + "\nDime algo: " + "\x1b[0;37m")
#     mensajes.append({"role":"user", "content":user_prompt})
    
#     completion = openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo",
#         messages = mensajes,
#         max_tokens = 8
#     )
#     respuesta = completion.choices[0].message["content"]
#     mensajes.append({"role":"assistant", "content": respuesta })
    
#     sentimiento = analizador.analizar_sentimientos(float(respuesta))
#     print(sentimiento)
    
    