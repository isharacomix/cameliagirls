# de
# Act 1 starts here.
init:
    # Declare language-specific characters used by this game.
    if persistent.lang == "german":
        $ classroom = "Klassenraum"
        $ teacher = "Lehrer"
        $ unknown = "Unbekannt"
label a1k1_start_de:
    scene black
    play music music_netbook1
    $ renpy.pause(1.0)
    scene bg sunrise
    with introfade
    nvl clear
    nvl show dissolve
    play countermusic sound_typing
    net "<Liebe Cyllia...>"
    net "<Ich bin endlich an der Camelia Mädchen Akademie angekommen...>"
    net "<Von heute an werde ich hier im Wohnheim leben, wie meine Eltern es so wollten...>"
    nvl hide dissolve
    stop countermusic
    scene bg academy
    with fade
    k_happy "Ah! Wenn du nur wüsstest, wie frisch die Morgenluft ist..."
    k_relieved "Und wie schön der Sonnenaufgang ist..."
    k_genki "Ich kann es kaum erwarten zu sehen, was ich hier erleben werde--"
    stop music
    $ renpy.play(sound_collide)
    with vpunch
    nar "scheinbar ist jemand in dich reingerannt..."
    nar "...und dadurch du fällst auf den Boden"
    show miharu grief at Fling(-0.5, 0.35, 1.5, 1.5, 1.0, 730.0)
    u "Hiyaaaah!!"
    nar "aber so sie..."
    play music music_miharu1
    menu:
        "Dir geht's gut, aber vielleicht ist sie verletzt?":
            jump a1k1_okay_de
        "Blöde Göre, sie soll hinschauen, wohin sie läuft!":
            jump a1k1_eyes_de
        "Hehe, sie sieht verwirrt aus. Ich spiele ihr einen Streich.":
            jump a1k2_bone_de
label a1k1_okay_de:
    k_worried "Autsch... Ah! Alles in Ordnung?"
    show miharu whimper at Rise(0.5, 1.0)
    u "Es tut mir wirklich Leid. Ja danke, mir geht's gut, was ist mit dir?"
    k_relieved "Auch gut."
    show miharu relieved
    u "Bin ich erleichert, das zu hören."
    show miharu uncomfortable at Bounce(1)
    u "Ah! Verdammt! Ich komme zu spät!"
    show miharu smile
    u "Entschuldige, aber ich muss los, also..."
    show miharu genki at ExitLeft(0.75)
    u "BIS DANN~!"
    k_nervous "Häh?"
    jump a1k1_who_de
label a1k1_eyes_de:
    k_furious "Hey! Bist du blind oder so?"
    show miharu grief at Rise(0.5, 0.25)
    u "HIYAAAHHH~!! ES TUT MIR SO LEID!!"
    show miharu uncomfortable at Bounce(1)
    u "Ah! Verdammt! Ich komme zu spät!"
    show miharu nervous
    u "Entschulde nochmals, aber ich muss los, also..."
    show miharu grief at ExitLeft(0.5)
    u "BIS DAAAAAAAAAANN........!!"
    k_shout "Hey! KOMM ZURÜCK!!"
    k_stare "...."
    k_unamused "....ah.... weg ist sie....."
    jump a1k1_who_de
label a1k2_bone_de:
    k_sneaky "AAH!! MEIN BEIN!!! ES IST GEBROCHEN!!! SCHMERZEN!!!"
    show miharu grief at Rise(0.5, 0.5)
    u "Gyaaaah!! Was habe ich getan?!"
    show miharu dread at Bounce(2)
    u "Muss den Notarzt anrufen~! Muss den Notarzt anrufen~!"
    k_genki "He.... Das war nur ein Scherz."
    show miharu grief at Bounce(1)
    u "AH! ICH KOMME AUCH NOCH ZU SPÄT!"
    show miharu confused at Bounce(2)
    u "Was soll ich tun~? Was soll ich tun~?"
    k_weird "He.... hörst du mir zu?"
    show miharu whimper
    u "Ja.....*schluchz*"
    k_smug "Entschuldige... aber das war eigentich nicht ernst gemeint..."
    show miharu grief at Bounce(4)
    u "DAS IST NICHT WAHR! DEIN BEIN IS WEGEN MIR GEBROCHEN!!"
    k_ehhh "Äh?!"
    show miharu cautious at Bow(1)
    u "Ich verspreche dir die volle Verantwortung zu übernehmen! Aber erst nachdem ich von meiner Arbeit zurück bin..."
    k_weird "Ähhhm.... okay...."
    show miharu uncomfortable
    u "Versuche bitte jemanden zu finden, der dich zur Klinik bringt...!"
    show miharu whimper at ExitLeft(0.75)
    u "Bis dann!"
    k_gasp "AH--!"
    k_unamused "..."
    k_sarcastic "War das ein \"Kommen-und-Gehen\"?"
    jump a1k1_who_de
label a1k1_who_de:
    k_sigh "...."
    show miharu smile at RunInDistance(-0.5, 1.5, 0.6, 0.75)
    nar "sie rannte davon, verließ das Schulgelände"
    nar "du wunderst dich, wer das Mädchen überhaupt war..."
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
    t "Der Unterricht beginnt!"
    t "Wie gestern bereits erwähnt, haben wir eine neue Schülerin, die heute zu uns kommen wird."
    show aizawa grateful
    t "Komm rein, Fräulein Schülerin! Stell dich vor!"
    show aizawa smile at ExitLeft(1.0)
    nar "du gehst in den Klassenraum rein, während du versuchst, nicht nervös zu werden"
    k_happy "Hallo alle zusammen... Mein Name ist Kana."
    k_genki "Es freut mich sehr euch kennen zu lernen..."
    show crowd nervous behind aizawa at Rise(0.50, 0.50)
    c "{=whispered}Sehr angenehm....{/=whispered}"
    show crowd nervous at Sit(0.75)
    nar "waren sie alle gelangweilt?"
    show aizawa sigh at EnterLeft(0.0, 0.5)
    t "*seufz*"
    show aizawa resign
    t "Was für eine durchschnittliche Vorstellung..."
    show aizawa fatigue
    stop music
    k_nervous "Häh?!"
    nar "Du hörst die ganze Klasse flüstern: \"ahh... sie fängt schon wieder damit an...\""
    show aizawa chastisecenter
    t "Wo ist deine LEIDENSCHAFT, Hana?! Dein Mangel an LEIDENSCHAFT stört mich...!"
    show aizawa sadistic
    t "MACH ES NOCHMAL!!"
    show aizawa revenge
    play music music_aizawa2
    k_omg "HÄHHHHH?!!!"
    k_nervous "...."
    k_genki "Ist dies ein Scherz für Neuankömmlinge oder so...?"
    show aizawa reprimand at Bounce(2)
    t "Absolut nicht!"
    show aizawa maniac
    t "ALSO MACH ES NOCHMAL ODER...!!!"
    show aizawa astound at ExitLeft(0.25)
    k_swirl "GYAAHHHH~!! SCHON GUT! SCHON GUT!"
    k_nervous "ähem...."
    menu:
        "Du solltest auf Nummer sicher gehen...":
            jump a1k1_hana_de
        "Sie will Leidenschaft? GIB IHR LEIDENSCHAFT!!!":
            jump a1k1_sama_de
        "Oh! Sag einfach das, was dir gerade einfällt...":
            jump a1k1_legend_de
label a1k1_hana_de:
    k_genki "Mein Name ist Kana, nicht Hana."
    stop music
    play sound sound_deadsilence
    c "{=whispered}*........stille..........*{/=whispered}"
    nar "du warst dir ziemlich sicher, dass du bist geliefert bist..."
    show aizawa chortlecenter at EnterLeft(0.0, 0.75)
    t "Okay, das reicht..."
    show aizawa schemecenter
    k_panic "DAS IST ALLES?!!"
    jump a1k1_intro_de
label a1k1_sama_de:
    stop music
    k_creepy "{=whispered}hihihi...{/=whispered}"
    play music music_pompous1
    k_evil "ICH BIN DIE GROSSE UND ALLMÄCHTIGE LADY KANA!!"
    k_villainous "KNIET VOR MIR NIEDER, IHR STERBLICHEN~!"
    stop music
    play sound sound_deadsilence
    c "{=whispered}*........stille..........*{/=whispered}"
    nar "\"Sie tut mir Leid...\", du hörst deine Klassenkameraden raunen"
    nar "wie peinlich..."
    play music music_aizawa2
    show aizawa obsessed at EnterLeft(0.0, 0.25)
    t "BRAVO!!!"
    show aizawa love
    t "WAS FÜR EINE GROSSARTIGE VORSTELLUNG!!! ICH BIN SO GLÜCKLICH, ICH KÖNNTE WEINEN!!!"
    show aizawa tearsofpride
    k_ehhh "HÄH?!!!"
    show aizawa squeal
    t "Ich mag dich bereits, Schwester!"
    show aizawa savor
    k_waterfall "Was ist hier los?!"
    k_angry "Und ich bin nicht ihr Schwester!"
    show aizawa sweetdream
    nar "du merkst, dass die Lehrerin dich nicht mehr beachtet"
    jump a1k1_intro_de
