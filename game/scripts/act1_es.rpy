# es
# Act 1 starts here.
init:
    # Declare language-specific characters used by this game.
    if persistent.lang == "spanish":
        $ classroom = "Clase"
        $ teacher = "Maestra"
        $ unknown = "Desconocida"
label a1k1_start_es:
    scene black
    play music music_netbook1
    $ renpy.pause(1.0)
    scene bg sunrise
    with introfade
    nvl clear
    nvl show dissolve
    play countermusic sound_typing
    net "<Kerida Cyllia...>"
    net "<Por fin he llegado a la Academia Para Niñas de Camelia...>"
    net "<A partir de hoy, voy a vivir akí en el dormitorio como mis padres kerían...>"
    nvl hide dissolve
    stop countermusic
    scene bg academy
    with fade
    k_happy "¡Ah! Si sólo pudieras respirar este hermoso aire fresco de la mañana..."
    k_relieved "Y qué hermosa se ve la salida del sol..."
    k_genki "No puedo esperar a ver qué aventuras me esperan--"
    stop music
    $ renpy.play(sound_collide)
    with vpunch
    nar "parece que alguien acaba de chocar contigo..."
    nar "...y caes al suelo"
    show miharu grief at Fling(-0.5, 0.35, 1.5, 1.5, 1.0, 730.0)
    u "Hiyaaaah!!"
    nar "pero la otra también se cae..."
    play music music_miharu1
    menu:
        "Estás bien, ¿pero tal vez ella está herida?":
            jump a1k1_okay_es
        "Babosa estúpida, no miras por dónde vas!":
            jump a1k1_eyes_es
        "Jeje, se ve perdida. Haz la una pequeña broma.":
            jump a1k2_bone_es
label a1k1_okay_es:
    k_worried "¡Ay! ¡Ah! ¿Estas bien?"
    show miharu whimper at Rise(0.5, 1.0)
    u "Lo siento mucho. Sí, estoy bien, gracias. ¿Y usted?"
    k_relieved "Estoy como si nada."
    show miharu relieved
    u "Me da mucho gusto escuchar eso!"
    show miharu uncomfortable at Bounce(1)
    u "¡Ah! ¡Recórcholis! voy a llegar tarde!"
    show miharu smile
    u "Lo siento mucho, pero tengo que irme, así que..."
    show miharu genki at ExitLeft(0.75)
    u "HASTA LUEGO~!"
    k_nervous "¿Eh?"
    jump a1k1_who_es
label a1k1_eyes_es:
    k_furious "¡OYE!! ¿ESTÁS CIEGA O QUÉ?!"
    show miharu grief at Rise(0.5, 0.25)
    u "HIYAAAHHH~!! ¡Disculpame! lo siento mucho!!"
    show miharu uncomfortable at Bounce(1)
    u "¡Ah! ¡Recórcholis! voy a llegar tarde!"
    show miharu nervous
    u "Lo siento de nuevo, pero tengo que irme ahora mismo... Así que..."
    show miharu grief at ExitLeft(0.5)
    u "HAAAAAAAAAASTA LUEEEEEEEEEGO~!"
    k_shout "¡OYE ME!!  ¿ADONDE CREES QUE VAS?!!"
    k_stare "...."
    k_unamused "...ah... Se me escapó..."
    jump a1k1_who_es
label a1k2_bone_es:
    k_sneaky "¡AY AY! ¡Mi pierna!!! Está rota! Estoy que me retuerzo del dolor!"
    show miharu grief at Rise(0.5, 0.5)
    u "Gyaaaah!! ¿Qué hice?!"
    show miharu dread at Bounce(2)
    u "Debo llamar a un hospital~! Debo llamar un hospital~!!"
    k_genki "Oi.... Sólo estoy bromeando."
    show miharu grief at Bounce(1)
    u "OH NO! Voy a llegar tarde!"
    show miharu confused at Bounce(2)
    u "¿Qué debo hacer~? ¿Qué debo hacer~?!"
    k_weird "Oi.... ¿Me estas escuchando?"
    show miharu whimper
    u "Sí.... *lloriquear*"
    k_smug "Lo siento... pero en realidad todo esto es una broma..."
    show miharu grief at Bounce(4)
    u "NO ES CIERTO! Su pierna esta toda rota por mi culpa!!"
    k_ehhh "¿Eh?!"
    show miharu cautious at Bow(1)
    u "Le prometo que asumiré toda responsabilidad! Pero después de que regreso del trabajo..."
    k_weird "Ehhhh.... Bueno...."
    show miharu uncomfortable
    u "En calidad de mientras, por favor consigua a alguien que la lleve a un hospital..."
    show miharu whimper at ExitLeft(0.75)
    u "Hasta luego, y por favor perdóname de nuevo~!"
    k_gasp "AH~!"
    k_unamused "..."
    k_sarcastic "Séra que ella \"se dió a la fuga\"?"
    jump a1k1_who_es
label a1k1_who_es:
    k_sigh "...."
    show miharu smile at RunInDistance(-0.5, 1.5, 0.6, 0.75)
    nar "ves como ella sale corriendo de la escuela"
    nar "\"¿Quién habra sido esa chica?\", te preguntas"
    stop music fadeout 3.5
    $ mouse_visible = False
    scene white
    with videofade_in
    show miniOP_1
    show miniOP_2 behind miniOP_1
    show miniOP_3 behind miniOP_2
    $ renpy.pause(7.5)
    play music music_konobangumiwa1
    show konobangumiwa_1
    show konobangumiwa_2
    $ renpy.pause(10.25)
    $ mouse_visible = True
    scene black
    stop music
    $ renpy.pause(0.25)
    play sound sound_schoolchime
    show schoolchime
    show actgeez
    $ act_name = 'act_1 "My name is Kana, not Hana"'
    show acttitle
    $ renpy.pause(7.5)
    scene bg classroom
    with dissolve
    play music music_aizawa1
    show aizawa glad at EnterLeft(0.0, 1.0)
    t "Bueno, presten atención!"
    t "Como les dije ayer, tenemos una nueva estudiante transferida que nos va acompañar empezando hoy."
    show aizawa grateful
    t "Adelante, Señorita Transferida! Introducete."
    show aizawa smile at ExitLeft(1.0)
    nar "entras al salon de clase, tratando todo lo posible para no lucir nerviosa"
    k_happy "Hola, queridas alumnas. Mi nombre es Kana."
    k_genki "Es un placer conocerlas."
    show crowd nervous behind aizawa at Rise(0.50, 0.50)
    c "{=whispered}Igualmente...{/=whispered}"
    show crowd nervous at Sit(0.75)
    nar "¿acaso no sonaban un poco... aburridas?"
    show aizawa sigh at EnterLeft(0.0, 0.5)
    t "*suspiro*"
    show aizawa resign
    t "¿Pretendes matarnos de hambre con esa dizque introducción?"
    show aizawa fatigue
    stop music
    k_nervous "¿Eh?!"
    nar "oyes susurros en todo el salon: \"¡Ah! ya va empezar de nuevo...\""
    show aizawa chastisecenter
    t "Adonde esta la pasión, Hana?! Me choca tu falta de pasión!"
    show aizawa sadistic
    t "Hazlo otra vez!"
    show aizawa revenge
    play music music_aizawa2
    k_omg "EHHHHHH?!!!"
    k_nervous "..."
    k_genki "¿Disculpame profesora, pero es esto una especie de broma para las del primer año...?"
    show aizawa reprimand at Bounce(2)
    t "¡Claro que no!"
    show aizawa maniac
    t "Ahora trata lo de nuevo, O NO QUERAS SABER LO QUE TE PASARÁ!"
    show aizawa astound at ExitLeft(0.25)
    k_swirl "GYAAHHHH~!! Está bien! Está bien!"
    k_nervous "ejem..."
    menu:
        "Más vale seguro que desconocido...":
            jump a1k1_hana_es
        "Ella quiere ver pasión? ENSEÑALE LO QUE ES LA PASIÓN!!":
            jump a1k1_sama_es
        "¡Oh! Nomás dí cualquier tonteria que se te viene...":
            jump a1k1_legend_es
label a1k1_hana_es:
    k_genki "Mi nombre es Kana, no Hana."
    stop music
    play sound sound_deadsilence
    c "{=whispered}*........ silencio ..........*{/=whispered}"
    nar "estás casi segura que tu vida a terminado..."
    show aizawa chortlecenter at EnterLeft(0.0, 0.75)
    t "Eh, que se le va hacer?  Está bien, pasaste..."
    show aizawa schemecenter
    k_panic "Eso es todo?!!"
    jump a1k1_intro_es
label a1k1_sama_es:
    stop music
    k_creepy "{=whispered}jujuju...{/=whispered}"
    play music music_pompous1
    k_evil "SOY LA GRAN Y TODOPODEROSA KANA-SAMA!!"
    k_villainous "Arrodillense delante de mí, chusma!"
    stop music
    play sound sound_deadsilence
    c "{=whispered}*........ silencio ..........*{/=whispered}"
    nar "\"Me da lástima... \", se oye susurrar entre tus compañeras de clase"
    nar "qué vergüenza..."
    play music music_aizawa2
    show aizawa obsessed at EnterLeft(0.0, 0.25)
    t "BRAVO!!!"
    show aizawa love
    t "QUE PADRISIMA INTRODUCCIÓN!!  Estoy que lloro de felicidad!!"
    show aizawa tearsofpride
    k_ehhh "EH?!!!"
    show aizawa squeal
    t "Tú sí eres de las mías, hermana!!"
    show aizawa savor
    k_waterfall "¿Qué está pasando aquí?!"
    k_angry "Y no soy su hermana!"
    show aizawa sweetdream
    nar "te das cuenta que la profesora dejó de prestarte atención"
    jump a1k1_intro_es
