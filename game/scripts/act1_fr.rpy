# fr
# Act 1 starts here.
init:
    # Declare language-specific characters used by this game.
    if persistent.lang == "french":
        $ classroom = "Salle de classe"
        $ teacher = "Professeur"
        $ unknown = "Inconnu"
label a1k1_start_fr:
    scene black
    play music music_netbook1
    $ renpy.pause(1.0)
    scene bg sunrise
    with introfade
    nvl clear
    nvl show dissolve
    play countermusic sound_typing
    net "<Chère Cyllia...>"
    net "<Je suis enfin arrivée au lycée pour filles Camelia...>"
    net "À partir d'aujourd'hui, je vais aller en pensionnat comme mes parents l'ont voulu..."
    nvl hide dissolve
    stop countermusic
    scene bg academy
    with fade
    k_happy "Ah ! Si seulement tu pouvais sentir l'air frais du matin ici..."
    k_relieved "Et regarder la splendeur du lever de soleil..."
    k_genki "Je suis impatiente de voir les histoires qui vont m'arriver ici--"
    stop music
    $ renpy.play(sound_collide)
    with vpunch
    nar "Il semblerait que quelqu'un vient tout juste de te percuter..."
    nar "... Et tu tombes par terre"
    show miharu grief at Fling(-0.5, 0.35, 1.5, 1.5, 1.0, 730.0)
    u "Hiyaaaah!!"
    nar "Mais elle aussi..."
    play music music_miharu1
    menu:
        "Tu vas bien, elle s'est peut-être bléssée ...":
            jump a1k1_okay_fr
        "Écervelée, regarde où tu vas !":
            jump a1k1_eyes_fr
        "Héhé, elle a l'air étourdie. Faisons-lui une farce.":
            jump a1k2_bone_fr
label a1k1_okay_fr:
    k_worried "Aïe... Ah ! Tu vas bien ?"
    show miharu whimper at Rise(0.5, 1.0)
    u "Je suis vraiment désolée. Ça va, merci, et toi ?"
    k_relieved "Je vais bien aussi."
    show miharu relieved
    u "Je suis rassurée."
    show miharu uncomfortable at Bounce(1)
    u "Ah ! Zut ! Je vais être en retard !"
    show miharu smile
    u "Désolée, mais je dois y aller, donc..."
    show miharu genki at ExitLeft(0.75)
    u "À PLUS~!"
    k_nervous "Hein ?"
    jump a1k1_who_fr
label a1k1_eyes_fr:
    k_furious "Hé ! T'es aveugle où quoi ?"
    show miharu grief at Rise(0.5, 0.25)
    u "HIYAAAHHH~!! JE SUIS DÉSOLÉE !!"
    show miharu uncomfortable at Bounce(1)
    u "Ah ! Zut ! Je vais être en retard !"
    show miharu nervous
    u "Encore désolée, mais je dois y aller... Sinon..."
    show miharu grief at ExitLeft(0.5)
    u "À PLUSSSSSSSSSSS !!!"
    k_shout "Hé ! REVIENS ICI TOUT DE SUITE !"
    k_stare "...."
    k_unamused "....Ah.... Elle est déjà partie...."
    jump a1k1_who_fr
label a1k2_bone_fr:
    k_sneaky "AAAH !!! MA JAMBE !!! ELLE EST CASSÉE !! JE ME CONTORSIONNE DE DOULEUR !!!"
    show miharu grief at Rise(0.5, 0.5)
    u "Gyaaaah !! Qu'est-ce que je viens donc de faire ?!!!"
    show miharu dread at Bounce(2)
    u "Je dois appeller l'hopital~! Vite l'hopital~ !"
    k_genki "Hé.... Je plaisantais."
    show miharu grief at Bounce(1)
    u "AH ! JE VAIS AUSSI ÊTRE EN RETARD !"
    show miharu confused at Bounce(2)
    u "Qu'est-ce que je dois faire~ ? Qu'est-ce que je dois faire~ ?"
    k_weird "Hé.... Tu m'écoutes ?"
    show miharu whimper
    u "Oui.....*larmes*"
    k_smug "Désolée... Mais je ne faisais que plaisanter..."
    show miharu grief at Bounce(4)
    u "MAIS NON ! TA JAMBE EST CASSÉE À CAUSE DE MOI !!"
    k_ehhh "Hein ?!"
    show miharu cautious at Bow(1)
    u "Je te jure d'en prendre l'entière responsabilité ! Mais après être allée au boulot..."
    k_weird "Euuuuh.... Si tu veux...."
    show miharu uncomfortable
    u "Éssaie de trouver quelqu'un pour t'emmener à l'hopital...!"
    show miharu whimper at ExitLeft(0.75)
    u "À plus !"
    k_gasp "AH--!"
    k_unamused "..."
    k_sarcastic "On appelle pas ça un \"Délit de fuite\”"
    jump a1k1_who_fr
label a1k1_who_fr:
    k_sigh "…."
    show miharu smile at RunInDistance(-0.5, 1.5, 0.6, 0.75)
    nar "Elle s'enfuit de la cour de l'école."
    nar "Mais qui était cette fille ? Vous vous demandez."
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
    t "Écoutez !"
    t "Comme je l'ai dit hier, nous avons une nouvelle élève transférée qui nous joindra à partir d'aujourd'hui."
    show aizawa grateful
    t "Viens, mademoiselle la transférée ! Présente-toi !"
    show aizawa smile at ExitLeft(1.0)
    nar "Tu t'avances dans la salle, essayant de ne pas être nerveuse face aux regards."
    k_happy "Bonjour tout le monde... Je m'appelle Kana."
    k_genki "Enchantée de faire votre connaissance..."
    show crowd nervous behind aizawa at Rise(0.50, 0.50)
    c "{=whispered}Enchanté de faire ta connaissance....{/=whispered}"
    show crowd nervous at Sit(0.75)
    nar "C'est moi ou ils avaient l'air ennuyés ?"
    show aizawa sigh at EnterLeft(0.0, 0.5)
    t "*pfff*"
    show aizawa resign
    t "Quelle présentation banale..."
    show aizawa fatigue
    stop music
    k_nervous "Hein ?!"
    nar "Tu entends la classe murmurer : \"ahhh... ça recommence...\""
    show aizawa chastisecenter
    t "Où est ta PASSION, Hana ?! Ton manque de PASSION me dérange...!"
    show aizawa sadistic
    t "REFAIS-LA !!"
    show aizawa revenge
    play music music_aizawa2
    k_omg "HEEEIN ?!!!"
    k_nervous "...."
    k_genki "C'est une blague ?"
    show aizawa reprimand at Bounce(2)
    t "Pas du tout !"
    show aizawa maniac
    t "MAINTENANT REFAIS-LA OU SINON !!!"
    show aizawa astound at ExitLeft(0.25)
    k_swirl "GYAAHHHH~!! D'ACCORD ! D'ACCORD !"
    k_nervous "ehem...."
    menu:
        "Joue juste la sécurité...":
            jump a1k1_hana_fr
        "Elle veut de la passion ? DONNE LUI EN !!!!":
            jump a1k1_sama_fr
        "Oh ! Sors-lui ce qui te viens à la tête...":
            jump a1k1_legend_fr
label a1k1_hana_fr:
    k_genki "Je m'appelle Kana, pas Hana."
    stop music
    play sound sound_deadsilence
    c "{=whispered}*........ Silence..........*{/=whispered}"
    nar "Tu penses que ça suffit."
    show aizawa chortlecenter at EnterLeft(0.0, 0.75)
    t "Ok..."
    show aizawa schemecenter
    k_panic "C'EST TOUT ?"
    jump a1k1_intro_fr
label a1k1_sama_fr:
    stop music
    k_creepy "{=whispered}fufufu...{/=whispered}"
    play music music_pompous1
    k_evil "JE SUIS LA GRANDE, VÉNÉRABLE ET TOUTE-PUISSANTE KANA !"
    k_villainous "INCLINEZ-VOUS DEVANT MOI, MORTELS~ !"
    stop music
    play sound sound_deadsilence
    c "{=whispered}*........ Silence..........*{/=whispered}"
    nar "\"Elle me fait pitié...\", disent tes camarades entre eux."
    nar "C'est embarassant..."
    play music music_aizawa2
    show aizawa obsessed at EnterLeft(0.0, 0.25)
    t "BRAVO !"
    show aizawa love
    t "QUELLE MAGNIFIQUE INTRODUCTION ! JE SUIS SI HEUREUSE !"
    show aizawa tearsofpride
    k_ehhh "DE QUOI ?"
    show aizawa squeal
    t "Toi je t'aime déjà, soeurette !"
    show aizawa savor
    k_waterfall "Mais c'est quoi ce lycée ?"
    k_angry "Et je suis pas votre soeur !"
    show aizawa sweetdream
    nar "Tu remarques que le professeur ne fait plus attention à toi."
    jump a1k1_intro_fr
