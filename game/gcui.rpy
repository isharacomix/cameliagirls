## This file is in the public domain. Feel free to modify it as a basis
## for your own screens.
#
## Use this for reference, if you want
## http://www.renpy.org/doc/html/screen_special.html
#
## You'll see it's a hybrid writing style, some are new, some are 'old'
## The difficult part were rewritten into a pure python coding style,
## so it becomes alot easier to handle.
## All the easy part were written in the new style, I must say, there're
## very convenient "build in" functions, it saves many extra works.
#
## I'm afraid this is a little bit hard to understand, but it's more
## powerful to write the GUI. And sometimes the veteran writing just
## makes more sense, don't ask before figure it out on your own ;P
#
## whatever, don't be afraid, take your time and it'll work out!


##############################################################################
# Say # what you can, if not then say what you can't do ^^
#
# Screen that's used to display adv-mode dialogue.

## Do not add until version 6.12.1
#screen say:
    # Defaults for side_image and two_window
    #default side_image = None

    #$ui.window(id="window")
    #vbox:
        #style "say_vbox"
        ##if who:
        #text _(who) id "who"
        #hbox:
            #null width 10
            #text _(what) id "what"

    # If there's a side image, display it above the text.
    #if side_image:
    #    add side_image
    #else:
    #    add SideImage() xalign 0.0 yalign 1.0


##############################################################################
# Choice # is something which can slows you down if you can't handle it
#
# Screen that's used to display in-game menus.

screen choice:

    $ui.window(style="menu_window", xalign=0.5, yalign=0.5)
    vbox:
        style "menu" spacing 2
        for caption, action, chosen in items:
            if action:
                $ui.button(clicked=action, style="menu_choice_button")
                text _(caption) style "menu_choice"
            else:
                text _(caption) style "menu_caption"

init -2 python:
    config.narrator_menu = True

    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input # is a even more evil way to slow you down in decision, so be careful!
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window:
        has vbox

        text prompt
        input id "input"


##############################################################################
# Nvl # tells you a story which takes almost the entire screen for it, quite
#     # like a Relaxo ^^
#
# Screen used for nvl-mode dialogue and menus.

screen nvl:

    $ui.window(style="nvl_window")
    vbox:
        style "nvl_vbox"
        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            $ui.window(id=window_id)
            hbox:
                spacing 10

                if who is not None:
                    text _(who) id who_id
                text _(what) id what_id

        # Display a menu, if given.
        if items:
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text _(caption) style "nvl_menu_choice"
                    else:
                        text _(caption) style "nvl_dialogue"

    ## Do not add until version 6.12.1
    #add SideImage() xalign 0.0 yalign 1.0

##############################################################################
# Main Menu # is THE place where your journey starts
#           # every journey over 1000 miles starts with the first step
#
# Screen that's used to display the main menu, when Ren'Py first starts

screen main_menu:
    tag menu # This ensures that any other menu screen is replaced.

    # The background of the main menu.
    $ui.window(style="mm_root")
    vbox:
        xalign .95  yalign .97
        ## Do not add until version 6.12.1
        #text ("@CG ", config.version)           xalign 1.0
        text ("@CG ", "Dev 2011-07-24")           xalign 1.0
        text ("OpenGL ", str(config.gl_enable)) xalign 1.0

    # The main menu buttons.
    frame:
        yalign .9  xalign .07 style_group "mm"
        has vbox

        python:
            # screw the new style! The traditional is more reliable
            txbuttn(_("Start"), Start())
            txbuttn(_("Load"), ShowMenu("load"))
            txbuttn(_("Language"), ShowMenu("language_chooser"))
            txbuttn(_("Preferences"), ShowMenu("preferences"))
            txbuttn(_("Quit"), Quit(confirm=False))


##############################################################################
# Navigation # this is your compass... no not really ^^; it's just the
#            # bar on the left with some buttons, at least no blinky thingy
#
# Screen that's included in other screens to display the game menu
# navigation and background.