label a1k1_legend_es:
    k_squeal "I am Legend!"
    stop music
    play sound sound_embarrass
    c "*........ gemidos ..........*"
    nar "\"Oh, ¿por qué dije cualquier tonteria que se me ocurrío?!\", te preguntas"
    show aizawa orly at EnterLeft(0.0, 1.0)
    t "Ya veo... Con que resulta que te gustan películas de ese tal Smith."
    show aizawa snicker
    k_panic "No, no es así...!"
    show aizawa chortlecenter
    t "No tienes que ocultarlo ... Parece que todas ustedes chicas aman a ese Smith."
    show aizawa schemecenter
    show crowd angry behind aizawa at Rise(0.5, 0.25)
    c "DÉJA DE DECIR LOCURAS!!"
    show crowd angry at Sit(0.25)
    jump a1k1_intro_es
label a1k1_intro_es:
    show aizawa cute
    t "Muy bien... Ahora es mi turno..."
    show aizawa smile
    stop music fadeout 1
    play sound sound_spotlight
    show ambient darken behind aizawa
    show prop spotlight at Appear(0.0, 0.0, 0.0, 0.0)
    nar "un foco?!"
    play music sound_drumroll
    show aizawa awesome
    t "SOY LA GRANDISIMA~!"
    show aizawa evilchuckle
    t "FABULOSA~!"
    show aizawa love
    t "MAGNIFICA~!"
    show aizawa impressed
    t "ASOMBROSA~!"
    show aizawa happy
    t "LEGENDARIA~!"
    show aizawa pleasantdream
    t "{=whispered}y sobre todo...{/=whispered}"
    show aizawa grateful
    t "BELLA~!"
    stop music
    play sound sound_drumtada
    show aizawa squeal at Bounce(1)
    t "PROFESORA AIZAWA!!!"
    play music music_pompous2
    show aizawa smile at MoveTo(0.5, 1.0)
    hide ambient darken
    with dissolve
    hide prop spotlight
    with dissolve
    with Pause(1)
    show snowblossom
    with dissolve
    nar "ella decide plantear una pose dramática demasiado cerca de ti"
    show aizawa genki
    ta "Quiubole!"
    show aizawa smile
    stop music fadeout 2
    hide snowblossom
    with dissolve
    k_weird "ehhh... ah... bien... Mucho gusto conocerla... Profesora Aizawa..."
    queue music [ music_aizawa3, music_aizawa4, music_aizawa5 ]
    show aizawa lecture at MoveTo(0.0, 0.5)
    ta "Adonde se me desapareció La Repre?!"
    show aizawa meditate
    show freya lecture behind aizawa at Rise(1.0, 0.25)
    f "Mi nombre es Freya!!"
    show aizawa complain
    show freya irritated
    ta "Qué me voy a estar acordando de tantos miles de nombres estudiantiles?!"
    show aizawa fatigue
    show freya shout at Bounce(3)
    f "Por lo menos acuerdate de las estudiantes EN TU PROPIA CLASE!!"
    show aizawa chortleleft
    show freya scowl
    ta "¿Pa que? no es como si fuera la maestra de salón."
    show aizawa schemeleft
    show freya annoyed
    show crowd shout behind freya at Rise(0.5, 0.25)
    c "{b}ERES LA MAESTRA DE SALÓN!!{/b}"
    show crowd calm
    show aizawa confuzzled
    ta "¿En serio? Pensé que lo era para clase 2-C...?"
    show aizawa confused
    show crowd angry
    show freya bored
    c "{b}ESTO ES 2-C!!{/b}"
    show crowd calm
    k_unamused "...."
    show aizawa resign
    nar "de repente la idea de salir corriendo de la escuela como que no suena tan malo..."
    show aizawa genki at Laugh(3)
    show freya pout
    ta "jajaja! ¡Oh, no le pongan importancia a esos detallitos....!"
    show aizawa smug
    show freya nag
    f "¿Qué quieres decir con \"esos detallitos\"?!"
    show aizawa awesome
    show freya upset
    ta "Lo que sea ... ¿Oye, ya hicieron la tarea de ayer?"
    show aizawa snide
    show crowd shout
    show freya angry
    c "¿Cual tarea?"
    show crowd calm
    show aizawa evilchuckle
    ta "¡Pues obvío! la tarea para la clase de historia moderna!"
    show aizawa smug
    show freya calm at Bounce(1)
    show freya annoyed
    f "Pero eres nuestra maestre de Inglés!"
    show aizawa dumbfounded at Laugh(2)
    ta "¿Eh? Ara! Como que se me olvido, LOL!"
    show aizawa nervous
    show crowd shout
    show freya tired
    c "NO NOS DIGAS \"LOL\"!"
    show crowd calm
    show aizawa sadistic
    show freya perturbed
    ta "¡Ah! ya dejan de chillar, y entregame la tarea!"
    show crowd angry
    show aizawa revenge
    show freya angry
    c "¿DE QUÉ TAREA ESTÁS HABLANDO?!"
    play countermusic sound_chatter fadein 0.25
    show crowd angry at VChatter
    show aizawa reel at MoveTo(0.25, 0.25)
    show freya defensive at MoveTo(0.75, 0.25)
    $ renpy.pause(0.25)
    show aizawa scream at HChatter(0.25, 0.28)
    show freya shout at HChatter(0.75, 0.72)
    nar "solo querias un primer día normal, pero el caos apenas empezaba"
    show crowd angry at Sit(0.25)
    show aizawa savor at ExitLeft(0.25)
    show freya bloodlust at ExitRight(0.25)
    $ renpy.pause(0.25)
    stop music fadeout 2
    stop countermusic fadeout 0.5
    scene bg cafeteria
    with fade
    outline "Hora de Almuerzo"
    play music music_roughday fadein 2.0
    k_sigh "*suspiro*"
    nar "estás tan agotada, que ni siquiera puedes levantar la comida"
    show freya nervouschuckle at EnterLeft(0.0, 0.5)
    f "Lo siento por ti."
    show freya nervous
    k_nervous "¿Por qué?"
    show freya covet
    f "La Profesora Aizawa..."
    show freya bashful
    menu:
        "Bueno... tienes que admitir que no hay tal como ella...":
            jump a1k1_interesting_es
        "Temés que se escapó de algun asilo...":
            jump a1k1_crazy_es
        "Quiza esta algo loca, pero tiene buen corazón.":
            jump a1k1_nice_es
label a1k1_interesting_es:
    k_sneaky "Es una ... persona interesante..."
    show freya glad
    f "Bueno ... Podríamos decir que ella es ... \"única\""
    show freya smile
    k_sarcastic "Única como bicho raro?"
    show freya cute at Bounce(1)
    f "¡Exactamente!"
    jump a1k1_classified_es
label a1k1_crazy_es:
    k_painful "Está loca!"
    show freya nervouschuckle
    f "Nadie lo pone en duda..."
    jump a1k1_classified_es
label a1k1_nice_es:
    k_genki "Ella me parece como una persona muy agradable."
    show freya omg at Laugh(2)
    f "EN SERÍO?! No te lavaron el cerebro?!"
    show freya nervous
    k_oops "...?"
    jump a1k1_classified_es
