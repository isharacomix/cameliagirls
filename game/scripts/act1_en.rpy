# en
# Act 1 starts here.
init:
    # Declare language-specific characters used by this game.
    if persistent.lang == "english":
        $ classroom = "Class"
        $ teacher = "Teacher"
        $ unknown = "Unknown"
label a1k1_start_en:
    scene black
    play music music_netbook1
    $ renpy.pause(1.0)
    scene bg sunrise
    with introfade
    nvl clear
    nvl show dissolve
    play countermusic sound_typing
    net "<Dear Cyllia...>"
    net "<I've finally arrived here at the Camelia All-Girls Academy...>"
    net "<Starting today, I will live here in the dorm like my parents wanted me to...>"
    nvl hide dissolve
    stop countermusic
    scene bg academy
    with fade
    k_happy "Ah! If only you could feel how fresh the morning air is..."
    k_relieved "And how beautiful the sunrise looks..."
    k_genki "I can't wait to see what kind of story awaits me here--"
    stop music
    $ renpy.play(sound_collide)
    with vpunch
    nar "seems someone has just collided with you..."
    nar "...and you fall to the ground"
    show miharu grief at Fling(-0.5, 0.35, 1.5, 1.5, 1.0, 730.0)
    u "Hiyaaaah!!"
    nar "but so does she..."
    play music music_miharu1
    menu:
        "You're okay, but maybe she's hurt?":
            jump a1k1_okay_en
        "Stupid ditz, doesn't watch where you're going!":
            jump a1k1_eyes_en
        "Hehe, she looks spacey. Play a small prank.":
            jump a1k2_bone_en
label a1k1_okay_en:
    k_worried "Ouch... Ah! Are you alright?"
    show miharu whimper at Rise(0.5, 1.0)
    u "I'm so sorry. Yeah I'm fine, thank you, how about you?"
    k_relieved "Fine here too."
    show miharu relieved
    u "I'm so glad to hear that."
    show miharu uncomfortable at Bounce(1)
    u "Ah! Damn! I'm going to be late!"
    show miharu smile
    u "Sorry, but I have to go, so..."
    show miharu genki at ExitLeft(0.75)
    u "SEE YAAAA~!"
    k_nervous "Huh?"
    jump a1k1_who_en
label a1k1_eyes_en:
    k_furious "Hey! Are you blind or something?!"
    show miharu grief at Rise(0.5, 0.25)
    u "HIYAAAHHH~!! I'M SO SORRY!!"
    show miharu uncomfortable at Bounce(1)
    u "Ah! Damn! I'm going to be late!"
    show miharu nervous
    u "Sorry again, but I have to go now... So..."
    show miharu grief at ExitLeft(0.5)
    u "SEEEEEEE YAAAAAAAAAA........!!"
    k_shout "Hey! COME BACK HERE!!"
    k_stare "...."
    k_unamused "....ah.... she's already gone....."
    jump a1k1_who_en
label a1k2_bone_en:
    k_sneaky "OWW!! MY LEG!!! IT'S BROKEN!!! I'M WRITHING IN PAIN!!!"
    show miharu grief at Rise(0.5, 0.5)
    u "Gyaaaah!! What have I done?!!!"
    show miharu dread at Bounce(2)
    u "Must call hospital~! Must call hospital~!"
    k_genki "Oi.... I'm just kidding."
    show miharu grief at Bounce(1)
    u "AH! I'M GOING TO BE LATE TOO!"
    show miharu confused at Bounce(2)
    u "What should I do~? What should I do~?"
    k_weird "Oi.... did you hear me?"
    show miharu whimper
    u "Yes.....*sob*"
    k_smug "Sorry... but I was actually just kidding..."
    show miharu grief at Bounce(4)
    u "NOT TRUE! YOUR LEG IS ALL BROKEN BECAUSE OF ME!!"
    k_ehhh "Eh?!"
    show miharu cautious at Bow(1)
    u "I promise I'll take full responsibility! But after I get back from my work..."
    k_weird "Errrr.... Okay...."
    show miharu uncomfortable
    u "Please try to get someone to take you to a hospital...!"
    show miharu whimper at ExitLeft(0.75)
    u "See ya!"
    k_gasp "AH--!"
    k_unamused "..."
    k_sarcastic "Was that a \"Hit-and-Run\"?"
    jump a1k1_who_en
label a1k1_who_en:
    k_sigh "...."
    show miharu smile at RunInDistance(-0.5, 1.5, 0.6, 0.75)
    nar "she runs off, leaving the school grounds"
    nar "who was that girl anyway?, you wonder"
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
    t "Okay class!"
    t "Like I mentioned yesterday, we have a new transfer student who will be joining us today."
    show aizawa grateful
    t "Come in, Miss Transfer Student! Introduce yourself!"
    show aizawa smile at ExitLeft(1.0)
    nar "you walk into the classroom, trying hard not to be nervous from all the stares"
    k_happy "Hello everyone... My name is Kana."
    k_genki "It's very nice to meet you..."
    show crowd nervous behind aizawa at Rise(0.50, 0.50)
    c "{=whispered}Nice to meet you too....{/=whispered}"
    show crowd nervous at Sit(0.75)
    nar "did they all just sound bored?"
    show aizawa sigh at EnterLeft(0.0, 0.5)
    t "*sigh*"
    show aizawa resign
    t "What a generic introduction..."
    show aizawa fatigue
    stop music
    k_nervous "Eh?!"
    nar "you can hear the whole class whispering: \"ahhh... she's at it again...\""
    show aizawa chastisecenter
    t "Where's your PASSION, Hana?! Your lack of PASSION disturbs me...!"
    show aizawa sadistic
    t "DO IT OVER!!"
    show aizawa revenge
    play music music_aizawa2
    k_omg "EHHHHHH?!!!"
    k_nervous "...."
    k_genki "Is this some kind of freshman joke or something...?"
    show aizawa reprimand at Bounce(2)
    t "Absolutely not!"
    show aizawa maniac
    t "NOW DO IT OVER OR ELSE!!!"
    show aizawa astound at ExitLeft(0.25)
    k_swirl "GYAAHHHH~!! OKAY! OKAY!"
    k_nervous "ehem...."
    menu:
        "You should just play it safe...":
            jump a1k1_hana_en
        "She wants passion? GIVE HER PASSION!!!":
            jump a1k1_sama_en
        "Oh! Just blurt out whatever crosses your mind...":
            jump a1k1_legend_en
label a1k1_hana_en:
    k_genki "My name is Kana, not Hana."
    stop music
    play sound sound_deadsilence
    c "{=whispered}*........silence..........*{/=whispered}"
    nar "you're almost sure you're done for..."
    show aizawa chortlecenter at EnterLeft(0.0, 0.75)
    t "Okay, you pass..."
    show aizawa schemecenter
    k_panic "THAT'S ALL?!!"
    jump a1k1_intro_en
label a1k1_sama_en:
    stop music
    k_creepy "{=whispered}fufufu...{/=whispered}"
    play music music_pompous1
    k_evil "I AM THE GREAT AND ALMIGHTY KANA-SAMA!!"
    k_villainous "BOW BEFORE ME, MORTALS~!"
    stop music
    play sound sound_deadsilence
    c "{=whispered}*........silence..........*{/=whispered}"
    nar "\"I pity her...\", you hear your classmates whispering amongst themselves"
    nar "how embarrassing..."
    play music music_aizawa2
    show aizawa obsessed at EnterLeft(0.0, 0.25)
    t "BRAVO!!!"
    show aizawa love
    t "WHAT A MAGNIFICENT INTRO!!! I'M SO HAPPY I COULD CRY!!!"
    show aizawa tearsofpride
    k_ehhh "EH?!!!"
    show aizawa squeal
    t "I like you already, sister!"
    show aizawa savor
    k_waterfall "What's going on here?!"
    k_angry "And I'm not your sister!"
    show aizawa sweetdream
    nar "you notice the teacher has stopped paying attention to you"
    jump a1k1_intro_en