screen navigation:
    modal True # this ensures that al the other screens are hidden

    if renpy.context()._main_menu:
        # The background of the game menu.
        $ui.window(style="gm_root")
    else:
        $ui.window(style="gm_root", background=Solid((0,0,0,128)))

    if not renpy.context()._main_menu:
        vbox:
            xalign .95 yalign .97
            $ minutes, seconds = divmod(int(renpy.get_game_runtime()), 60)
            if seconds <= 9:
                $stime = str(minutes)+":0"+str(seconds)
            else:
                $stime = str(minutes)+":"+str(seconds)
            text _("Time elapsed") size 16 color "#A1A1A1"
            text stime  size 18 color "#A1A1A1" xalign 0.5

    # THE (stress the 'e' for more effect) buttons

    $ui.frame(xpos=.05, yfill=True, ymargin=20)
    $ui.vbox(xmaximum=185, xfill=True) # master vbox open

    null height 100
    $txbuttn(_("Return"), Return(), False)

    null height 5
    $txbuttn(_("Load"), ShowMenu("load"))
    $txbuttn(_("Load"), ShowMenu("load"), False)
    $txbuttn(_("Save"), ShowMenu("save"), False)

    null height 5
    $txbuttn(_("Language"), ShowMenu("language_chooser"))
    $txbuttn(_("Preferences"), ShowMenu("preferences"))
    $txbuttn(_("Preferences"), ShowMenu("preferences"), False)

    null height 5
    $txbuttn(_("Return"), Return())
    $txbuttn(_("Main menu"), MainMenu(), False)

    null height 2
    $txbuttn(_("Quit"), Quit(), False)

    $ui.close() # master vbox close


init -2 python:
    ## now everything is here, so the code will be much shorter and
    ## easier to check than before
    def txbuttn(name, action_bam, c_mainm=True):
        if c_mainm == renpy.context()._main_menu:
            ui.button(action=action_bam, ypadding=10)
            ui.hbox()
            ui.null(width=10)
            ui.text(name, style=style.text["menu_butt"])
            ui.null(width=20)
            ui.close()

    ## now the style grouping doesn't make some fuss anymore
    style.mm_button.size_group = "mm"


##############################################################################
# Save, Load # ahh, if the real world has someting like that too...
#            # failed your day? Well..., load state from yesterday, simple!
#            # What? You didn't save before danger? Too bad...
#
# Screens that allow the user to save and load the game.

# A growing list is easy, but a 'layout.yesno_prompt'-call NOT!
# Somehow I can't call a yesno-dialog inside a function, which is
# nessesary for asking you if you really want to delete a file in example.
# And if it's a custom dialog, it's the 'new context'-problem...
#
# So I've tuned the standard file picker a little more, ah, by the way,
# a scrolling list is a piece of cake, but it's not as nice as the page system...
# And I've limited it to 50 slots, that's far more than enough
# Golden Sun 1/2 has only three slots, Pokémon even only one!! So be happy.

screen file_pickery:
    $ui.vbox(style_group="pref") # master vbox open

    $ui.frame(top_margin=20, xalign=1.0)
    hbox:
        xalign 1.0
        $ui.label(_("Load"), bold=True)
        null width 30

    $ui.frame(top_margin=10)
    vbox:
        $ columns = 2
        $ rows = 5
        # Display a grid of file slots.
        $ui.grid(columns,rows, transpose=True, xfill=True, style_group="file_picker")
        # Display ten file slots, numbered 1 - 10.
        for i in range(1, columns * rows + 1):
            # Each file slot is a button.
            $ui.side(['c', 'r'])
            $ui.button(xfill=True, ypadding=10, xpadding=10, clicked=FileAction(i))
            hbox:
                add FileScreenshot(i)
                null width 10
                $ description = "%s. %s\n%s" % (
                    FileSlotName(i, columns * rows),
                    FileTime(i, empty=_("\nEmpty Slot")),
                    FileSaveName(i))
                text description
            if FileTime(i) and renpy.current_screen().screen_name[0] == "load":
                $ui.textbutton("", style=style.button["trash"], clicked=FileDelete(i))
            $ui.close()
        $ui.close() # grid
        # The buttons at the bottom allow the user to pick a page of files.

        $ui.side(['l', 'c', 'r'], style_group="file_picker_nav", xfill=True)
        textbutton " << "    action FilePagePrevious()
        hbox:
            textbutton _("Auto") action FilePage("auto")
            textbutton (persistent._file_page+"/5") xfill True
        textbutton " >> "    action FilePageNext(max=5)
        $ui.close()

    $ui.close() # master vbox close