label a1k1_legend_fr:
    k_squeal "Je suis une légende !"
    stop music
    play sound sound_embarrass
    c "*........ Gémissements..........*"
    nar "\"Raah pourquoi j'ai dit la première CONNERIE qui me venait à la tête ?\", te dis-tu"
    show aizawa orly at EnterLeft(0.0, 1.0)
    t "Je vois.... Tu aimes regarder les films de mr Smith."
    show aizawa snicker
    k_panic "C'est pas ça...!"
    show aizawa chortlecenter
    t "Aaah, pas besoin d'en avoir honte... Toutes les jeunes ont l'air d'aimer ce gars."
    show aizawa schemecenter
    show crowd angry behind aizawa at Rise(0.5, 0.25)
    c "ARRÊTEZ DE DIRE N'IMPORTE QUOI !"
    show crowd angry at Sit(0.25)
    jump a1k1_intro_fr
label a1k1_intro_fr:
    show aizawa cute
    t "Très bien... Je devrais donc me présenter..."
    show aizawa smile
    stop music fadeout 1
    play sound sound_spotlight
    show ambient darken behind aizawa
    show prop spotlight at Appear(0.0, 0.0, 0.0, 0.0)
    nar "Un projecteur ?"
    play music sound_drumroll
    show aizawa awesome
    t "JE SUIS LA GRANDE~ !"
    show aizawa evilchuckle
    t "FABULEUSE~ !"
    show aizawa love
    t "MAGNIFIQUE~ !"
    show aizawa impressed
    t "INSPIRANT LA CRAINTE~ !"
    show aizawa happy
    t "LA LÉGENDAIRE~ !"
    show aizawa pleasantdream
    t "{=whispered}Et surtout...{/=whispered}"
    show aizawa grateful
    t "LA BELLE~ !"
    stop music
    play sound sound_drumtada
    show aizawa squeal at Bounce(1)
    t "PROFESSEUR AIZAWA !"
    play music music_pompous2
    show aizawa smile at MoveTo(0.5, 1.0)
    hide ambient darken
    with dissolve
    hide prop spotlight
    with dissolve
    with Pause(1)
    show snowblossom
    with dissolve
    nar "Elle prend une pose devant toi, un peu trop près."
    show aizawa genki
    ta "Enchantée de faire ta connaissance !"
    show aizawa smile
    stop music fadeout 2
    hide snowblossom
    with dissolve
    k_weird "Euuh.... Ah.... D'accord.... Enchantée.... Mademoiselle Aizawa...."
    queue music [ music_aizawa3, music_aizawa4, music_aizawa5 ]
    show aizawa lecture at MoveTo(0.0, 0.5)
    ta "DÉLÉGUÉE DE CLASSE, LEVEZ-VOUS !"
    show aizawa meditate
    show freya lecture behind aizawa at Rise(1.0, 0.25)
    f "Je m'appelle Freya !"
    show aizawa complain
    show freya irritated
    ta "Vous savez, c'est dur de se souvenir du nom de mille élèves."
    show aizawa fatigue
    show freya shout at Bounce(3)
    f "Rappellez-vous au moins des noms des élèves DE VOTRE CLASSE !"
    show aizawa chortleleft
    show freya scowl
    ta "Je suis pas votre professeur principal, donc j'ai pas à m'en inquiéter...."
    show aizawa schemeleft
    show freya annoyed
    show crowd shout behind freya at Rise(0.5, 0.25)
    c "VOUS {b}ÊTES{/b} NOTRE PROFESSEUR PRINCIPAL !"
    show crowd calm
    show aizawa confuzzled
    ta "Vraiment ? Je pensais être le professeur principal de la 1ère C...?"
    show aizawa confused
    show crowd angry
    show freya bored
    c "CECI {b}EST{/b} LA 1ère C !"
    show crowd calm
    k_unamused "...."
    show aizawa resign
    nar "Fuir de l'école ne me paraît pas être une si mauvaise idée..."
    show aizawa genki at Laugh(3)
    show freya pout
    ta "Hahaha ! Laissons les petits détails de côtés..."
    show aizawa smug
    show freya nag
    f "Que voulez-vous dire par \"petits détails\" ?"
    show aizawa awesome
    show freya upset
    ta "Peu importe... Avez-vous fait vos devoirs pour aujourd'hui ?"
    show aizawa snide
    show crowd shout
    show freya angry
    c "Quels devoirs ?"
    show crowd calm
    show aizawa evilchuckle
    ta "Mais, les devoirs d'Histoire Moderne bien sûr."
    show aizawa smug
    show freya calm at Bounce(1)
    show freya annoyed
    f "Mais vous êtes notre professeur d'Anglais."
    show aizawa dumbfounded at Laugh(2)
    ta "Quoi ? Ah ! J'ai oublié LOL !"
    show aizawa nervous
    show crowd shout
    show freya tired
    c "PAS DE \"LOL\" !"
    show crowd calm
    show aizawa sadistic
    show freya perturbed
    ta "Oh ! Commencez à ramasser les devoirs."
    show crowd angry
    show aizawa revenge
    show freya angry
    c "COMME NOUS L'AVONS DIT, VOUS PARLEZ DE QUELS DEVOIRS ?"
    play countermusic sound_chatter fadein 0.25
    show crowd angry at VChatter
    show aizawa reel at MoveTo(0.25, 0.25)
    show freya defensive at MoveTo(0.75, 0.25)
    $ renpy.pause(0.25)
    show aizawa scream at HChatter(0.25, 0.28)
    show freya shout at HChatter(0.75, 0.72)
    nar "Tu avais espéré un premier jour d'école normal, mais ce chaos n'est que le commencement."
    show crowd angry at Sit(0.25)
    show aizawa savor at ExitLeft(0.25)
    show freya bloodlust at ExitRight(0.25)
    $ renpy.pause(0.25)
    stop music fadeout 2
    stop countermusic fadeout 0.5
    scene bg cafeteria
    with fade
    outline "L'heure de manger"
    play music music_roughday fadein 2.0
    k_sigh "*Pffff*"
    nar "Tu es épuisée, tu n'arrives même pas à transporter la nourriture à ta bouche"
    show freya nervouschuckle at EnterLeft(0.0, 0.5)
    f "Je suis désolée pour toi."
    show freya nervous
    k_nervous "Pourquoi ?"
    show freya covet
    f "Mademoiselle Aizawa...."
    show freya bashful
    menu:
        "Bon, il est vrai qu'elle est bizarre...":
            jump a1k1_interesting_fr
        "Tu te demandes si elle n'est pas sortie d'un asile psychiatrique...":
            jump a1k1_crazy_fr
        "Elle peut paraître bizarre, mais elle a dans le fond un grand coeur.":
            jump a1k1_nice_fr
label a1k1_interesting_fr:
    k_sneaky "Elle est... intéressante..."
    show freya glad
    f "Hé bien... On peut dire qu'elle est... \"unique\"."
    show freya smile
    k_sarcastic "Unique comme un animal rare ?"
    show freya cute at Bounce(1)
    f "Exactement !"
    jump a1k1_classified_fr
label a1k1_crazy_fr:
    k_painful "Elle est folle !"
    show freya nervouschuckle
    f "Elle l'est...."
    jump a1k1_classified_fr
label a1k1_nice_fr:
    k_genki "Je pense que c'est une personne très gentille."
    show freya omg at Laugh(2)
    f "HAAA ! TU T'ES FAIT LOBOTOMISER ?"
    show freya nervous
    k_oops "... ?"
    jump a1k1_classified_fr