label a1k1_classified_es:
    show freya glad
    f "Por cierto..."
    f "¿Te puedo hacer una pregunta?"
    show freya smile
    k_happy "Claro...."
    show freya sarcastic
    f "¿Por qué transferistes aquí, Kana?"
    show freya uneasy
    stop music fadeout 1
    k_sad "...?"
    k_oops "Acaso hay algo malo en esta escuela?"
    $ renpy.pause(1.0)
    show freya bashful
    $ renpy.pause(0.5)
    show freya tender
    $ renpy.pause(0.25)
    show freya love
    f "Oh, no lo digo así.  Nomás tengo curiosidad."
    show freya cute
    f "A todas a las que pregunto siempre tienen historias fascinantes para contarme."
    show freya calm
    play music music_flashback1 fadein 2.0
    k_dream "Ya veo... Bueno..."
    show freya curious at ExitLeft(0.25)
    $ renpy.pause(0.25)
    scene bg flashback1
    with flashbackfade
    k_happy "Mis padres me mandaron aquí porque fueron al extranjero en comisión de servicio,"
    k_sad "...Y no van a poder regresar por mucho tiempo."
    scene bg flashback2
    with flashbackfade
    k_happy "No tengo mas parientes en este país,"
    k_genki "... Así que me dejaron bajo la custodia de la directora ya que ella es vieja amiga de ellos."
    scene bg flashback3
    with flashbackfade
    k_tired "Ahora que lo pienso, no tenía mucho que podía decir al respecto."
    k_happy "Pero aún así..."
    k_dream "Estoy seguro de que tendré un tiempo maravilloso aquí en Camelia!"
    scene bg cafeteria
    with flashbackfade
    show freya sweetdream at EnterLeft(0.0, 0.5)
    f "Aha..."
    k_relieved "¿Y tú, Freya?"
    show freya pleasantdream
    f "Pues mas o menos lo mismo que tú..."
    show freya sweetdream
    stop music
    k_nervous "..."
    play music music_roughday
    k_unamused "En otras palabras, no fue fascinante para nada."
    show freya mock
    f "Tuvo sus momentos."
    show freya snicker
    k_sigh "*suspiro*"
    show freya tender at ExitLeft(0.25)
    $ renpy.pause(0.25)
    stop music fadeout 2
    scene bg classroom
    with fade
    outline "Después de Clases"
    play music music_aizawa4 fadein 2.0
    show aizawa pleasantdream at EnterLeft(0.0, 0.25)
    ta "Bueno chicas, esos todo por hoy."
    show aizawa glad
    ta "Si todavía tienen preguntas, mejor guardenlo para mañan--"
    play sound sound_doorslam
    show aizawa astound
    nar "la puerta se habre de golpe"
    show aizawa amused at MoveTo(1.0, 0.25)
    show miharu grief behind aizawa at EnterLeft(0.0, 0.25)
    u "PERDÓNAME POR LA TARDANZA!  LO SIENTO MUCHO!"
    k_shock "AH! ERES TÚ!"
    show aizawa naive
    show miharu confused
    u "¿Tú ...?"
    u ".... ¿Quien...?"
    show miharu nervous
    show aizawa inquisitive
    k_sneaky "Nos encontramos en la puerta principal, ¿recuerdas?!"
    show miharu wonder
    show aizawa snide
    u "ahhhh...."
    show miharu curious
    show aizawa cool
    u "...."
    show miharu excited at Bounce(1)
    show aizawa evilsmile
    u "¡ah!"
    queue music [ music_aizawa3, music_aizawa4, music_aizawa5 ]
    stop countermusic fadeout 3.0
    show aizawa evilchuckle at Bounce(3)
    show miharu smile
    ta "Ah! con que resulta que son tanitas, ¿eh?"
    show aizawa evilsmile
    k_angry "¡NO!"
    show aizawa grateful
    ta "Entonces, ¿que onda con tanta amistad?"
    show aizawa drunksmile
    k_stare "¿A eso lo llamas ser amistoso?"
    show miharu cute
    show aizawa awesome
    ta "Por cierto .... que bueno que por fin llegaste Miharu, y justo cuando acabamos por el día."
    show miharu sad at Bow(1)
    show aizawa snide
    m "Lo siento..."
    show aizawa genki at Laugh(3)
    ta "¡Jajaja! No te preocupes... Como soy persona agradable, te lo perdono..."
    show crowd angry behind miharu at Rise(0.50, 0.25)
    show miharu happy
    show aizawa smile
    c "QUIÉN ES AGRADABLE?!"
    show crowd angry at Sit(0.25)
    show miharu cute
    show aizawa happy
    ta "Hay después date una vueltesita por la sala de profesores, y recoge los folletos para la lección de hoy."
    show miharu genki at Bow(1)
    show aizawa smile
    m "Muchas gracias! Es usted la mejor, Profesora Aizawa!"
    show miharu smile at ExitLeft(0.25)
    show aizawa squeal at Laugh(3)
    ta "Jajaja!"
    show aizawa savor
    show crowd nervous behind aizawa at Rise(0.50, 0.25)
    c "No puede ser..."
    show crowd nervous at Sit(0.25)
    show aizawa orly
    ta "Ahora si largemonos chicas!  Y no vuelvan a olvidar la tarea!"
    show aizawa snicker at ExitRight(0.25)
    show crowd angry behind aizawa at Rise(0.50, 0.25)
    c "PERO VOLVEMOS A LO MISMO!  ¿DE QUE TAREA HABLAS?!!"
    show freya chide at Rise(0.50, 0.25)
    f "*suspiro* Qué profesora mas problemática tenemos...."
    show crowd calm
    show freya annoyed at Sit(0.25)
    $ renpy.music.set_volume(0.25, 1, channel="music")
    play countermusic sound_chatter fadein 1.0
    show crowd calm at VChatter
    nar "sin la profesora presente en el salón..."
    nar "el ruido de tus compañeras revolviendo sus pertenencias y platicando..."
    nar "suena relajante en comparación"
    stop countermusic fadeout 2.0
    $ renpy.music.set_volume(1, 1, channel="music")
    m "Ah Freya!"
    play countermusic music_miharu3 fadein 3.0
    stop music fadeout 3.0
    show crowd calm at Sit(0.25)
    show miharu happy at EnterLeft(0.0, 0.25)
    show freya cool at EnterRight(1.0, 0.25)
    m "Perdone la molestia de nuevo, pero me puede dejar ver sus notas de hoy?"
    m "La hago un dibujo a cambio..."
    show freya cute
    f "Ah, no tienes que hacer eso... Me alegra que puedo ser de alguna ayuda."
    show miharu genki at Bounce(1)
    show freya calm
    m "Es usted una buena amiga, la mejor que he tenido!"
    show freya curious
    show prop bookworm at Appear(0.15, 0.4, 0.0, 0.0)
    with dissolve
    $ renpy.pause(0.5)
    show miharu relieved
    show freya angry
    m "Es por eso que este dibujo--"
    show prop bookworm at MoveTo(0.8,1.0)
    $ renpy.pause(1.0)
    show freya psycho at Bounce(3)
    show prop bookworm at Fling(0.8, 0.4, -0.30, 0.35, 0.35, 1095)
    $ renpy.pause(0.15)
    show miharu grief at Fling (0.0, 0.0, -1.0, -0.5, 0.5, 790)
    $ renpy.play(sound_collide)
    stop countermusic
    hide prop bookworm
    f "No lo necesito! Nomás ten estas notas!!"
    hide miharu
    queue music [ music_miharu1, music_miharu3 ]
    show freya disturbed
    $ renpy.pause(1.00)
    show freya meditate
    $ renpy.pause(0.50)
    nar "por un momento juras que... nah, estás seguro de que sólo era tu imaginación..."
    show freya glad at Bounce(1)
    f "¡Ah! Por cierto Kana, esta es Miharu. Va ser tu compañera de cuarto en el dormitorio."
    show freya smile at ExitRight(0.25)
    show miharu happybandage at EnterLeft(0.5, 0.5)
    m "Así que es usted la estudiante transferida."
    show miharu uncomfortablebandage
    m "Lo siento mucho por la molestia que la causé esta mañana."
    menu:
        "Que linda, todavía se preocupe de ti.":
            jump a1k1_forget_es
        "Oh no! esta no se escapa de tus garras!":
            jump a1k1_hell_es
label a1k1_forget_es:
    k_relieved "Está bien, ya se me olvido todo ese asunto."
    show miharu relievedbandage
    m "Que persona mas amable es usted..."
    k_genki "Por cierto, es un placer conocerte Miharu."
    jump a1k1_conclusion_es
label a1k1_hell_es:
    play sound sound_thunder
    show lightning
    show miharu dreadbandage
    k_furious "¿Cómo demonios pretendes que me olvide de eso?!"
    hide lightning
    show miharu griefbandage at Bow(1)
    m "Hiyaaaahhhhhh ...!! Perdoooooname ..!!"
    k_scheme "Pero creo que te lo puedo dejar pasar, así que ..."
    show miharu curiousbandage
    k_genki "...Mucho gusto conocerte, Miharu."
    jump a1k1_conclusion_es
label a1k1_conclusion_es:
    show miharu excitedbandage
    m "Encantada de conocerla también, Kana."
    show freya cute at EnterRight(1.0, 0.25)
    show miharu cutebandage
    f "Bueno...."
    f "Creo que es hora de que nos dirigimos al dormitorio."
    show freya calm at ExitRight(0.25)
    show miharu smilebandage at ExitRight(0.5)
    $ renpy.pause(0.5)
    stop music fadeout 3.0
    scene bg dorm
    with introfade
    outline "Dormitorio Camelia"
    play music music_mellow
    scene bg dormhall
    with dissolve
    show freya keen at EnterRight(0.5, 0.75)
    f "Esto es nuestro dormitorio. Todas las estudiantes que asisten a Camelia viven aquí."
    f "En total hay tres pisos, además de un sótano que no podemos entrar..."
    show freya cute at MoveTo(1.0, 0.5)
    f "Tienes el registro, teléfono, cafetería, y espacios de almacenamiento en el primer piso"
    show freya curious at MoveTo(0.0, 0.75)
    f "Y todas nuestras habitaciones, salones, baños y duchas en los dos pisos superiores"
    show freya love at MoveTo(0.5, 0.5)
    f "Hay cuatro camas en cada habitación,"
    f "...Así que tienes que compartirlo con tres otras personas."
    show freya glad at MoveTo(0.0, 0.5)
    f "Tu habitación, #327, es en el tercer piso, dos vueltas a la derecha después de la primera caja de escaleras,"
    show freya smile at MoveTo(0.5, 0.25)
    show miharu smug at EnterLeft(0.0, 0.25)
    f "...Y Miharu aquí es una de tus compañeras de cuarto."
    show freya smile at MoveTo(0.0, 0.25)
    show miharu smile at ExitLeft(0.25)
    $ renpy.pause(0.75)
    show freya keen
    f "¿Alguna pregunta?"
    show freya cool
    menu:
        "¡Ay! Como habla...":
            jump a1k1_enough_es
        "Espera! Otras TRES personas?!!":
            jump a1k1_two_es
label a1k1_enough_es:
    k_nervous "Creo que estoy bien por ahora..."
    show freya glad
    f "Perfecto."
    jump a1k1_fine_es
label a1k1_two_es:
    k_nervous "¿A caso sabes quienes son las otras dos compañeras de mi cuarto?"
    show freya sarcastic
    f "Bueno..."
    f "Son dos estudiantes de último año llamados Reina y Q.U.E.E.N."
    show freya weary
    k_baka "\"Reina\" y \"R.E.I.N.A.\"?  Algo esta raro aquí."
    show freya yearn
    f "Igual pienso yo, pero así son las cosas."
    show freya love
    f "Por cierto, si desea escribir el nombre de Q.U.E.E.N., asegúrate de usar puras letras mayusculas."
    show freya tender
    k_genki "¿Por qué? ¿Ella se cree líder o algo así?"
    $ renpy.pause(0.75)
    show freya suspicious
    f "Créame, es mejor que lo hagas."
    show freya snide
    k_baka "¿Eh?"
    show freya evil
    f "A menos que quieras averiguarlo de la manera difícil...."
    show freya cynical
    k_gasp "...!!"
    $ renpy.pause(1.0)
    jump a1k1_fine_es
