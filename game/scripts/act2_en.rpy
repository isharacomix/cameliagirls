# en
# Act 2 starts here.
init:
    # Declare constants used in this Act
    $ alt_emailend2a = False
    $ alt_emailend2b = False
    $ alt_emailend2c = False
label a2k1_start_en:
    scene black
    play music sound_birdsongs fadein 4.0
    $ renpy.pause(4.0)
    m "Kya!"
    nar "you're suddenly woken up by some unnerving whispers..."
    m "{=whispered}Ah... don't.... It tickles...{/=whispered}"
    r "{=whispered}It's just for a little while...{/=whispered}"
    nar "you're curious about what they're doing, but are still too tired to even lift your head."
    nar "they weren't kidding about getting up early...."
    nar "better to just stay nice and snug under your bedsheets"
    nar "and go back to slee--"
    m "{=whispered}Your breath...{/=whispered}"
    m "{=whispered}I can feel... your breath... on my neck...{/=whispered}"
    play music music_yuri1
    nar "HUHHHHHHHHHH~?!!!!!!"
    show lotsoflove2
    r "{=whispered}Shush my dear.... We wouldn't want to wake up Kana, now would we...?{/=whispered}"
    nar "oh now you just HAD to wake up!"
    m "{=whispered}I'm rather sensitive, you know....{/=whispered}"
    r "{=whispered}So beautiful....{/=whispered}"
    nar "Beautiful?!"
    m "Ahhh...!!! Please stop... Reina...!!"
    m "I'm... at my limit...!"
    nar "LIMIT?!!!!"
    r "{=whispered}Almost done....{/=whispered}"
    m "No...!"
    m "Ahhhhh...!"
    m "Aaaaaaaaahhhhh...!"
    k_omg "?!!!!!!!!!!!"
    m "{b}HIYAAAAAAAAAAAAAAAAAAAAAAAAAAAH!!!!!!!!!!!{/b}"
    menu:
        "WHAT THE HELL ARE THEY DOING?!!!!":
            jump a2k1_doing_en
        "Stay in bed and eavesdrop some more...":
            jump a2k1_stay_en
label a2k1_doing_en:
    hide lotsoflove2
    play sound sound_woosh
    show yellow at Fling(0.5, -1.0, 0.5, 0.5, 0.5, 0.0)
    show white at DissolveAppear(0, 0, 0, 0, 0.5)
    k_shout "HEY!!!! WHAT ARE YOU TWO DOING AT THIS--?!!!!"
    $ renpy.pause(1.5)
    scene bg newdormroom1
    show reina coolstare behind white at Appear(0.55, 0, 0.5, 0)
    show miharu confused behind white at Appear(0.45, 0.3, 0.5, 0)
    show prop hairbrush behind white at Appear(0.55, 0.5, 0.5, 0.5)
    show overlay kanabed1 behind white
    $ renpy.music.set_volume(0.20, 1, channel="music")
    show white at SelfDissolve(1.0, 0.0, 1.0)
    k_bewildered "..."
    show miharu smile
    m "Mm?"
    show reina scold
    r "What's your problem?"
    show reina scowl
    nar "your face turns beet-red when you spot Reina's comb on Miharu's hair"
    show reina chastise
    show prop hairbrush at Rattle(0.5, 0.1, 100, 0.75)
    r "Were you perhaps imagining something else?"
    show reina smirk
    show miharu cute
    k_weird "..."
    k_sneaky "...nope..."
    show miharu smile
    show reina mock
    r "hehe... Liar..."
    show reina taunt
    k_nervous "Huh?"
    show reina naughtydream
    show prop hairbrush at Appear(0.55, 0.5, 0.5, 0.5)
    $ renpy.music.set_volume(1, 1, channel="music")
    r "Don't worry.  The time for THAT will come... *chuckle*"
    show reina fantasize at Laugh(2)
    nar "Reina's expression leaves a chill running down your spine"
    jump a2k1_OP_en