label a1k1_legend_en:
    k_squeal "I am Legend!"
    stop music
    play sound sound_embarrass
    c "*........groans..........*"
    nar "\"Oh why did I just say the first SILLY thing to cross my mind?\", you wonder"
    show aizawa orly at EnterLeft(0.0, 1.0)
    t "I see.... You like to watch movies of that Smith guy."
    show aizawa snicker
    k_panic "It's not like that...!"
    show aizawa chortlecenter
    t "Awww, you don't need to be shy about it. It seems all you young ones love that Smith guy."
    show aizawa schemecenter
    show crowd angry behind aizawa at Rise(0.5, 0.25)
    c "STOP TALKING NONSENSE!!"
    show crowd angry at Sit(0.25)
    jump a1k1_intro_en
label a1k1_intro_en:
    show aizawa cute
    t "Very well... I shall introduce myself to you then..."
    show aizawa smile
    stop music fadeout 1
    play sound sound_spotlight
    show ambient darken behind aizawa
    show prop spotlight at Appear(0.0, 0.0, 0.0, 0.0)
    nar "a spotlight?!"
    play music sound_drumroll
    show aizawa awesome
    t "I AM THE GREAT~!"
    show aizawa evilchuckle
    t "FABULOUS~!"
    show aizawa love
    t "MAGNIFICENT~!"
    show aizawa impressed
    t "AWE-INSPIRING~!"
    show aizawa happy
    t "LEGENDARY~!"
    show aizawa pleasantdream
    t "{=whispered}and most important of all...{/=whispered}"
    show aizawa grateful
    t "BEAUTIFUL~!"
    stop music
    play sound sound_drumtada
    show aizawa squeal at Bounce(1)
    t "TEACHER AIZAWA!!!"
    play music music_pompous2
    show aizawa smile at MoveTo(0.5, 1.0)
    hide ambient darken
    with dissolve
    hide prop spotlight
    with dissolve
    with Pause(1)
    show snowblossom
    with dissolve
    nar "she strikes a dramatic pose a little too close to you"
    show aizawa genki
    ta "Nice to meet ya'!"
    show aizawa smile
    stop music fadeout 2
    hide snowblossom
    with dissolve
    k_weird "errr.... uh.... okay.... Nice to meet you too.... Ms. Aizawa...."
    queue music [ music_aizawa3, music_aizawa4, music_aizawa5 ]
    show aizawa lecture at MoveTo(0.0, 0.5)
    ta "ARISE, CLASS REP!"
    show aizawa meditate
    show freya lecture behind aizawa at Rise(1.0, 0.25)
    f "My name is Freya!!"
    show aizawa complain
    show freya irritated
    ta "It's hard to remember about a thousand students' names, y'know."
    show aizawa fatigue
    show freya shout at Bounce(3)
    f "At least remember the names of the students IN YOUR OWN CLASS!"
    show aizawa chortleleft
    show freya scowl
    ta "I'm not your homeroom teacher, so I can't be bothered with that stuff...."
    show aizawa schemeleft
    show freya annoyed
    show crowd shout behind freya at Rise(0.5, 0.25)
    c "YOU {b}ARE{/b} OUR HOMEROOM TEACHER!!"
    show crowd calm
    show aizawa confuzzled
    ta "Really? I thought I was the homeroom teacher for 2-C...?"
    show aizawa confused
    show crowd angry
    show freya bored
    c "THIS {b}IS{/b} 2-C!!"
    show crowd calm
    k_unamused "...."
    show aizawa resign
    nar "suddenly running out of the school doesn't sound so bad after all..."
    show aizawa genki at Laugh(3)
    show freya pout
    ta "Hahaha! Oh, don't mind the little things..."
    show aizawa smug
    show freya nag
    f "What exactly do you mean by \"little things\"?!"
    show aizawa awesome
    show freya upset
    ta "Whatever... Have you done yesterday's homework assignment?"
    show aizawa snide
    show crowd shout
    show freya angry
    c "What homework?"
    show crowd calm
    show aizawa evilchuckle
    ta "Why, the Modern History Class homework of course."
    show aizawa smug
    show freya calm at Bounce(1)
    show freya annoyed
    f "But you're our English teacher."
    show aizawa dumbfounded at Laugh(2)
    ta "Eh? Ara! I forgot, LOL!"
    show aizawa nervous
    show crowd shout
    show freya tired
    c "DON'T \"LOL\" US!"
    show crowd calm
    show aizawa sadistic
    show freya perturbed
    ta "Oh! Just gather your homework already."
    show crowd angry
    show aizawa revenge
    show freya angry
    c "LIKE WE SAID, WHAT HOMEWORK ARE YOU TALKING ABOUT?!"
    play countermusic sound_chatter fadein 0.25
    show crowd angry at VChatter
    show aizawa reel at MoveTo(0.25, 0.25)
    show freya defensive at MoveTo(0.75, 0.25)
    $ renpy.pause(0.25)
    show aizawa scream at HChatter(0.25, 0.28)
    show freya shout at HChatter(0.75, 0.72)
    nar "you had hoped for a normal first day, but this chaos was just the beginning..."
    show crowd angry at Sit(0.25)
    show aizawa savor at ExitLeft(0.25)
    show freya bloodlust at ExitRight(0.25)
    $ renpy.pause(0.25)
    stop music fadeout 2
    stop countermusic fadeout 0.5
    scene bg cafeteria
    with fade
    outline "Lunch Break"
    play music music_roughday fadein 2.0
    k_sigh "*sigh*"
    nar "you're so exhausted, you can't even lift your food"
    show freya nervouschuckle at EnterLeft(0.0, 0.5)
    f "I feel so sorry for you."
    show freya nervous
    k_nervous "Why?"
    show freya covet
    f "Ms. Aizawa...."
    show freya bashful
    menu:
        "Well you have to admit, she's one of a kind...":
            jump a1k1_interesting_en
        "You're worried she escaped from an asylum...":
            jump a1k1_crazy_en
        "She might be quirky, but she has a good heart.":
            jump a1k1_nice_en
label a1k1_interesting_en:
    k_sneaky "She's an... interesting person..."
    show freya glad
    f "Well... I guess we can say she's... \"unique\""
    show freya smile
    k_sarcastic "Unique like a rare animal?"
    show freya cute at Bounce(1)
    f "Exactly!"
    jump a1k1_classified_en
label a1k1_crazy_en:
    k_painful "She's crazy!"
    show freya nervouschuckle
    f "That she is...."
    jump a1k1_classified_en
label a1k1_nice_en:
    k_genki "I think she's a really nice person."
    show freya omg at Laugh(2)
    f "HAAAH?! YOU GOT BRAINWASHED?!"
    show freya nervous
    k_oops "...?"
    jump a1k1_classified_en