screen save:
    tag menu        # ensures menu screen replacement
    use navigation
    use file_pickery    # file_pickery with save mode

screen load:
    tag menu        # ensures menu screen replacement
    use navigation
    use file_pickery    # file_pickery with load mode


##############################################################################
# Coose Language # wähle deine Sprache, werd' glücklich und lass mich in Ruh'
#
# Screen that allows the user to change the languange.
# Hey, we are international, aren't we?
# Deshalb schreibe ich einfach Mal auf diese Weise, weil mir langweilig ist

screen language_chooser:
    tag menu        # ensures menu screen replacement
    use navigation

    $ui.vbox(style_group="pref") # master vbox open

    $ui.frame(top_margin=20, xalign=1.0)
    hbox:
        xalign 1.0
        $ui.label(_("Choose a language"), bold=True)
        null width 30

    $ui.frame(top_margin=10, ypadding=20, xpadding=20)
    vbox:
        for i in languagechoice:
            $ui.hbox()
            textbutton i[0] action [SetField(persistent,"lang",i[1]),set_language]
            if persistent.lang == i[1]:
                add im.Image("gameui/check_s.png")
            $ui.close()
    $ui.close() # master vbox close


##############################################################################
# Preferences # let user tunes and breaks the system, ain't that cool?
#
# Screen that allows the user to change the preferences.

screen preferences:
    tag menu
    # Include the navigation.
    use navigation

    $ui.vbox(style_group="pref", xalign = 1.0) # overlord vbox open

    $ui.frame(top_margin=20, xalign=1.0)
    hbox:
        xalign 1.0
        #label persistent.opt_mode
        #null width 30
        label _("Preferences")
        null width 30

    $ui.frame(top_margin=10, xalign=1.0, ypadding=20, xpadding=20)
    $ui.vbox() # master vbox open

    hbox:
        $tab_button("Game", "game")
        $tab_button("Video", "video")
        $tab_button("Sound", "sound")
        $tab_button("Theme", "theme")

    null height 20

    if persistent.opt_mode == "game":
        vbox: # slave box 1
            $check_button(_("Skip unread dialog"), Preference("skip", "toggle"))
            $check_button(_("Skip after Choices"), Preference("after choices", "toggle"))

            null height 20
            $bar_slider(_("Auto-Forward Time"), 40, _preferences.afm_time, u_afmt)
            $bar_slider(_("Text Speed"), 150, _preferences.text_cps, u_tcps)


    if persistent.opt_mode == "video":
        vbox: # slave box 1
            $check_button(_("Fullscreen"), Preference("display", "toggle"))
            $check_button(_("Transitions"), Preference("transitions", "toggle"))

            null height 20
            if persistent.opengl:
                $info_text("Following setting will deactivate OpenGL")
                $bgl_role="selected_"
            else:
                $info_text("Following setting will turn on OpenGL again")
                $bgl_role=None

            $info_text("The system will be restarted automatically to apply the setting")

            $check_button(_("OpenGL"), toggle_opgl, bgl_role)


    if persistent.opt_mode == "sound":
        vbox: # slave box 1
            $bar_slider(_("Music"), 100, _preferences.get_volume("music")*100, u_music)
            $bar_slider(_("Voice"), 100, _preferences.get_volume("voice")*100, u_voice)
            null height 10
            $ui.hbox()
            $adj = ui.adjustment(100, _preferences.get_volume("sfx")*100, changed=u_sfx)
            $ui.bar(adjustment=adj, xmaximum=200)
            null width 10
            text _("Sound") style style.text['cbx'] yalign .5
            null width 20
            if config.sample_sound:
                $ui.button(style=style.button["sound_test"], clicked=sound_test)
                hbox:
                    null width 20
                    text _("Test") style style.text['cbx'] yalign .5
            $ui.close()


    if persistent.opt_mode == "theme":
        vbox: # slave box 1
            $info_text("For now, the theme only changes the colour according to\nthe selected character. But you have to restart the game manually.")
            null height 10
            for i in themechoice:
                $ui.hbox()
                button:
                    left_margin 0
                    xpadding 5
                    action [SetField(persistent,"theme",i[1]),set_theme]
                    add im.Image("gameui/butt_"+i[1]+".png")
                #textbutton i[0]
                if persistent.theme == i[1]:
                    vbox:
                        null height 30
                        add im.Image("gameui/check_s.png")
                $ui.close()

    $ui.close() # master vbox close

    $ui.close() # overlord vbox close


