import random as r
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD" : "Tiene muchos usos, pero generalmente se usa como sarcasmo",
            "RED FLAG" : "Indica los aspectos negativos de una persona",
            "BASADO" : "Alguien muy top, muy bueno en lo que hace",
            "CHAMBA": "Trabajar"
            }

print(meme_dict.keys())
word = input("Escribe una palabra que no entiendas o escribe 'sorprendeme' para que elijamos una por ti: ").upper()

if word in meme_dict.keys():
    print("significado de", word, ":", meme_dict[word])

elif word == "SORPRENDEME":
    r_word = r.choice(list(meme_dict.keys()))
    print("la palabra que conoceras hoy es:",r_word,":",meme_dict[r_word])

else:
    agregar = input("Esta palabra aún no se agrega al diccionario, te gustaría agregarla?(si o no)").lower()
    if agregar=="si":
        sig_nuevo = input("Escribe el significado de la palabra que ingresaste: ").lower()
        meme_dict.update({word: sig_nuevo})
        print("¡La palabra ha sido agregada exitosamente!",meme_dict)