label a1k1_legend_de:
    k_squeal "Ich bin eine Legende!"
    stop music
    play sound sound_embarrass
    c "*........stöhnen..........*"
    nar "\"Oh... warum musste ich das erste SINNLOSE sagen, das mir gerade einfällt?\", wunderst du dich"
    show aizawa orly at EnterLeft(0.0, 1.0)
    t "Soso.... Du schaust dir gerne Filme von diesem Smith Kerl an."
    show aizawa snicker
    k_panic "Das ist nicht so gemeint...!"
    show aizawa chortlecenter
    t "Awww... du brauchst dich nicht zu schämen. Alle jungen Leute scheinen diesen Smith Kerl zu lieben."
    show aizawa schemecenter
    show crowd angry behind aizawa at Rise(0.5, 0.25)
    c "REDE KEIN UNSINN!!"
    show crowd angry at Sit(0.25)
    jump a1k1_intro_de
label a1k1_intro_de:
    show aizawa cute
    t "Also gut... dann werde ich mich mal vorstellen..."
    show aizawa smile
    stop music fadeout 1
    play sound sound_spotlight
    show ambient darken behind aizawa
    show prop spotlight at Appear(0.0, 0.0, 0.0, 0.0)
    nar "ein Scheinwerfer?!"
    play music sound_drumroll
    show aizawa awesome
    t "ICH BIN DIE GROSSE~!"
    show aizawa evilchuckle
    t "FABELHAFTE~!"
    show aizawa love
    t "GROSSARTIGE~!"
    show aizawa impressed
    t "EHRFÜRCHTIGE~!"
    show aizawa happy
    t "LEGENDÄRE~!"
    show aizawa pleasantdream
    t "{=whispered}und vor allem...{/=whispered}"
    show aizawa grateful
    t "SCHÖNE~!"
    stop music
    play sound sound_drumtada
    show aizawa squeal at Bounce(1)
    t "LEHRERIN AIZAWA!!!"
    play music music_pompous2
    show aizawa smile at MoveTo(0.5, 1.0)
    hide ambient darken
    with dissolve
    hide prop spotlight
    with dissolve
    with Pause(1)
    show snowblossom
    with dissolve
    nar "sie macht eine dramatische Pose, die dir zu Nahe kommt"
    show aizawa genki
    ta "Nett dich kennen zu lernen!"
    show aizawa smile
    stop music fadeout 2
    hide snowblossom
    with dissolve
    k_weird "ähmm.... öh.... okay.... Ganz meinerseits.... Frau Aizawa...."
    queue music [ music_aizawa3, music_aizawa4, music_aizawa5 ]
    show aizawa lecture at MoveTo(0.0, 0.5)
    ta "ERHEBE DICH, KLASSENSPRECHERIN!"
    show aizawa meditate
    show freya lecture behind aizawa at Rise(1.0, 0.25)
    f "Mein Name ist Freya!!"
    show aizawa complain
    show freya irritated
    ta "Es ist schwer, sich tausende Namen der Schülern zu merken, weiß du."
    show aizawa fatigue
    show freya shout at Bounce(3)
    f "Merken sie sich wenigstens die Namen der Schüler IN IHRER EIGENEN KLASSE!"
    show aizawa chortleleft
    show freya scowl
    ta "Ich bin nicht eure Klassenlehrerin, deshalb kümmert mich das nicht...."
    show aizawa schemeleft
    show freya annoyed
    show crowd shout behind freya at Rise(0.5, 0.25)
    c "SIE {b}SIND{/b} UNSERE KLASSENLEHRERIN!!"
    show crowd calm
    show aizawa confuzzled
    ta "Wirklich? Ich dachte, ich wäre die Klassenlehrerin der 2-C...?"
    show aizawa confused
    show crowd angry
    show freya bored
    c "DAS HIER {b}IST{/b} DIE 2-C!!"
    show crowd calm
    k_unamused "...."
    show aizawa resign
    nar "plötzlich aus der Schule abzuhauen klang gar nicht Mal so übel..."
    show aizawa genki at Laugh(3)
    show freya pout
    ta "Hahaha! Oh, lass dich nicht wegen der kleinen Sache stören..."
    show aizawa smug
    show freya nag
    f "Was genau meinen sie mit \"kleinen Sache\"?!"
    show aizawa awesome
    show freya upset
    ta "Was auch immer... Habt ihr die gestrige Hausaufgabe gemacht?"
    show aizawa snide
    show crowd shout
    show freya angry
    c "Welche Hausaufgabe?"
    show crowd calm
    show aizawa evilchuckle
    ta "Wie, die Geschichtshausaufgabe zum Thema Neuzeit natürlich."
    show aizawa smug
    show freya calm at Bounce(1)
    show freya annoyed
    f "Aber sie sind unsere Englisch Lehrerin."
    show aizawa dumbfounded at Laugh(2)
    ta "Häh? Ara! Ich hab's vergessen, LOL!"
    show aizawa nervous
    show crowd shout
    show freya tired
    c "\"LOL\" nicht mit uns!"
    show crowd calm
    show aizawa sadistic
    show freya perturbed
    ta "Ach! Nun sammelt schon die Hausaufgaben ein."
    show crowd angry
    show aizawa revenge
    show freya angry
    c "WIE GESAGT, ÜBER WAS FÜR HAUSAUFGABEN REDEN SIE?!"
    play countermusic sound_chatter fadein 0.25
    show crowd angry at VChatter
    show aizawa reel at MoveTo(0.25, 0.25)
    show freya defensive at MoveTo(0.75, 0.25)
    $ renpy.pause(0.25)
    show aizawa scream at HChatter(0.25, 0.28)
    show freya shout at HChatter(0.75, 0.72)
    nar "du hattest einen normalen ersten Tag erhofft, aber dieses Chaos war nur der Anfang..."
    show crowd angry at Sit(0.25)
    show aizawa savor at ExitLeft(0.25)
    show freya bloodlust at ExitRight(0.25)
    $ renpy.pause(0.25)
    stop music fadeout 2
    stop countermusic fadeout 0.5
    scene bg cafeteria
    with fade
    outline "Mittagspause"
    play music music_roughday fadein 2.0
    k_sigh "*seufz*"
    nar "du bist so erschöpft, dass du nicht Mal dein Essen anheben kannst"
    show freya nervouschuckle at EnterLeft(0.0, 0.5)
    f "Ich habe Mitleid mit dir."
    show freya nervous
    k_nervous "Wieso?"
    show freya covet
    f "Frau Aizawa...."
    show freya bashful
    menu:
        "Nun ja, du muss zugeben, sie ist ein von der Sorte...":
            jump a1k1_interesting_de
        "Du machst dir Sorgen, dass sie aus einer Psychiatrie entkam...":
            jump a1k1_crazy_de
        "Sie ist vielleicht eigenartig, aber sie hat ein gutes Herz.":
            jump a1k1_nice_de
label a1k1_interesting_de:
    k_sneaky "Sie ist eine... interessante Person..."
    show freya glad
    f "Nun... ich vermute, dass wir sagen können, sie sei... \"einzigartig\""
    show freya smile
    k_sarcastic "Einzigartig wie ein seltenes Tier?"
    show freya cute at Bounce(1)
    f "Ganz genau!"
    jump a1k1_classified_de
label a1k1_crazy_de:
    k_painful "Sie ist verrückt!"
    show freya nervouschuckle
    f "Das ist sie...."
    jump a1k1_classified_de
label a1k1_nice_de:
    k_genki "Ich denke, dass sie eine wirklich nette Person ist."
    show freya omg at Laugh(2)
    f "WAAAS?! HAT MAN DIR EINE GEHIRNWÄSCHE VERPASST?!"
    show freya nervous
    k_oops "...?"
    jump a1k1_classified_de
