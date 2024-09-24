 
#Se crea una función para pedir al usuario que introduzca las palabras
def obtener_palabra(tipo_palabra):
    return input(f"Por favor, introduce {tipo_palabra}: ")
     
def generar_madlib():
    nom = obtener_palabra('tu nombre: ')
    prof = obtener_palabra('tu profesión: ')
    sust1 = obtener_palabra('una cualidad: ')
    sust2 = obtener_palabra('un nombre común(m): ')
    verb1 = obtener_palabra('un verbo(inf): ')
    verb2 = obtener_palabra('otro verbo(inf): ')
    verb3 = obtener_palabra('un verbo(inf) más: ')
    adj1 = obtener_palabra('un adjetivo(f): ')
    adj2 = obtener_palabra('un adjetivo(f) más: ')
    adj3 = obtener_palabra('otro adjetivo(f) más: ')

    story1 = f"""
    Hola, me llamo {nom}, y trabajo como {prof}, una labor que me apasiona porque me permite
    desarrollar mi {sust1}. Me considero una persona {adj1} y {adj2} y siempre en busca de nuevos
    aprendizajes, lo que me ha llevado a crecer tanto en lo personal como en lo {sust2}.
    Fuera del trabajo, me encanta dedicar mi tiempo a {verb2}, ya que me ayuda a desconectar y encontrar
    inspiración. También me gusta {verb1}, que es una manera divertida de mantenerme activo y 
    social. Soy una persona muy {adj3}, me gusta {verb3} a los demás y siempre busco maneras de
    ayudar.
    ¡Encantado de conocerte!
    """

    print("\n--- Tu Madlib ---")
    print(story1)

# Esta pregunta se lanza al inicio, para preguntar al usuario si quiere jugar o no.
# Es el gran cambio de esta versión. La pregunta es real, si se contesta de forma negativa el juego no se inicia.
# Se ha incluido un 'else' por si se responde con algo que no sea 'si' o 'no'
def pregunta_para_jugar():
    respuesta = input("¿Quieres jugar (si/no): ".lower())
    if respuesta == 'si':
        generar_madlib()
    elif respuesta == 'no':
        print("No pasa nada, otra vez será")
    else:
        print("Respuesta no válida. Por favor responde con 'si' o 'no'.")
        pregunta_para_jugar()
    
# Aquí está orden que hace que se inicie el programa 
if __name__ == "__main__":
    pregunta_para_jugar()