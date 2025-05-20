# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define antonio = Character("Antonio")
define cura = Character("Cura")

image bg church_day = "images/fondo3.jpeg"

image antonio neutral = "images/antonio3.png"
image antonio confused = "images/antonio1.png"
image antonio sad = "images/antonio4.png"
image antonio angry = "images/antonio5.png"
image antonio relieved = "images/antonio6.png"
image antonio calm = "images/antonio2.png"
image antonio thoughtful = "images/antonio4.png"
image antonio determined = "images/antonio7.png"
image antonio hesitant = "images/antonio1.png"

image cura smile = "images/cura6.png"
image cura serious = "images/cura2.png"

# El juego comienza aquí.

label start:

    jump iglesia_confesion

label iglesia_confesion:

    scene bg church_day
    with fade

    "Antonio camina lentamente por la calle empedrada, hasta llegar a la iglesia del pueblo."

    show antonio neutral at center
    antonio "No sé qué hago aquí, pero... quizás hablar con él me ayude."

    "Antonio entra en la iglesia, se detiene al fondo y observa el altar. Al poco tiempo, el cura aparece."

    show cura smile at left
    cura "Antonio... ¿eres tú? Hacía años que no te veía por aquí."

    show antonio confused
    antonio "Sí, padre. He estado... alejado. Pero necesitaba hablar con alguien."

    cura "Claro, hijo. ¿Qué te preocupa?"

    show antonio sad
    antonio "Estoy pasando por una crisis. Siento que quiero hacer cosas que nunca me había planteado. Y no sé cómo lidiar con eso."

    show cura serious
    cura "Eso es normal, Antonio. Pero ante todo, debes escucharte a ti mismo. El alma humana es compleja... y lo importante es vivir con verdad."

    menu:
        "Lo toma bien y se siente aliviado":
            jump reaccion_buena

        "Se siente juzgado y se aleja":
            jump reaccion_mala

label reaccion_mala:

    show antonio angry
    antonio "No lo entiende... nadie lo entiende."

    return

label reaccion_buena:

    show antonio relieved
    antonio "Gracias, padre. Me ayuda oír eso, es usted muy comprensivo."

    cura "Dios es comprensión, hijo. Sé fiel a ti mismo."

    "Antonio sonríe ligeramente, con una carga menos en los hombros."

    menu:
        "Sí, abre su corazón completamente":
            jump conversacion_profunda

        "No, prefiere despedirse ya":
            jump despedida_paz

label despedida_paz:

    show antonio calm
    antonio "Creo que por hoy es suficiente. Gracias por escucharme."

    cura "Siempre, hijo. Aquí tienes un lugar seguro."

    return

label conversacion_profunda:

    show antonio thoughtful
    antonio "A veces sueño que bailo, que me miro al espejo con maquillaje y no me reconozco... y a la vez me siento más yo que nunca."

    cura "El camino hacia uno mismo es el más difícil, pero también el más hermoso."

    menu:
        "Se anima a dar el primer paso hacia su expresión":
            jump paso_valentia

        "Decide esperar y reflexionar más tiempo":
            jump paso_espera

label paso_valentia:

    show antonio determined
    antonio "Gracias, padre. Creo que quiero empezar a ser quien soy, sin miedo."

    cura "Si me dejas, yo estaré aquí para acompañarte y guiarte, Antonio."

    return

label paso_espera:

    show antonio hesitant
    antonio "Aún no sé si estoy listo. Pero hablarlo... ya es un paso, ¿no?"

    cura "Todos los caminos comienzan con una pregunta. Confía en tu tiempo."

    return