label a1k1_classified_en:
    show freya glad
    f "By the way...."
    f "Can I ask you something?"
    show freya smile
    k_happy "Okay..."
    show freya sarcastic
    f "Why did you transfer here, Kana?"
    show freya uneasy
    stop music fadeout 1
    k_sad "...?"
    k_oops "There's something wrong with this school?"
    $ renpy.pause(1.0)
    show freya bashful
    $ renpy.pause(0.5)
    show freya tender
    $ renpy.pause(0.25)
    show freya love
    f "Oh, I didn't mean it that way. I'm just curious."
    show freya cute
    f "Everyone I've talked to always has a fascinating story to tell about that."
    show freya calm
    play music music_flashback1 fadein 2.0
    k_dream "I see... Well...."
    show freya curious at ExitLeft(0.25)
    $ renpy.pause(0.25)
    scene bg flashback1
    with flashbackfade
    k_happy "My parents sent me here because they went overseas on business..."
    k_sad "...and won't return for a long time."
    scene bg flashback2
    with flashbackfade
    k_happy "I don't have any relatives here,"
    k_genki "...so they trusted me to the Headmaster because she's an old friend of theirs."
    scene bg flashback3
    with flashbackfade
    k_tired "Come to think of it, I didn't have much say in the matter."
    k_happy "But still..."
    k_dream "I'm confident I'll have a wonderful time here at Camelia!"
    scene bg cafeteria
    with flashbackfade
    show freya sweetdream at EnterLeft(0.0, 0.5)
    f "*nod nod*"
    k_relieved "What about you, Freya?"
    show freya pleasantdream
    f "Kinda the same as you..."
    show freya sweetdream
    stop music
    k_nervous "..."
    play music music_roughday
    k_unamused "In other words, that wasn't fascinating at all."
    show freya mock
    f "It had its moments."
    show freya snicker
    k_sigh "*sigh*"
    show freya tender at ExitLeft(0.25)
    $ renpy.pause(0.25)
    stop music fadeout 2
    scene bg classroom
    with fade
    outline "After School"
    play music music_aizawa4 fadein 2.0
    show aizawa pleasantdream at EnterLeft(0.0, 0.25)
    ta "Well I think that's all for today."
    show aizawa glad
    ta "If you still have any questions, please save them for--"
    play sound sound_doorslam
    show aizawa astound
    nar "the door bursts open"
    show aizawa amused at MoveTo(1.0, 0.25)
    show miharu grief behind aizawa at EnterLeft(0.0, 0.25)
    u "SORRY I'M LATE! REALLY!!"
    k_shock "AH! YOU!!"
    show aizawa naive
    show miharu confused
    u "You...?"
    u ".....who.....?"
    show miharu nervous
    show aizawa inquisitive
    k_sneaky "We \"met\" at the front gate, remember?!"
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
    ta "I see, you two know each other from before...?"
    show aizawa evilsmile
    k_angry "NO!"
    show aizawa grateful
    ta "So what's with this friendly attitude?"
    show aizawa drunksmile
    k_stare "You call that friendly?"
    show miharu cute
    show aizawa awesome
    ta "By the way.... You're finally here Miharu, but we're already finished for the day."
    show miharu sad at Bow(1)
    show aizawa snide
    m "I'm sorry..."
    show aizawa genki at Laugh(3)
    ta "Hahaha! Not a problem... I'm such a nice person, so I forgive you..."
    show crowd angry behind miharu at Rise(0.50, 0.25)
    show miharu happy
    show aizawa smile
    c "WHO'S THE NICE PERSON?!!"
    show crowd angry at Sit(0.25)
    show miharu cute
    show aizawa happy
    ta "You can stop by later in the Staff Room and pick up a handout for today's lesson."
    show miharu genki at Bow(1)
    show aizawa smile
    m "Thank you very much! You are the best, Ms. Aizawa!"
    show miharu smile at ExitLeft(0.25)
    show aizawa squeal at Laugh(3)
    ta "Hahaha!"
    show aizawa savor
    show crowd nervous behind aizawa at Rise(0.50, 0.25)
    c "You've got to be kidding..."
    show crowd nervous at Sit(0.25)
    show aizawa orly
    ta "Well then, that's all! Don't forget your homework this time!"
    show aizawa snicker at ExitRight(0.25)
    show crowd angry behind aizawa at Rise(0.50, 0.25)
    c "BUT YOU DIDN'T GIVE US ANY!!!"
    show freya chide at Rise(0.50, 0.25)
    f "*sigh* What a troublesome teacher we have.... "
    show crowd calm
    show freya annoyed at Sit(0.25)
    $ renpy.music.set_volume(0.25, 1, channel="music")
    play countermusic sound_chatter fadein 1.0
    show crowd calm at VChatter
    nar "with the teacher gone from the room..."
    nar "the bustling sound of your classmates shuffling their belongings and chatting..."
    nar "...actually sounds peaceful by comparison"
    stop countermusic fadeout 2.0
    $ renpy.music.set_volume(1, 1, channel="music")
    m "Ah Freya!"
    play countermusic music_miharu3 fadein 3.0
    stop music fadeout 3.0
    show crowd calm at Sit(0.25)
    show miharu happy at EnterLeft(0.0, 0.25)
    show freya cool at EnterRight(1.0, 0.25)
    m "Sorry for troubling you again, but can you let me look at your notes?"
    m "I'll draw something for you in exchange..."
    show freya cute
    f "Ah, you don't have to... I'm glad to help."
    show miharu genki at Bounce(1)
    show freya calm
    m "You are such a good friend, the best I've ever had!"
    show freya curious
    show prop bookworm at Appear(0.15, 0.4, 0.0, 0.0)
    with dissolve
    $ renpy.pause(0.5)
    show miharu relieved
    show freya angry
    m "That's why this drawing--"
    show prop bookworm at MoveTo(0.8,1.0)
    $ renpy.pause(1.0)
    show freya psycho at Bounce(3)
    show prop bookworm at Fling(0.8, 0.4, -0.30, 0.35, 0.35, 1095)
    $ renpy.pause(0.15)
    show miharu grief at Fling (0.0, 0.0, -1.0, -0.5, 0.5, 790)
    $ renpy.play(sound_collide)
    stop countermusic
    hide prop bookworm
    f "I don't need it! Just take these notes already!!"
    hide miharu
    queue music [ music_miharu1, music_miharu3 ]
    show freya disturbed
    $ renpy.pause(1.00)
    show freya meditate
    $ renpy.pause(0.50)
    nar "you wonder... nah, you're sure it's just your imagination..."
    show freya glad at Bounce(1)
    f "Ah! That reminds me! Kana, this is Miharu. She'll be your roommate over at the dorm."
    show freya smile at ExitRight(0.25)
    show miharu happybandage at EnterLeft(0.5, 0.5)
    m "So this is the transfer student."
    show miharu uncomfortablebandage
    m "I'm very sorry for the trouble I caused you this morning."
    menu:
        "That's so sweet, she's still worrying about you.":
            jump a1k1_forget_en
        "Oh no! She's not getting away THAT easily!":
            jump a1k1_hell_en
label a1k1_forget_en:
    k_relieved "It's okay, I already forgot about it."
    show miharu relievedbandage
    m "What a kind person you are...."
    k_genki "By the way, it's nice to meet you Miharu."
    jump a1k1_conclusion_en
label a1k1_hell_en:
    play sound sound_thunder
    show lightning
    show miharu dreadbandage
    k_furious "How the HELL can I forget THAT?!"
    hide lightning
    show miharu griefbandage at Bow(1)
    m "Hiyaaaahhhhhh...!! Sorryyyyy..!!"
    k_scheme "But I guess I'll let it slide, so..."
    show miharu curiousbandage
    k_genki "...Nice to meet you Miharu."
    jump a1k1_conclusion_en
label a1k1_conclusion_en:
    show miharu excitedbandage
    m "Nice to meet you too, Kana."
    show freya cute at EnterRight(1.0, 0.25)
    show miharu cutebandage
    f "Well...."
    f "I think it's about time we head back to the dorm."
    show freya calm at ExitRight(0.25)
    show miharu smilebandage at ExitRight(0.5)
    $ renpy.pause(0.5)
    stop music fadeout 3.0
    scene bg dorm
    with introfade
    outline "Camelia Dorm"
    play music music_mellow
    scene bg dormhall
    with dissolve
    show freya keen at EnterRight(0.5, 0.75)
    f "This is our dormitory. All students attending Camelia live here."
    f "There are three floors in this dorm, plus a basement we can't go into..."
    show freya cute at MoveTo(1.0, 0.5)
    f "You have the registry, telephone, cafeteria, and storage spaces on the first floor"
    show freya curious at MoveTo(0.0, 0.75)
    f "And all our rooms, lounges, lavatories and showers are on the top two floors"
    show freya love at MoveTo(0.5, 0.5)
    f "There are four beds in each room,"
    f "...so that means you have to share your room with three other people."
    show freya glad at MoveTo(0.0, 0.5)
    f "Your room, #327, is on the third floor, two turns right after the first stairwell,"
    show freya smile at MoveTo(0.5, 0.25)
    show miharu smug at EnterLeft(0.0, 0.25)
    f "...and Miharu here is one of your roommates."
    show freya smile at MoveTo(0.0, 0.25)
    show miharu smile at ExitLeft(0.25)
    $ renpy.pause(0.75)
    show freya keen
    f "Any questions?"
    show freya cool
    menu:
        "Wow! She talks a lot...":
            jump a1k1_enough_en
        "Wait! THREE other people?!!":
            jump a1k1_two_en