label a2k1_stay_en:
    nar "fighting temptation, you decide to stay in bed and pretend to be sleeping"
    nar "you're not sure if you're paralyzed with fear,..."
    nar "...or just morbidly curious enough to want to avoid interrupting"
    r "{=whispered}Pssst... Don't shout...{/=whispered}"
    m "{=whispered}Sorry...{/=whispered}"
    m "{=whispered}But that hurt a little...{/=whispered}"
    r "Okay, done!  What do you think?"
    m "Ah! It's perfect as always, teehee!"
    r "But of course!"
    hide lotsoflove2
    show yellowrotate at Appear(1.0, 1.0, 0.5, 0.5)
    r "My Miharu-dear's hair is so soft and cuddly, just like her!"
    show yellowrotate at BackgroundFling(1.0, 1.0, 0.75, -90, 1.0)
    show white at DissolveAppear(0, 0, 0, 0, 0.75)
    #$ renpy.play(sound_silence15sec, sound_silence30sec, sound_collide)
    play sound sound_silence
    queue sound sound_collide
    with vpunch    
    stop music fadeout 1.0
    k_swirl "GAH!!!"
    $ renpy.pause(0.75)
    play music music_ridiculous fadein 1.0
    show bg newdormroom1 behind white at Appear(0.5, 0.5, 0.5, 0.5)
    show bg newdormroom1 at BackgroundFling(0.5, 0.85, 0.0, -90, 1.35)
    show reina bored behind white at Appear(0.5, 0.45, 0.5, 0.5)
    show reina bored at BackgroundFling(0.65, 0.45, 0.0, -90, 1.0)
    show miharu dread behind white at Appear(0.5, 0.6, 0.5, 0.5)
    show miharu dread at BackgroundFling(0.85, 0.6, 0.0, -90, 1.0)
    show prop hairbrush behind white at Appear(0.5, 0.4, 0.5, 0.5)
    show prop hairbrush at BackgroundFling(0.8, 0.4, 0.0, -90, 1.0)
    show overlay kanabed2 behind white
    show white at SelfDissolve(1.0, 0.0, 0.75)
    $ renpy.pause(1.5)
    show miharu uncomfortable
    m "Ah! Are you okay, Kana?"
    show miharu nervous
    k_nervous "Haha... Yeah, I'm fine"
    show reina mock
    r "What? You were having a nightmare?"
    k_sneaky "Yeah, 'cause of you..."
    show miharu relieved
    show reina huh
    r "Haaah?!"
    jump a2k1_OP_en
label a2k1_OP_en:
    stop music fadeout 2.5 
    show white at SelfDissolve(0.0, 1.0, 2.5)
    $ renpy.pause(2.5)
    hide reina
    hide miharu
    hide prop hairbrush
    hide overlay kanabed1
    hide bg newdormroom1
    $ renpy.pause(0.05)
    $ mouse_visible = False
    scene black
    play music music_OP
    show newOP_1
    show newOP_2
    show newOP_3
    show newOP_4
    show newOP_5
    $ renpy.pause(91.25)
    stop music
    stop music
    hide OP_1
    hide OP_2
    hide OP_3
    hide OP_4
    hide OP_5
    play music music_konobangumiwa1
    show konobangumiwa_1b
    show konobangumiwa_2
    $ renpy.pause(10.25)
    $ mouse_visible = True
    stop music
    jump a2k1_reality_en