init -2 python:
    style.pref_frame.xfill        = True
    style.pref_frame.left_margin  = 250
    style.pref_frame.right_margin = 20
    style.pref_frame.top_margin   = 5

    def check_button(name, clicked, roly=None):
        ui.button(style=style.button["cbx"], clicked=clicked, role=roly)
        ui.hbox()
        ui.null(width=30)
        ui.text(name, style=style.text['cbx'], yalign=.5)
        ui.close()

    def bar_slider(name, adj_max, adj_what, adj_change):
        ui.null(height=10)
        ui.hbox()
        adj = ui.adjustment(adj_max, adj_what, changed=adj_change)
        ui.bar(adjustment=adj, xmaximum=200)
        ui.null(width=10)
        ui.text(name, style=style.text['cbx'], yalign=.5)
        ui.close()

    def tab_button(name, mode):
        if persistent.opt_mode == mode:
            bgl_role="selected_"
        else:
            bgl_role=None
        ui.textbutton(name, clicked=renpy.curry(set_mode)(mode), role=bgl_role)

    def info_text(text):
        ui.text(text, style=style.text['info'], left_padding=10)

    def set_mode(mode):
        persistent.opt_mode = mode
        renpy.restart_interaction()

    def sound_test():
        renpy.play(config.sample_sound)

    def toggle_opgl():
        if config.gl_enable:
            persistent.opengl = False
        else:
            persistent.opengl = True
        renpy.music.stop(channel="music")
        renpy.utter_restart()

    def u_afmt(x):
        _preferences.afm_time = x
    def u_tcps(x):
        _preferences.text_cps = x
    def u_music(x):
        _preferences.set_volume("music", x/100.0)
    def u_voice(x):
        _preferences.set_volume("voice", x/100.0)
    def u_sfx(x):
        _preferences.set_volume("sfx", x/100.0)


##############################################################################
# Yes/No Prompt # Are you sure you want to delete your saves?
#               # Eh.. no?
#               # Check, don't want it deleted, then we BURN it.
#               # wait, what? NOOOOOOOOO!!!!
#
# Screen that asks the user a yes or no question. And NOTHING between!

screen yesno_prompt:
    # A string that, when evaluated, determines of the created screen should be modal.
    # The modal screen prevents screens underneath it from receiving input events.
    modal True

    $ui.window(style="gm_root")

    $ui.frame(style_group="yesno", xfill=True, xmargin=.2, ypos=.3, yanchor=0, ypadding=.05)
    vbox:
        xalign .5 yalign .5 spacing 30
        label _(message) xalign .5
        hbox:
            xalign .5 spacing 100
            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

init -2 python:
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5

