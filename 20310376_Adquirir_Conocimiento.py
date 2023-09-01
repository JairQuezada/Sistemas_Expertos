from nltk.chat.util import Chat, reflections

def peer_load(archive):
    peers = []
    try:
        with open(archive, 'r', encoding='utf-8') as archivo:
            lines = archivo.readlines()
            for line in lines:
                parts = line.strip().split('|')
                pattern = parts[0].strip()
                answers = [answer.strip() for answer in parts[1:]]
                peers.append([pattern, answers])
    except FileNotFoundError:
        print("El documento 'Respuestas.txt' no existe")
    return peers

def chats():
    print("Bienvenido a tu bot, es momento de empezar.\nSi quieres salir del bot, por favor escribe 'Parar'.\nDe lo contrario, puedes empezar a preguntar.")

    peers = peer_load("respuestas.txt")
    chat = Chat(peers, reflections)

    exit_flag = False 

    while not exit_flag:
        user = input("Usted: ")
        if user.lower() == "parar":
            print("Bot: Muy bien, hasta luego ^-^")
            exit_flag = True  
            continue 

        answer = chat.respond(user)
        if answer is None:
            print("Bot: Lo lamento, pero no tengo una respuesta adecuada. ¿Puedes enseñarme cómo responderla?\nSi/No")
            while True:
                decision = input("Usted: ")
                if decision.lower() == "si":
                    new_question = user.lower()
                    new_answer = input("Bot: ¿Cuál sería la mejor respuesta para esa pregunta? ")
                    peers.append([new_question, [new_answer]])
                    with open("respuestas.txt", "a", encoding='utf-8') as archivo:
                        archivo.write(f"\n{new_question} | {new_answer}")
                    print("Bot: Todo listo, gracias por tu contribución. ")
                    chat = Chat(peers, reflections)
                    break
                elif decision.lower() == "no":
                    print("Bot: Muy bien, por favor pregunte algo que esté en mi base o agregue su conocimiento.")
                    break
                else:
                    print("Bot: Por favor, escriba una de las dos opciones ('Si' o 'No').")
        else:
            print("Bot:", answer)


if __name__ == "__main__":
    chats()