label a1k1_enough_en:
    k_nervous "I think that's fine for now..."
    show freya glad
    f "Good."
    jump a1k1_fine_en
label a1k1_two_en:
    k_nervous "Do you know who the other two roommates are?"
    show freya sarcastic
    f "Well..."
    f "They're two seniors named Reina and Q.U.E.E.N."
    show freya weary
    k_baka "<Queen>? Is that even a real name?"
    show freya yearn
    f "It is now."
    show freya love
    f "By the way, if you want to write her name make sure to use all CAPS."
    show freya tender
    k_genki "Why? Is she a leader or something?"
    $ renpy.pause(0.75)
    show freya suspicious
    f "Trust me, just do it."
    show freya snide
    k_baka "Huh?"
    show freya evil
    f "Unless you want to find out the hard way...."
    show freya cynical
    k_gasp "...!!"
    $ renpy.pause(1.0)
    jump a1k1_fine_en
label a1k1_fine_en:
    show freya glad
    f "Well, if you need any help, have any more questions, or just want to pay me a visit..."
    show freya cute
    f "Feel free to drop by my room, #156, on the 1st floor."
    show freya calm
    k_happy "Okay, thanks!"
    show freya smile at ExitRight(0.75)
    nar "Freya walks off"
    k_genki "Well, I guess it's time we head back to our room ourselves."
    k_smile "..."
    show miharu confused at EnterLeft(0.0, 0.25)
    m "...?"
    k_sarcastic "...uh... Okay, honestly I don't remember a thing Freya said."
    show miharu relieved
    k_waterfall "Please lead the way."
    show miharu glad at Bounce(1)
    m "Of course!  Follow me...    "
    scene bg dormhall1
    with dissolve
    $ renpy.pause(0.25)
    show miharu chibi1 at Bobble(1.15, 0.6, -0.15, 0.6, 0.35, 2.0)
    nar "and you do"
    scene bg dormhall2
    with dissolve
    show miharu chibi1 at Bobble(-0.15, 0.0, 1.15, 0.2, 0.25, 3.0)
    nar "but much to your surprise, Miharu seems pretty lost herself"
    scene bg dormhall3
    with dissolve
    show miharu chibi1 at Fling(1.15, 0.7, -0.15, 0.3, 2.00, 365.0)
    nar "following the klutzy girl, you spend 15 minutes wandering the mazelike corridors,"
    scene black
    with dissolve
    stop music fadeout 3.0
    nar "...until finally you arrive at your room"
    scene bg dormroom
    with dissolve
    play music music_quirky
    show miharu genki at EnterLeft(0.0, 0.25)
    m "Here we are...! Room Sweet Room!"
    k_swirl "UGH!!!  Never get a job as a tour guide!"
    show miharu smile at ExitLeft(0.25)
    nar "you want to flop down on the bed and rest, but you're not sure which one is yours"
    show prop haku at Appear(0.45, 0.2, 0.0, 0.0)
    with dissolve
    nar "plus you notice the room is full of all sorts of interesting things"
    k_squeal "Ah! What a cute doll!"
    k_happy "Yours?"
    show miharu happy at EnterLeft(0.0, 0.25)
    m "Oh no, that is Q.U.E.E.N.'s property."
    k_ehhh "Eh?!!"
    nar "so this \"Q.U.E.E.N.\" person likes to play with dolls?"
    nar "what kind of person is she?"
    k_sarcastic "Well whatever. Let me get settled in...."
    show miharu smile at ExitRight(0.75)
    $ renpy.pause(0.25)
    show prop haku at ExitRight(0.50)
    nar "you both enter the room"
    nar "while Miharu is busy looking through school notes, you begin unpacking your bag"
    nar "after pulling out clothes, pictures and some decorations,"
    nar "...you take out your netbook and set it on the desk."
    show miharu genki at EnterRight(1.0, 0.25)
    m "Whoa!  How cute!"
    show miharu worried
    m "But is that the same bag you dropped when I bumped into you?"
    k_genki "Yep."
    show miharu concern
    m "....Is it okay?"
    k_smile "Mmm?"
    show miharu curious at MoveTo(0.85, 0.25)
    m "The thingie..."
    k_glad "Oh, the netbook?  Yeah, it's fine."
    show prop netbook at Appear(0.5, 0.5, 0.5, 0.5)
    with dissolve
    nar "you lift it off the desk and flip it around with ease"
    show miharu wonder
    nar "its actually very light, but Miharu looks at you like you're super strong"
    show prop netbook at Shake(0.4, 2)
    k_genki "See? Not even a scratch."
    show miharu relieved at Bounce(1)
    m "Oh! I'm so glad to hear that!"
    k_happy "Yeah, this cutie is very strong."
    show prop netbook at Heft(0.4, 3)
    show miharu cute
    k_smug "I've already dropped her about ten times, but she still keeps working!"
    show miharu genki
    m "Nice! And the color is sooo cute too!"
    show miharu excited
    m "It must have cost you a fortune..."
    show miharu cute
    k_happy "Not really.  For this one, I think I must have spent about... Rp 1,500,000."
    k_relieved "Pretty good for a computer, and I know there are cheaper ones."
    show miharu genki at Bounce(1)
    m "Amazing! That's so much cheaper than I thought!"
    hide prop netbook
    with dissolve
    show miharu smile
    k_smile "hehe..."
    show miharu grief at MoveTo(0.5, 0.25)
    m "Speaking of cheap, I'm dirt poor and hungry..."
    k_oops "?!"
    show miharu excited at Bounce(4)
    m "...so let's go eat at the Bombshelter tonight!"
    show miharu cute
    k_nervous ".........\"Bombshelter\"?"
    show miharu happy
    m "That's what we call the dorm's cafeteria."
    show miharu cute
    k_weird "Um... okay...."
    nar "your day is already so full of strangeness, there can't possibly be anything left to surprise you"
    k_nervous "Let's.... Let's go eat then."
    show miharu glad at Bounce(2)
    $ renpy.pause(0.25)
    show miharu smile at ExitLeft(0.5)
    $ renpy.pause(0.5)
    stop music fadeout 3.0
    scene bg bombshelter
    with slowdissolve
    outline "The Bombshelter"
    play music music_bombshelter1 fadein 2.0
    nar "you see now why they call it the \"Bombshelter\""
    nar "concrete walls, dim lighting, no windows, uncomfortable chairs, sparse decorations"
    nar "it looks better suited for surviving air raids than for serving meals"
    nar "no wonder the food is so cheap..."
    show miharu genki at Rise(0.5, 0.25)
    m "I'm so happy!  I haven't eaten anything since this morning!"
    show miharu smile
    nar "the phrase \"Hunger is the best spice\" must be true,"
    play sound sound_thunderstep
    with vpunch
    nar "...because this is some of the worst food you've eaten in your life"
    show reina silhoutte behind miharu at EnterRight(0.7, 2.5)
    play sound sound_thunderstep
    with vpunch
    show ambient darken
    with slowdissolve
    play sound sound_thunderstep
    with vpunch
    nar "but right before you get to poke fun,"
    show miharu wonder
    nar "...you're shocked when a tall figure suddenly looms over and hugs Miharu"
    show reina relievedblush
    show ambient darkenhole
    with dissolve
    u "Miharu dear!  It's been a long time!"
    show miharu happy
    show reina tenderblush
    m "A \"long time\"?"
    show reina relievedblush
    u "Yeah, since this morning."
    show reina desire
    u "But without seeing you it's like five years..."
    hide ambient darkenhole
    show miharu cute
    show reina lovestarved
    k_sigh "Ehem!"
    show reina stare
    k_sarcastic "Sorry to disturb you two, but may I ask who you are?"
    show reina calm at Bounce(1)
    show reina oppose
    u "Her lover."
    show miharu uncomfortable
    show reina frown
    nar "GASP! how forward!"
    show miharu genki at Laugh(3)
    show reina lust
    m "Hahaha!  What do you mean by \"lovers\"?  We're just roommates."
    show miharu smile
    show reina hentai
    k_nervous "Eh?"
    show miharu happy
    show reina fantasize
    m "Yes, she's Reina, our roommate."
    show miharu cute
    show reina blush
    k_omg "EHHHH?!"
    show miharu smile at Sit(0.25)
    show reina taunt at MoveTo(0.5, 0.75)
    r "I see... So this is that new transfer student."
    show reina mock
    r "mmmmm... I forget, is it Kana or Hana?"
    play sound sound_wind
    show ambient icy
    with dissolve
    show reina fufufu
    nar "you shudder at what almost feels like an icy jealous stare"
    show reina sinister
    k_nervous "...Kana."
    hide ambient icy
    with dissolve
    show reina reluctant
    r "Ah yes... Kana."
    show reina evil
    r "I'm Reina. Nice to meet you."
    show reina smug
    k_nervous "Uh... Nice to meet you too... Senior Reina"
    show reina chastise
    r "Just \"Reina\" is fine....     "
    show reina happydream at MoveTo(0.7, 0.25)
    show miharu calm at Rise(0.5, 0.25)
    nar "and with that she goes back to fawn over Miharu"
    show reina kawaii
    r "So would you like something else to eat, Miharu dear?"
    r "My treat..."
    show reina kawaiismile
    $ renpy.pause(0.5)
    show miharu genki at Bounce(3)
    show prop foodbubble1 at Appear(0.30, 0.18, 0.5, 0.5)
    show prop foodbubble1 at Heft(0.55, 20)
    m "Ah, that's so nice of you!  Thank you, I'd love some bihun goreng!"
    hide prop foodbubble1
    show miharu smile
    show reina happy
    r "Anything for you..."
    show prop foodbubble2 at Appear(0.25, 0.60, 0.5, 0.5)
    show prop foodbubble2 at Heft(0.55, 20)
    show miharu calm
    show reina smile
    k_genki "Then I want some nasgor, please."
    show prop foodbubble2 at Fling(0.25, 0.60, -0.5, 0.7, 0.5, 730)
    show miharu worried
    show reina suspicious
    r "I'm not asking you."
    hide prop foodbubble2
    show reina angry
    k_sneaky "heh?"
    show miharu genki at Laugh(3)
    show reina bashfulleft
    m "Hahaha! Oh, don't say it like that, Reina."
    show miharu glad
    show reina enchanted
    m "People will misunderstand you because of that, hahaha..."
    show miharu smile
    show reina awkward
    nar "Miharu thinks Reina is joking, but clearly it's a serious matter for Reina"
    show reina lecherous
    nar "it's pretty obvious she has her sights on Miharu and no one else"
    show reina naughtydream
    nar "if that's the case... you wonder if... maybe..."
    show miharu confused
    show reina mesmerized
    k_sigh "Fine then, I'll go get something by myself..."
    show miharu happy at MoveTo(0.0, 0.5)
    show reina embarrassed at Bounce(1)
    m "Well, in that case I'll follow you."
    show reina gulp at Bounce(3)
    $ renpy.pause(0.15)
    show reina overprotect at MoveTo(0.15, 0.25)
    show miharu cute
    r "NO WAIT!"
    show reina tense
    nar "hehe, gotcha!"
    show reina awkward
    r "Okay fine, let me take BOTH of your orders."
    show miharu genki at Bow(1)
    show reina nervousblush
    m "Really?! Thank you soooo much!"
    show miharu smile
    show reina genki
    r "No problem, Miharu dear."
    show ambient reinaglare
    with dissolve
    show reina evil
    nar "your feeling of victory is short lived when you see the evil smile flashed at you"
    nar "feeling a chill over you, you worry about what concoction she'll bring back"
    hide ambient reinaglare
    show prop foodbubble3 at Appear(0.85, 0.25, 0.5, 0.5)
    show prop foodbubble3 at Heft(0.55, 20)
    show miharu curious
    show reina shock
    ta "And bring me some kalasan fried chicken while you're at it!  Thanks!"
    hide prop foodbubble3
    nar "..........."
    nar "you turn very nervously towards the direction of the obnoxious voice"
    menu:
        "Should you scream loudly...?":
            jump a1k1_kya_en
        "...or VERY loudly?":
            jump a1k1_gya_en