label a1k1_classified_de:
    show freya glad
    f "Übrigens...."
    f "Kann ich dich was fragen?"
    show freya smile
    k_happy "Okay..."
    show freya sarcastic
    f "Warum bist du zu dieser Schule gewechselt, Kana?"
    show freya uneasy
    stop music fadeout 1
    k_sad "...?"
    k_oops "Ist mit der Schule irgendwas nicht in Ordnung?"
    $ renpy.pause(1.0)
    show freya bashful
    $ renpy.pause(0.5)
    show freya tender
    $ renpy.pause(0.25)
    show freya love
    f "Oh, so habe ich das nicht gemeint. Ich bin nur neugierig."
    show freya cute
    f "Jeder, mit dem ich sprach, hatte immer eine faszinierende Geschichte zu erzählen."
    show freya calm
    play music music_flashback1 fadein 2.0
    k_dream "So ist das... Nun...."
    show freya curious at ExitLeft(0.25)
    $ renpy.pause(0.25)
    scene bg flashback1
    with flashbackfade
    k_happy "Meine Eltern schickten mich hierher, da sie im Ausland auf Dienstreisen sind..."
    k_sad "...und werden für eine lange Zeit nicht heimkehren."
    scene bg flashback2
    with flashbackfade
    k_happy "Ich habe keine Verwandten hier,..."
    k_genki "...deshalb vertrauten sie mich der Schulleiterin an, da sie eine alte Freundin meiner Eltern waren."
    scene bg flashback3
    with flashbackfade
    k_tired "Wenn ich's mir recht überlege, hatte ich nichts zu melden."
    k_happy "Aber trotzdem..."
    k_dream "...bin ich mir sicher, dass ich eine wunderbare Zeit bei der Camelia haben werde!"
    scene bg cafeteria
    with flashbackfade
    show freya sweetdream at EnterLeft(0.0, 0.5)
    f "*nick nick*"
    k_relieved "Was ist mir dir, Freya?"
    show freya pleasantdream
    f "Irgendwie dasselbe wie du..."
    show freya sweetdream
    stop music
    k_nervous "..."
    play music music_roughday
    k_unamused "Mit anderen Worten, das war überhaupt nicht faszinierend."
    show freya mock
    f "Es hatte ihre Momente."
    show freya snicker
    k_sigh "*seufz*"
    show freya tender at ExitLeft(0.25)
    $ renpy.pause(0.25)
    stop music fadeout 2
    scene bg classroom
    with fade
    outline "Nach der Schule"
    play music music_aizawa4 fadein 2.0
    show aizawa pleasantdream at EnterLeft(0.0, 0.25)
    ta "Gut, ich denke, das war's für heute."
    show aizawa glad
    ta "Wenn ihr noch Fragen habt, merkt euch das für--"
    play sound sound_doorslam
    show aizawa astound
    nar "die Tür platzt auf"
    show aizawa amused at MoveTo(1.0, 0.25)
    show miharu grief behind aizawa at EnterLeft(0.0, 0.25)
    u "ENTSCHULDIGE, ICH BIN ZU SPÄT! WIRKLICH!!"
    k_shock "AH! DU!!"
    show aizawa naive
    show miharu confused
    u "Du...?"
    u ".....wer.....?"
    show miharu nervous
    show aizawa inquisitive
    k_sneaky "Wir \"trafen\" uns am Schultor, erinnerst du dich?!"
    show miharu wonder
    show aizawa snide
    u "ahhhh...."
    show miharu curious
    show aizawa cool
    u "...."
    show miharu excited at Bounce(1)
    show aizawa evilsmile
    u "ah!"
    queue music [ music_aizawa3, music_aizawa4, music_aizawa5 ]
    stop countermusic fadeout 3.0
    show aizawa evilchuckle at Bounce(3)
    show miharu smile
    ta "Ach so, ihr beide kennt euch von damals...?"
    show aizawa evilsmile
    k_angry "NEIN!"
    show aizawa grateful
    ta "Also, was ist mit dieser freundlichen Miene?"
    show aizawa drunksmile
    k_stare "Sie nennen das freundlich?"
    show miharu cute
    show aizawa awesome
    ta "Übrigens.... Du bis zwar letztendlich hier Miharu, aber wir sind für heute bereits fertig."
    show miharu sad at Bow(1)
    show aizawa snide
    m "Es tut mir Leid..."
    show aizawa genki at Laugh(3)
    ta "Hahaha! Kein Problem... Ich bin so ein netter Mensch, deshalb verzeihe ich dir..."
    show crowd angry behind miharu at Rise(0.50, 0.25)
    show miharu happy
    show aizawa smile
    c "WER IST DER NETTE MENSCH?!!"
    show crowd angry at Sit(0.25)
    show miharu cute
    show aizawa happy
    ta "Du kannst später beim Lehrerzimmer vorbeikommen und dir einen Handout für die heutige Stunde holen."
    show miharu genki at Bow(1)
    show aizawa smile
    m "Vielen, vielen Dank! Sie sind die Beste, Frau Aizawa!"
    show miharu smile at ExitLeft(0.25)
    show aizawa squeal at Laugh(3)
    ta "Hahaha!"
    show aizawa savor
    show crowd nervous behind aizawa at Rise(0.50, 0.25)
    c "Sie machen wohl Witze..."
    show crowd nervous at Sit(0.25)
    show aizawa orly
    ta "Na dann, das war's! Vergesst dieses Mal nicht die Hausaufgabe!"
    show aizawa snicker at ExitRight(0.25)
    show crowd angry behind aizawa at Rise(0.50, 0.25)
    c "ABER SIE HABEN UNS KEINE GEGEBEN!!!"
    show freya chide at Rise(0.50, 0.25)
    f "*seufz* Was für eine lästige Lehrerin wir haben...."
    show crowd calm
    show freya annoyed at Sit(0.25)
    $ renpy.music.set_volume(0.25, 1, channel="music")
    play countermusic sound_chatter fadein 1.0
    show crowd calm at VChatter
    nar "mit dem Verschwinden der Lehrerin aus dem Raum..."
    nar "klingt das Rascheln beim Sortieren der Sachen deiner Klassenkameraden und die Unterhaltungen..."
    nar "...eher friedlich im Vergleich"
    stop countermusic fadeout 2.0
    $ renpy.music.set_volume(1, 1, channel="music")
    m "Ah Freya!"
    play countermusic music_miharu3 fadein 3.0
    stop music fadeout 3.0
    show crowd calm at Sit(0.25)
    show miharu happy at EnterLeft(0.0, 0.25)
    show freya cool at EnterRight(1.0, 0.25)
    m "Tut mir Leid, dass ich dich wieder störe, aber lässt du mich in deine Notizen rein schauen?"
    m "Dafür werde ich etwas für dich zeichnen..."
    show freya cute
    f "Ah, du muss nicht... Ich bin froh, helfen zu können."
    show miharu genki at Bounce(1)
    show freya calm
    m "Du bist solch eine gute Freundin, die Beste, die ich jemals hatte!"
    show freya curious
    show prop bookworm at Appear(0.15, 0.4, 0.0, 0.0)
    with dissolve
    $ renpy.pause(0.5)
    show miharu relieved
    show freya angry
    m "Deshalb ist diese Zeichung--"
    show prop bookworm at MoveTo(0.8,1.0)
    $ renpy.pause(1.0)
    show freya psycho at Bounce(3)
    show prop bookworm at Fling(0.8, 0.4, -0.30, 0.35, 0.35, 1095)
    $ renpy.pause(0.15)
    show miharu grief at Fling (0.0, 0.0, -1.0, -0.5, 0.5, 790)
    $ renpy.play(sound_collide)
    stop countermusic
    hide prop bookworm
    f "Ich brauche das nicht! Nimm endlich die Notizen!!"
    hide miharu
    queue music [ music_miharu1, music_miharu3 ]
    show freya disturbed
    $ renpy.pause(1.00)
    show freya meditate
    $ renpy.pause(0.50)
    nar "du wunderst dich... nee, das bildest du dir bestimmt nur ein..."
    show freya glad at Bounce(1)
    f "Ah! Das erinnert mich... Kana, das ist Miharu. Sie wird deine Mitbewohnerin im Wohnheim sein."
    show freya smile at ExitRight(0.25)
    show miharu happybandage at EnterLeft(0.5, 0.5)
    m "Also ist das die Schülerin, die hierher gewechselt ist."
    show miharu uncomfortablebandage
    m "Es tut mir sehr Leid für den Ärger heute morgen, den ich verursacht hatte."
    menu:
        "Das ist so süß, sie sorgt sich immer noch um dich.":
            jump a1k1_forget_de
        "Oh nein! SO leicht kommt sie mir nicht davon!":
            jump a1k1_hell_de
label a1k1_forget_de:
    k_relieved "Das geht in Ordnung, ich hab's bereits vergessen."
    show miharu relievedbandage
    m "Das ist nett von dir...."
    k_genki "Übrigens, es freut mich dich kennen zu lernen, Miharu."
    jump a1k1_conclusion_de
label a1k1_hell_de:
    play sound sound_thunder
    show lightning
    show miharu dreadbandage
    k_furious "Wie zur HÖLLE kann ich DAS vergessen?!"
    hide lightning
    show miharu griefbandage at Bow(1)
    m "Hiyaaaahhhhhh...!! Es tut mir Leeeeid..!!"
    k_scheme "Aber gut, ich drück' Mal ein Auge zu, deshalb..."
    show miharu curiousbandage
    k_genki "...nett dich kennen zu lernen, Miharu."
    jump a1k1_conclusion_de
label a1k1_conclusion_de:
    show miharu excitedbandage
    m "Ganz meinerseits, Kana."
    show freya cute at EnterRight(1.0, 0.25)
    show miharu cutebandage
    f "Nun...."
    f "Ich denke, es ist an der Zeit, in das Wohnheim zurückzukehren."
    show freya calm at ExitRight(0.25)
    show miharu smilebandage at ExitRight(0.5)
    $ renpy.pause(0.5)
    stop music fadeout 3.0
    scene bg dorm
    with introfade
    outline "Camelia Wohnheim"
    play music music_mellow
    scene bg dormhall
    with dissolve
    show freya keen at EnterRight(0.5, 0.75)
    f "Dies ist unser Wohnheim. Alle Schülerinnen der Camelia leben hier."
    f "Es gibt drei Stockwerke in diesem Wohnheim, plus ein Keller, wohin wir nicht rein können..."
    show freya cute at MoveTo(1.0, 0.5)
    f "Die Registrierung, das Telefon, die Cafeteria und Abstellräume findest du im ersten Stock"
    show freya curious at MoveTo(0.0, 0.75)
    f "Und all unsere Zimmer, Aufenthaltsräume, Toiletten und Duschen sind in den oberen zwei Stockwerke"
    show freya love at MoveTo(0.5, 0.5)
    f "Es gibt vier Betten in jedem Zimmer,"
    f "...das heißt, dass du dein Zimmer mit drei weiteren Leute teilen muss."
    show freya glad at MoveTo(0.0, 0.5)
    f "Dein Raum, #327, ist im dritten Stock, nach dem ersten Treppengang zweimal rechts,"
    show freya smile at MoveTo(0.5, 0.25)
    show miharu smug at EnterLeft(0.0, 0.25)
    f "...und Miharu hier ist eine deine Mitbewohnerin."
    show freya smile at MoveTo(0.0, 0.25)
    show miharu smile at ExitLeft(0.25)
    $ renpy.pause(0.75)
    show freya keen
    f "Noch Fragen?"
    show freya cool
    menu:
        "Wow! Sie redet viel...":
            jump a1k1_enough_de
        "Warte! DREI weitere Leute?!!":
            jump a1k1_two_de