label a1k1_fine_es:
    show freya glad
    f "Bueno, si necesitas ayuda o tienes alguna pregunta, o simplemente quieres hacerme una pequeña visita..."
    show freya cute
    f "Seras bienvenida a mi habitación, #156, en el 1er piso."
    show freya calm
    k_happy "Muy bien, gracias!"
    show freya smile at ExitRight(0.75)
    nar "Freya se va, dejandote solo con Miharu"
    k_genki "Bueno, supongo que ya debemos regresar a nuestro cuarto, no?"
    k_smile "...."
    show miharu confused at EnterLeft(0.0, 0.25)
    m "...?"
    k_sarcastic "... Eh ... Bueno, la verdad es que las explicaciones de Freya me dejaron perdida."
    show miharu relieved
    k_waterfall "¿Me puedes llevar allá, por favor?"
    show miharu glad at Bounce(1)
    m "¡Por supuesto! Sígueme..."
    scene bg dormhall1
    with dissolve
    $ renpy.pause(0.25)
    show miharu chibi1 at Bobble(1.15, 0.6, -0.15, 0.6, 0.35, 2.0)
    nar "y la sigues"
    scene bg dormhall2
    with dissolve
    show miharu chibi1 at Bobble(-0.15, 0.0, 1.15, 0.2, 0.25, 3.0)
    nar "pero triste tu decepción, Miharu está igual de perdida"
    scene bg dormhall3
    with dissolve
    show miharu chibi1 at Fling(1.15, 0.7, -0.15, 0.3, 2.00, 365.0)
    nar "siguiendo a la muchacha torpe, te pasas 15 minutos deambulando por los pasillos laberínticos,"
    scene black
    with dissolve
    stop music fadeout 3.0
    nar "...hasta que finalmente lleguan a la habitación"
    scene bg dormroom
    with dissolve
    play music music_quirky
    show miharu genki at EnterLeft(0.0, 0.25)
    m "Ya llegamos!  Cuarto, dulce cuarto!"
    k_swirl "QUE BARBARA!!!  No te metas de guía de turismo!"
    show miharu smile at ExitLeft(0.25)
    nar "quieres tirarte en la cama y descansar, pero no estás segura cual cama es tuya"
    show prop haku at Appear(0.45, 0.2, 0.0, 0.0)
    with dissolve
    nar "aparte de que te distraes con las curiosidades regadas por toda la habitación"
    k_squeal "¡Ah! Que adorable muñeco!"
    k_happy "Tuya?"
    show miharu happy at EnterLeft(0.0, 0.25)
    m "Oh no, eso le pertenece a Q.U.E.E.N."
    k_ehhh "Eh?!!"
    nar "conque resulta que a esta \"Q.U.E.E.N.\" le gusta jugar con muñecas?"
    nar "qué clase de persona es ella?"
    k_sarcastic "Bueno lo que sea. Tengo que desempacar mis cosas..."
    show miharu smile at ExitRight(0.75)
    $ renpy.pause(0.25)
    show prop haku at ExitRight(0.50)
    nar "las dos entran al habitación"
    nar "mientras Miharu está ocupado revisando las notas de Freya, tu empiezas a desempacar tu bolsa"
    nar "después de sacar ropa, retratos y algunas decoraciones,"
    nar "...sacas tu netbook y lo pones sobre tu escritorio."
    show miharu genki at EnterRight(1.0, 0.25)
    m "¡AH! Qué lindo!"
    show miharu worried
    m "Pero esa es la misma bolsa que cayó cuando me encontré con usted?"
    k_genki "Síp"
    show miharu concern
    m "....¿Está bien?"
    k_smile "Mmm?"
    show miharu curious at MoveTo(0.85, 0.25)
    m "La cosita..."
    k_glad "Oh, el netbook? Sí, está bien."
    show prop netbook at Appear(0.5, 0.5, 0.5, 0.5)
    with dissolve
    nar "lo levantas de la mesa y lo volteas con mucha facilidad"
    show miharu wonder
    nar "en realidad no pesa casi nada, pero de todos modos Miharu te mira como si fueras culturista"
    show prop netbook at Shake(0.4, 2)
    k_genki "¿Ves? Ni siquiera un rasguñito."
    show miharu relieved at Bounce(1)
    m "¡Oh! Me alegra escuchar eso!"
    k_happy "Sí, esta computadorsita es bastante fuerte."
    show prop netbook at Heft(0.4, 3)
    show miharu cute
    k_smug "Ya se me a caído como dies veces, pero todavía sigue trabajando!"
    show miharu genki
    m "Increible! Y también el color es taaan bonito!"
    show miharu excited
    m "Debe de haberla costado una fortuna..."
    show miharu cute
    k_happy "Fijate que no. Para éste, creo que pague como... Rp 1,500,000."
    k_relieved "Bastante bien para una computadora, y sé que hay otras aun más baratas."
    show miharu genki at Bounce(1)
    m "Que asombroso! Eso es mucho más barato de lo que me imaginaba!"
    hide prop netbook
    with dissolve
    show miharu smile
    k_smile "jeje..."
    show miharu grief at MoveTo(0.5, 0.25)
    m "Hablando de barato, ahorita estoy pobretona y hambrienta..."
    k_oops "?!"
    show miharu excited at Bounce(4)
    m "... Así que vamos a comer esta noche en el Bombshelter!"
    show miharu cute
    k_nervous ".........\"Bombshelter\"?"
    show miharu happy
    m "Es lo que nosotros llamamos a la cafetería de este dormitorio."
    show miharu cute
    k_weird "Ah... Ya veo... Creo..."
    nar "el día está tan lleno de extrañezas, que más da otra anormalidad?"
    k_nervous "Bueno... Entonces vamos a comer ahí."
    show miharu glad at Bounce(2)
    $ renpy.pause(0.25)
    show miharu smile at ExitLeft(0.5)
    $ renpy.pause(0.5)
    stop music fadeout 3.0
    scene bg bombshelter
    with slowdissolve
    outline "El Bombshelter"
    play music music_bombshelter1 fadein 2.0
    nar "ahora ves por qué le llaman el \"Bombshelter\""
    nar "paredes de concreto, luz pobre, sin ventanas, sillas incómodas, decoración escasa..."
    nar "se ve mas apto para sobrevivir ataques aéreos, que para servir comida"
    nar "con razón los precios eran tan bajos"
    show miharu genki at Rise(0.5, 0.25)
    m "¡Que felicidad! No he comido nada desde la mañana!"
    show miharu smile
    nar "la frase \"El hambre es la mejor especia\" debe ser verdad,"
    play sound sound_thunderstep
    with vpunch
    nar "...porque esto son uno de los peores platillos que has comido en tu vida"
    show reina silhoutte behind miharu at EnterRight(0.7, 2.5)
    play sound sound_thunderstep
    with vpunch
    show ambient darken
    with slowdissolve
    play sound sound_thunderstep
    with vpunch
    nar "pero justo cuando ibas a empezar a burlarte,"
    show miharu wonder
    nar "...te asombras cuando de repente una figura alta se eleva sobre Miharu, y la abraza"
    show reina relievedblush
    show ambient darkenhole
    with dissolve
    u "Miharica! Mucho tiempo desde que te veo!"
    show miharu happy
    show reina tenderblush
    m "Mucho tiempo?"
    show reina relievedblush
    u "Sí, desde la mañana. "
    show reina desire
    u "Pero vale, pa mí es casi como cinco años!"
    hide ambient darkenhole
    show miharu cute
    show reina lovestarved
    k_sigh "Ejem!"
    show reina stare
    k_sarcastic "Perdoneme la pequeñita molestia, pero le podría preguntar quién eres?"
    show reina calm at Bounce(1)
    show reina oppose
    u "Su novia."
    show miharu uncomfortable
    show reina frown
    nar "HUY!  que directa!"
    show miharu genki at Laugh(3)
    show reina lust
    m "Jajaja! ¿Qué quiere decir con eso? Si solo somos compañeras de cuarto."
    show miharu smile
    show reina hentai
    k_nervous "Eh?"
    show miharu happy
    show reina fantasize
    m "Sí, le presento a Reina, nuestra compañera de cuarto."
    show miharu cute
    show reina blush
    k_omg "EHHHH?!"
    show miharu smile at Sit(0.25)
    show reina taunt at MoveTo(0.5, 0.75)
    r "Vale, con que esta chama es la transferida?"
    show reina mock
    r "mmmmm... Se me olvida, es Kana o Hana?"
    play sound sound_wind
    show ambient icy
    with dissolve
    show reina fufufu
    nar "tiemblas ante lo que casi se siente como una fria mirada celosa"
    show reina sinister
    k_nervous "...Kana."
    hide ambient icy
    with dissolve
    show reina reluctant
    r "Vale pues... Kana."
    show reina evil
    r "Soy Reina.  Gusto conocerte."
    show reina smug
    k_nervous "Eh... También es un placer conocerla, Sra. Reina."
    show reina chastise
    r "Prefiero nomás \"Reina\"."
    show reina happydream at MoveTo(0.7, 0.25)
    show miharu calm at Rise(0.5, 0.25)
    nar "y con eso volvió a adular sobre Miharu"
    show reina kawaii
    r "Deseas algún fritanga por hay, Miharica?"
    r "Yo invito."
    show reina kawaiismile
    $ renpy.pause(0.5)
    show miharu genki at Bounce(3)
    show prop foodbubble1 at Appear(0.30, 0.18, 0.5, 0.5)
    show prop foodbubble1 at Heft(0.55, 20)
    m "¡Ah! Que generosa! Muchas gracias, me encantaría un pocito de bihun goreng!"
    hide prop foodbubble1
    show miharu smile
    show reina happy
    r "Cualquier cosica para mi querida!"
    show prop foodbubble2 at Appear(0.25, 0.60, 0.5, 0.5)
    show prop foodbubble2 at Heft(0.55, 20)
    show miharu calm
    show reina smile
    k_genki "En ese caso me podrías traer una plato de nasgor, por favor?"
    show prop foodbubble2 at Fling(0.25, 0.60, -0.5, 0.7, 0.5, 730)
    show miharu worried
    show reina suspicious
    r "No recuerdo haberte preguntado."
    hide prop foodbubble2
    show reina angry
    k_sneaky "Eh?"
    show miharu genki at Laugh(3)
    show reina bashfulleft
    m "Jajaja! ¡Oh, no lo diga así, Reina."
    show miharu glad
    show reina enchanted
    m "La gente le va mal entender por eso, jajaja ..."
    show miharu smile
    show reina awkward
    nar "Miharu piensa que Reina está bromeando, pero se trata de un asunto muy serio para Reina"
    show reina lecherous
    nar "es bastante obvio que tiene su mira fijada en Miharu y en nadie más"
    show reina naughtydream
    nar "si ese es el caso ... te preguntas si ... tal vez ..."
    show miharu confused
    show reina mesmerized
    k_sigh "Está bien, voy a buscar algo de comer por mí misma..."
    show miharu happy at MoveTo(0.0, 0.5)
    show reina embarrassed at Bounce(1)
    m "En ese caso, le acompaño."
    show reina gulp at Bounce(3)
    $ renpy.pause(0.15)
    show reina overprotect at MoveTo(0.15, 0.25)
    show miharu cute
    r "¡ESPERA!"
    show reina tense
    nar "jeje, ya te tengo!"
    show reina awkward
    r "Vale pues, entonces les traigo comida a las dos."
    show miharu genki at Bow(1)
    show reina nervousblush
    m "¿En serio?! Gracias!  Se la agradece muuucho!"
    show miharu smile
    show reina genki
    r "No hay problema, Miharica."
    show ambient reinaglare
    with dissolve
    show reina evil
    nar "la sensación de victoria se quedó corta cuando ves la sonrisa diabolica que te hace Reina"
    nar "sintiendo escalofrío, tienes miedo de la mezcla venenosa que planea traerte"
    hide ambient reinaglare
    show prop foodbubble3 at Appear(0.85, 0.25, 0.5, 0.5)
    show prop foodbubble3 at Heft(0.55, 20)
    show miharu curious
    show reina shock
    ta "Y ya que estas ahí de metiche, traeme una ordén de pollo frito à la Kalasan! Gracias!"
    hide prop foodbubble3
    nar "..........."
    nar "volteas nerviosamente hacia la dirección de la voz desagradable"
    menu:
        "Grita con voz alta ...?":
            jump a1k1_kya_es
        "... o para ensordecer ?":
            jump a1k1_gya_es