label a1k1_kya_en:
    show miharu uncomfortable
    k_swirl "KYAAAA!!"
    show reina huh at Bounce(1)
    r "ARGH?!!"
    show aizawa calm at EnterRight(1.0, 0.25)
    show miharu confused
    show reina chide
    ta "What kind of sorry reaction is that?!"
    jump a1k1_reaction_en
label a1k1_gya_en:
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
    ta "A-ha!  Now THAT'S a reaction with passion, LOL!"
    hide redsiren
    stop sound
    jump a1k1_reaction_en
label a1k1_reaction_en:
    show miharu glad at Bow(1)
    show aizawa snide
    show reina frustrated
    m "Good evening, Ms. Aizawa."
    show miharu smile
    show aizawa grateful
    ta "Ah! Good evening, Miharu!"
    show miharu happy
    show aizawa amused
    show reina impatient
    m "What brings you here, Ms. Aizawa?"
    show miharu cute
    show aizawa cute
    ta "Why, to get free dinner of course...~"
    show aizawa smug
    show miharu confused at ExitLeft(1.00)
    show reina smile at MoveTo(-0.4, 0.75)
    $ renpy.pause(1.25)
    hide miharu
    show reina angry at MoveTo(0.5, 0.15)
    show aizawa baka
    $ renpy.pause(0.25)
    show reina shout at Bounce(3)
    r "You're not a student, remember?! So go pay for it yourself!"
    show aizawa complain at Laugh(2)
    show reina angry
    ta "tsk tsk! How rude, I am a student you know."
    show aizawa fatigue
    show reina chastise
    r "{b}WAS{/b} a student..."
    show aizawa meditate
    play sound sound_gong
    show ambient zen behind reina at Appear(0.0, 0.0, 0.0, 0.0)
    with slowdissolve
    show aizawa lecture
    show reina bored
    ta "My child... In life, one never ceases to become a student."
    show aizawa pity
    show reina calm at Bounce(1)
    show ambient zen behind reina at Fling(0.0, 0.0, 0.0, 2.5, 0.75, 365)
    show reina nag
    r "Don't philosophize me!  You graduated five years ago!"
    show reina complain
    r "So if you want dinner, PAY UP!"
    hide ambient zen
    show aizawa yelp at Bounce(2)
    show reina chide
    ta "Awww! You're evil!"
    show aizawa accuse
    ta "The altitude up there must make you grouchy!"
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
    r "We're... {p}... {p}...{=whispered}both the same height....{/=whispered}"
    show aizawa orly at Laugh(4)
    show reina shameright
    ta "Oh-hohoho! That might've been true in the past..."
    show aizawa squeal
    show reina furiousblush
    ta "But now you're so {b}HUGE{/b}..."
    show angrytwitch at Appear(0.4, 0.1, 0.5, 0.5)
    show aizawa evilchuckle
    ta "You're taller and more handsome than all the boys!"
    show aizawa genki at Laugh(4)
    show reina impatient
    ta "Haha! Careful my Prince or I might fall for you too, LOL!"
    show aizawa amused
    hide angrytwitch
    $ renpy.pause(2.5)
    show reina taunt at Laugh(3)
    r "fufufu!  Well, better try your luck..."
    show aizawa astound
    show reina mock
    r "Because I'm the closest thing a {b}LEBAY{/b} like you..."
    show aizawa unamused
    show angrytwitch at Appear(0.9, 0.1, 0.5, 0.5)
    show reina evil
    r "...is ever going to have for a boyfriend."
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
    nar "as funny as it is watching them fight,"
    nar "...you want to stop them before the bad aura consumes the whole cafeteria"
    stop music
    stop countermusic
    m "Okay, that's enough!"
    show reina gulp at MoveTo(0.25, 0.25)
    show aizawa confuzzled at MoveTo(0.75, 0.25)
    nar "fortunately Miharu intervenes for you..."
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
    m "No fighting, okay? Remember, we're all human beings...."
    m "We must get along with each other and create good relationships..."
    show reina bored
    m "...since there's no benefit in beating each other up, is there?"
    show reina chide
    r "THERE IS!"
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
    r "I will get the satisfaction of revenge..."
    show reina scold at Bounce(1)
    r "...after she tried to kill me with that deadly birthday cake last year!"
    show aizawa moronic
    show reina angry
    play music music_ridiculous fadein 2.0
    show prop blackforest1 behind reina at Appear(0.5, 0.4, 0.5, 0.5)
    with dissolve
    ta "That's mean! I worked so hard to make it!"
    show aizawa yelp at Bounce(2)
    show reina threaten
    ta "I toiled non-stop for three days!"
    show reina reprimand at Bounce(1)
    show aizawa pity
    r "And you left it outside for four!"
    play countermusic sound_poison fadein 2.0
    show prop blackforest2 behind reina
    with slowdissolve
    show aizawa dumbfounded
    show reina pout
    r "You didn't even feel guilty when you sent it to me full of growing things,..."
    show reina pout at Bounce(2)
    show aizawa nervous
    r "...and told me it was a new type of Black Forest cake!"
    show miharu excited at EnterLeft (0.2, 0.25)
    show reina mope
    m "Haha! Ah! I think I remember that...!"
    stop countermusic
    hide prop blackforest2
    with dissolve
    show overlay hospital
    with dissolve
    show miharu happy
    show aizawa chastiseright
    show reina hopeless
    m "We all became unconcsious after eating it, and got hospitalized for the whole week because of food poisoning..."
    show miharu glad
    show aizawa schemeright
    show reina speechless
    m "After that, Ms. Aizawa became known as the \"Baker of Death\"."
    hide overlay hospital
    with dissolve
    show aizawa chortleright at Laugh(2)
    show miharu smile
    show reina impatient
    ta "Now now, you have to put up with a little pain here and there,"
    show aizawa orly
    ta "...so you can grow up to be strong healthy adults, LOL!"
    show aizawa nervous
    stop music
    $ renpy.pause(2.50)
    show reina ippenshindemiru
    r "DON'T... {p}\"LOL\"... {p}{b}ME!!!{/b}"
    play music music_crazyfight3 fadein 1.0
    play countermusic sound_war fadein 2.0
    show miharu grief at Sit(0.25)
    show reina scold at MoveTo(0.25, 0.25)
    show aizawa shock at MoveTo(0.75, 0.25)
    $ renpy.pause(0.25)
    show reina shout at HChatter(0.25, 0.28)
    show aizawa scream at HChatter(0.75, 0.72)
    $ renpy.pause(2.0)
    nar "*sigh*... you can kind of see why Reina is angry,"
    hide miharu
    show ambient fire behind reina
    with dissolve
    nar "but then again, the fighting is getting even louder now..."
    show crowd calm behind ambient
    with dissolve
    nar "sure enough, all the students in the cafeteria are crowding to watch the spectacle"
    k_unamused "Ugh! Please stop this already, it's embarrassing!"
    show miharu nervous behind aizawa at EnterLeft (0.5, 0.25)
    $ renpy.pause(0.25)
    show miharu dread behind aizawa at HChatter(0.5, 0.52)
    m "Please stop!"
    show miharu grief at QuickFling (-1.0, -0.5, 0.5, 550)
    show prop chair behind crowd at Appear(0.1, 0.8, 0.5, 0.5)
    show prop chair behind crowd at SetPosition(0.2, -45.0)
    show prop chair behind crowd at SendTo(0.1, 0.45, 1.0)
    nar "but they keep on fighting... it seems nothing can stop them now..."
    hide miharu
    show angrytwitch at Appear(0.15, 0.35, 0.5, 0.5)
    u "{b}Did you not hear what Miharu said?!{/b}"
    u "{b}STOP THIS FOOLISHNESS AT ONCE!!!{/b}"
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
    nar "you're surprised at the booming voice and the massive chair that got hurled from the crowd"
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
    nar "after the commotion dies down, a refined-looking girl walks over towards them"
    show angrytwitch at Appear(0.35, 0.35, 0.5, 0.5)
    u "Well well.... It appears you two have ruined my mood..."
    hide angrytwitch
    u "All I desired was for a little peace and tranquility so I could savor my dinner..."
    u "*sigh* But now you... especially you Ms. Aizawa..."
    show aizawa complain behind crowd at SendTo(0.8, 0.5, 0.15)
    ta "ME AGAIN?!"
    show aizawa complain behind crowd at SendTo(0.8, 0.8, 0.25)
    u "...have gone and spoiled it."
    hide reina
    hide aizawa
    show queen frown behind crowd at Heft(0.45, 3)
    u "This shall not go unpunished!!"
    nar "avoiding getting dragged into the new drama, you whisper to Miharu..."
    k_sarcastic "{=whispered}Is she one of the Black Forest victims too?{/=whispered}"
    show miharu concern at EnterLeft(0.0, 0.25)
    m "{=whispered}Yup...{/=whispered}"
    show miharu doubt
    k_sneaky "{=whispered}Figures. Who's she?{/=whispered}"
    show miharu concern
    m "{=whispered}Q.U.E.E.N.{/=whispered}"
    show miharu doubt
    k_dream "{=whispered}Oh, Q.U.E.E.N..... Q.U.E.E.N.....{/=whispered}"
    show miharu dread
    k_omg "{b}.....EHHHHH?!!!{/b}"
    show queen frown behind crowd at Heft(0.45, 1)
    $ renpy.pause(0.25)
    show queen frown behind crowd at ExitRight(0.5)
    play music music_queen1 fadein 4.0
    nar "your shriek interrupts Q.U.E.E.N.'s scolding,"
    hide queen
    show queen lecture at EnterRight(1.0, 0.25)
    show miharu nervous at MoveTo(-0.3, 0.25)
    q "WHO DARES?!!"
    show queen frown
    nar "...and you fear for the worst when she suddenly turns around to leer at the offender"
    nar "fortunately, another voice from the crowd comes to save you from danger"
    show freya berate at EnterLeft(0.0, 0.25)
    f "Please don't start another scene, Q.U.E.E.N!"
    show freya glare
    k_incredulous "Freya! You're here too!"
    show freya irked
    f "Of course, everyone in the dorm comes to have dinner here."
    show freya troubled
    show queen bored
    nar "Everyone? Cheapskates..."
    show freya fury at MoveTo(0.5, 0.25)
    $ renpy.pause(0.25)
    show freya shout at Bounce(4)
    $ renpy.pause(0.5)
    show miharu confused at MoveTo(0.0, 1.0)
    f "{b}Okay, get back to your seats people!  Nothing to see here!{/b}"
    show freya irritated
    hide crowd nervous
    with dissolve
    nar "the crowd lets out a collective groan as they all get back to what they were doing"
    show freya obligated at Sit (0.25)
    $ renpy.pause(1.0)
    show freya reprimand at Rise(0.5, 0.25)
    show aizawa aho at Rise(0.7, 0.25)
    $ renpy.pause(0.25)
    show miharu cute
    show queen frown
    f "And Ms. Aizawa, I don't know how many times I have to tell you this,"
    show freya scold at Bounce(1)
    show aizawa confused
    f "...but can you head back to your home already?!"
    show freya shout at Bounce(3)
    show aizawa confuzzled
    f "Stop being a kid, and set a good example for all the students!"
    show miharu smile
    show aizawa cry
    show freya irritated
    ta "But I haven't paid the rent, so I can't go back..."
    show aizawa weep
    show freya lecture
    show queen calm
    f "Didn't you get this month's salary already?"
    show aizawa whimper
    show freya irritated
    ta "Oh, of course, they're never late paying me."
    show aizawa aho
    show freya leer
    ta "But... you see... I kinda splurged on some shopping..."
    show miharu uncomfortable
    show queen bored
    ta "...and when I realized it, it was all gone."
    show aizawa orly at Laugh(8)
    show freya angry
    show queen boredleft
    ta "Haha! Now I'm three months behind rent, LOL!"
    show aizawa nervous
    stop music
    play sound sound_deadsilence
    show miharu nervous
    nar "Mrs Aizawa rightfully gets a few seconds of uncomfortable silence from everyone"
    play music music_ridiculous fadein 5.0
    show freya defensive
    k_unamused "You're kidding..."
    show reina chide behind miharu at EnterLeft(-0.4, 0.25)
    r "How reckless..."
    show miharu sad at Bow(1)
    show reina leer
    m "Poor Mrs--"
    show queen chideleft at Bounce(1)
    show miharu dread
    q "Imbecile."
    show aizawa calm at Laugh(3)
    show miharu confused
    show aizawa genki
    show freya annoyed
    show reina angry
    show queen boredleft
    ta "Haha!  I know!  The Headmaster said the same thing when I told her!"
    show aizawa happy
    ta "That's why she gave me permission to live here for a while."
    show miharu nervous
    show aizawa megasigh
    show freya evildream
    show angrytwitch at Appear(0.47, 0.18, 0.5, 0.5)
    show reina scowl
    show queen stareleft
    ta "*sigh* If only she had a bit more sympathy,"
    show aizawa pleasantdream at Laugh(2)
    show reina chastise
    show queen stareright
    ta "...and would just give me one of her mansions, or at least an apartment...."
    show reina speechless
    show aizawa sweetdream
    hide angrytwitch
    $ renpy.pause(2.0)
    show freya psycho at Bounce(6)
    show miharu sigh
    show aizawa gasp
    f "{b}YOU HAVE NO SHAME!!!{/b}"
    show aizawa cry
    play sound sound_stomachgrowl
    show freya shock
    show reina shock
    show queen stareleft
    $ renpy.pause(0.75)
    show miharu uncomfortable at Bounce(1)
    show freya surprised
    show queen meditate
    m "Ah! That reminds me!"
    show miharu grief at Bounce(2)
    show aizawa weep
    show reina gulp
    m "I still haven't gotten my bihun yet!"
    show freya complain at MoveTo(0.35, 0.25)
    show miharu dread
    show reina embarrassed
    f "HOW IS THIS AND THAT RELATED?!"
    show reina awkward at Bounce(1)
    show aizawa whimper
    show freya bored
    r "Ack! Forgot!"
    show miharu sad
    show aizawa weep
    show reina nervousblush
    m "Nyuuuu....."
    show miharu doubt
    show aizawa whimper
    show reina shoo
    r "Sorry, I'll go get it now...!"
    show aizawa weep
    show reina shoofrown at ExitLeft(0.5)
    show prop foodbubble4 at Appear(0.65, 0.5, 0.5, 0.5)
    show prop foodbubble4 at Heft(0.55, 20)
    show freya sigh
    show queen mumble
    q "Don't forget my <fried rice>.  And make it istimewa!"
    show aizawa whimper
    show reina huh at EnterLeft(-0.4, 0.25)
    hide prop foodbubble4
    show miharu confused
    show queen meditate
    r "When did you~?  Ugh~! Oh alright!"
    show prop foodbubble5 at Appear(0.5, 0.45, 0.5, 0.5)
    show prop foodbubble5 at Heft(0.55, 20)
    show aizawa tearsofjoy at Laugh(2)
    show miharu uncomfortable
    show freya perturbed
    show reina furious
    ta "And my kalasan too, hehe!"
    show prop foodbubble5 at QuickFling(1.5, 0.3, 0.5, 365)
    show reina reprimand at Bounce(3)
    show miharu nervous
    show aizawa moronic
    show freya perplexed
    show queen calm
    r "{b}SHUT UP! GET IT YOURSELF!!!{/b}"
    show aizawa cry at Bow(1)
    show miharu smile
    show freya irked
    show reina furious
    ta "Hauu.... *sniffles*"
    show aizawa whimper
    show reina impatient at ExitLeft(0.25)
    show freya mocksideways
    nar "Reina dashes off, leaving you to wonder if she even remembers your order"
    show miharu smile at ExitLeft(0.25)
    show aizawa weep at Sit(0.25)
    show freya mocksideways at ExitRight(0.25)
    show queen calm at ExitRight(0.25)
    $ renpy.pause(0.25)
    stop music fadeout 3.0
    scene bg dormroom
    with dissolve
    outline "BACK IN THE ROOM"
    play music music_quirky
    show miharu genki at Rise(0.0, 1.0)
    m "Ah~! I'm so full...!"
    show miharu smile at VChatter
    k_painful "Of course you are!"
    show miharu glad at ExitLeft(0.25)
    $ renpy.pause(0.25)
    show prop nasgor at Appear(0.5, 0.5, 0.5, 0.5)
    with dissolve
    nar "Reina did in fact remember your nasi goreng and it seemed safe to eat"
    show prop nasgormini
    with dissolve
    nar "but the portion was such that you finished it in three bites"
    nar "good thing you had already eaten something"
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
    nar "on the other hand, Miharu was showered by almost 10 bowls of bihun goreng,"
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
    nar "...and much to your shock she devoured them all!"
    nar "\"What kind of metabolism does she have?!\", you keep wondering to yourself"
    hide miharu
    show queen talk at EnterRight(1.0, 0.25)
    q "If memory serves, your name is Hana, is it not?"
    show queen calm
    k_nervous "Uh... that would be Kana...."
    show queen talk
    q "I regret the belatedness, but it is a pleasure to meet your acquaintance."
    show queen calm
    stop music fadeout 2.0
    menu:
        "Just act casually.":
            jump a1k1_nice1_en
        "Oh, just go along with her.":
            jump a1k1_hermajesty_en