label a1k1_enough_de:
    k_nervous "Ich denke, das reicht für's Erste..."
    show freya glad
    f "Gut."
    jump a1k1_fine_de
label a1k1_two_de:
    k_nervous "Weiß du, wer die anderen zwei Mitbewohner sind?"
    show freya sarcastic
    f "Nun..."
    f "Die sind zwei Ältere namens Reina und Q.U.E.E.N."
    show freya weary
    k_baka "<Queen>? Ist das überhaupt ein richtiger Name?"
    show freya yearn
    f "Es ist jetzt einer."
    show freya love
    f "So nebenbei, wenn du ihr Name schreiben willst, sorge dafür alles GROSS zu schreiben."
    show freya tender
    k_genki "Wieso? Ist sie eine Anführerin oder so?"
    $ renpy.pause(0.75)
    show freya suspicious
    f "Glaube mir, tue es einfach."
    show freya snide
    k_baka "Häh?"
    show freya evil
    f "Es sei denn, du willst es auf die harte Tour erfahren...."
    show freya cynical
    k_gasp "...!!"
    $ renpy.pause(1.0)
    jump a1k1_fine_de
label a1k1_fine_de:
    show freya glad
    f "Gut, wenn du Hilfe brauchst, mehr Fragen hast oder mich nur besuchen willst..."
    show freya cute
    f "...kannst du einfach bei mir in Raum #156 im ersten Stock vorbei schauen."
    show freya calm
    k_happy "Okay, danke!"
    show freya smile at ExitRight(0.75)
    nar "Freya ging"
    k_genki "Nun, ich denke es ist Zeit, dass wir selbst zu unseren Zimmer zurückkehren."
    k_smile "..."
    show miharu confused at EnterLeft(0.0, 0.25)
    m "...?"
    k_sarcastic "...öh... Okay, ehrlich gesagt kann ich mich an nichts erinnern, was Freya gesagt hatte."
    show miharu relieved
    k_waterfall "Weise bitte den Weg."
    show miharu glad at Bounce(1)
    m "Natürlich!  Folge mir...    "
    scene bg dormhall1
    with dissolve
    $ renpy.pause(0.25)
    show miharu chibi1 at Bobble(1.15, 0.6, -0.15, 0.6, 0.35, 2.0)
    nar "und du folgst ihr"
    scene bg dormhall2
    with dissolve
    show miharu chibi1 at Bobble(-0.15, 0.0, 1.15, 0.2, 0.25, 3.0)
    nar "aber zu deiner Überraschung ist Miharu selbst ziemlich ratlos"
    scene bg dormhall3
    with dissolve
    show miharu chibi1 at Fling(1.15, 0.7, -0.15, 0.3, 2.00, 365.0)
    nar "während du dem tollpatschigen Mädchen folgst, läufst du 15 Minuten lang ziellos in den Gängen herum,"
    scene black
    with dissolve
    stop music fadeout 3.0
    nar "...bis du schließlich dein Zimmer erreichst"
    scene bg dormroom
    with dissolve
    play music music_quirky
    show miharu genki at EnterLeft(0.0, 0.25)
    m "Hier sind wir...!"
    k_swirl "ARGH!!!  Werde niemals Reiseführerin!"
    show miharu smile at ExitLeft(0.25)
    nar "du willst dich auf das Bett fallen lassen und dich ausruhen, nur weiß du nicht, welches deines ist"
    show prop haku at Appear(0.45, 0.2, 0.0, 0.0)
    with dissolve
    nar "und du merkst, dass das Zimmer voll mit allen möglichen interessanten Dingen ist"
    k_squeal "Ah! Was für eine hübsch Puppe!"
    k_happy "Deine?"
    show miharu happy at EnterLeft(0.0, 0.25)
    m "Oh nein, das ist Q.U.E.E.N.'s Eigentum."
    k_ehhh "Häh?!!"
    nar "also spielt diese \"Q.U.E.E.N.\" gerne mit Puppen?"
    nar "was für eine Art Person ist sie?"
    k_sarcastic "Naja, was auch immer. Lass es mich gemütlich machen...."
    show miharu smile at ExitRight(0.75)
    $ renpy.pause(0.25)
    show prop haku at ExitRight(0.50)
    nar "ihr beide betretet den Raum"
    nar "während Miharu beschäftigt ist, die Schulnotizen durchzublättern, fängst du an, deine Tasche auszupacken"
    nar "nachdem du die Kleidungen, Fotos und ein paar Dekorationen ausgepackt hast,"
    nar "...nimmst du dein Netbook raus und stellst es auf den Tisch."
    show miharu genki at EnterRight(1.0, 0.25)
    m "Whoa!  Wie niedlich!"
    show miharu worried
    m "Aber ist das die gleiche Tasche, die runter gefallen ist, als ich in dich rein gerannt war?"
    k_genki "Genau."
    show miharu concern
    m "....Ist es in Ordnung?"
    k_smile "Mmm?"
    show miharu curious at MoveTo(0.85, 0.25)
    m "Das Teil..."
    k_glad "Oh, Das Netbook?  Ja, 'ist in Ordnung."
    show prop netbook at Appear(0.5, 0.5, 0.5, 0.5)
    with dissolve
    nar "du hebst es vom Tisch und schwingst es mit Leichtigkeit herum"
    show miharu wonder
    nar "es ist eigentlich sehr leicht, aber Miharu sieht dich an, als wärst du super stark"
    show prop netbook at Shake(0.4, 2)
    k_genki "Siehst du? Nicht mal ein Kratzer."
    show miharu relieved at Bounce(1)
    m "Oh! Bin ich erleichtert das zu hören!"
    k_happy "Ja, der Süße ist sehr stark."
    show prop netbook at Heft(0.4, 3)
    show miharu cute
    k_smug "Ich habe sie bereits zehnmal runter fallen lassen, aber sie läuft immer noch!"
    show miharu genki
    m "Super! Und die Farbe ist auch noch sooo niedlich!"
    show miharu excited
    m "Es muss dich ein Vermögen gekostet haben..."
    show miharu cute
    k_happy "Nicht wirklich.  Für diesen einen glaube ich etwa... Rp 1,500,000 bezahlt zu haben."
    k_relieved "Ziemlich gut für ein Computer, und ich weiß, dass es billigere gibt."
    show miharu genki at Bounce(1)
    m "Unglaublich! Das ist viel billiger als ich's gedacht habe!"
    hide prop netbook
    with dissolve
    show miharu smile
    k_smile "hehe..."
    show miharu grief at MoveTo(0.5, 0.25)
    m "Apropos billig, ich bin bettelarm und hungrig..."
    k_oops "?!"
    show miharu excited at Bounce(4)
    m "...lass uns deshalb heute Abend im Bunker Essen!"
    show miharu cute
    k_nervous ".........\"Bunker\"?"
    show miharu happy
    m "So nennen wir unsere Cafeteria im Wohnheim."
    show miharu cute
    k_weird "Öhm... okay...."
    nar "dein Tag ist schon voll genug mit merkwürdigen Dingen, da kann unmöglich noch irgendwas sein, dass dich überraschen würde"
    k_nervous "Lass... Lass uns dann essen gehen."
    show miharu glad at Bounce(2)
    $ renpy.pause(0.25)
    show miharu smile at ExitLeft(0.5)
    $ renpy.pause(0.5)
    stop music fadeout 3.0
    scene bg bombshelter
    with slowdissolve
    outline "Der Bunker"
    play music music_bombshelter1 fadein 2.0
    nar "du wusstest nun, warum sie es den \"Bunker\" nannten"
    nar "Betonwände, gedämpftes Licht, keine Fenster, unbequeme Stühle, spärliche Dekorationen"
    nar "es sieht mehr geeignet für das Überleben von Luftangriffe als für das servieren von Mahlzeiten aus"
    nar "kein Wunder, dass das Essen so billig ist..."
    show miharu genki at Rise(0.5, 0.25)
    m "Ich bin so glücklich!  Ich habe seit diesem Morgen nichts gegessen!"
    show miharu smile
    nar "das Sprichwort \"Hunger ist das beste Gewürzt\" muss wahr sein,"
    play sound sound_thunderstep
    with vpunch
    nar "...da dieses Essen eines der Schlimmsten ist, den du jemals gegessen hast"
    show reina silhoutte behind miharu at EnterRight(0.7, 2.5)
    play sound sound_thunderstep
    with vpunch
    show ambient darken
    with slowdissolve
    play sound sound_thunderstep
    with vpunch
    nar "aber genau dann, bevor du dich über etwas lustig machen konntest,"
    show miharu wonder
    nar "... erschrakst du, als plötzlich eine große Gestalt auftaucht und Miharu umarmte"
    show reina relievedblush
    show ambient darkenhole
    with dissolve
    u "Miharu Liebes!  Es ist lange her!"
    show miharu happy
    show reina tenderblush
    m "Es ist \"lange her\"?"
    show reina relievedblush
    u "Ja, seit diesem Morgen."
    show reina desire
    u "Aber ohne dich zu sehen ist es wie fünf Jahre..."
    hide ambient darkenhole
    show miharu cute
    show reina lovestarved
    k_sigh "Ähem!"
    show reina stare
    k_sarcastic "Tut mir Leid euch stören zu müssen, aber dürfte ich fragen, wer du bist?"
    show reina calm at Bounce(1)
    show reina oppose
    u "Ihr Verlobte."
    show miharu uncomfortable
    show reina frown
    nar "KEUCH! so direkt!"
    show miharu genki at Laugh(3)
    show reina lust
    m "Hahaha!  Was meinst du mit \"Verlobte\"?  Wir sind doch nur Zimmergenossinnen."
    show miharu smile
    show reina hentai
    k_nervous "Häh?"
    show miharu happy
    show reina fantasize
    m "Ja, sie ist Reina, unsere Mitbewohnerin."
    show miharu cute
    show reina blush
    k_omg "HÄHHH?!"
    show miharu smile at Sit(0.25)
    show reina taunt at MoveTo(0.5, 0.75)
    r "Ich verstehe... das ist also die neue Schülerin."
    show reina mock
    r "Hmmmm... ich vergaß, ist es Kana oder Hana?"
    play sound sound_wind
    show ambient icy
    with dissolve
    show reina fufufu
    nar "du schauderst wegen etwas, was sich fast wie ein eisiger und eifersüchtiger Blick anfühlt"
    show reina sinister
    k_nervous "...Kana."
    hide ambient icy
    with dissolve
    show reina reluctant
    r "Ah genau... Kana."
    show reina evil
    r "Ich bin Reina. Es freut mich dich kennenzulernen."
    show reina smug
    k_nervous "Öh... ganz meinerseits... Fräulein Reina"
    show reina chastise
    r "\"Reina\" reicht...."
    show reina happydream at MoveTo(0.7, 0.25)
    show miharu calm at Rise(0.5, 0.25)
    nar "und damit umschwärmt sie Miharu wieder"
    show reina kawaii
    r "So, willst du etwas anderes zu Essen haben, Miharu Liebes?"
    r "Das geht auf's Haus..."
    show reina kawaiismile
    $ renpy.pause(0.5)
    show miharu genki at Bounce(3)
    show prop foodbubble1 at Appear(0.30, 0.18, 0.5, 0.5)
    show prop foodbubble1 at Heft(0.55, 20)
    m "Ah, das ist so nett von dir!  Danke, ich würde gerne bihun goreng!"
    hide prop foodbubble1
    show miharu smile
    show reina happy
    r "Alles für dich..."
    show prop foodbubble2 at Appear(0.25, 0.60, 0.5, 0.5)
    show prop foodbubble2 at Heft(0.55, 20)
    show miharu calm
    show reina smile
    k_genki "Dann würde ich gerne nasgor bitte."
    show prop foodbubble2 at Fling(0.25, 0.60, -0.5, 0.7, 0.5, 730)
    show miharu worried
    show reina suspicious
    r "Ich habe dich nicht gefragt."
    hide prop foodbubble2
    show reina angry
    k_sneaky "häh?"
    show miharu genki at Laugh(3)
    show reina bashfulleft
    m "Hahaha! Oh, sag das doch nicht so, Reina."
    show miharu glad
    show reina enchanted
    m "Die Leute werden dich deswegen missverstehen, hahaha..."
    show miharu smile
    show reina awkward
    nar "Miharu denkt, dass Reina nur Spaß gemacht hat, aber für Reina ist es eindeutig eine ernste Angelegenheit"
    show reina lecherous
    nar "es ist ziemlich offensichtlich, dass sie mit ihren Gedanken bei Miharu und bei niemandem anderen ist"
    show reina naughtydream
    nar "wenn das der Fall ist... wunderst du dich, ob... vielleicht..."
    show miharu confused
    show reina mesmerized
    k_sigh "Fein, dann werde ich mir selbst was holen..."
    show miharu happy at MoveTo(0.0, 0.5)
    show reina embarrassed at Bounce(1)
    m "Wenn das so ist, dann komme ich mit dir."
    show reina gulp at Bounce(3)
    $ renpy.pause(0.15)
    show reina overprotect at MoveTo(0.15, 0.25)
    show miharu cute
    r "NEIN, WARTET!"
    show reina tense
    nar "hehe, hab dich! "
    show reina awkward
    r "Okay, in Ordnung, lass mich eure BEIDEN Bestellungen aufnehmen."
    show miharu genki at Bow(1)
    show reina nervousblush
    m "Wirklich?! Danke vieeelmals!"
    show miharu smile
    show reina genki
    r "Kein Problem, Miharu Liebes."
    show ambient reinaglare
    with dissolve
    show reina evil
    nar "dein Siegeszug ist nur kurzlebig, als du das böse Grinsen sehen konntest"
    nar "schaudernd machst du dir sorgen, was für ein Gebräu sie dir wohl bringen wird"
    hide ambient reinaglare
    show prop foodbubble3 at Appear(0.85, 0.25, 0.5, 0.5)
    show prop foodbubble3 at Heft(0.55, 20)
    show miharu curious
    show reina shock
    ta "Und bringe mir etwas kalasan Brathähnchen, wenn du gerade dabei bist! Danke!"
    hide prop foodbubble3
    nar "..........."
    nar "du drehst dich sehr nervös in die Richtung des widerlichen Stimme"
    menu:
        "Solltest du laut schreien...?":
            jump a1k1_kya_de
        "…oder SEHR laut?":
            jump a1k1_gya_de