label a1k1_kya_es:
    show miharu uncomfortable
    k_swirl "KYAAAA!!"
    show reina huh at Bounce(1)
    r "AAAH?!!"
    show aizawa calm at EnterRight(1.0, 0.25)
    show miharu confused
    show reina chide
    ta "Que reacción más pésima fue esa?!"
    jump a1k1_reaction_es
label a1k1_gya_es:
    show redsiren
    play sound sound_airraidsiren
    show miharu grief
    k_shock "GYAAAAAAAAAAAAAHHH!!!"
    show reina reprimand at Bounce(5)
    r "AAAAAAAAAAAH?!!!"
    show aizawa savor behind redsiren at EnterRight(1.0, 0.25)
    $ renpy.pause(0.25)
    show aizawa squeal at Laugh(2)
    show miharu curious
    show reina ippenshindemiru
    ta "Aja!  Ahora ESA fue una reacción con pasión, LOL!"
    hide redsiren
    stop sound
    jump a1k1_reaction_es
label a1k1_reaction_es:
    show miharu glad at Bow(1)
    show aizawa snide
    show reina frustrated
    m "Buenas noches, Profesora Aizawa."
    show miharu smile
    show aizawa grateful
    ta "¡Ah! Buenas noches, Miharu!"
    show miharu happy
    show aizawa amused
    show reina impatient
    m "¿A qué se debe el gusto de su visita?"
    show miharu cute
    show aizawa cute
    ta "Ah, nomás estoy aquí para gorrearles la cena."
    show aizawa smug
    show miharu confused at ExitLeft(1.00)
    show reina smile at MoveTo(-0.4, 0.75)
    $ renpy.pause(1.25)
    hide miharu
    show reina angry at MoveTo(0.5, 0.15)
    show aizawa baka
    $ renpy.pause(0.25)
    show reina shout at Bounce(3)
    r "Dejate de pichirre, que ya no eres estudiante!  "
    show aizawa complain at Laugh(2)
    show reina angry
    ta "Hijole con esta grosera.... Claro que soy estudiante!"
    show aizawa fatigue
    show reina chastise
    r "{b}ERAS{/b} estudiante..."
    show aizawa meditate
    play sound sound_gong
    show ambient zen behind reina at Appear(0.0, 0.0, 0.0, 0.0)
    with slowdissolve
    show aizawa lecture
    show reina bored
    ta "Mija,... en la Vida, uno nunca cese de ser estudiante."
    show aizawa pity
    show reina calm at Bounce(1)
    show ambient zen behind reina at Fling(0.0, 0.0, 0.0, 2.5, 0.75, 365)
    show reina nag
    r "No seas pantallera!  Te graduaste hace cinco años!  "
    show reina complain
    r "Entonces si quieres comer, PAGA POR EL!"
    hide ambient zen
    show aizawa yelp at Bounce(2)
    show reina chide
    ta "Ay, que malvada eres!"
    show aizawa accuse
    ta "¿Será que a tú altura, la falta de oxigeno te hace sangrona?!"
    show reina blush
    show aizawa stare
    stop music
    r "..."
    show reina shameshiftleft at MoveTo(0.25, 0.5)
    $ renpy.pause(1.0)
    show aizawa revenge
    show reina shameshiftleft at MoveTo(0.15, 0.25)
    $ renpy.pause(0.5)
    show reina shameshiftleft at MoveTo(0.0, 0.25)
    $ renpy.pause(0.75)
    play music music_crazyfight1
    show reina shameleft
    r "Somos... {p}... {p}...{=whispered}de la misma altura....{/=whispered}"
    show aizawa orly at Laugh(4)
    show reina shameright
    ta "jojo! Sí como no... Quiza fue así en el pasado...."
    show aizawa squeal
    show reina furiousblush
    ta "Pero ahora eres tan {b}GRANDOTOTA{/b}..."
    show angrytwitch at Appear(0.4, 0.1, 0.5, 0.5)
    show aizawa evilchuckle
    ta "Que ya eres más alta y guapa que cualquier muchacho que conozco!"
    show aizawa genki at Laugh(4)
    show reina impatient
    ta "jaja! Cuidate mi Principe, o capaz que termino enamorándome de ti, LOL!"
    show aizawa amused
    hide angrytwitch
    $ renpy.pause(2.5)
    show reina taunt at Laugh(3)
    r "jujuju!  Entonces prueba tu suerte, vale..."
    show aizawa astound
    show reina mock
    r "Porque soy lo más cerca que un {b}LEBAY{/b} como tú..."
    show aizawa unamused
    show angrytwitch at Appear(0.9, 0.1, 0.5, 0.5)
    show reina evil
    r "Jamas va tener como novio!"
    show reina winkleft
    r "{b}\"L-O-L\"{/b}"
    show reina smug
    stop music
    hide angrytwitch
    $ renpy.pause(3.0)
    play music music_crazyfight2
    play countermusic sound_catfight fadein 0.25
    show reina scold at MoveTo(0.25, 0.25)
    show aizawa frustrated at MoveTo(0.75, 0.25)
    $ renpy.pause(0.25)
    show reina shout at HChatter(0.25, 0.28)
    show aizawa scream at HChatter(0.75, 0.72)
    ta "¡Me las vas a pagar!"
    $ renpy.pause(2.0)
    nar "por más divertido que fuera ver a las dos pelear,"
    nar "...sabias que alguien las tenia que parar antes de que la mala aura consumiera toda la cafetería"
    stop music
    stop countermusic
    m "Deténganse, por favor!"
    show reina gulp at MoveTo(0.25, 0.25)
    show aizawa confuzzled at MoveTo(0.75, 0.25)
    nar "afortunadamente Miharu interviene por ti..."
    play music music_angelic
    play countermusic sound_bells
    show angelicblossom
    show ambient heaven behind reina
    with slowdissolve
    $ renpy.pause(2.0)
    show reina oops at MoveTo(-0.3, 0.25)
    show aizawa baka at MoveTo(1.0, 0.25)
    $ renpy.pause(0.25)
    show miharu chibi2 behind reina at Appear(0.5, 0.5, 0.5, 0.5)
    with dissolve
    $ renpy.pause(0.5)
    show miharu chibi2 behind reina at Fling(0.5, 0.5, 0.5, 0.20, 20.0, 0.0)
    m "No se permite pelear, ¿de acuerdo? Todos aqui somos seres humanos...."
    m "Hay que llevarse bien unas con otras y crear buenas relaciones...."
    show reina bored
    m "Debido a que no hay beneficio en batallar entre nosotros, ¿verdad?"
    show reina chide
    r "CLARO QUE LO HAY!"
    show aizawa aho
    show reina bored
    show overlay garbage behind miharu at Fling(0.5, -1.0, 0.5, 0.5, 0.25, 0.0)
    $ renpy.pause(0.25)
    show overlay garbage at Appear (0.5, 0.5, 0.5, 0.5)
    play sound sound_thunderstep
    stop music
    stop countermusic
    hide angelicblossom
    show overlay garbage behind miharu at Rattle(0.5, 0.52, 5, 0.05)
    show miharu chibi2 behind reina at QuickFling(0.3, 1.5, 1.2, -115)
    m "nyuuuu...?"
    show aizawa confused
    show overlay garbage at Appear (0.5, 0.5, 0.5, 0.5)
    hide ambient heaven
    hide miharu
    show reina complain
    r "Tendré el gusto de vengarme..."
    show reina scold at Bounce(1)
    r "...Después de que casi me tumba con ese pastel asesino el año pasado!"
    show aizawa moronic
    show reina angry
    play music music_ridiculous fadein 2.0
    show prop blackforest1 behind reina at Appear(0.5, 0.4, 0.5, 0.5)
    with dissolve
    ta "Malagradecida!  Si yo batí y batí para hacértela!"
    show aizawa yelp at Bounce(2)
    show reina threaten
    ta "Trabajé sin parar por tres días!"
    show reina reprimand at Bounce(1)
    show aizawa pity
    r "Y lo dejastes afuera por cuatro, vale!"
    play countermusic sound_poison fadein 2.0
    show prop blackforest2 behind reina
    with slowdissolve
    show aizawa dumbfounded
    show reina pout
    r "Ni te remordió cuando me la enviaste llena de hongos,"
    show reina pout at Bounce(2)
    show aizawa nervous
    r "...Y dijiste que era un nuevo tipo de pastel Black Forest!"
    show miharu excited at EnterLeft (0.2, 0.25)
    show reina mope
    m "Jaja! ¡Ah! Creo que recuerdo eso...!"
    stop countermusic
    hide prop blackforest2
    with dissolve
    show overlay hospital
    with dissolve
    show miharu happy
    show aizawa chastiseright
    show reina hopeless
    m "Todas caímos inconscientes después de comerlo, y tuvimos que estar hospitalizadas por una semana a causa de intoxicación alimentaria..."
    show miharu glad
    show aizawa schemeright
    show reina speechless
    m "Después de eso, la Profesora Aizawa fue conocida como la \"Panadera de la Muerte\"."
    hide overlay hospital
    with dissolve
    show aizawa chortleright at Laugh(2)
    show miharu smile
    show reina impatient
    ta "Ya ya, no es pa tanto!  Ustedes tienen que aguantar un poco de dolor de vez en cuando."
    show aizawa orly
    ta "Así pueden llegar a ser adultas sanas y fuertes como yo, LOL!"
    show aizawa nervous
    stop music
    $ renpy.pause(2.50)
    show reina ippenshindemiru
    r "NO... {p}ME DIGAS... {p}{b}\"LOL\"!!!!{/b}"
    play music music_crazyfight3 fadein 1.0
    play countermusic sound_war fadein 2.0
    show miharu grief at Sit(0.25)
    show reina scold at MoveTo(0.25, 0.25)
    show aizawa shock at MoveTo(0.75, 0.25)
    $ renpy.pause(0.25)
    show reina shout at HChatter(0.25, 0.28)
    show aizawa scream at HChatter(0.75, 0.72)
    $ renpy.pause(2.0)
    nar "*suspiro* ...honestamente puedes ver por qué Reina estaria enojada"
    hide miharu
    show ambient fire behind reina
    with dissolve
    nar "pero ahora la pelea se estaba intensificando..."
    show crowd calm behind ambient
    with dissolve
    nar "y dentro de poco, todas las estudiantes de la cafetería se juntarian para ver el espectáculo"
    k_unamused "¡Uf! Por favor, dejen esto ya! Es vergonzoso!"
    show miharu nervous behind aizawa at EnterLeft (0.5, 0.25)
    $ renpy.pause(0.25)
    show miharu dread behind aizawa at HChatter(0.5, 0.52)
    m "Paren, por favor!"
    show miharu grief at QuickFling (-1.0, -0.5, 0.5, 550)
    show prop chair behind crowd at Appear(0.1, 0.8, 0.5, 0.5)
    show prop chair behind crowd at SetPosition(0.2, -45.0)
    show prop chair behind crowd at SendTo(0.1, 0.45, 1.0)
    nar "pero solo seguían peleando...  parecía que nada podría detenerlas ahora..."
    hide miharu
    show angrytwitch at Appear(0.15, 0.35, 0.5, 0.5)
    u "{b}¿Vosotros no escucháis a Miharu?!{/b}"
    u "{b}Pará esta pavada INMEDIATAMENTE!!!{/b}"
    hide angrytwitch
    hide prop chair
    show prop chair behind ambient at Appear(0.1, 0.45, 0.5, 0.5)
    show prop chair behind ambient at SetPosition(0.2, -45.0)
    show prop chair behind ambient at BackgroundFling(0.5, 0.3, 1.0, 655, 1.0)
    $ renpy.pause(1.0)
    stop music
    stop countermusic
    $ renpy.play(sound_collide)
    show reina shock at QuickFling (-0.2, -1.5, 0.5, 550)
    show aizawa aho at QuickFling (1.2, -1.5, 0.5, 550)
    $ renpy.pause(0.15)
    hide prop chair
    show crowd nervous
    nar "te sorprende la voz retumbante, al igual que la silla masiva que fue lanzada desde la multitud"
    hide reina
    hide aizawa
    show reina fuss behind crowd at SetPosition(0.2, 0.0)
    show reina fuss behind crowd at Fling(0.6, -1.0, 0.6, 0.8, 1.0, 655)
    $ renpy.pause(0.25)
    show aizawa cry behind crowd at SetPosition(0.2, 0.0)
    show aizawa cry behind crowd at Fling(0.8, -1.0, 0.8, 0.8, 1.0, 655)
    $ renpy.pause(1.25)
    hide ambient fire
    with dissolve
    show queen frown behind crowd at Appear(0.1, 0.8, 0.5, 0.5)
    show queen frown behind crowd at SetPosition(0.2, 0.0)
    show queen frown behind crowd at SendTo(0.1, 0.5, 1.0)
    $ renpy.pause(1.00)
    show queen frown behind crowd at Bobble(0.1, 0.5, 0.4, 0.5, 0.4, 1.0)
    $ renpy.pause(1.0)
    show queen frown behind crow at SendTo(0.4, 0.5, 0.0)
    nar "después de que regresa la calma, una estudiante de aspecto refinado se acerca hacia ellas"
    show angrytwitch at Appear(0.35, 0.35, 0.5, 0.5)
    u "Ah, que bien, che... ustedes no tienen nada mejor que hacer que arruinar mi comida..."
    hide angrytwitch
    u "Lo unico que queria era un poco de paz y tranquilidad mientras disfrutaba de este manjar, che..."
    u "*suspiro* Pero ahora ustedes... especialmente vos, Profesora Aizawa..."
    show aizawa complain behind crowd at SendTo(0.8, 0.5, 0.15)
    ta "¡¿PUES QUE TRAEN CONMIGO?!"
    show aizawa complain behind crowd at SendTo(0.8, 0.8, 0.25)
    u "...llegan como unos tarados para arruinarlo todo, che."
    hide reina
    hide aizawa
    show queen frown behind crowd at Heft(0.45, 3)
    u "Ahora les toca una paliza!"
    nar "para evitar ser involucrado en esta nueva drama, hablas en voz baja con Miharu..."
    k_sarcastic "{=whispered}¿Tambíen es ella una de las víctimas del Black Forest?{/=whispered}"
    show miharu concern at EnterLeft(0.0, 0.25)
    m "{=whispered}Sí...{/=whispered}"
    show miharu doubt
    k_sneaky "{=whispered}Me lo imaginaba. ¿Quién es? {/=whispered}"
    show miharu concern
    m "{=whispered}Q.U.E.E.N.{/=whispered}"
    show miharu doubt
    k_dream "{=whispered}Ah, Q.U.E.E.N.... Q.U.E.E.N..... {/=whispered}"
    show miharu dread
    k_omg "{b}.....EHHHHH?!!!{/b}"
    show queen frown behind crowd at Heft(0.45, 1)
    $ renpy.pause(0.25)
    show queen frown behind crowd at ExitRight(0.5)
    play music music_queen1 fadein 4.0
    nar "sin querer, tu grito interrumpe los regaños de Q.U.E.E.N."
    hide queen
    show queen lecture at EnterRight(1.0, 0.25)
    show miharu nervous at MoveTo(-0.3, 0.25)
    q "Quien se atreve?"
    show queen frown
    nar "...temés lo peor cuando de repente se da vuelta Q.U.E.E.N. para confrontar su agresor"
    nar "afortunadamente, otra voz de la multitud viene a salvarte del peligro"
    show freya berate at EnterLeft(0.0, 0.25)
    f "Por favor no armés un escandalo, Q.U.E.E.N!"
    show freya glare
    k_incredulous "Freya!  También estás aquí!"
    show freya irked
    f "Por supuesto, toda las chicas del dormitorio vienen a cenar aquí."
    show freya troubled
    show queen bored
    nar "Todas?  Tacañas..."
    show freya fury at MoveTo(0.5, 0.25)
    $ renpy.pause(0.25)
    show freya shout at Bounce(4)
    $ renpy.pause(0.5)
    show miharu confused at MoveTo(0.0, 1.0)
    f "{b}Ya vuelven a sus asientos chicas, que se termino la fiesta!  No hay nada mas que ver aquí!{/b}"
    show freya irritated
    hide crowd nervous
    with dissolve
    nar "la multitud deja escapar un quejido colectivo, antes de regresar a lo que estaban haciendo"
    show freya obligated at Sit (0.25)
    $ renpy.pause(1.0)
    show freya reprimand at Rise(0.5, 0.25)
    show aizawa aho at Rise(0.7, 0.25)
    $ renpy.pause(0.25)
    show miharu cute
    show queen frown
    f "Y Profesora Aizawa, no sé cuántos veces te tengo que decir esto,"
    show freya scold at Bounce(1)
    show aizawa confused
    f "...Pero puedes hacernos el favor de regresar a tu casa?!"
    show freya shout at Bounce(3)
    show aizawa confuzzled
    f "Deja de actuar como niña, y sé buen ejemplo para todas las estudiantes!"
    show miharu smile
    show aizawa cry
    show freya irritated
    ta "Pero no he pagado la renta, así que no tengo adonde regresar..."
    show aizawa weep
    show freya lecture
    show queen calm
    f "¿No recibiste ya el salario de este mes?"
    show aizawa whimper
    show freya irritated
    ta "Oh, claro que sí, nunca se tardan en pagarme."
    show aizawa aho
    show freya leer
    ta "Pero... como te lo pondré... quizá me aloque un poquitito cuando salí de compras..."
    show miharu uncomfortable
    show queen bored
    ta "...Y cuando me di cuenta, me quedé sin quinto."
    show aizawa orly at Laugh(8)
    show freya angry
    show queen boredleft
    ta "Jaja! Ahora mi renta está con tres meses de retraso, LOL!"
    show aizawa nervous
    stop music
    play sound sound_deadsilence
    show miharu nervous
    nar "Profesora Aizawa recibió unos bien merecidos segundos de silencio incómodo"
    play music music_ridiculous fadein 5.0
    show freya defensive
    k_unamused "¿En serio?"
    show reina chide behind miharu at EnterLeft(-0.4, 0.25)
    r "Que tontería..."
    show miharu sad at Bow(1)
    show reina leer
    m "Pobre Profesora--"
    show queen chideleft at Bounce(1)
    show miharu dread
    q "Que boluda."
    show aizawa calm at Laugh(3)
    show miharu confused
    show aizawa genki
    show freya annoyed
    show reina angry
    show queen boredleft
    ta "Jaja! ¡Lo sé! La directora me dijo lo mismo cuando le conté todo!"
    show aizawa happy
    ta "Por eso me dio permiso de vivir aquí por un tiempesito."
    show miharu nervous
    show aizawa megasigh
    show freya evildream
    show angrytwitch at Appear(0.47, 0.18, 0.5, 0.5)
    show reina scowl
    show queen stareleft
    ta "*suspiro* Si solo no fuera tan tacaña,"
    show aizawa pleasantdream at Laugh(2)
    show reina chastise
    show queen stareright
    ta "...así me hubiera prestado una de sus mansiones, o por lo menos un apartamentito por hay..."
    show reina speechless
    show aizawa sweetdream
    hide angrytwitch
    $ renpy.pause(2.0)
    show freya psycho at Bounce(6)
    show miharu sigh
    show aizawa gasp
    f "{b}NO TIENES VERGÜENZA!!!{/b}"
    show aizawa cry
    play sound sound_stomachgrowl
    show freya shock
    show reina shock
    show queen stareleft
    $ renpy.pause(0.75)
    show miharu uncomfortable at Bounce(1)
    show freya surprised
    show queen meditate
    m "¡Ah! Hablando de eso..."
    show miharu grief at Bounce(2)
    show aizawa weep
    show reina gulp
    m "Todavía no he conseguido mi bihun!"
    show freya complain at MoveTo(0.35, 0.25)
    show miharu dread
    show reina embarrassed
    f "QUÉ TIENE QUE VER UNO CON EL OTRO?!"
    show reina awkward at Bounce(1)
    show aizawa whimper
    show freya bored
    r "AY! Perdón que estuve papando moscas, vale!"
    show miharu sad
    show aizawa weep
    show reina nervousblush
    m "Nyuuuu...."
    show miharu doubt
    show aizawa whimper
    show reina shoo
    r "Ahoritica te lo traigo..."
    show aizawa weep
    show reina shoofrown at ExitLeft(0.5)
    show prop foodbubble4 at Appear(0.65, 0.5, 0.5, 0.5)
    show prop foodbubble4 at Heft(0.55, 20)
    show freya sigh
    show queen mumble
    q "Che, no te olvidés de mi <arroz frito>. Y lo quiero al estilo istimewa!"
    show aizawa whimper
    show reina huh at EnterLeft(-0.4, 0.25)
    hide prop foodbubble4
    show miharu confused
    show queen meditate
    r "¿Cuándo te~? Uf~! Está bien!"
    show prop foodbubble5 at Appear(0.5, 0.45, 0.5, 0.5)
    show prop foodbubble5 at Heft(0.55, 20)
    show aizawa tearsofjoy at Laugh(2)
    show miharu uncomfortable
    show freya perturbed
    show reina furious
    ta "Y tambíen mi Kalasan, porfis! jeje!"
    show prop foodbubble5 at QuickFling(1.5, 0.3, 0.5, 365)
    show reina reprimand at Bounce(3)
    show miharu nervous
    show aizawa moronic
    show freya perplexed
    show queen calm
    r "{b}¡CÁLLATE! VETE A COMPRÁRTELO!!!{/b}"
    show aizawa cry at Bow(1)
    show miharu smile
    show freya irked
    show reina furious
    ta "Hauu.... *lloriquear*"
    show aizawa whimper
    show reina impatient at ExitLeft(0.25)
    show freya mocksideways
    nar "Reina salio corriendo, dejandote pensando si acaso se acordará de tu orden"
    show miharu smile at ExitLeft(0.25)
    show aizawa weep at Sit(0.25)
    show freya mocksideways at ExitRight(0.25)
    show queen calm at ExitRight(0.25)
    $ renpy.pause(0.25)
    stop music fadeout 3.0
    scene bg dormroom
    with dissolve
    outline "REGRESO A LA HABITACÍON"
    play music music_quirky
    show miharu genki at Rise(0.0, 1.0)
    m "Ah~! Que llena estoy...!"
    show miharu smile at VChatter
    k_painful "Obviamente!"
    show miharu glad at ExitLeft(0.25)
    $ renpy.pause(0.25)
    show prop nasgor at Appear(0.5, 0.5, 0.5, 0.5)
    with dissolve
    nar "Reina siempre si se acordó de tu nasi goreng y no parecía que tenía nada malo"
    show prop nasgormini
    with dissolve
    nar "pero la porción era tal que sólo te duró tres mordidas"
    nar "lo bueno que ya habías comido algo para ese entonces"
    hide prop nasgormini
    with dissolve
    show bihun1 at Appear(0.2, 0.5, 0.5, 0.5)
    with quickdissolve
    show bihun2 at Appear (0.35, 0.5, 0.5, 0.5)
    with quickdissolve
    show bihun3 at Appear (0.5, 0.5, 0.5, 0.5)
    with quickdissolve
    show bihun4 at Appear (0.65, 0.5, 0.5, 0.5)
    with quickdissolve
    show bihun5 at Appear (0.8, 0.5, 0.5, 0.5)
    with quickdissolve
    nar "por otra parte, a Miharu le tocó una banquete de casi diez platos de bihun goreng,"
    show miharu chibi3 at Bobble(-0.15, 0.5, 1.15, 0.5, 0.35, 2.5)
    $ renpy.pause(0.2)
    hide bihun1
    with quickdissolve
    $ renpy.pause(0.2)
    hide bihun2
    with quickdissolve
    $ renpy.pause(0.2)
    hide bihun3
    with quickdissolve
    $ renpy.pause(0.2)
    hide bihun4
    with quickdissolve
    $ renpy.pause(0.2)
    hide bihun5
    with quickdissolve
    nar "...y te impresiono ver como las devoró todos!"
    nar "\"¿Qué tipo de metabolismo tiene esta chica?!\", te preguntas"
    hide miharu
    show queen talk at EnterRight(1.0, 0.25)
    q "Si no mal recuerdo, vos sos Hana, ¿no?"
    show queen calm
    k_nervous "Eh,... en realidad es Kana..."
    show queen talk
    q "Che, lamento el retraso, pero es un placer conocerte."
    show queen calm
    stop music fadeout 2.0
    menu:
        "Actuá casualmente.":
            jump a1k1_nice1_es
        "Nomás siguele la corriente.":
            jump a1k1_hermajesty_es