label a1k1_nice1_en:
    play music music_queen1
    k_glad "Ah!"
    k_genki "Nice to meet you too, Q.U.E.E.N."
    show queen mumble at Laugh(1)
    q "I see you spelled my name correctly.  How diligent of you."
    jump a1k1_question_en
label a1k1_hermajesty_en:
    play music music_royalty
    k_dream "*bow* The honor and pleasure is all mine, Your Highness."
    show queen mumble at Laugh(3)
    q "Oh-hoho! How droll!"
    show queen rebuke
    q "But even if I am a <queen>, I actually much despise being called anything else."
    show queen annoyed
    k_nervous "Oh... sorry...."
    show queen mumble at Laugh(2)
    q "Hoho! That's perfectly alright.  You're new so I'll let it pass."
    show queen comment
    q "But just this once...."
    show queen stare
    k_gasp "?!! "
    k_nervous "Hehe, um..."
    jump a1k1_question_en
label a1k1_question_en:
    show queen calm
    k_happy "Mind if I ask a question?"
    show queen talk
    q "Certainly."
    show queen calm
    k_glad "Is this \"Q.U.E.E.N.\" your real name or something...?"
    show queen chide
    q "It is for you."
    show queen bored
    nar "\"That didn't even answer my question!\", you wonder..."
    show miharu genki at EnterLeft(0.0, 0.25)
    show queen stareleft
    m "Yep! Q.U.E.E.N. is Q.U.E.E.N.!"
    show miharu glad at Laugh(2)
    m "No doubt about it, hehe!"
    stop music fadeout 2.0
    show queen stareright at ExitRight(0.5)
    show miharu doubt at MoveTo(-0.3, 1.0)
    nar "while Q.U.E.E.N. is distracted, Miharu takes you to a corner and whispers to you...."
    show miharu concern
    m "{=whispered}Don't ask, or you'll get cursed by that doll....{/=whispered}"
    show miharu doubt
    k_ehhh "{=whispered}Huh?{/=whispered}"
    show miharu concern
    m "{=whispered}Haku, her favorite doll.{/=whispered}"
    show miharu dread
    m "{=whispered}It's not just any doll, it's for voodoo....{/=whispered}"
    play music music_haku
    menu:
        "Yeah right.":
            jump a1k1_kidding_en
        "Oh no, not more crazy people...":
            jump a1k1_scary_en
