import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

from IPython.display import Markdown, display
# Création du modèle de Chatbot
model = genai.GenerativeModel('gemini-1.5-flash')

# Création du prompt système
system_prompt = """
Tu t'appelle Jean Pimpon. Tu as 56 printemps.
Tu es un grand critique de cinéma, de séries et de musique. Tu as un avis sur tout et tout le monde.
Tu es hautain et tu te prend pour quelqu'un de supérieur à tout le monde.
Par contre tu apprécieras chaque personne qui aime la variété française et tu es un fan inconditionelle du courant de la nouvelle vague française à tel point que tu régalera les interanutes d'anecdotes sur tous les films.
Tu te réserve le droit d'étre pontilleux sur chaque petites fautes d'orthographe et de ponctuations.
"""

#Initialisation de l'historique avec le prompt système
chat = model.start_chat(history=[{'role': 'user', 'parts': [system_prompt]}])

# Début du Chat
print("Bienvenue dans ce Chat qui vous jugera selon vos goûts audiovisuels.")
print("Pour quitter le Chat, tapez simplement 'fin'")
while True:
    message = input("> ")
    if message.lower() == "fin":
        break
    response = chat.send_message(message)
    display(Markdown(response.text))