label a1k1_nice1_es:
    play music music_queen1
    k_glad "¡Ah!"
    k_genki "¡Igualmente! Estoy encantada de conocerla, Q.U.E.E.N."
    show queen mumble at Laugh(1)
    q "Veo que deletreás bien mi nombre. Che, que diligente que sos!"
    jump a1k1_question_es
label a1k1_hermajesty_es:
    play music music_royalty
    k_dream "*reverencia* El honor y placer es todo mía, Su Alteza."
    show queen mumble at Laugh(3)
    q "¡Oh-jojo! Que graciosa!"
    show queen rebuke
    q "Pero aunque yo sea una <reina>, me re molesta que me llamen cualquier otra cosa."
    show queen annoyed
    k_nervous "Oh... Perdón..."
    show queen mumble at Laugh(2)
    q "¡jojo! Se entiende, che. Vos sos nueva así que ya fue."
    show queen comment
    q "Pero sólo esta vez...."
    show queen stare
    k_gasp "?!! "
    k_nervous "jeje, eh...."
    jump a1k1_question_es
label a1k1_question_es:
    show queen calm
    k_happy "Le importa si le hago una pregunta?"
    show queen talk
    q "Por supuesto."
    show queen calm
    k_glad "¿Este apodo \"Q.U.E.E.N.\" es su nombre verdadero...?"
    show queen chide
    q "Lo es para vos."
    show queen bored
    nar "\"eso ni siquiera respondió mi pregunta!\", te imaginás diciendo"
    show miharu genki at EnterLeft(0.0, 0.25)
    show queen stareleft
    m "Clarinetes! Q.U.E.E.N. es Q.U.E.E.N.!"
    show miharu glad at Laugh(2)
    m "No hay ni un dudita de eso, jeje!"
    stop music fadeout 2.0
    show queen stareright at ExitRight(0.5)
    show miharu doubt at MoveTo(-0.3, 1.0)
    nar "mientras Q.U.E.E.N. se distrae, Miharu te lleva a una esquina y te susurra..."
    show miharu concern
    m "{=whispered}No pregunte eso, o el muñeco le va traer una maldición....{/=whispered}"
    show miharu doubt
    k_ehhh "{=whispered}Que? {/=whispered}"
    show miharu concern
    m "{=whispered}Haku, su muñeco favorito. {/=whispered}"
    show miharu dread
    m "{=whispered}No es cualquier muñeco de peluche, es para vudú....{/=whispered}"
    play music music_haku
    menu:
        "Sí, sobre todo...":
            jump a1k1_kidding_es
        "¡Oh no! más gente espeluznante!":
            jump a1k1_scary_es