label a1k1_classified_fr:
    show freya glad
    f "Au fait...."
    f "Je peux te poser une question ?"
    show freya smile
    k_happy "Vas-y..."
    show freya sarcastic
    f "Pourquoi on t'a transféré ici, Kana ?"
    show freya uneasy
    stop music fadeout 1
    k_sad "... ?"
    k_oops "Il y a quelque chose qui cloche dans cette école ?"
    $ renpy.pause(1.0)
    show freya bashful
    $ renpy.pause(0.5)
    show freya tender
    $ renpy.pause(0.25)
    show freya love
    f "Oh, Je me posais juste la question. Je suis curieuse."
    show freya cute
    f "Toutes les personnes à qui je pose la question ont des histoires fascinantes à raconter à ce propos."
    show freya calm
    play music music_flashback1 fadein 2.0
    k_dream "Je vois... Bien...."
    show freya curious at ExitLeft(0.25)
    $ renpy.pause(0.25)
    scene bg flashback1
    with flashbackfade
    k_happy "Mes parents m'ont envoyé ici car ils sont partis à l'étranger pour leur boulot,"
    k_sad "...et ils ne reviendront pas avant longtemps."
    scene bg flashback2
    with flashbackfade
    k_happy "Je ne connais personne ici,"
    k_genki "... Ils m'ont envoyé ici, car la directrice est une de leurs vieilles amies."
    scene bg flashback3
    with flashbackfade
    k_tired "En y repensant, je n'ai pas grand chose à dire d'autre."
    k_happy "Mais..."
    k_dream "Je suis sûre que je vais me plaire ici, à Camelia !"
    scene bg cafeteria
    with flashbackfade
    show freya sweetdream at EnterLeft(0.0, 0.5)
    f "*Approuve*"
    k_relieved "Et toi, Freya ?"
    show freya pleasantdream
    f "Je suis un peu comme toi..."
    show freya sweetdream
    stop music
    k_nervous "..."
    play music music_roughday
    k_unamused "En d'autre mots, c'est pas très trépidant."
    show freya mock
    f "Elle a eu ses moments."
    show freya snicker
    k_sigh "*Pfff*"
    show freya tender at ExitLeft(0.25)
    $ renpy.pause(0.25)
    stop music fadeout 2
    scene bg classroom
    with fade
    outline "Après l'école"
    play music music_aizawa4 fadein 2.0
    show aizawa pleasantdream at EnterLeft(0.0, 0.25)
    ta "Bon, je crois que c'est tout pour aujourd'hui."
    show aizawa glad
    ta "Si vous avez des questions, gardez les en tête pour le cours suiv--"
    play sound sound_doorslam
    show aizawa astound
    nar "La porte s'ouvre dans un vacarme"
    show aizawa amused at MoveTo(1.0, 0.25)
    show miharu grief behind aizawa at EnterLeft(0.0, 0.25)
    u "DÉSOLÉE, JE SUIS EN RETARD ! VRAIMENT DÉSOLÉE !"
    k_shock "AH ! TOI !"
    show aizawa naive
    show miharu confused
    u "Toi... ?"
    u "..... Qui.....?"
    show miharu nervous
    show aizawa inquisitive
    k_sneaky "On s'est \"rencontrées\" devant la porte de l'école, tu te souviens ?"
    show miharu wonder
    show aizawa snide
    u "Ahhhh...."
    show miharu curious
    show aizawa cool
    u "...."
    show miharu excited at Bounce(1)
    show aizawa evilsmile
    u "Ah !"
    queue music [ music_aizawa3, music_aizawa4, music_aizawa5 ]
    stop countermusic fadeout 3.0
    show aizawa evilchuckle at Bounce(3)
    show miharu smile
    ta "Je vois, vous vous connaissiez déjà avant... ?"
    show aizawa evilsmile
    k_angry "NON !"
    show aizawa grateful
    ta "Alors c'était quoi cette attitude amicale ?"
    show aizawa drunksmile
    k_stare "Vous appellez ça \"amicale\" ?"
    show miharu cute
    show aizawa awesome
    ta "À propos.... Tu es finalement arrivée, Miharu, mais la journée est terminée."
    show miharu sad at Bow(1)
    show aizawa snide
    m "Je suis désolée..."
    show aizawa genki at Laugh(3)
    ta "Hahaha ! Il n'y a pas de problème... Je suis tellement gentille, je te pardonne déjà..."
    show crowd angry behind miharu at Rise(0.50, 0.25)
    show miharu happy
    show aizawa smile
    c "QUI EST GENTILLE ?"
    show crowd angry at Sit(0.25)
    show miharu cute
    show aizawa happy
    ta "Tu pourras t'arrêter tout à l'heure à la salle des professeurs pour prendre un polycopié de la leçon d'aujourd'hui."
    show miharu genki at Bow(1)
    show aizawa smile
    m "Merci beaucoup ! Vous êtes la meilleure, Mademoiselle Aizawa !"
    show miharu smile at ExitLeft(0.25)
    show aizawa squeal at Laugh(3)
    ta "Hahaha !"
    show aizawa savor
    show crowd nervous behind aizawa at Rise(0.50, 0.25)
    c "C'est une blague..."
    show crowd nervous at Sit(0.25)
    show aizawa orly
    ta "Bien, c'est tout ! N'oubliez pas de faire vos devoirs cette fois !"
    show aizawa snicker at ExitRight(0.25)
    show crowd angry behind aizawa at Rise(0.50, 0.25)
    c "VOUS NOUS EN AVEZ DONNÉ AUCUN !"
    show freya chide at Rise(0.50, 0.25)
    f "*Pfff* Quel pénible professeur nous avons là.... "
    show crowd calm
    show freya annoyed at Sit(0.25)
    $ renpy.music.set_volume(0.25, 1, channel="music")
    play countermusic sound_chatter fadein 1.0
    show crowd calm at VChatter
    nar "Avec le professeur parti de la classe..."
    nar "Le son animé des bavardages de tes camarades..."
    nar "... Te semblent paisibles en comparaison."
    stop countermusic fadeout 2.0
    $ renpy.music.set_volume(1, 1, channel="music")
    m "Ah Freya !"
    play countermusic music_miharu3 fadein 3.0
    stop music fadeout 3.0
    show crowd calm at Sit(0.25)
    show miharu happy at EnterLeft(0.0, 0.25)
    show freya cool at EnterRight(1.0, 0.25)
    m "Désolée de te déranger à nouveau, mais est-ce que je peux regarder tes cours ?"
    m "Je te dessinnerai un truc en échange..."
    show freya cute
    f "Ah, pas besoin... Je suis contente de t'aider."
    show miharu genki at Bounce(1)
    show freya calm
    m "Tu es tellement gentille, la meilleure amie que j'ai jamais eue !"
    show freya curious
    show prop bookworm at Appear(0.15, 0.4, 0.0, 0.0)
    with dissolve
    $ renpy.pause(0.5)
    show miharu relieved
    show freya angry
    m "C'est pourquoi ce dessin--"
    show prop bookworm at MoveTo(0.8,1.0)
    $ renpy.pause(1.0)
    show freya psycho at Bounce(3)
    show prop bookworm at Fling(0.8, 0.4, -0.30, 0.35, 0.35, 1095)
    $ renpy.pause(0.15)
    show miharu grief at Fling (0.0, 0.0, -1.0, -0.5, 0.5, 790)
    $ renpy.play(sound_collide)
    stop countermusic
    hide prop bookworm
    f "J'en ai pas besoin ! Prend juste les notes pour l'instant !!!"
    hide miharu
    queue music [ music_miharu1, music_miharu3 ]
    show freya disturbed
    $ renpy.pause(1.00)
    show freya meditate
    $ renpy.pause(0.50)
    nar "Tu réfléchis ... Ah, ce doit être ton imagination..."
    show freya glad at Bounce(1)
    f "Ah ! Pendant que j'y pense, Kana, elle, c'est Miharu. Elle va être dans la même chambre que toi."
    show freya smile at ExitRight(0.25)
    show miharu happybandage at EnterLeft(0.5, 0.5)
    m "Donc c'est elle la transférée."
    show miharu uncomfortablebandage
    m "Désolée pour les problèmes que je t'ai causé ce matin."
    menu:
        "C'est mignon, elle continue à se soucier de toi.":
            jump a1k1_forget_fr
        "Oh non ! Elle va pas s'en tirer aussi facilement !":
            jump a1k1_hell_fr
label a1k1_forget_fr:
    k_relieved "C'est bon, j'ai déjà oublié."
    show miharu relievedbandage
    m "Comme tu es gentille ..."
    k_genki "Au fait, enchantée de te rencontrer Miharu."
    jump a1k1_conclusion_fr
label a1k1_hell_fr:
    play sound sound_thunder
    show lightning
    show miharu dreadbandage
    k_furious "COMMENT j'aurais pu oublier ÇA ?!"
    hide lightning
    show miharu griefbandage at Bow(1)
    m "Hiyaaaahhhhhh...!! Désolééééé..!!"
    k_scheme "Bon, je crois que je vais passer l'éponge, donc..."
    show miharu curiousbandage
    k_genki "... Ravie de faire ta connaissance Miharu."
    jump a1k1_conclusion_fr
label a1k1_conclusion_fr:
    show miharu excitedbandage
    m "Moi de même, Kana."
    show freya cute at EnterRight(1.0, 0.25)
    show miharu cutebandage
    f "Bien...."
    f "Je crois qu'il est temps d'aller aux dortoirs."
    show freya calm at ExitRight(0.25)
    show miharu smilebandage at ExitRight(0.5)
    $ renpy.pause(0.5)
    stop music fadeout 3.0
    scene bg dorm
    with introfade
    outline "Dortoir Camelia"
    play music music_mellow
    scene bg dormhall
    with dissolve
    show freya keen at EnterRight(0.5, 0.75)
    f "C'est notre dortoir. Toutes les étudiantes de Camelia y habitent."
    f "Il y a 3 étages dans ce dortoir,  plus un sous-sol mais on ne peut pas y aller..."
    show freya cute at MoveTo(1.0, 0.5)
    f "Au premier étage il y a le registre, le téléphone, la caféteria, et un espace de stockage."
    show freya curious at MoveTo(0.0, 0.75)
    f "Nos chambres, salons, salles de bains et douches sont au deuxième étage."
    show freya love at MoveTo(0.5, 0.5)
    f "Il y a quatre lits par chambre,"
    f "... Donc tu vas devoir partager ta chambre avec trois autres personnes."
    show freya glad at MoveTo(0.0, 0.5)
    f "Ta chambre, la #327, est au troisième étage, tourne deux fois à droite après la cage d'escalier,"
    show freya smile at MoveTo(0.5, 0.25)
    show miharu smug at EnterLeft(0.0, 0.25)
    f "...Et Miharu ici présente est une de tes camarades de chambre."
    show freya smile at MoveTo(0.0, 0.25)
    show miharu smile at ExitLeft(0.25)
    $ renpy.pause(0.75)
    show freya keen
    f "Des questions ?"
    show freya cool
    menu:
        "Wouah ! Elle parle énormément...":
            jump a1k1_enough_fr
        "Attends ! TROIS autres personnes ?!!":
            jump a1k1_two_fr