label a1k1_kidding_en:
    show ambient haunted behind miharu
    with slowdissolve
    show miharu nervous
    k_sarcastic "{=whispered}You've got to be kidding...{/=whispered}"
    show hauntedtwirl behind miharu
    with dissolve
    show miharu confused
    m "{=whispered}I'm serious!{/=whispered}"
    show creepyqueenhaku behind miharu
    with dissolve
    show miharu dread
    m "{=whispered}His full name is SHI NO HAKUSHAKU!{/=whispered}"
    m "{=whispered}That means \"Earl of Death\"!{/=whispered}"
    show miharu nervous
    k_sneaky "{=whispered}Huh~?!!{/=whispered}"
    jump a1k1_proof_en
label a1k1_scary_en:
    k_incredulous "Whoa!! SCARY~!!!"
    show miharu worried
    m "{=whispered}It is, right?{/=whispered}"
    jump a1k1_proof_en
label a1k1_proof_en:
    show miharu dread
    m "{=whispered}And Reina has proof of its power~{/=whispered}"
    k_panic "{b}REINA?!!{/b}"
    hide ambient haunted
    hide hauntedtwirl
    hide creepyqueenhaku
    show queen hakuchideleft at EnterRight(1.0, 0.5)
    show miharu nervous
    q "My my... Are you children talking behind my back now?"
    show miharu uncomfortable at MoveTo(0.0, 0.25)
    show queen hakuboredleft
    m "Oh no, not at all~!"
    show miharu whimper
    k_nervous "Haha! Uh... what makes you say that?"
    show queen hakuannoyed at Bounce(1)
    show miharu doubt
    q "Hmpf!"
    stop music fadeout 1.0
    play sound sound_doorslam
    $ renpy.pause(0.5)
    nar "just then, Reina enters the room very loudly"
    play music music_reina1 fadein 2.0
    queue music [ music_reina2, music_reina1 ]
    show miharu cute
    nar "for once this evening, you're happy to see her"
    show reina relieved behind miharu at EnterLeft(0.5, 0.5)
    show miharu happy
    show queen hakucalm
    r "Ahhh~!! Finally home~!!"
    show miharu genki at Laugh(2)
    show reina tenderblush
    m "Welcome back, teehee~!"
    show reina coo at MoveTo(0.1, 0.25)
    show miharu cute
    r "Miharu dear, did you miss me already~?!"
    show queen hakustareleft
    nar "as if fawning over Miharu all throughout dinner wasn't enough,"
    show miharu smile at ExitLeft(0.75)
    show reina hentai at ExitLeft(0.75)
    nar "...now she rushes over to hug Miharu in the room too"
    show lotsoflove
    nar "you hope this won't last all night long..."
    show queen hakustare
    k_nervous "Reina is... a little obsessed with Miharu, isn't she?"
    show queen hakucomment
    q "It really isn't any of my concern."
    q "...But yes, you can say it's something like that."
    show queen hakuboredleft at MoveTo(0.7, 1.0)
    nar "you want to ask her something else, but she turns her attention to the \"couple\" instead"
    show queen hakuchideleft at Bounce(2)
    q "I hate to interrupt, but where on Earth have you been, Rei?!"
    hide lotsoflove
    show reina complain at EnterLeft(-0.4, 0.25)
    show queen hakuboredleft
    r "Washing dishes of course.  I'm on clean-up duty this day, you know."
    show reina threaten at Bounce(6)
    r "*leer* And I had to do DOUBLE work to cover for YOU too!!!"
    show queen hakucommentleft at Laugh(1)
    show reina furious
    q "Ah, I see!  You have my thanks.  Carry on then."
    show reina suspicious at Bounce(3)
    show queen hakustareleft
    r "*grumble*"
    show miharu sigh at EnterLeft(0.0, 0.5)
    show reina curious
    show queen hakucalm
    m "*yawn*  It's getting kinda late.  We should be going to bed soon."
    show reina yawn at Bow(1)
    show miharu tired
    r "Yeah, I'm exhausted after all that...*yawn*"
    show queen hakumumble at Bounce(1)
    show reina tired
    q "Then say no more.  We shall all go to bed this instant!"
    show reina sleepy at ExitLeft(0.5)
    show miharu sigh at ExitLeft(0.5)
    show queen hakumeditate at ExitRight(0.5)
    $ renpy.pause(0.5)
    stop music fadeout 3.0
    scene black
    with dissolve
    nar "while not as immediate as that, everyone is already brushed, in pajamas, and in bed within only a few minutes"
    nar "that includes you"
    scene bg dormroom2
    with dissolve
    q "Pleasant dreams everyone."
    m "Thank you Q.U.E.E.N.!  Good night everyone!"
    r "Good night, just my Miharu dear!"
    q "Will you not bid me a good night too?"
    r "No, you can have a bad one, hehe."
    q "Fool."
    k_genki "Good night all! It was really nice meeting you today!"
    m "It was nice meeting you too! See you in the morning!"
    r "Bright and early! Or we toss you off the bed!"
    q "Maybe."
    k_nervous "hehe... uh, okay..."
    nar "both Reina and Q.U.E.E.N. turn over and fall fast asleep"
    nar "Miharu stretches over to turn off the lamp light"
    play sound sound_lightswitch
    scene bg dormroom3
    nar "and it's only in the pitch-black darkness..."
    nar "...that she notices the warm glow of the netbook you're using in bed"
    play music music_calm1 fadein 5.0
    m "Oh, you're not going to sleep?"
    k_smile "I will shortly.  Just have a few things to do."
    m "Okay... don't stay up too late. Good night..."
    k_relieved "Night..."
    nar "within a few seconds, Miharu is sound asleep as well"
    show prop unr1 at DissolveAppear(0.09, 0.3, 0.0, 0.0, 0.5)
    show overlay netbook at DissolveAppear(0.03, 0.2, 0.0, 0.0, 0.5)
    nar "you're thankful the netbook keyboard and trackpad are whisper quiet"
    show prop unr2
    with quickdissolve
    nar "so you can type and navigate the Internet without waking anyone up"
    show prop unr3
    with quickdissolve
    nar "you check the news of the day, projects you're involved with"
    show prop unr5
    with quickdissolve
    nar "new artwork, games and music,"
    show prop unr4
    with quickdissolve
    nar "...and other sites you routinely visit"
    show prop unr6
    with quickdissolve
    stop music fadeout 3.0
    nar "you open your webmail and find only a few quick-reply messages"
    play music music_netbook1 fadein 5.0
    scene bg email1
    with dissolve
    nar "with those cleared out, all that is left to do is to compose one more message..."
    nvl clear
    nvl show dissolve
    play countermusic sound_typing
    net "<Dear Cyllia...>"
    net "<I had my first class today, and ZOMG I swear I was tossed into another dimension, lol!>"
    net "<I have this crazy teacher that seems to have escaped from an insane asylum.> >.<"
    net "<And I keep running into all sorts of unique and just plain weird people, too.>"
    net "<Heck, I'm sharing a room with THREE of them, LOL!!!> ^^;"
    net "<But still... I want to keep thinking positively.>"
    net "<After I know them a little more, I'm sure they'll turn out to be nice people.>"
    net "<Or maybe they'll drive me crazy too, hahaha....!> ^___^'"
    stop music fadeout 3.0
    net "<Well, I think that's all for today. I'll tell you more about them later.>"
    net "<Have a big day tomorrow, so wish me luck!> ^^"
    nvl hide nodissolve
    show ambient darken
    $ mouse_visible = False
    play music music_ED1a fadein 25.0
    queue music [ music_ED1b, music_silence ]
    $ floatingtext1 = Text("<Good night...!>\n\n...\n\n<LOL! I forgot it's probably daytime over there!>\n<Have a good day then!> ^____^\n\n<Best Regards,>\nKana-chan ^____^v\n\n\nPS:\n<.....As usual, sorry for my bad English.> ^^;", slow=True, slow_speed=10, style="emailed")
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
    jump a2k1_start_en
