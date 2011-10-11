## This file contains some of the options that can be changed to customize
## your Ren'Py game. It contains the needed options... there
## is quite a bit more customization you can do.
#
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:
    ## Should we enable the use of developer tools? This should be
    ## set to False before the game is released.
    config.developer = False

    #config.allow_skipping = False
    #config.rollback_enabled = False
    config.has_autosave = False

    infinity = 99999999999
    ## pyTom says, autosave can't be prevented easily, therefore we've
    ## setted the frequency as high as needed to avoid autosave
    config.autosave_frequency = infinity # now THIS has to be ^^

    _preferences.afm_time = 0

    ## These control the width and height of the screen.
    config.screen_width  = 800
    config.screen_height = 600

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.
    config.window_title = u"@Camelia Girls"     # title declaration
    ## Do not add until version 6.12.1
    #config.version      = "Dev 2011-06-20"      # needs right version

    config.window_icon  = "icon.png"    # windows icon, which you see
    config.windows_icon = "icon.png"    # in the corner of the window

    ## persistent information storation, those parameters, which
    ## should stay after turning off and on the game
    if persistent.lang is None:         # language
        persistent.lang = "english"

    if persistent.theme is None:        # theme
        persistent.theme = "kana"

    if persistent.arrow_anim is None:   # 'click-to-continue'-Arrow
        persistent.arrow_anim = True

    if persistent.opengl is None:       # OpenGL
        persistent.opengl = True
    config.gl_enable = persistent.opengl

    persistent.opt_mode = "game"

    ## This centers the main window, neat, isn't it?
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    #########################################
    # Themes

    ## We then want to call a theme function. themes.roundrect is
    ## a theme that features the use of rounded rectangles.
    #
    ## The parameters were token out of this and is now stored
    ## in the 'ui_theme.rpy', because we decide to add a theme change
    ## function, so you can dynamically change colour or theme
    #
    ## so if you want to see more, look into the ui_theme.rpy file,
    ## you should find everything there

    theme.roundrect(
        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#ffffc8",

        ## The color of disabled widget text.
        disabled_text = "#c8c8c8",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,
        )

    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.
    config.has_sound = True

    ## Set this to False if the game does not have any music.
    config.has_music = True

    ## Set this to False if the game does not have voicing.
    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    config.sample_sound = "sound/schoolchime.ogg"

    ## Music that is played while the user is at the main menu.

    config.main_menu_music = "music/Renich_-_Rola_Z.ogg"
    # fade effect for smooth music switching
    config.fade_music = 0.2

    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.
    config.help = None

    # 'Think the help file will come after the game has reached
    # a playable status


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = None

    ## Used when exiting the game menu to the game.
    config.exit_transition = None

    ## Used between screens of the game menu.
    config.intra_transition = dissolve

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = None

    ## Used when returning to the main menu from the game.
    config.game_main_transition = None

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = dissolve

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = dissolve

    ## Used when a game is loaded.
    config.after_load_transition = None

    ## Used when the window is shown.
    config.window_show_transition = None

    ## Used when the window is hidden.
    config.window_hide_transition = None


    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode? Naa! It would be bothersome.
    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.
    config.default_text_cps = 0

    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persisten information can be found by the init code.)
python early:
    config.save_directory = "cameliagirls"