label a1k1_enough_fr:
    k_nervous "Je pense que c'est tout pour pour aujourd'hui..."
    show freya glad
    f "Bien."
    jump a1k1_fine_fr
label a1k1_two_fr:
    k_nervous "Sais-tu qui sont les deux autres personnes ?"
    show freya sarcastic
    f "Hé bien..."
    f "Ce sont deux ainées nommées Reina et Q.U.E.E.N."
    show freya weary
    k_baka "<Queen> ? C'est un prénom ça ?"
    show freya yearn
    f "Maintenant oui."
    show freya love
    f "Au fait, si tu écrit son nom, tu dois l'écrire en majuscules."
    show freya tender
    k_genki "Pourquoi ? C'est une sorte de leader ?"
    $ renpy.pause(0.75)
    show freya suspicious
    f "Crois-moi, fais-le."
    show freya snide
    k_baka "Hein ?"
    show freya evil
    f "Sauf si tu veux en subir les conséquences...."
    show freya cynical
    k_gasp "...!!"
    $ renpy.pause(1.0)
    jump a1k1_fine_fr
label a1k1_fine_fr:
    show freya glad
    f "Bon, si tu as besoin d'aide, si tu as d'autres questions, ou si tu veux juste me rendre visite..."
    show freya cute
    f "N'hésite pas à aller à ma chambre, la n°156 au 1ème étage."
    show freya calm
    k_happy "Ok, merci !"
    show freya smile at ExitRight(0.75)
    nar "Freya part"
    k_genki "Hé bien, je pense qu'il est temps de retourner à nos chambres respectives."
    k_smile "…"
    show miharu confused at EnterLeft(0.0, 0.25)
    m "… ?"
    k_sarcastic "... Euh... Ok, je ne me rapelle plus de ce que Freya m'a dit."
    show miharu relieved
    k_waterfall "Montre-moi le chemin s'il-te-plaît."
    show miharu glad at Bounce(1)
    m "Bien sûr ! Suis-moi...    "
    scene bg dormhall1
    with dissolve
    $ renpy.pause(0.25)
    show miharu chibi1 at Bobble(1.15, 0.6, -0.15, 0.6, 0.35, 2.0)
    nar "C'est ce que tu fais"
    scene bg dormhall2
    with dissolve
    show miharu chibi1 at Bobble(-0.15, 0.0, 1.15, 0.2, 0.25, 3.0)
    nar "mais sans que cela ne te surprenne, Miharu semble s'être perdue"
    scene bg dormhall3
    with dissolve
    show miharu chibi1 at Fling(1.15, 0.7, -0.15, 0.3, 2.00, 365.0)
    nar "en suivant cette fille bizarre, tu passes 15 minutes à marcher dans les couloirs sans fin,"
    scene black
    with dissolve
    stop music fadeout 3.0
    nar "...jusqu'à arriver à ta chambre"
    scene bg dormroom
    with dissolve
    play music music_quirky
    show miharu genki at EnterLeft(0.0, 0.25)
    m "On y est !"
    k_swirl "ARG !!! Ne deviens jamais guide !"
    show miharu smile at ExitLeft(0.25)
    nar "tu veux t'aplatir sur ton lit et te reposer, mais tu ne sais pas lequel est le tien"
    show prop haku at Appear(0.45, 0.2, 0.0, 0.0)
    with dissolve
    nar "de plus, tu vois que cette chambre contient plein de choses intéressantes"
    k_squeal "Ah ! Elle est mignonne cette poupée !"
    k_happy "La tienne ?"
    show miharu happy at EnterLeft(0.0, 0.25)
    m "Ah non, elle est à Q.U.E.E.N."
    k_ehhh "Hein ?!!"
    nar "Donc cette fameuse \"Q.U.E.E.N.\" aime jouer avec des poupées ?"
    nar "Quel genre de fille est-ce donc ?"
    k_sarcastic "Hum peu importe. Laisse-moi t'installer tes affaires...."
    show miharu smile at ExitRight(0.75)
    $ renpy.pause(0.25)
    show prop haku at ExitRight(0.50)
    nar "vous entrez toutes les deux dans la pièce"
    nar "pendant que Miharu lit ses cours, tu commences à déplier tes bagages"
    nar "Après avoir sorti tes vêtements, photos et décorations,"
    nar "... Tu prends ton ordinateur portable et l'installes sur le bureau."
    show miharu genki at EnterRight(1.0, 0.25)
    m "Wouah ! C'est mignon !"
    show miharu worried
    m "Mais c'est le même sac que celui que tu portais quand je te suis rentrée dedans, non ?"
    k_genki "Ouais."
    show miharu concern
    m ".... Tout est ok ?"
    k_smile "Mmm ?"
    show miharu curious at MoveTo(0.85, 0.25)
    m "Ce machin..."
    k_glad "Oh, l'ordinateur ? Nan, aucun problème."
    show prop netbook at Appear(0.5, 0.5, 0.5, 0.5)
    with dissolve
    nar "tu le  lèves et le tournes avec une facilitée déconcertante"
    show miharu wonder
    nar "il est très léger, mais Miharu te regarde comme si tu avais une force herculéenne    "
    show prop netbook at Shake(0.4, 2)
    k_genki "Tu vois ? Pas une seule égratinure."
    show miharu relieved at Bounce(1)
    m "Oh ! Je suis contente de l'entendre."
    k_happy "Ouais, ce petit-là est très costaud."
    show prop netbook at Heft(0.4, 3)
    show miharu cute
    k_smug "Je l'ai déjà fait tomber une dizaine de fois et il marche encore !"
    show miharu genki
    m "Pas mal ! Et la couleur est trooop jolie !"
    show miharu excited
    m "Il a dû coûter une fortune..."
    show miharu cute
    k_happy ""
    k_relieved "Pas vraiment. Pour celui là je crois avoir dépensé environs ... 1 500 000 Rp"
    show miharu genki at Bounce(1)
    m "Incroyable ! Je le pensais plus cher !"
    hide prop netbook
    with dissolve
    show miharu smile
    k_smile "héhé ..."
    show miharu grief at MoveTo(0.5, 0.25)
    m "En parlant de choses pas très chères, je suis sale, pauvre et affamée..."
    k_oops "?!"
    show miharu excited at Bounce(4)
    m "... Donc allons manger au Bombshelter ce soir !"
    show miharu cute
    k_nervous ".........\"Bombshelter\"?"
    show miharu happy
    m "On appelle la caféteria du campus comme ça."
    show miharu cute
    k_weird "Hum... D'accord...."
    nar "la journée ayant déjà eu son lot de bizarreries, plus rien ne peut te surprendre"
    k_nervous "Allons.... Allons-y alors."
    show miharu glad at Bounce(2)
    $ renpy.pause(0.25)
    show miharu smile at ExitLeft(0.5)
    $ renpy.pause(0.5)
    stop music fadeout 3.0
    scene bg bombshelter
    with slowdissolve
    outline "Le Bombshelter"
    play music music_bombshelter1 fadein 2.0
    nar "Tu comprend alors pourquoi il s'appelle le \"Bombshelter\""
    nar "murs de béton, faible éclairage, pas de fenêtres, des chaises inconfortables, décorations clairsemées"
    nar "ça ressemble plus à un abri anti-nucléaire qu'à une caféteria"
    nar "pas étonnant que la nourriture soit si bon marché..."
    show miharu genki at Rise(0.5, 0.25)
    m "Je suis si contente ! J'ai rien mangé depuis ce matin !"
    show miharu smile
    nar "Le dicton \"Le meilleur prix est la faim\" doit être vrai,"
    play sound sound_thunderstep
    with vpunch
    nar "... Parce que c'est la nourriture la plus dégueulasse qu'il t'a été donné de manger dans toute ta vie"
    show reina silhoutte behind miharu at EnterRight(0.7, 2.5)
    play sound sound_thunderstep
    with vpunch
    show ambient darken
    with slowdissolve
    play sound sound_thunderstep
    with vpunch
    nar "mais juste avant de parler de ça en s'amusant,"
    show miharu wonder
    nar "... Tu es choquée de voir une grande silouhette apparaitre soudainement pour enlacer Miharu"
    show reina relievedblush
    show ambient darkenhole
    with dissolve
    u "Ma chère Miharu ! Ça faisait si longtemps !"
    show miharu happy
    show reina tenderblush
    m "Si \"longtemps\"?"
    show reina relievedblush
    u "Oui, depuis ce matin."
    show reina desire
    u "Mais pour moi ça a été comme 5 ans sans te voir..."
    hide ambient darkenhole
    show miharu cute
    show reina lovestarved
    k_sigh "Aheum !"
    show reina stare
    k_sarcastic "Désolée de vous déranger, mais je peux savoir qui vous êtes ?"
    show reina calm at Bounce(1)
    show reina oppose
    u "Son amante."
    show miharu uncomfortable
    show reina frown
    nar "OUCH ! comment elle l'a balancé !"
    show miharu genki at Laugh(3)
    show reina lust
    m "Hahaha ! Pourquoi dis-tu \"amante\"?  On est juste camarades de chambre et amies."
    show miharu smile
    show reina hentai
    k_nervous "Hein ?"
    show miharu happy
    show reina fantasize
    m "Oui, c'est Reina, une des colocataires."
    show miharu cute
    show reina blush
    k_omg "DE QUOI ?!"
    show miharu smile at Sit(0.25)
    show reina taunt at MoveTo(0.5, 0.75)
    r "Je vois... Donc c'est elle la transférée."
    show reina mock
    r "mmmmmh... C'est Kana ou Hana ?"
    play sound sound_wind
    show ambient icy
    with dissolve
    show reina fufufu
    nar "Tu frissonne, sentant comme un regard jaloux peser sur toi"
    show reina sinister
    k_nervous "... Kana."
    hide ambient icy
    with dissolve
    show reina reluctant
    r "Ah oui... Kana."
    show reina evil
    r "Je suis Reina. Enchantée de faire ta connaissance."
    show reina smug
    k_nervous "Euh... Moi de même... Mon ainée Reina."
    show reina chastise
    r "Juste \"Reina\", ça me va....     "
    show reina happydream at MoveTo(0.7, 0.25)
    show miharu calm at Rise(0.5, 0.25)
    nar "et ainsi elle retourne idolâtrer Miharu"
    show reina kawaii
    r "Alors, que veux-tu manger, ma chère Miharu ?"
    r "Mon gâteau..."
    show reina kawaiismile
    $ renpy.pause(0.5)
    show miharu genki at Bounce(3)
    show prop foodbubble1 at Appear(0.30, 0.18, 0.5, 0.5)
    show prop foodbubble1 at Heft(0.55, 20)
    m "Ah, comme c'est gentil !  Merci, j'aimerais du bihun goreng !"
    hide prop foodbubble1
    show miharu smile
    show reina happy
    r "Quelque chose pour toi ?"
    show prop foodbubble2 at Appear(0.25, 0.60, 0.5, 0.5)
    show prop foodbubble2 at Heft(0.55, 20)
    show miharu calm
    show reina smile
    k_genki "Heu je prendrais du nasgor, s'il-te-plaît."
    show prop foodbubble2 at Fling(0.25, 0.60, -0.5, 0.7, 0.5, 730)
    show miharu worried
    show reina suspicious
    r "Je t'ai rien demandé toi."
    hide prop foodbubble2
    show reina angry
    k_sneaky "hein ?"
    show miharu genki at Laugh(3)
    show reina bashfulleft
    m "Hahaha ! Oh, on ne dit pas ça comme ça, Reina."
    show miharu glad
    show reina enchanted
    m "On ne comprendrait pas ce que tu veux dire, hahaha..."
    show miharu smile
    show reina awkward
    nar "Miharu pense que Reina rigole, mais pour elle c'est serieux."
    show reina lecherous
    nar "c'est assez évident qu'elle a des vues sur Miharu"
    show reina naughtydream
    nar "si c'est le cas... Alors... Peut-être..."
    show miharu confused
    show reina mesmerized
    k_sigh "C'est pas grave, je vais aller me chercher quelque chose moi-même..."
    show miharu happy at MoveTo(0.0, 0.5)
    show reina embarrassed at Bounce(1)
    m "Dans ce cas je te suis."
    show reina gulp at Bounce(3)
    $ renpy.pause(0.15)
    show reina overprotect at MoveTo(0.15, 0.25)
    show miharu cute
    r "NON ATTENDS !"
    show reina tense
    nar "héhé, dans le mille!"
    show reina awkward
    r "Ok c'est bon, je prends la commande pour VOUS DEUX !"
    show miharu genki at Bow(1)
    show reina nervousblush
    m "Vraiment ?! Merci beaucoup !"
    show miharu smile
    show reina genki
    r "C'est normal, ma chère Miharu."
    show ambient reinaglare
    with dissolve
    show reina evil
    nar "ton sentiment de victoire est anéanti en voyant un sourire démoniaque dirigé vers toi"
    nar "un frisson te parcourt, tu te demandes quel mélange elle va rapporter"
    hide ambient reinaglare
    show prop foodbubble3 at Appear(0.85, 0.25, 0.5, 0.5)
    show prop foodbubble3 at Heft(0.55, 20)
    show miharu curious
    show reina shock
    ta "Et apporte-moi un peu de poulet frit Kalasan pendant que tu y es ! Merci !"
    hide prop foodbubble3
    nar "..........."
    nar "tu te retournes nerveusement en direction de cette odieuse voix"
    menu:
        "Est-ce que tu devrais crier fort... ?":
            jump a1k1_kya_fr
        "...ou TRÈS fort ?":
            jump a1k1_gya_fr
