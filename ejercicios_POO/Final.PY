# #ejercicio final
# from textblob import TextBlob

# class AnalisadorDeSentimiento:
#     def analisar_sentimiento(self,texto):
#         analisis = TextBlob(texto)
#         if analisis.sentiment.polarity > 0:
#             return 'positivo'
#         elif analisis.sentiment.polarity == 0:
#             return 'neutral'
#         else: 
#             return 'negativo'
        
# analizadors = AnalisadorDeSentimiento()
# resultado = analizadors.analisar_sentimiento("Hello today i'm sad")
# print(resultado)

import openai
openai.api_key = "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" # NO SE PUDO TOCA CON API DE PAGO