label a2k1_reality_en:
    scene black
    $ renpy.pause(0.25)
    play music music_netbook2
    show bg dorm2 at SelfDissolve (0.0, 1.0, 1.0)
    show actgeez
    $ act_name = 'act_2 "The Pink Pineapple"'
    show acttitle
    $ renpy.pause(7.5)
    show bg dorm2 at ZoomInOut(0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.45, 0.25, 180.0, 1.0, 4.0):
    nvl clear
    nvl show dissolve
    play countermusic sound_mouseclicks
    netcyl "<Dear Kana,>"
    netcyl "<Sounds like you had an eventful first day.  ((^o^))>"
    netcyl "<I'm not one to talk, but I can guarantee...>"
    netcyl "<That while things may seem strange in the beginning, you will get used to it.>"
    netcyl "<In a month from now you'll be laughing this off. ((^.^))>"
    netcyl "<But just in case...((¬_¬))>"
    netcyl "<Give me the number to the nearest asylum, in case I have to come visit you! ((>v<))>"
    nvl clear
    netcyl "<I'm kidding, you'll be fine!>"
    netcyl "<Rather than worrying about crazy classmates, how about checking out the attached id.po file?>"
    netcyl "<The Indonesian translation of Inkscape is coming along beautifully, in my honest opinion.>"
    netcyl "<I hope your new friends will enjoy it too. (do any of them do vector artwork?)>"    
    netcyl "<And all it cost us was a baby tiger adoption.>"
    netcyl "<And it's quite the CUTIE!!!! ((^.^))>"
    nvl clear
    netcyl "<Well, that's all I have for you today.>"
    netcyl "<You have a busy day ahead of you, so I won't keep you.  ((^_~))>"
    netcyl "<Have fun, study hard, eat right and take care,...>"
    netcyl "Temen saya."
    nvl clear
    netcyl "<Digitally Yours,>"
    netcyl "<--Cyllia-chan>"
    nvl clear
    netcyl "<PS:>"
    netcyl "<And WOW!  You're up early today!  ((*v*))>"
    netcyl "<But why the sudden fascination with hair? ((O_o))>"
    netcyl "<And yeah, my hair DOES look like my avatar's.>"
    netcyl "<And uh... no,...>"
    netcyl "<I don't make strange noises when I comb it. ((^^;))>"
    nvl hide dissolve
    stop countermusic
    stop music fadeout 0.5
    scene black
    show bg newdormroom1
    with fade
    play music music_quirky
    show miharu dread at EnterRight(0.5, 0.5)
    $ renpy.pause(0.5)
    show miharu grief at Bounce(10)
    m "KYAAAAAA!!!!  I'M GOING TO BE LATE!!!!!!!"
    show miharu whimper at Panic(1.0, 1.0)
    nar "you notice that Miharu is already dressed up, and looking rather frantic"
    k_ehhh "Hey hey,..."
    k_nervous "Isn't it, um,... a little too early for school?"
    show miharu whimper at MoveTo(1.5, 0.5)
    $ renpy.pause(0.5)
    show miharu casual_confused at MoveTo(0.5, 0.5)
    m "Part-time job!" 
    show miharu casual_confused at Bounce(5)
    m "Must deliver newspapers!  Must deliver newspapers!"
    show miharu casual_nervous
    k_gasp "Uh,... then why are you dressed like that?"
    show miharu casual_grief at Bounce(3)
    m "Nyuuu!"
    show miharu casual_whimper
    k_sneaky "You, uh,... You short of money or something...?"
    show miharu casual_uncomfortable
    m "Oh no, nothing like that..."
    show reina tense behind miharu at EnterRight(0.7, 0.5)
    r "Miharu Dear, you're gonna be late if you keep chatting here!"
    show reina joy
    show miharu casual_grief at Bounce(1)
    m "Ah! You're right!"
    show miharu casual_glad
    m "Okay, I'm leaving!"
    show reina love
    show miharu casual_glad at ExitLeft(0.5)
    m "See you two at school!"
    show reina genki at MoveTo(0.45, 0.5)
    r "Ta--... Take care, my darling!"
    play sound sound_doorslam
    show reina lovestarved
    r "*whimper*"
    k_unamused "..."
    show reina fuss at Bounce(1)
    r "WAAAH!  Now I'm all lonely...."
    nar "How dramatic..."
    k_evil "Well, there's always Q.U.E.E.N., you know."
    show reina furious
    r "Hmmm?!!"
    k_worried "Although now that I mention it, I haven't seen her all morning...."
    show reina chide
    r "Oh her...  Yeah, she's..."
    show reina pout
    r "...somewhere around here..."
    show reina mope
    k_dream "That means you don't know."
    show reina dream
    r "I don't know exactly where she is... but I can still feel her presence in this dorm..."
    show reina impatient
    k_squeal "Haha!  You're psychic or something?!"
    show reina reprimand at Bounce(2)
    r "NO!!!"
    show reina reluctant
    r "Well,... maybe,... "
    show reina complain
    r "That damn doll did some strange things to me...."
    show reina impatient
    k_bewildered "...?"
    k_sad "Come to think of it, Miharu told me that you were cursed by that Haku doll."
    stop music
    show reina blush
    $ renpy.pause(0.75)
    k_sad "Why did she do that?"
    play music music_haku
    show reina hentai
    r "hehe, looks like Miharu Dear still can't keep a secret...."
    show prop haku behind bg at PanAndZoom(0.25, 0.0, 0.5, 0.0, 0.75, 0.0, 0.5, 0.0, 30.0, 3.0, 3.5, 30.0, 0.0, 0.4)
    show bg newdormroom1 at SelfDissolve(1.0, 0.15, 30.0)
    show reina excuse
    r "*sigh* But I guess the whole dorm knows about it anyway, so..."
    show reina nervous
    k_sad "...?"
    r "..."
    show reina pout
    r "...Actually... I don't know why she cursed me back then...."
    r "Whenever I ask her, she always says something silly like:"
    show reina oppose
    r "'There is only room for one <queen> here! Hohohoho!'"
    show reina complain
    r "Or some other such nonsense.  *sigh*"
    show reina impatient
    k_nervous "Hehehe..."
    show reina frustrated
    r "Trust me, I still have no clue what that means."
    show reina stubborn
    k_baka "hehe, that makes two of us."
    r "..."
    k_oops "..."
    show reina suspicious
    r "...Kana?"
    show reina stern
    k_worried "hmm?"
    hide prop haku
    show bg newdormroom1 at SelfDissolve(0.25, 1.0, 0.0)
    stop music
    show reina evil at Bounce(2)
    r "...Get dressed for school already."
    play music music_quirky
    show reina coolsmile
    k_shout "HEY!!"