label a1k1_kya_fr:
    show miharu uncomfortable
    k_swirl "KYAAAA !!"
    show reina huh at Bounce(1)
    r "ARGH ?!!"
    show aizawa calm at EnterRight(1.0, 0.25)
    show miharu confused
    show reina chide
    ta "C'est quoi cette réaction ?!"
    jump a1k1_reaction_fr
label a1k1_gya_fr:
    show redsiren
    play sound sound_airraidsiren
    show miharu grief
    k_shock "GYAAAAAAAAAAAAAHHH !!!"
    show reina reprimand at Bounce(5)
    r "AAAAAAAAARGH ?!!!"
    show aizawa savor behind redsiren at EnterRight(1.0, 0.25)
    $ renpy.pause(0.25)
    show aizawa squeal at Laugh(2)
    show miharu curious
    show reina ippenshindemiru
    ta "A-ha! Voilà une réaction avec PASSION, LOL!"
    hide redsiren
    stop sound
    jump a1k1_reaction_fr
label a1k1_reaction_fr:
    show miharu glad at Bow(1)
    show aizawa snide
    show reina frustrated
    m "Bonsoir, Mlle. Aizawa."
    show miharu smile
    show aizawa grateful
    ta "Ah ! Bonsoir, Miharu!"
    show miharu happy
    show aizawa amused
    show reina impatient
    m "Qu'est-ce qui vous amène ici, Mlle Aizawa?"
    show miharu cute
    show aizawa cute
    ta "Hé bien, la bouffe gratuite evidemment...~"
    show aizawa smug
    show miharu confused at ExitLeft(1.00)
    show reina smile at MoveTo(-0.4, 0.75)
    $ renpy.pause(1.25)
    hide miharu
    show reina angry at MoveTo(0.5, 0.15)
    show aizawa baka
    $ renpy.pause(0.25)
    show reina shout at Bounce(3)
    r "Vous n'êtes pas une élève, vous savez ?! Donc vous devez payer votre nourriture !"
    show aizawa complain at Laugh(2)
    show reina angry
    ta "tss tsss ! Si méchante ! Je suis une élève, hein."
    show aizawa fatigue
    show reina chastise
    r "{b}ÉTAIS{/b} une élève..."
    show aizawa meditate
    play sound sound_gong
    show ambient zen behind reina at Appear(0.0, 0.0, 0.0, 0.0)
    with slowdissolve
    show aizawa lecture
    show reina bored
    ta "Mon enfant ... Dans la vie, on ne cesse d'être élève."
    show aizawa pity
    show reina calm at Bounce(1)
    show ambient zen behind reina at Fling(0.0, 0.0, 0.0, 2.5, 0.75, 365)
    show reina nag
    r "Pas de philosophie ! Vous ne l'êtes plus depuis 5 ans !"
    show reina complain
    r "Donc si vous voulez un diner, PAYEZ !"
    hide ambient zen
    show aizawa yelp at Bounce(2)
    show reina chide
    ta "Aïe ! Quelle ingrate !"
    show aizawa accuse
    ta "Sa taille doit t'énerver je pense !"
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
    r "On a... {p}... {p}... {=whispered}exactement la même taille....{/=whispered}"
    show aizawa orly at Laugh(4)
    show reina shameright
    ta "OOh-hohoho ! Peut-être qu'avant c'était le cas..."
    show aizawa squeal
    show reina furiousblush
    ta "Mais maintenant tu es tellement {b}GRANDE{/b}..."
    show angrytwitch at Appear(0.4, 0.1, 0.5, 0.5)
    show aizawa evilchuckle
    ta "Tu es plus grande et plus élégante que tous les garçons !"
    show aizawa genki at Laugh(4)
    show reina impatient
    ta "Haha ! Fait attention mon prince, ou je vais tomber raide dingue de toi moi aussi, LOL !"
    show aizawa amused
    hide angrytwitch
    $ renpy.pause(2.5)
    show reina taunt at Laugh(3)
    r "fufufu ! Eh bien, tente ta chance..."
    show aizawa astound
    show reina mock
    r "Parce que si j'étais {b}PRINCE{/b} comme tu le dis..."
    show aizawa unamused
    show angrytwitch at Appear(0.9, 0.1, 0.5, 0.5)
    show reina evil
    r "Je voudrais ne jamais t'avoir comme petite amie."
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
    ta "Elles se battent à coups de paroles !!"
    $ renpy.pause(2.0)
    nar "même si c'est très marrant de les voir se battre comme ça,"
    nar "... Tu veux les arrêter avant que leurs ondes négatives ne détruisent toute la caféteria"
    stop music
    stop countermusic
    m "Bon, ça suffit !"
    show reina gulp at MoveTo(0.25, 0.25)
    show aizawa confuzzled at MoveTo(0.75, 0.25)
    nar "heureusement Miharu intervient avant toi..."
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
    m "Pas de bagarres, ok ? Nous restons des humains...."
    m "Nous devons nous entendre entre nous et avoir de bonnes relations ensemble..."
    show reina bored
    m "Il n'y a aucun avantage à se bagarrer, non ?"
    show reina chide
    r "IL Y EN A !"
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
    m "nyuuuu... ?"
    show aizawa confused
    show overlay garbage at Appear (0.5, 0.5, 0.5, 0.5)
    hide ambient heaven
    hide miharu
    show reina complain
    r "J'aurai la satisfaction de m'être vengée..."
    show reina scold at Bounce(1)
    r "... Après qu'elle ait faillit me tuer avec le gâteau d'anniversaire empoisonné de l'année dernière !"
    show aizawa moronic
    show reina angry
    play music music_ridiculous fadein 2.0
    show prop blackforest1 behind reina at Appear(0.5, 0.4, 0.5, 0.5)
    with dissolve
    ta "C'est cruel ! J'ai travaillé si dur pour le faire !"
    show aizawa yelp at Bounce(2)
    show reina threaten
    ta "J'ai travaillé sans arrêt pendant trois jours !"
    show reina reprimand at Bounce(1)
    show aizawa pity
    r "Et tu l'as laissé dehors quatre jours !"
    play countermusic sound_poison fadein 2.0
    show prop blackforest2 behind reina
    with slowdissolve
    show aizawa dumbfounded
    show reina pout
    r "Tu n'as ressenti aucune honte en me l'envoyant, couvert de machins qui bougaient,"
    show reina pout at Bounce(2)
    show aizawa nervous
    r "... En me disant que c'était un nouveau genre de gâteau forêt noire !"
    show miharu excited at EnterLeft (0.2, 0.25)
    show reina mope
    m "Haha ! Ah ! Je crois m'en rappeler... !"
    stop countermusic
    hide prop blackforest2
    with dissolve
    show overlay hospital
    with dissolve
    show miharu happy
    show aizawa chastiseright
    show reina hopeless
    m "On a tous perdu conscience après l'avoir mangé, et on est tous parti à l'hôpital pendant une semaine pour indigestion grave..."
    show miharu glad
    show aizawa schemeright
    show reina speechless
    m "Après, Mlle. Aizawa a reçu le surnom de \"Cuisinière de la mort\"."
    hide overlay hospital
    with dissolve
    show aizawa chortleright at Laugh(2)
    show miharu smile
    show reina impatient
    ta "Ahlala... C'est avec ce genre de choses,"
    show aizawa orly
    ta "... Qu'on peut grandir et devenir une grande personne, LOL!"
    show aizawa nervous
    stop music
    $ renpy.pause(2.50)
    show reina ippenshindemiru
    r "ARRÊTEZ... DE... {p}\"LOLER\"... {p}"
    play music music_crazyfight3 fadein 1.0
    play countermusic sound_war fadein 2.0
    show miharu grief at Sit(0.25)
    show reina scold at MoveTo(0.25, 0.25)
    show aizawa shock at MoveTo(0.75, 0.25)
    $ renpy.pause(0.25)
    show reina shout at HChatter(0.25, 0.28)
    show aizawa scream at HChatter(0.75, 0.72)
    $ renpy.pause(2.0)
    nar "*soupir*...  vous pouvez comprendre pourquoi Reina est en colère,"
    hide miharu
    show ambient fire behind reina
    with dissolve
    nar "mais la dispute devient de plus en plus bruyante..."
    show crowd calm behind ambient
    with dissolve
    nar "evidemment, tous les lycéens dans la caféteria arrivent en masse pour voir le spectacle"
    k_unamused "Hé ! Arrêtez ça immédiatement, c'est embarrassant ! "
    show miharu nervous behind aizawa at EnterLeft (0.5, 0.25)
    $ renpy.pause(0.25)
    show miharu dread behind aizawa at HChatter(0.5, 0.52)
    m "Arrêtez !"
    show miharu grief at QuickFling (-1.0, -0.5, 0.5, 550)
    show prop chair behind crowd at Appear(0.1, 0.8, 0.5, 0.5)
    show prop chair behind crowd at SetPosition(0.2, -45.0)
    show prop chair behind crowd at SendTo(0.1, 0.45, 1.0)
    nar "mais elles continuent de se battre... rien ne semble les arrêter..."
    hide miharu
    show angrytwitch at Appear(0.15, 0.35, 0.5, 0.5)
    u "{b}Vous avez entendu ce que Miharu a dit ?!{/b}"
    u "{b}ARRÊTEZ VOS STUPIDITÉS !!!{/b}"
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
    nar "la voix explosante de la foule te surprend"
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
    nar "après que l'agitation se soit dissipée, une jeune fille ayant l'air raffinée vient dans ta direction"
    show angrytwitch at Appear(0.35, 0.35, 0.5, 0.5)
    u "Hé bien.... Il semblerait que vous ayez ruiné ma bonne humeur vous deux..."
    hide angrytwitch
    u "Je voulais juste un peu de calme et de tranquillité pour savourer mon diner..."
    u "*soupir* Mais là... particulièremment vous Mlle. Aizawa..."
    show aizawa complain behind crowd at SendTo(0.8, 0.5, 0.15)
    ta "ENCORE MOI ?!"
    show aizawa complain behind crowd at SendTo(0.8, 0.8, 0.25)
    u "... Avez réussi à me le gâcher."
    hide reina
    hide aizawa
    show queen frown behind crowd at Heft(0.45, 3)
    u "Vous n'allez pas rester impunie !!!"
    nar "évitant de se laisser entraîner dans un nouveau drame, tu chuchotes à Miharu... "
    k_sarcastic "{=whispered}Elle fait partie des victimes de la forêt noire ?{/=whispered}"
    show miharu concern at EnterLeft(0.0, 0.25)
    m "{=whispered}Oui...{/=whispered}"
    show miharu doubt
    k_sneaky "{=whispered}Je vois. C'est qui ?{/=whispered}"
    show miharu concern
    m "{=whispered}Q.U.E.E.N.{/=whispered}"
    show miharu doubt
    k_dream "{=whispered}Oh, Q.U.E.E.N..... Q.U.E.E.N.....{/=whispered}"
    show miharu dread
    k_omg "{b}.....EHHHHH ?!!!{/b}"
    show queen frown behind crowd at Heft(0.45, 1)
    $ renpy.pause(0.25)
    show queen frown behind crowd at ExitRight(0.5)
    play music music_queen1 fadein 4.0
    nar "ton cri interrompt la leçon de Q.U.E.E.N.,"
    hide queen
    show queen lecture at EnterRight(1.0, 0.25)
    show miharu nervous at MoveTo(-0.3, 0.25)
    q "QUI OSE ?!!"
    show queen frown
    nar "...et tu crains le pire quand elle se retourne brusquement pour regarder la personne gênante nerveusement."
    nar "heureusement, une autre voix venant de la foule te sauve du danger"
    show freya berate at EnterLeft(0.0, 0.25)
    f "S'il-te-plait ne recommence pas une autre scène, Q.U.E.E.N !"
    show freya glare
    k_incredulous "Freya ! Tu es là aussi ?"
    show freya irked
    f "Bien sûr, tout le monde dans le dortoir vient ici pour dîner."
    show freya troubled
    show queen bored
    nar "Tout le monde ? Radins..."
    show freya fury at MoveTo(0.5, 0.25)
    $ renpy.pause(0.25)
    show freya shout at Bounce(4)
    $ renpy.pause(0.5)
    show miharu confused at MoveTo(0.0, 1.0)
    f "{b}Ok, retournez à vos places ! Il n'y a plus rien à voir ici !{/b}"
    show freya irritated
    hide crowd nervous
    with dissolve
    nar "La foule retourne à ses occupations en grommelant"
    show freya obligated at Sit (0.25)
    $ renpy.pause(1.0)
    show freya reprimand at Rise(0.5, 0.25)
    show aizawa aho at Rise(0.7, 0.25)
    $ renpy.pause(0.25)
    show miharu cute
    show queen frown
    f "Et Mlle. Aizawa, je ne sais pas combiens de fois je dois vous le dire,"
    show freya scold at Bounce(1)
    show aizawa confused
    f "... Mais est-ce que vous pouvez rentrer chez vous ?!"
    show freya shout at Bounce(3)
    show aizawa confuzzled
    f "Arrêtez de faire l'enfant, donnez l'exemple aux étudiants !"
    show miharu smile
    show aizawa cry
    show freya irritated
    ta "Mais j'ai pas payé le loyer, donc je peux pas rentrer..."
    show aizawa weep
    show freya lecture
    show queen calm
    f "Vous n'avez pas encore reçu votre salaire ?"
    show aizawa whimper
    show freya irritated
    ta "Oh, bien sûr, ils me payent toujours quand il faut."
    show aizawa aho
    show freya leer
    ta "Mais... vois-tu... J'ai d'une certaine manière tout dépensé en shopping..."
    show miharu uncomfortable
    show queen bored
    ta "... Et quand je l'ai réalisé, je n'avais plus un rond."
    show aizawa orly at Laugh(8)
    show freya angry
    show queen boredleft
    ta "Haha ! Maintenant j'ai 3 mois de loyer de retard, LOL!"
    show aizawa nervous
    stop music
    play sound sound_deadsilence
    show miharu nervous
    nar "Mlle Aizawa réussit à créer quelques secondes de silence pesantes"
    play music music_ridiculous fadein 5.0
    show freya defensive
    k_unamused "Vous rigolez..."
    show reina chide behind miharu at EnterLeft(-0.4, 0.25)
    r "Quelle écervelée..."
    show miharu sad at Bow(1)
    show reina leer
    m "Pauvre Mlle--"
    show queen chideleft at Bounce(1)
    show miharu dread
    q "Imbécile."
    show aizawa calm at Laugh(3)
    show miharu confused
    show aizawa genki
    show freya annoyed
    show reina angry
    show queen boredleft
    ta "Haha ! Je sais ! La directrice m'a dit la même chose quand je lui ai dit !"
    show aizawa happy
    ta "C'est pour ça qu'elle m'a donné la permission de vivre ici quelque temps."
    show miharu nervous
    show aizawa megasigh
    show freya evildream
    show angrytwitch at Appear(0.47, 0.18, 0.5, 0.5)
    show reina scowl
    show queen stareleft
    ta "*soupir* Si seulement elle était un peu plus sympathique,"
    show aizawa pleasantdream at Laugh(2)
    show reina chastise
    show queen stareright
    ta "... Et me donnait une de ses maisons, ou même un appartement...."
    show reina speechless
    show aizawa sweetdream
    hide angrytwitch
    $ renpy.pause(2.0)
    show freya psycho at Bounce(6)
    show miharu sigh
    show aizawa gasp
    f "{b} VOUS N'AVEZ AUCUNE HONTE !!!{/b}"
    show aizawa cry
    play sound sound_stomachgrowl
    show freya shock
    show reina shock
    show queen stareleft
    $ renpy.pause(0.75)
    show miharu uncomfortable at Bounce(1)
    show freya surprised
    show queen meditate
    m "Ah ! Ça  me rapelle que... !"
    show miharu grief at Bounce(2)
    show aizawa weep
    show reina gulp
    m "J'ai toujours pas eu mon Bihun !"
    show freya complain at MoveTo(0.35, 0.25)
    show miharu dread
    show reina embarrassed
    f "EN QUOI EST-CE DONC LIÉ ?!"
    show reina awkward at Bounce(1)
    show aizawa whimper
    show freya bored
    r "Ack ! Oublié !!"
    show miharu sad
    show aizawa weep
    show reina nervousblush
    m "Nyuuuu....."
    show miharu doubt
    show aizawa whimper
    show reina shoo
    r "Désolée, je vais te le chercher maintenant...!"
    show aizawa weep
    show reina shoofrown at ExitLeft(0.5)
    show prop foodbubble4 at Appear(0.65, 0.5, 0.5, 0.5)
    show prop foodbubble4 at Heft(0.55, 20)
    show freya sigh
    show queen mumble
    q "N'oublie pas mon <riz à la poêle>. Un istimewa !"
    show aizawa whimper
    show reina huh at EnterLeft(-0.4, 0.25)
    hide prop foodbubble4
    show miharu confused
    show queen meditate
    r "Quand as-tu~?  Ugh~! Oh je vois !"
    show prop foodbubble5 at Appear(0.5, 0.45, 0.5, 0.5)
    show prop foodbubble5 at Heft(0.55, 20)
    show aizawa tearsofjoy at Laugh(2)
    show miharu uncomfortable
    show freya perturbed
    show reina furious
    ta "Et mon kalasan aussi, héhé !"
    show prop foodbubble5 at QuickFling(1.5, 0.3, 0.5, 365)
    show reina reprimand at Bounce(3)
    show miharu nervous
    show aizawa moronic
    show freya perplexed
    show queen calm
    r "{b}TAISEZ-VOUS ! ALLEZ LE CHERCHER VOUS-MÊME !!!{/b}"
    show aizawa cry at Bow(1)
    show miharu smile
    show freya irked
    show reina furious
    ta "Hauu.... *snif*"
    show aizawa whimper
    show reina impatient at ExitLeft(0.25)
    show freya mocksideways
    nar "Reina s'en va, vous espérez qu'elle se souvienne des commandes"
    show miharu smile at ExitLeft(0.25)
    show aizawa weep at Sit(0.25)
    show freya mocksideways at ExitRight(0.25)
    show queen calm at ExitRight(0.25)
    $ renpy.pause(0.25)
    stop music fadeout 3.0
    scene bg dormroom
    with dissolve
    outline "DE RETOUR DANS LA CHAMBRE"
    play music music_quirky
    show miharu genki at Rise(0.0, 1.0)
    m "Ah~! J'ai trop mangé...!"
    show miharu smile at VChatter
    k_painful "Forcément !"
    show miharu glad at ExitLeft(0.25)
    $ renpy.pause(0.25)
    show prop nasgor at Appear(0.5, 0.5, 0.5, 0.5)
    with dissolve
    nar "Heureusement Reina n'a pas oublié de commander ton nasi goreng"
    show prop nasgormini
    with dissolve
    nar "mais la portion était telle que tu l'as finie en 3 bouchées"
    nar "mais au moins tu as mangé quelque chose"
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
    nar "enfin, quand même, Miharu a commandé quasiment 10 bols de bihun goreng,"
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
    nar "... Et à ta grande surprise elle les a tous mangés !"
    nar "\"Il a quelle taille son estomac ?!\", tu te poses la question"
    hide miharu
    show queen talk at EnterRight(1.0, 0.25)
    q "Si je me souviens bien, tu t'appelles Hana, non ?"
    show queen calm
    k_nervous "Heu... c'est plutôt Kana...."
    show queen talk
    q "Désolée de ne pas te l'avoir dit avant, mais je suis enchantée de faire ta connaissance."
    show queen calm
    stop music fadeout 2.0
    menu:
        "Comporte-toi normalement.":
            jump a1k1_nice1_fr
        "Entre dans son jeu.":
            jump a1k1_hermajesty_fr