label a1k1_kya_de:
    show miharu uncomfortable
    k_swirl "KYAAAA!!"
    show reina huh at Bounce(1)
    r "ARGH?!!"
    show aizawa calm at EnterRight(1.0, 0.25)
    show miharu confused
    show reina chide
    ta "Was für eine halbherzige Reaktion ist denn das?!"
    jump a1k1_reaction_de
label a1k1_gya_de:
    show redsiren
    play sound sound_airraidsiren
    show miharu grief
    k_shock "GYAAAAAAAAAAAAAHHH!!!"
    show reina reprimand at Bounce(5)
    r "AAAAAAAAARGH?!!!"
    show aizawa savor behind redsiren at EnterRight(1.0, 0.25)
    $ renpy.pause(0.25)
    show aizawa squeal at Laugh(2)
    show miharu curious
    show reina ippenshindemiru
    ta "A-ha!  Na DAS ist eine Reaktion mit Leidenschaft, LOL!    "
    hide redsiren
    stop sound
    jump a1k1_reaction_de
label a1k1_reaction_de:
    show miharu glad at Bow(1)
    show aizawa snide
    show reina frustrated
    m "Guten Abend, Frau Aizawa."
    show miharu smile
    show aizawa grateful
    ta "Ah! Guten Abend, Miharu!"
    show miharu happy
    show aizawa amused
    show reina impatient
    m "Was führt sie hierher, Frau Aizawa?"
    show miharu cute
    show aizawa cute
    ta "Wieso, um freies Abendessen zu bekommen natürlich...~"
    show aizawa smug
    show miharu confused at ExitLeft(1.00)
    show reina smile at MoveTo(-0.4, 0.75)
    $ renpy.pause(1.25)
    hide miharu
    show reina angry at MoveTo(0.5, 0.15)
    show aizawa baka
    $ renpy.pause(0.25)
    show reina shout at Bounce(3)
    r "Sie sind keine Schülerin, schon vergessen?! Bezahlen sie es deshalb selbst!"
    show aizawa complain at Laugh(2)
    show reina angry
    ta "tsk tsk! Wie unhöflich, ich bin eine Schülerin, weiß du."
    show aizawa fatigue
    show reina chastise
    r "{b}WAR{/b} eine Schülerin..."
    show aizawa meditate
    play sound sound_gong
    show ambient zen behind reina at Appear(0.0, 0.0, 0.0, 0.0)
    with slowdissolve
    show aizawa lecture
    show reina bored
    ta "Mein Kind... Im Leben hört man niemals auf, Schüler zu werden."
    show aizawa pity
    show reina calm at Bounce(1)
    show ambient zen behind reina at Fling(0.0, 0.0, 0.0, 2.5, 0.75, 365)
    show reina nag
    r "Philosophieren sie nicht mit mir!  Sie haben die Schule vor fünf Jahre absolviert!"
    show reina complain
    r "Wenn sie also Essen haben wollen, BEZAHLEN SIE!"
    hide ambient zen
    show aizawa yelp at Bounce(2)
    show reina chide
    ta "Awww! Du bist böse!"
    show aizawa accuse
    ta "Die Höhe muss dich wohl sehr griesgrämig gemacht haben!"
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
    r "Wie sind... {p}... {p}...{=whispered}gleich groß....{/=whispered}"
    show aizawa orly at Laugh(4)
    show reina shameright
    ta "Oh-hohoho! Das könnte damals gestimmt haben..."
    show aizawa squeal
    show reina furiousblush
    ta "Aber jetzt bist du {b}RIESIG{/b}..."
    show angrytwitch at Appear(0.4, 0.1, 0.5, 0.5)
    show aizawa evilchuckle
    ta "Du bist größer und attraktiver als die ganzen Jungs!"
    show aizawa genki at Laugh(4)
    show reina impatient
    ta "Haha! Sei vorsichtig mein Prinz oder ich verknall' mich auch noch in dich, LOL!"
    show aizawa amused
    hide angrytwitch
    $ renpy.pause(2.5)
    show reina taunt at Laugh(3)
    r "hihihi!  Nun, versuchen sie ihr Glück..."
    show aizawa astound
    show reina mock
    r "da ich das Nächste bin, welche ein {b}LEBAY{/b} wie sie"
    show aizawa unamused
    show angrytwitch at Appear(0.9, 0.1, 0.5, 0.5)
    show reina evil
    r "...jemals als Freund haben werden."
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
    ta "Them's fightin' words!!"
    $ renpy.pause(2.0)
    nar "so witzig es auch sei, die beim kämpfen zu zuschauen,"
    nar "...so willst du die aufhalten, bevor die schlechte Aura auf die ganze Cafeteria über schwappt"
    stop music
    stop countermusic
    m "Also gut, das reicht!"
    show reina gulp at MoveTo(0.25, 0.25)
    show aizawa confuzzled at MoveTo(0.75, 0.25)
    nar "zum Glück greift Miharu für dich ein..."
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
    m "Kein Gewalt, okay? Denkt daran, wir sind alle Menschen...."
    m "Wir müssen miteinander auskommen und eine gute Beziehung aufbauen, ..."
    show reina bored
    m "...da es keinen Nutzen gibt, sich sich gegenseitig zu schlagen, oder?"
    show reina chide
    r "DOCH!"
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
    r "Ich bekomme die Rechtfertigung für die Rache..."
    show reina scold at Bounce(1)
    r "...nachdem sie versucht hatte, mich letztes Jahr mit der tödlichen Geburtstagstorte umzubringen!"
    show aizawa moronic
    show reina angry
    play music music_ridiculous fadein 2.0
    show prop blackforest1 behind reina at Appear(0.5, 0.4, 0.5, 0.5)
    with dissolve
    ta "Das ist gemein! Ich hatte hart daran gearbeitet, das zu machen!"
    show aizawa yelp at Bounce(2)
    show reina threaten
    ta "Ich habe drei Tage ohne Pause geschuftet!"
    show reina reprimand at Bounce(1)
    show aizawa pity
    r "Und sie haben es vier Tage draußen stehen lassen!"
    play countermusic sound_poison fadein 2.0
    show prop blackforest2 behind reina
    with slowdissolve
    show aizawa dumbfounded
    show reina pout
    r "Es tat ihnen nicht Mal Leid, als sie es mir voll mit wachsenden Dingen geschickt hatten, ..."
    show reina pout at Bounce(2)
    show aizawa nervous
    r "... und mir versicherten, dass das eine neue Sorte Schwarzwald Kuchen sei!"
    show miharu excited at EnterLeft (0.2, 0.25)
    show reina mope
    m "Haha! Ah! Ich denke, ich kann mich daran erinnern...!"
    stop countermusic
    hide prop blackforest2
    with dissolve
    show overlay hospital
    with dissolve
    show miharu happy
    show aizawa chastiseright
    show reina hopeless
    m "Wir wurden, nachdem wir davon gegessen hatten, bewusstlos und lagen eine ganze Woche wegen Lebensmittelvergiftung im Krankenhaus..."
    show miharu glad
    show aizawa schemeright
    show reina speechless
    m "Danach wurde Frau Aizawa als die \"Bäckerin des Todes\" bekannt."
    hide overlay hospital
    with dissolve
    show aizawa chortleright at Laugh(2)
    show miharu smile
    show reina impatient
    ta "Aber, aber, ihr müsst schon hier und da ein bisschen Schmerzen aushalten,"
    show aizawa orly
    ta "...damit ihr zu kräftige und gesunde Erwachsene aufwachsen könnt, LOL!"
    show aizawa nervous
    stop music
    $ renpy.pause(2.50)
    show reina ippenshindemiru
    r "{p}\"LOL\"...{p} NICHT... MIT... {b}MIR!!!{/b}"
    play music music_crazyfight3 fadein 1.0
    play countermusic sound_war fadein 2.0
    show miharu grief at Sit(0.25)
    show reina scold at MoveTo(0.25, 0.25)
    show aizawa shock at MoveTo(0.75, 0.25)
    $ renpy.pause(0.25)
    show reina shout at HChatter(0.25, 0.28)
    show aizawa scream at HChatter(0.75, 0.72)
    $ renpy.pause(2.0)
    nar "*seufz*... du kannst in etwa sehen, warum Reina wütend ist,"
    hide miharu
    show ambient fire behind reina
    with dissolve
    nar "aber nun wurde die Prügelei sogar lauter..."
    show crowd calm behind ambient
    with dissolve
    nar "tatsächlich drängen sich alle Schülerinnen in der Cafeteria um den Spektakel herum, um es zu sehen"
    k_unamused "Uff! Hört bitte auf, das ist peinlich!"
    show miharu nervous behind aizawa at EnterLeft (0.5, 0.25)
    $ renpy.pause(0.25)
    show miharu dread behind aizawa at HChatter(0.5, 0.52)
    m "Hört bitte auf!"
    show miharu grief at QuickFling (-1.0, -0.5, 0.5, 550)
    show prop chair behind crowd at Appear(0.1, 0.8, 0.5, 0.5)
    show prop chair behind crowd at SetPosition(0.2, -45.0)
    show prop chair behind crowd at SendTo(0.1, 0.45, 1.0)
    nar "aber sie prügeln sich weiter... es sieht so aus, als könnte sie niemand mehr aufhalten"
    hide miharu
    show angrytwitch at Appear(0.15, 0.35, 0.5, 0.5)
    u "{b}Habt ihr nicht gehört, was Miharu gesagt hat?!{/b}"
    u "{b}HÖRT MIT DIESER DUMMHEIT SOFORT AUF!!!{/b}"
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
    nar "du warst von der dröhnende Stimme und dem wuchtigen Stuhl, welches aus der Menge geschleudert wurde, überrascht"
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
    nar "Nachdem sich die Aufregung gelegt hat, marschiert ein edel aussehendes Mädchen zu ihnen rüber"
    show angrytwitch at Appear(0.35, 0.35, 0.5, 0.5)
    u "Nun gut .... scheinbar habt ihr beide meine Stimmung ruiniert..."
    hide angrytwitch
    u "Alles, was ich gewünscht hatte, war ein wenig Ruhe und Frieden, damit ich mein Abendessen genießen konnten..."
    u "*seufz* Aber jetzt sind sie... besonders sie Frau Aizawa..."
    show aizawa complain behind crowd at SendTo(0.8, 0.5, 0.15)
    ta "ICH SCHON WIEDER?!"
    show aizawa complain behind crowd at SendTo(0.8, 0.8, 0.25)
    u "...gekommen und haben es verdorben."
    hide reina
    hide aizawa
    show queen frown behind crowd at Heft(0.45, 3)
    u "Dies soll nicht ungestraft bleiben!!"
    nar "vermeidend in den neuen Drama hineingezogen zu werden, fragst du Miharu..."
    k_sarcastic "{=whispered}Ist sie auch eine von den Schwarzwald Opfern?{/=whispered}"
    show miharu concern at EnterLeft(0.0, 0.25)
    m "{=whispered}Jo...{/=whispered}"
    show miharu doubt
    k_sneaky "{=whispered}Hab's mir gedacht. Wer ist sie?{/=whispered}"
    show miharu concern
    m "{=whispered}Q.U.E.E.N.{/=whispered}"
    show miharu doubt
    k_dream "{=whispered}Oh, Q.U.E.E.N..... Q.U.E.E.N.....{/=whispered}"
    show miharu dread
    k_omg "{b}.....HÄHHHH?!!!{/b}"
    show queen frown behind crowd at Heft(0.45, 1)
    $ renpy.pause(0.25)
    show queen frown behind crowd at ExitRight(0.5)
    play music music_queen1 fadein 4.0
    nar "dein Geschrei unterbrach Q.U.E.E.N.'s Beschimpfung,"
    hide queen
    show queen lecture at EnterRight(1.0, 0.25)
    show miharu nervous at MoveTo(-0.3, 0.25)
    q "WER WAGT ES?!!"
    show queen frown
    nar "...und du befürchtest das Schlimmste, als sie sich plötzlich umdreht, um nach dem Täter zu blicken"
    nar "glücklicherweise hebt sich eine andere Stimme aus der Menge, um dich vor diese Gefahr zu retten"
    show freya berate at EnterLeft(0.0, 0.25)
    f "Bitte fang' nicht noch einen Theater an, Q.U.E.E.N!"
    show freya glare
    k_incredulous "Freya! Du bist auch hier!"
    show freya irked
    f "Natürlich, jeder im Wohnheim kommt hierher um zu essen."
    show freya troubled
    show queen bored
    nar "Jeder? Geizhälse..."
    show freya fury at MoveTo(0.5, 0.25)
    $ renpy.pause(0.25)
    show freya shout at Bounce(4)
    $ renpy.pause(0.5)
    show miharu confused at MoveTo(0.0, 1.0)
    f "{b}Okay Leute, kehrt zu euren Plätzen zurück! Es gibt nichts zu sehen!{/b}"
    show freya irritated
    hide crowd nervous
    with dissolve
    nar "die Menge stöhnte kollektiv, als sie wieder das tun, was sie ursprünglich getan hatten"
    show freya obligated at Sit (0.25)
    $ renpy.pause(1.0)
    show freya reprimand at Rise(0.5, 0.25)
    show aizawa aho at Rise(0.7, 0.25)
    $ renpy.pause(0.25)
    show miharu cute
    show queen frown
    f "Und Frau Aizawa, ich weiß nicht, wie oft ich es ihnen sagen muss,"
    show freya scold at Bounce(1)
    show aizawa confused
    f "...aber können sie nicht endlich nach Hause zurückkehren?!"
    show freya shout at Bounce(3)
    show aizawa confuzzled
    f "Hören sie auf sich wie ein Kind aufzuführen und seien sie ein gutes Beispiel für all die Schülerinnen hier!"
    show miharu smile
    show aizawa cry
    show freya irritated
    ta "Aber ich habe meine Miete nicht bezahlt und kann deshalb nicht zurück..."
    show aizawa weep
    show freya lecture
    show queen calm
    f "Haben sie nicht dieses Monatsgehalt bereits bekommen?"
    show aizawa whimper
    show freya irritated
    ta "Oh, natürlich, sie sind immer pünktlich mit der Bezahlung."
    show aizawa aho
    show freya leer
    ta "Aber... also... ich habe es für's Einkaufsbummel verprasselt..."
    show miharu uncomfortable
    show queen bored
    ta "...und als ich das bemerkte, war alles weg."
    show aizawa orly at Laugh(8)
    show freya angry
    show queen boredleft
    ta "Haha! Nun bin ich der Miete drei Monate hinterher, LOL!"
    show aizawa nervous
    stop music
    play sound sound_deadsilence
    show miharu nervous
    nar "Frau Aizawa bekam zu Recht ein paar Sekunden unangenehm stilles Schweigen"
    play music music_ridiculous fadein 5.0
    show freya defensive
    k_unamused "Das soll wohl ein Scherz sein..."
    show reina chide behind miharu at EnterLeft(-0.4, 0.25)
    r "Wie rücksichtslos..."
    show miharu sad at Bow(1)
    show reina leer
    m "Arme Frau--"
    show queen chideleft at Bounce(1)
    show miharu dread
    q "Schwachkopf."
    show aizawa calm at Laugh(3)
    show miharu confused
    show aizawa genki
    show freya annoyed
    show reina angry
    show queen boredleft
    ta "Haha!  Ich weiß!  Die Schulleiterin sagte das Gleiche, als ich ihr davon erzählte!"
    show aizawa happy
    ta "Deswegen gab sie mir die Erlaubnis, hier eine Weile zu wohnen."
    show miharu nervous
    show aizawa megasigh
    show freya evildream
    show angrytwitch at Appear(0.47, 0.18, 0.5, 0.5)
    show reina scowl
    show queen stareleft
    ta "*seufz* Wenn sie etwas mehr Mitleid hätte..."
    show aizawa pleasantdream at Laugh(2)
    show reina chastise
    show queen stareright
    ta "...und mir eines ihre Wohnhäuser, oder wenigstens ein Apartment geben würde...."
    show reina speechless
    show aizawa sweetdream
    hide angrytwitch
    $ renpy.pause(2.0)
    show freya psycho at Bounce(6)
    show miharu sigh
    show aizawa gasp
    f "{b}SCHÄMEN SIE SICH!!!{/b}"
    show aizawa cry
    play sound sound_stomachgrowl
    show freya shock
    show reina shock
    show queen stareleft
    $ renpy.pause(0.75)
    show miharu uncomfortable at Bounce(1)
    show freya surprised
    show queen meditate
    m "Ah! Das erinnert mich...!"
    show miharu grief at Bounce(2)
    show aizawa weep
    show reina gulp
    m "Ich habe mein bihun noch nicht bekommen!"
    show freya complain at MoveTo(0.35, 0.25)
    show miharu dread
    show reina embarrassed
    f "WAS HAT DIES UND DAS MITEINANDER ZU TUN?!"
    show reina awkward at Bounce(1)
    show aizawa whimper
    show freya bored
    r "Ack! Hab's vergessen!"
    show miharu sad
    show aizawa weep
    show reina nervousblush
    m "Nyuuuu....."
    show miharu doubt
    show aizawa whimper
    show reina shoo
    r "Tut mit Leid, ich hole es jetzt ...!"
    show aizawa weep
    show reina shoofrown at ExitLeft(0.5)
    show prop foodbubble4 at Appear(0.65, 0.5, 0.5, 0.5)
    show prop foodbubble4 at Heft(0.55, 20)
    show freya sigh
    show queen mumble
    q "Vergiss mein <gebratenen Reis> nicht.  Und mach es istimewa!"
    show aizawa whimper
    show reina huh at EnterLeft(-0.4, 0.25)
    hide prop foodbubble4
    show miharu confused
    show queen meditate
    r "Seit wann hast du~?  Argh~! Ohh, na gut!"
    show prop foodbubble5 at Appear(0.5, 0.45, 0.5, 0.5)
    show prop foodbubble5 at Heft(0.55, 20)
    show aizawa tearsofjoy at Laugh(2)
    show miharu uncomfortable
    show freya perturbed
    show reina furious
    ta "Und mein kalasan auch, hehe!"
    show prop foodbubble5 at QuickFling(1.5, 0.3, 0.5, 365)
    show reina reprimand at Bounce(3)
    show miharu nervous
    show aizawa moronic
    show freya perplexed
    show queen calm
    r "{b}HALTEN SIE DEN MUND! HOLEN SIE ES SICH SELBST!!!{/b}"
    show aizawa cry at Bow(1)
    show miharu smile
    show freya irked
    show reina furious
    ta "Hauu.... *schnüff*"
    show aizawa whimper
    show reina impatient at ExitLeft(0.25)
    show freya mocksideways
    nar "Reina stürzte davon, ließ dich wundern, ob sie überhaupt deine Bestellung gemerkt hat"
    show miharu smile at ExitLeft(0.25)
    show aizawa weep at Sit(0.25)
    show freya mocksideways at ExitRight(0.25)
    show queen calm at ExitRight(0.25)
    $ renpy.pause(0.25)
    stop music fadeout 3.0
    scene bg dormroom
    with dissolve
    outline "ZURÜCK IM ZIMMER"
    play music music_quirky
    show miharu genki at Rise(0.0, 1.0)
    m "Ah~! Bin ich voll...!"
    show miharu smile at VChatter
    k_painful "Natürlich bist du das!"
    show miharu glad at ExitLeft(0.25)
    $ renpy.pause(0.25)
    show prop nasgor at Appear(0.5, 0.5, 0.5, 0.5)
    with dissolve
    nar "Reina hatte sich wirklich an deinem nasi goreng erinnert und es war sicher zu essen"
    show prop nasgormini
    with dissolve
    nar "aber die Portion war so, dass du es in drei Bissen fertig hattest"
    nar "Gute Sache dass du schon etwas gegessen hattest"
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
    nar "auf der anderen Seite wurde Miharu mit beinahe zehn bihun goreng überrumpelt,"
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
    nar "...und zu deinem Schreck verschlang sie alles!"
    nar "\"Was für ein Stoffwechsel hat sie?!\", fragst du dich immer wieder"
    hide miharu
    show queen talk at EnterRight(1.0, 0.25)
    q "Wenn ich mich nicht täusche, war dein Name Hana, richtig?"
    show queen calm
    k_nervous "Äh... das wäre Kana...."
    show queen talk
    q "Ich bedaure die späte Begrüßung, aber es ist mir ein Vergnügen, deine Bekanntschaft zu machen."
    show queen calm
    stop music fadeout 2.0
    menu:
        "Benimmt dich einfach normal.":
            jump a1k1_nice1_de
        "Oh, mach es einfach wie sie.":
            jump a1k1_hermajesty_de