label a1k1_kidding_es:
    show ambient haunted behind miharu
    with slowdissolve
    show miharu nervous
    k_sarcastic "{=whispered}Ahora lo he visto todo...{/=whispered}"
    show hauntedtwirl behind miharu
    with dissolve
    show miharu confused
    m "{=whispered}Lo digo en serio! {/=whispered}"
    show creepyqueenhaku behind miharu
    with dissolve
    show miharu dread
    m "{=whispered}Su nombre completo es SHI NO HAKUSHAKU!{/=whispered}"
    m "{=whispered}Eso quiere decir el \"Conde de la Muerte\"!{/=whispered}"
    show miharu nervous
    k_sneaky "{=whispered}Como~?!!{/=whispered}"
    jump a1k1_proof_es
label a1k1_scary_es:
    k_incredulous "{=whispered}¡HUY!! QUE ESPANTOSO~!!!{/=whispered}"
    show miharu worried
    m "{=whispered}¿Verdad?{/=whispered}"
    jump a1k1_proof_es
label a1k1_proof_es:
    show miharu dread
    m "{=whispered}Y Reina tiene prueba de su poder~{/=whispered}"
    k_panic "{b}REINA?!!{/b}"
    hide ambient haunted
    hide hauntedtwirl
    hide creepyqueenhaku
    show queen hakuchideleft at EnterRight(1.0, 0.5)
    show miharu nervous
    q "De que hablan a espaldas mio, chicas?"
    show miharu uncomfortable at MoveTo(0.0, 0.25)
    show queen hakuboredleft
    m "¡Oh, no, de nada~!"
    show miharu whimper
    k_nervous "¡jaja! Eh,.. sí, nada. ¿Que le dio esa idea?"
    show queen hakuannoyed at Bounce(1)
    show miharu doubt
    q "Bah!"
    stop music fadeout 1.0
    play sound sound_doorslam
    $ renpy.pause(0.5)
    nar "justo en ese momento, Reina entra con fuerza por la puerta"
    play music music_reina1 fadein 2.0
    queue music [ music_reina2, music_reina1 ]
    show miharu cute
    nar "por una vez esta noche, estás feliz de verla"
    show reina relieved behind miharu at EnterLeft(0.5, 0.5)
    show miharu happy
    show queen hakucalm
    r "Épale, que ya llegué!"
    show miharu genki at Laugh(2)
    show reina tenderblush
    m "Bienvenida a casa, jiji!"
    show reina coo at MoveTo(0.1, 0.25)
    show miharu cute
    r "Miharica querida, me extrañabas~?!"
    show queen hakustareleft
    nar "como si adulando a Miharu durante la cena entera no era suficiente,"
    show miharu smile at ExitLeft(0.75)
    show reina hentai at ExitLeft(0.75)
    nar "...ahora pretendíá continuar los besos y abrazos aquí en el cuarto"
    show lotsoflove
    nar "solo esperas que esto no durará toda la noche..."
    show queen hakustare
    k_nervous "Reina está... un poco obsesionada con Miharu, ¿no?"
    show queen hakucomment
    q "La verdad no deberia importarme."
    q "...Pero si, che, podrias decir que el asunto es asi."
    show queen hakuboredleft at MoveTo(0.7, 1.0)
    nar "quieres preguntarle algo más, pero ella dirige su atención hacia la \"pareja\""
    show queen hakuchideleft at Bounce(2)
    q "No me gusta interrumpir, pero por qué llegás tan tarde, Rei?!"
    hide lotsoflove
    show reina complain at EnterLeft(-0.4, 0.25)
    show queen hakuboredleft
    r "Estuve lavando platos por supuesto. Hoy soy parte del servicio de limpieza, vale."
    show reina threaten at Bounce(6)
    r "*mirada* Y tenía que fajar doble para cubrir a ti!!"
    show queen hakucommentleft at Laugh(1)
    show reina furious
    q "Ah, ya veo! Te agradezco, che. Podes continuar..."
    show reina suspicious at Bounce(3)
    show queen hakustareleft
    r "*quejido*"
    show miharu sigh at EnterLeft(0.0, 0.5)
    show reina curious
    show queen hakucalm
    m "*bostezo* Se está haciendo un poquito tarde. Debemos ir a dormir pronto."
    show reina yawn at Bow(1)
    show miharu tired
    r "Cierto vale, que estoy exhausta después de todo eso... *bostezo*"
    show queen hakumumble at Bounce(1)
    show reina tired
    q "Entonces ni hablar, nos vamos todas a la cama ahora!"
    show reina sleepy at ExitLeft(0.5)
    show miharu sigh at ExitLeft(0.5)
    show queen hakumeditate at ExitRight(0.5)
    $ renpy.pause(0.5)
    stop music fadeout 3.0
    scene black
    with dissolve
    nar "aunque no era tan inmediata como pensabas, todos están cepillados, en pijama, y en la cama en tan sólo unos minutos"
    nar "incluyendo a tí"
    scene bg dormroom2
    with dissolve
    q "Que duerman bien!"
    m "Muchas gracias Q.U.E.E.N.! Que sueñen con los angelitos!"
    r "Buenas noches, sólo pa mi Miharica!"
    q "Che, y a mi no me deseás una buena noche?"
    r "No, te puede ir mal, vale."
    q "Tonta."
    k_genki "Buenas noches a todos! Fue muy divertido conocerlas hoy!"
    m "Fue un placer conocerla también! Nos vemos en la mañana!"
    r "Te levantas tempranica!  O te tiramos con toda y cama!"
    q "Tal vez."
    k_nervous "jeje... eh, tratare lo mejor..."
    nar "Reina y Q.U.E.E.N. se voltean de lado y caen a dormir casi luego"
    nar "Miharu se extiende para apagar la lámpara"
    play sound sound_lightswitch
    scene bg dormroom3
    nar "y es sólo en la oscuridad profunda del cuarto..."
    nar "...que se da cuenta del esplendor del netbook que estás usando en la cama"
    play music music_calm1 fadein 5.0
    m "¡Oh! ¿no se va ir a dormir?"
    k_smile "Dentro de poco. Sólo tengo que acabar unas cositas que me faltan."
    m "Bueno...  Por favor no se duerme muy tarde. Buenas noches..."
    k_relieved "Que descanses..."
    nar "en pocos segundos, Miharu también se duerme"
    show prop unr1 at DissolveAppear(0.09, 0.3, 0.0, 0.0, 0.5)
    show overlay netbook at DissolveAppear(0.03, 0.2, 0.0, 0.0, 0.5)
    nar "estás agradecida que el teclado y trackpad del netbook son silenciosos"
    show prop unr2
    with quickdissolve
    nar "así puedes escribir y navegar el Internet sin despertar a nadie"
    show prop unr3
    with quickdissolve
    nar "te pones a leer las noticias del día, proyectos en que estás involucrada,"
    show prop unr5
    with quickdissolve
    nar "nuevas obras de arte, juegos y música,"
    show prop unr4
    with quickdissolve
    nar "...y otras paginas web que visitas regularmente"
    show prop unr6
    with quickdissolve
    stop music fadeout 3.0
    nar "abres tu correo web y encuentras sólo unos pocos mensajes de respuesta rápida"
    play music music_netbook1 fadein 5.0
    scene bg email1
    with dissolve
    nar "con la lista de recibidos despejado, nomás te queda componer un solo mensaje..."
    nvl clear
    nvl show dissolve
    play countermusic sound_typing
    net "<Kerida Cyllia...>"
    net "<Tuve mi primera clase hoy, y ¡HOCHALE! Parecía ke me habían jalado a otra dimensión, LOL!>"
    net "<Tengo una maestra tan chiflada ke parece haber escapado de un asilo!>"
    net "<Y sigo tropezándome con pura tipa rara o loca! jeje!>"
    net "<Es mas, estoy compartiendo cuarto con TRES DE ELLAS, LOL!!!> ^^;"
    net "<Pero aún así ... Kiero seguir pensando positivamente.>"
    net "<Kizá después de ke las conozca un poco más, me van a caer muy bien.>"
    net "<O si no, hay me volveran igual de loca, jaja...!> ^___^'"
    stop music fadeout 3.0
    net "<Bueno, eso es todo por hoy. Te diré más acerca de ellas en otro tiempesito.>"
    net "<Mañana va ser bien importante para mi, entonces hay deseame suerte, porfis!> ^^"
    nvl hide nodissolve
    show ambient darken
    $ mouse_visible = False
    play music music_ED1a fadein 25.0
    queue music [ music_ED1b, music_silence ]
    $ floatingtext1 = Text("<Buenas noches...!>\n\n...\n\n<LOL! Se me olvida ke es día por allá!>\n<En ese caso, ke tengas buen día!> ^____^\n\n<Saludos y abrasos,>\nKana-chan ^____^v\n\n\nPD:\n<....Como siempre, disculpa mi pesímo ingles.> ^^;", slow=True, slow_speed=10, style="emailed")
    $ renpy.show("mytext1", [Position(xpos=0.1, ypos=0.1, xanchor=0.0, yanchor=0.0)], what=floatingtext1)
    $ ui.pausebehavior(3.0)
    $ ui.interact ()
    $ renpy.pause(17.0)
    stop countermusic
    scene white
    with videofade_in
    show ED1_1
    show ED1_2
    show ED1_3
    show ED1_4
    show ED1_5
    $ renpy.pause(74.75)
    stop music
    $ renpy.pause(1.0)
    show konobangumiwa_1
    $ renpy.pause(0.25)
    play music music_konobangumiwa2
    show konobangumiwa_2
    $ renpy.pause(10.25)
    show kanagoodbye
    stop music
    $ renpy.pause(3.0)
    $ mouse_visible = True
    scene black
    $ renpy.pause(1.0)
    