label a1k1_nice1_fr:
    play music music_queen1
    k_glad "Ah !"
    k_genki "Enchantée de te rencontrer, Q.U.E.E.N."
    show queen mumble at Laugh(1)
    q "Je vois que tu as épelé mon nom correctement. C'est très courtois de ta part."
    jump a1k1_question_fr
label a1k1_hermajesty_fr:
    play music music_royalty
    k_dream "Tout l'honneur est pour moi, Majesté."
    show queen mumble at Laugh(3)
    q "Oh-hoho ! Comme c'est amusant !"
    show queen rebuke
    q "Mais même si je suis une <reine>, je préfère qu'on ne m'appelle pas d'un autre nom."
    show queen annoyed
    k_nervous "Oh... Désolée...."
    show queen mumble at Laugh(2)
    q "Hoho ! C'est très bien. Tu es nouvelle donc je vais passer l'éponge."
    show queen comment
    q "Mais seulement cette fois-là...."
    show queen stare
    k_gasp "?!! "
    k_nervous "Héhé, heu..."
    jump a1k1_question_fr
label a1k1_question_fr:
    show queen calm
    k_happy "Je peux te poser une question ?"
    show queen talk
    q "Bien sûr."
    show queen calm
    k_glad "\"Q.U.E.E.N.\", c'est ton vrai nom ou... ?"
    show queen chide
    q "Il l'est pour toi."
    show queen bored
    nar "C'est pas une réponse ça !"
    show miharu genki at EnterLeft(0.0, 0.25)
    show queen stareleft
    m "Ouais ! Q.U.E.E.N. est Q.U.E.E.N.!"
    show miharu glad at Laugh(2)
    m "Aucun doute, héhé !"
    stop music fadeout 2.0
    show queen stareright at ExitRight(0.5)
    show miharu doubt at MoveTo(-0.3, 1.0)
    nar "Pendant que Q.U.E.E.N. est occupée, Miharu te prend à coté et te chuchotte...."
    show miharu concern
    m "{=whispered}Ne lui demande pas, ou tu vas te faire maudire par la poupée....{/=whispered}"
    show miharu doubt
    k_ehhh "{=whispered}Hein ?{/=whispered}"
    show miharu concern
    m "{=whispered}Haku, sa poupée favorite.{/=whispered}"
    show miharu dread
    m "{=whispered}C'est pas une simple poupée, elle peut faire du vaudoux avec....{/=whispered}"
    play music music_haku
    menu:
        "Ok, j'ai compris.":
            jump a1k1_kidding_fr
        "Oh non, j'en ai marre des fous ici...":
            jump a1k1_scary_fr