label a1k1_nice1_de:
    play music music_queen1
    k_glad "Ah!"
    k_genki "Es freut mich auch dich kennenzulernen, Q.U.E.E.N."
    show queen mumble at Laugh(1)
    q "Oh, du hast meinen Namen richtig ausgesprochen.  Wie gewissenhaft von dir."
    jump a1k1_question_de
label a1k1_hermajesty_de:
    play music music_royalty
    k_dream "*beug* Die Ehre ist ganz meinerseits, eure Hoheit."
    show queen mumble at Laugh(3)
    q "Oh-hoho! Wie drollig!"
    show queen rebuke
    q "Aber auch wenn ich eine <queen> wäre, verachte ich es ehrlich gesagt, anders genannt zu werden."
    show queen annoyed
    k_nervous "Oh... das tut mir Leid...."
    show queen mumble at Laugh(2)
    q "Hoho! Das ist völlig in Ordnung.  Du bist neu, deshalb drücke ich ein Auge zu."
    show queen comment
    q "Aber nur dieses eine Mal...."
    show queen stare
    k_gasp "?!! "
    k_nervous "Hehe, ähm..."
    jump a1k1_question_de
label a1k1_question_de:
    show queen calm
    k_happy "Darf ich eine Frage stellen?"
    show queen talk
    q "Sicherlich."
    show queen calm
    k_glad "Ist \"Q.U.E.E.N.\" dein richtiger Name oder so...?"
    show queen chide
    q "Es ist, für dich."
    show queen bored
    nar "\"Das hat nicht Mal meine Frage beantwortet!\", wunderst du dich..."
    show miharu genki at EnterLeft(0.0, 0.25)
    show queen stareleft
    m "Jep! Q.U.E.E.N. ist Q.U.E.E.N.!"
    show miharu glad at Laugh(2)
    m "Kein Zweifel, hehe!"
    stop music fadeout 2.0
    show queen stareright at ExitRight(0.5)
    show miharu doubt at MoveTo(-0.3, 1.0)
    nar "während Q.U.E.E.N. abgelenkt war, bringt dich Miharu in die Ecke und flüstert dir zu...."
    show miharu concern
    m "{=whispered}Frag nicht, oder du wirst von der Puppe verflucht....{/=whispered}"
    show miharu doubt
    k_ehhh "{=whispered}Häh?{/=whispered}"
    show miharu concern
    m "{=whispered}Haku, ihr Lieblingspuppe.{/=whispered}"
    show miharu dread
    m "{=whispered}Es ist nicht irgendeine Puppe, es ist für Voodoo....{/=whispered}"
    play music music_haku
    menu:
        "Ja sicher.":
            jump a1k1_kidding_de
        "Oh nein, nicht noch mehr verrückte Leute...":
            jump a1k1_scary_de