label a1k1_kidding_fr:
    show ambient haunted behind miharu
    with slowdissolve
    show miharu nervous
    k_sarcastic "{=whispered}Tu rigoles...{/=whispered}"
    show hauntedtwirl behind miharu
    with dissolve
    show miharu confused
    m "{=whispered}Je suis on-ne-peut-plus sérieuse !{/=whispered}"
    show creepyqueenhaku behind miharu
    with dissolve
    show miharu dread
    m "{=whispered}Son nom en entier est SHI NO HAKUSHAKU !{/=whispered}"
    m "{=whispered}Ce qui signifie \"Comtesse de la mort\"!{/=whispered}"
    show miharu nervous
    k_sneaky "{=whispered}Hein~?!!{/=whispered}"
    jump a1k1_proof_fr
label a1k1_scary_fr:
    k_incredulous "Wow !! EFFRAYANT~!!!"
    show miharu worried
    m "{=whispered}N'est-ce pas?{/=whispered}"
    jump a1k1_proof_fr
label a1k1_proof_fr:
    show miharu dread
    m "{=whispered}Et Reina peut témoigner de ses pouvoirs~{/=whispered}"
    k_panic "{b}REINA ?!!{/b}"
    hide ambient haunted
    hide hauntedtwirl
    hide creepyqueenhaku
    show queen hakuchideleft at EnterRight(1.0, 0.5)
    show miharu nervous
    q "Ohlala... C'est quoi ces messes basses derrière mon dos ?"
    show miharu uncomfortable at MoveTo(0.0, 0.25)
    show queen hakuboredleft
    m "Oh, rien du tout~!"
    show miharu whimper
    k_nervous "Haha ! Tu en es sûre ?"
    show queen hakuannoyed at Bounce(1)
    show miharu doubt
    q "Humf !"
    stop music fadeout 1.0
    play sound sound_doorslam
    $ renpy.pause(0.5)
    nar "c'est alors que Reina entre soudainement dans la pièce très bruyamment"
    play music music_reina1 fadein 2.0
    queue music [ music_reina2, music_reina1 ]
    show miharu cute
    nar "pour une fois dans la soirée, tu es contente de la voir rappliquer"
    show reina relieved behind miharu at EnterLeft(0.5, 0.5)
    show miharu happy
    show queen hakucalm
    r "Ahhh~!! Enfin à la maison~!!"
    show miharu genki at Laugh(2)
    show reina tenderblush
    m "Bienvenue, teehee~!"
    show reina coo at MoveTo(0.1, 0.25)
    show miharu cute
    r "Ma chère Miharu, je te manquais déjà~?!"
    show queen hakustareleft
    nar "comme si regarder Miharu pendant tout le diner n'était pas assez,"
    show miharu smile at ExitLeft(0.75)
    show reina hentai at ExitLeft(0.75)
    nar "... Maintenant elle accourt pour aller embrasser Miharu dans sa chambre"
    show lotsoflove
    nar "tu espères que ça ne va pas durer toute la nuit..."
    show queen hakustare
    k_nervous "Reina est... un peu obsédée par Miharu, pas vrai ?"
    show queen hakucomment
    q "Cela ne me regarde pas."
    q "... Mais oui, on peut dire ça comme ça."
    show queen hakuboredleft at MoveTo(0.7, 1.0)
    nar "tu veux lui demander quelque chose d'autre, mais elle se retourne pour regarder le \"couple\" finalement"
    show queen hakuchideleft at Bounce(2)
    q "Je déteste interrompre les gens, mais où étais-tu, Rei ?!"
    hide lotsoflove
    show reina complain at EnterLeft(-0.4, 0.25)
    show queen hakuboredleft
    r "Partie laver la vaisselle évidemment. J'étais de corvée aujourd'hui, tu sais."
    show reina threaten at Bounce(6)
    r "*regard mauvais* ET j'ai dû travailler DEUX FOIS plus à cause de toi !!"
    show queen hakucommentleft at Laugh(1)
    show reina furious
    q "Ah, je vois ! Je t'en suis reconnaissante. Continue ainsi."
    show reina suspicious at Bounce(3)
    show queen hakustareleft
    r "*râle*"
    show miharu sigh at EnterLeft(0.0, 0.5)
    show reina curious
    show queen hakucalm
    m "*baille* Il se fait tard. On devrait aller dormir."
    show reina yawn at Bow(1)
    show miharu tired
    r "Oui, je suis crevée...*baille*"
    show queen hakumumble at Bounce(1)
    show reina tired
    q "Alors n'en dis pas plus. Nous allons tous nous coucher maintenant !"
    show reina sleepy at ExitLeft(0.5)
    show miharu sigh at ExitLeft(0.5)
    show queen hakumeditate at ExitRight(0.5)
    $ renpy.pause(0.5)
    stop music fadeout 3.0
    scene black
    with dissolve
    nar "même si ça n'a pas été aussi immédiat que ça, maintenant tout le monde est en pyjama, prêt à dormir dans quelques minutes"
    nar "toi y compris"
    scene bg dormroom2
    with dissolve
    q "Faites de beaux rêves."
    m "Toi aussi Q.U.E.E.N.!  Bonne nuit tout le monde !"
    r "Bonne nuit, pour toi ma Miharu !"
    q "Tu ne me le souhaites pas à moi aussi ?"
    r "Non, tu peux en avoir de mauvais toi, héhé."
    q "Imbécile."
    k_genki "Bonne nuit tout le monde ! Contente de vous avoir rencontré !"
    m "C'est réciproque ! À demain matin !"
    r "Tôt le matin ! Où on te jettera hors du lit !"
    q "Peut-être."
    k_nervous "Héhé... Compris..."
    nar "Reina et Q.U.E.E.N. se retournent et tombent immédiatement dans un profond sommeil"
    nar "Miharu se retourne et éteint la lumière"
    play sound sound_lightswitch
    scene bg dormroom3
    nar "Il fait nuit noire..."
    nar "...quand tu remarques la lumière de l'ordinateur portable que tu utilises dans ton lit"
    play music music_calm1 fadein 5.0
    m "Oh, tu ne dors pas ?"
    k_smile "Je ne vais pas tarder. Juste un ou deux trucs à faire."
    m "Ok... ne te couche pas trop tard. Bonne nuit..."
    k_relieved "nuit..."
    nar "en quelques secondes, Miharu semble s'être endormie"
    show prop unr1 at DissolveAppear(0.09, 0.3, 0.0, 0.0, 0.5)
    show overlay netbook at DissolveAppear(0.03, 0.2, 0.0, 0.0, 0.5)
    nar "tu es contente de voir que l'ordinateur ne fait pas trop de bruit"
    show prop unr2
    with quickdissolve
    nar "Tu surfes sur le net sans réveiller personne"
    show prop unr3
    with quickdissolve
    nar "Tu regardes les news de la journée, les projets te concernant"
    show prop unr5
    with quickdissolve
    nar "nouveaux artwork, jeux et musiques,"
    show prop unr4
    with quickdissolve
    nar "... Et d'autres sites que tu regardes quotidiennement"
    show prop unr6
    with quickdissolve
    stop music fadeout 3.0
    nar "Tu ouvres ta boite de messagerie, il y a quelques mails"
    play music music_netbook1 fadein 5.0
    scene bg email1
    with dissolve
    nar "après les avoir regardé,  il ne te reste plus qu'à composer un petit message..."
    nvl clear
    nvl show dissolve
    play countermusic sound_typing
    net "<Chère Cyllia...>"
    net "<J'ai eu mon premier jour de classe aujourd'hui, et ZOMG je te jure que je suis arrivée dans une autre dimension, lol!>"
    net "<J'ai une prof complètement barjo qui a dû s'enfuir d'un asile pour fous.> >.<"
    net "<Et je rencontre que des gens uniques et bizarres aussi.>"
    net "<De plus, je suis en train de partager ma chambre avec TROIS d'entre eux, LOL!!!> ^^;"
    net "<Mais... Je veux continuer à penser positivement.>"
    net "<En les connaissant un peu plus, je suis sûre que l'on s'entendra très bien.>"
    net "<Ou alors c'est moi qui vais devenir folle, hahaha....!> ^___^"
    stop music fadeout 3.0
    net "<Bon, je crois que c'est tout pour aujourd'hui. Je te parlerai plus d'eux demain.>"
    net "<Demain va être chargé, souhaite-moi bonne chance !> ^^"
    nvl hide nodissolve
    show ambient darken
    $ mouse_visible = False
    play music music_ED1a fadein 25.0
    queue music [ music_ED1b, music_silence ]
    $ floatingtext1 = Text("<Bonne nuit !>\n\n...\n\n<LOL! J'ai oublié qu'il devait probablement faire jour chez toi !>\n<Bonne journée alors !> ^____^\n\n<Sincèrement,>\nKana-chan ^____^v\n\n\nPS:\n<..... Comme d'habitude, désolé pour mon français.> ^^;", slow=True, slow_speed=10, style="emailed")
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
    