label a1k1_kidding_de:
    show ambient haunted behind miharu
    with slowdissolve
    show miharu nervous
    k_sarcastic "{=whispered}Das soll wohl ein Scherz sein...{/=whispered}"
    show hauntedtwirl behind miharu
    with dissolve
    show miharu confused
    m "{=whispered}Ich meine das ernst!{/=whispered}"
    show creepyqueenhaku behind miharu
    with dissolve
    show miharu dread
    m "{=whispered}Sein voller Name ist SHI NO HAKUSHAKU!{/=whispered}"
    m "{=whispered}Das heißt soviel wie \"Graf des Todes\"!{/=whispered}"
    show miharu nervous
    k_sneaky "{=whispered}Häh~?!!{/=whispered}"
    jump a1k1_proof_de
label a1k1_scary_de:
    k_incredulous "Whoa!! BEÄNGSTIGEND~!!!"
    show miharu worried
    m "{=whispered}Ist es, nicht?{/=whispered}"
    jump a1k1_proof_de
label a1k1_proof_de:
    show miharu dread
    m "{=whispered}Und Reina hat Beweise von seiner Macht~{/=whispered}"
    k_panic "{b}REINA?!!{/b}"
    hide ambient haunted
    hide hauntedtwirl
    hide creepyqueenhaku
    show queen hakuchideleft at EnterRight(1.0, 0.5)
    show miharu nervous
    q "So so... Redet ihr Kinder nun hinter meinen Rücken?"
    show miharu uncomfortable at MoveTo(0.0, 0.25)
    show queen hakuboredleft
    m "Oh nein, ganz und gar nicht~!"
    show miharu whimper
    k_nervous "Haha! Öh... wie kommst du darauf?"
    show queen hakuannoyed at Bounce(1)
    show miharu doubt
    q "Hmpf!"
    stop music fadeout 1.0
    play sound sound_doorslam
    $ renpy.pause(0.5)
    nar "dann betritt Reina das Zimmer mit einem Krachen"
    play music music_reina1 fadein 2.0
    queue music [ music_reina2, music_reina1 ]
    show miharu cute
    nar "einmal nun, an diesem Abend, bist du glücklich sie zu sehen"
    show reina relieved behind miharu at EnterLeft(0.5, 0.5)
    show miharu happy
    show queen hakucalm
    r "Ahhh~!! endlich zu Hause~!!"
    show miharu genki at Laugh(2)
    show reina tenderblush
    m "Willkommen zurück, teehee~!"
    show reina coo at MoveTo(0.1, 0.25)
    show miharu cute
    r "Miharu Liebes, hast du mich bereits vermisst~?!"
    show queen hakustareleft
    nar "als wäre das Umschwärmen um Miharu beim Abendessen nicht genug,"
    show miharu smile at ExitLeft(0.75)
    show reina hentai at ExitLeft(0.75)
    nar "...hetzt sie nun auch ins Zimmer zu Miharu und umarmte sie"
    show lotsoflove
    nar "du hoffst, dass das nicht lange anhalten wird..."
    show queen hakustare
    k_nervous "Reina ist... etwas besessen von Miharu, oder nicht?"
    show queen hakucomment
    q "Das ist wirklich nicht meine Sorge."
    q "...Aber ja, so etwas in der Richtung."
    show queen hakuboredleft at MoveTo(0.7, 1.0)
    nar "du willst sie was anderes fragen, aber sie hat stattdessen ihre Aufmerksamkeit auf \"das Paar\" gerichtet"
    show queen hakuchideleft at Bounce(2)
    q "Ich hasse es euch zu unterbrechen, aber wo um alles in der Welt warst du die ganze Zeit, Rei?!"
    hide lotsoflove
    show reina complain at EnterLeft(-0.4, 0.25)
    show queen hakuboredleft
    r "Abwaschen natürlich.  Ich bin heute für das Aufräumen zuständig, weiß du."
    show reina threaten at Bounce(6)
    r "*starr* Und ich musste die DOPPELTE Arbeit machen, einschließlich DEINE!!!"
    show queen hakucommentleft at Laugh(1)
    show reina furious
    q "Ah, ich verstehe!  Du hast meinen Dank.  Mach weiter so."
    show reina suspicious at Bounce(3)
    show queen hakustareleft
    r "*nörgel*"
    show miharu sigh at EnterLeft(0.0, 0.5)
    show reina curious
    show queen hakucalm
    m "*gähn*  Es wird irgendwie spät.  Wir sollten früh ins Bett."
    show reina yawn at Bow(1)
    show miharu tired
    r "Ja, Ich bin völlig erschöpft nach allem...*gähn*"
    show queen hakumumble at Bounce(1)
    show reina tired
    q "Dann sage kein Wort mehr.  Wir sollten augenblicklich ins Bett gehen!"
    show reina sleepy at ExitLeft(0.5)
    show miharu sigh at ExitLeft(0.5)
    show queen hakumeditate at ExitRight(0.5)
    $ renpy.pause(0.5)
    stop music fadeout 3.0
    scene black
    with dissolve
    nar "zwar nicht so augenblicklich wie gesagt, haben alle die Zähne geputzt, sind im Schlafanzug, und waren innerhalb von nur wenigen Minuten im Bett"
    nar "das gilt auch für dich"
    scene bg dormroom2
    with dissolve
    q "Allem angenehme Träume."
    m "Danke Q.U.E.E.N.!  Gute Nacht allesamt!"
    r "Gute Nacht, nur meiner Miharu Liebes!"
    q "Willst du mir nicht auch eine gute Nacht wünschen?"
    r "Nein, du kannst eine Schlechte haben, hehe."
    q "Narr."
    k_genki "Gute Nacht alle! Es war wirklich schön, euch heute kennenzulernen!"
    m "Es war auch schön dich kennen zu lernen! Wir sehen uns dann Morgen!"
    r "In aller Frühe! Oder wir werfen dich aus dem Bett!"
    q "Vielleicht."
    k_nervous "hehe... öh, okay..."
    nar "Reina und Q.U.E.E.N. drehen sich um und waren bereits eingeschlafen"
    nar "Miharu streckte ihr Arm aus, um das Licht auszuschalten"
    play sound sound_lightswitch
    scene bg dormroom3
    nar "und es war nur in der völligen Dunkelheit..."
    nar "...als sie das warme Leuchten des Netbooks, den du gerade benutzt, bemerkt hat"
    play music music_calm1 fadein 5.0
    m "Oh, wirst du nicht schlafen?"
    k_smile "Ich werde gleich.  Nur noch ein paar Dinge zu tun."
    m "Okay... bleib' nicht zu lange wach. Gute Nacht..."
    k_relieved "Nacht..."
    nar "innerhalb wenigen Sekunden ist auch Miharu eingeschlafen"
    show prop unr1 at DissolveAppear(0.09, 0.3, 0.0, 0.0, 0.5)
    show overlay netbook at DissolveAppear(0.03, 0.2, 0.0, 0.0, 0.5)
    nar "du bist dankbar das die Netbook-Tastatur und das Trackpad flüsterleise sind"
    show prop unr2
    with quickdissolve
    nar "so kannst du tippen und im Internet surfen, ohne jemanden aufzuwecken"
    show prop unr3
    with quickdissolve
    nar "du überprüfst die Nachrichten des Tages, Projekte, mit dem du zu tun hattest"
    show prop unr5
    with quickdissolve
    nar "neue Artwork, Spiele und Musik,"
    show prop unr4
    with quickdissolve
    nar "...und andere Seiten, die du für gewöhnlich besuchst"
    show prop unr6
    with quickdissolve
    stop music fadeout 3.0
    nar "du öffnest dein E-Mail-Programm und findest nur ein paar Schnellantworten"
    play music music_netbook1 fadein 5.0
    scene bg email1
    with dissolve
    nar "nach dem Entrümpeln ist da nur noch das Verfassen einer weiteren Nachricht..."
    nvl clear
    nvl show dissolve
    play countermusic sound_typing
    net "<Liebe Cyllia...>"
    net "<Ich hatte mein erste Schultag heute, und ZOMG, ich schwöre, ich wurde in einer anderen Dimension geschickt!>"
    net "<Ich hatte diese verrückte Lehrerin, die vermutlich aus dem Irrenanstalt entkam.> >.<"
    net "<Und ich lief auch noch immer wieder allen Arten von einzigartigen und einfach nur komischen Leuten über den Weg.>"
    net "<Zum Kuckuck, ich teile ein Zimmer mit DREI von denen LOL!!!> ^^;"
    net "<Aber dennoch... möchte ich weiter optimistisch denken.>"
    net "<Nachdem ich die ein wenig besser kenne, bin ich mir sicher, dass die nette Leute sind.>"
    net "<Oder vielleicht treiben sie mich auch zum Wahnsinn, hahaha....!> ^___^'"
    stop music fadeout 3.0
    net "<Also, ich denke dass das für heute reicht. Ich werde dir später mehr von ihnen erzählen.>"
    net "<Mach dir einen schönen Tag morgen und wünscht mir Glück!> ^^"
    nvl hide nodissolve
    show ambient darken
    $ mouse_visible = False
    play music music_ED1a fadein 25.0
    queue music [ music_ED1b, music_silence ]
    $ floatingtext1 = Text("<Gute Nacht...!>\n\n...\n\n<LOL! Ich hab's vergessen, es ist bestimmt Tag bei euch!>\n<Hab' einen guten Tag dann!> ^____^\n\n<Mit freundlichen Grüßen ,>\nKana-chan ^____^v\n\n\nPS:\n<.....Vergib mir für mein mieses Deutsch.> ^^;", slow=True, slow_speed=10, style="emailed")
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
    
