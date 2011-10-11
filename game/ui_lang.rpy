#
## THE (please stress the 'e' for more funky effect) language system,
## if you want to add a translation, do it here.
#
## I've renamed many things, so you can't use the standard from
## the Internet I'm afraid ;P
#
## I'll explain how this works:
## First, if you choose a language in the langauge menu,
## 'set_language()' is called. You can see the English template
## don't have the 'persistent.lang'-asking. So the English
## translation WILL be called with 'set_language()', no exceptions.
#
## THEN, if you have another language than English, i.e. German, then
## it will activate by the 'persistent.lang'-asking and translate
## everything AGAIN.
## So to say, except English, all the other languages will
## be set two times, one time in English, then in their own language.
#
## Don't tell me it's futile, think a little bit, and you know why
## this is important and safe.
#
## And now the way to translate this game, good luck!
#

init python:

### FIRST, YOU declare your language here, look at the other
##  declarings, then you know what you have to do here
#
##  'alk1_start_en' is the name of the label, which you have to create
##  and translate too, don't worry, those two files are now the only
##  one you have to change, I've got rid of all dependencies already
#
    languagechoice = [
        ("English",          "english",    "a1k1_start_en"),
        ("Bahasa Indonesia", "indonesian", "a1k1_start_id"),
        ("Español",          "spanish",    "a1k1_start_es"),
        ("Français",         "french",     "a1k1_start_fr"),
        ("Deutsch",          "german",     "a1k1_start_de")
        ]

    def set_language():
### SECOND, after declaring, you can pick this template to translate
##  the game to your desire language

    ## template/english goes from here ---
        config.translations.update({
        # system's translation
        u'Play'         : u'Play',
        u'Load'         : u'Load',
        u'Save'         : u'Save',
        u'Main menu'    : u'Main menu',
        u'Language'     : u'Language',
        u'Preferences'  : u'Preferences',
        u'Quit'         : u'Quit',
        u'Help'         : u'Help',
        u'Return'       : u'Return',
        u'Skip mode'    : u'Skip mode',
        u'Auto mode'    : u'Auto mode',
        u'Version '     : u'Version ',

        u'Choose a language'    : u'Choose a language',
        u'Cancel'               : u'Cancel',

        u'Fullscreen'           : u'Fullscreen',
        u'Transitions'          : u'Transitions',
        u'OpenGL'               : u'OpenGL',
        u'Skip unread dialog'   : u'Skip unread dialog',
        u'Skip after Choices'   : u'Skip after Choices',
        u'Auto-Forward Time'    : u'Auto-Forward Time',
        u'Text Speed'           : u'Text Speed',
        u'Music'                : u'Music',
        u'Voice'                : u'Voice',
        u'Sound'                : u'Sound',
        u'Test'                 : u'Test',
        u'Rollback'             : u'Rollback',

        u'Auto'                 : u'Auto',
        u'Quick'                : u'Quick',
        u'Empty Slot'           : u'Empty Slot',
        u'Create new save state': u'Create new save state',

        u'Yes'  : u'Yes',
        u'No'   : u'No',

        u'All'  : u'All',
        u'Some' : u'Some',
        u'None' : u'None',

        u'Are you sure?'
        : u'Are you sure?',

        u'Are you sure you want to quit?'
        : u'Are you sure you want to quit?',

        u'Are you sure you want to overwrite your save?'
        : u'Are you sure you want to overwrite your save?',

        u'Are you sure you want to return to the main menu?\nThis will lose unsaved progress.'
        : u'Are you sure you want to return to the main menu?\nThis will lose unsaved progress.',

        u'Are you sure you want to delete this save?'
        : u'Are you sure you want to delete this save?',

        u'Loading will lose unsaved progress.\nAre you sure you want to do this?'
        : u'Loading will lose unsaved progress.\nAre you sure you want to do this?',

        u'Save Failed.'
        : u'Save Failed.'
        })
    ## until here ---


        if persistent.lang is None:
            persistent.lang = "english"

        elif persistent.lang == "indonesian":
            config.translations.update({
            # your nickname here
            u'Play'         : u'Bermain',
            u'Load'         : u'Lanjutkan',
            u'Save'         : u'Simpan',
            u'Main menu'    : u'Menu Utama',
            u'Language'     : u'Bahasa',
            u'Preferences'  : u'Preferensi',
            u'Quit'         : u'Keluar',
            u'Help'         : u'Bantuan',
            u'Return'       : u'Kembali',
            u'Skip mode'    : u'Lompat modus',
            u'Auto mode'    : u'Otomatis modus',
            u'Version '     : u'Versi ',

            u'Choose a language'    : u'Pilih bahasa',
            u'Cancel'               : u'Membatalkan',

            u'Fullscreen'           : u'Layar penuh',
            u'Transitions'          : u'Transisi',
            u'OpenGL'               : u'OpenGL',
            u'Skip unread dialog'   : u'Lompat dialog belum dibaca',
            u'Skip after Choices'   : u'Lompat setelah pilihan',
            u'Auto-Forward Time'    : u'Otomatis Mempercepat Waktu',
            u'Text Speed'           : u'Kecepatan teks',
            u'Music'                : u'Musik',
            u'Voice'                : u'Suara',
            u'Sound'                : u'Lagu',
            u'Test'                 : u'Menguji',
            u'Rollback'             : u'Kembali',

            u'Auto'                 : u'Otomatis',
            u'Quick'                : u'Cepat',
            u'Empty Slot'           : u'Slot Kosong',
            u'Create new save state': u'Membuat simpanan baru',

            u'Yes'  : u'Ya',
            u'No'   : u'Tidak',

            u'All'  : u'Semua',
            u'Some' : u'Sedikit',
            u'None' : u'Nol',

            u'Are you sure?'
            : u'Apakah anda yakin?',

            u'Are you sure you want to quit?'
            : u'Apakah anda yakin ingin keluar?',

            u'Are you sure you want to overwrite your save?'
            : u'Apakah anda yakin ingin menimpa simpanan ini?',

            u'Are you sure you want to return to the main menu?\nThis will lose unsaved progress.'
            : u'Apakah anda yakin ingin kembali ke menu utama?\nAnda akan kehilangan progress yang belum disimpan.',

            u'Are you sure you want to delete this save?'
            : u'Apakah anda yakin ingin menghapus simpanan ini?',

            u'Loading will lose unsaved progress.\nAre you sure you want to do this?'
            : u'Loading akan menghilangan progress yang belum disimpan.\nApakah anda yakin ingin melakukan ini?',

            u'Save Failed.'
            : u'Tidak simpan.'
            })

        elif persistent.lang == "spanish":
            config.translations.update({
            # your nickname here
            u'Play'         : u'Jugar',
            u'Load'         : u'Continuar',
            u'Save'         : u'Guardar',
            u'Main menu'    : u'Menú Principal',
            u'Language'     : u'Idioma',
            u'Preferences'  : u'Preferencias',
            u'Quit'         : u'Salir',
            u'Help'         : u'Ayuda',
            u'Return'       : u'Regresar',
            u'Skip mode'    : u'Modo de salto',
            u'Auto mode'    : u'Modo automático',
            u'Version '     : u'Version ',

            u'Choose a language'    : u'Escoja un lenguaje',
            u'Cancel'               : u'Cancelar',

            u'Fullscreen'           : u'Pantalla completa',
            u'Transitions'          : u'Transicioness',
            u'OpenGL'               : u'OpenGL',
            u'Skip unread dialog'   : u'Saltar texto no leído',
            u'Skip after Choices'   : u'Saltar después de opciones',
            u'Auto-Forward Time'    : u'Auto-adelantar tiempo',
            u'Text Speed'           : u'Velocidad de texto',
            u'Music'                : u'Música',
            u'Voice'                : u'Voz',
            u'Sound'                : u'Sonido',
            u'Test'                 : u'Prueba',
            u'Rollback'             : u'Revertir cambios',

            u'Auto'                 : u'Auto',
            u'Quick'                : u'rápido',
            u'Empty Slot'           : u'Espacio vacío',
            u'Create new save state': u'Crear un nuevo juego salvado',

            u'Yes'  : u'Sí',
            u'No'   : u'No',

            u'All'  : u'Todos',
            u'Some' : u'Algunos',
            u'None' : u'Nada',

            u'Are you sure?'
            : u'¿Estás seguro?',

            u'Are you sure you want to quit?'
            : u'¿Estás seguro de que deseas salir?',

            u'Are you sure you want to overwrite your save?'
            : u'¿Está seguro de que deseas sobrescribir?',

            u'Are you sure you want to return to the main menu?\nThis will lose unsaved progress.'
            : u'¿Estás seguro de que desea volver al menú principal?\nEste perderá el progreso sin guardar.',

            u'Are you sure you want to delete this save?'
            : u'¿Estás seguro que quieres eliminar este archivo?',

            u'Loading will lose unsaved progress.\nAre you sure you want to do this?'
            : u'Cargar perderá el progreso sin guardar.\n¿Estás seguro que quieres hacer esto?',

            u'Save Failed.'
            : u'No se pudo guardar.'
            })

        elif persistent.lang == "french":
            config.translations.update({
            # your nickname here
            u'Play'         : u'Jouer',
            u'Load'         : u'Charger',
            u'Save'         : u'Sauver',
            u'Main menu'    : u'Menu Principal',
            u'Language'     : u'Langage',
            u'Preferences'  : u'Préférences',
            u'Quit'         : u'Quitter',
            u'Help'         : u'Assistance',
            u'Return'       : u'Retour',
            u'Skip mode'    : u'Mode de saut',
            u'Auto mode'    : u'Mode automatique',
            u'Version '     : u'Version ',

            u'Choose a language'    : u'Choisir une langue',
            u'Cancel'               : u'Annuler',

            u'Fullscreen'           : u'Plein Ecran',
            u'Transitions'          : u'Transitions',
            u'OpenGL'               : u'OpenGL',
            u'Skip unread dialog'   : u'Saut dialogue non lus',
            u'Skip after Choices'   : u'Saut après choix',
            u'Auto-Forward Time'    : u'Ecoulement du Temps',
            u'Text Speed'           : u'Vitesse du Texte',
            u'Music'                : u'Musique',
            u'Voice'                : u'Voix',
            u'Sound'                : u'Son',
            u'Test'                 : u'Tester',
            u'Rollback'             : u'Annuler les changements',

            u'Auto'                 : u'Automatique',
            u'Quick'                : u'Rapide',
            u'Empty Slot'           : u'Emplacement Libre',
            u'Create new save state': u'Créer une nouvelle sauvegarde',

            u'Yes'  : u'Oui',
            u'No'   : u'Non',

            u'All'  : u'Tous',
            u'Some' : u'Quelques',
            u'None' : u'Rien',

            u'Are you sure?'
            : u'Êtes-vous sûr?',

            u'Are you sure you want to quit?'
            : u'Êtes-vous sûr de vouloir quitter?',

            u'Are you sure you want to overwrite your save?'
            : u'Êtes-vous sûr de vouloir écraser cette sauvegarde?',

            u'Are you sure you want to return to the main menu?\nThis will lose unsaved progress.'
            : u'Êtes-vous sûr de vouloir retourner au menu principal?\nCela fera perdre la progression en cours.',

            u'Are you sure you want to delete this save?'
            : u'Êtes-vous sûr de vouloir supprimer cette sauvegarde?',

            u'Loading will lose unsaved progress.\nAre you sure you want to do this?'
            : u'Le chargement fera perdre la progression en cours.\nÊtes-vous sûr de vouloir faire cela?',

            u'Save Failed.'
            : u'Sauvegarde a échoué'
            })

        elif persistent.lang == "german":
            config.translations.update({
            # tKensum's translation
            u'Play'         : u'Start',
            u'Load'         : u'Laden',
            u'Save'         : u'Speichern',
            u'Main menu'    : u'Hauptmenü',
            u'Language'     : u'Sprache',
            u'Preferences'  : u'Einstellungen',
            u'Quit'         : u'Beenden',
            u'Help'         : u'Hilfe',
            u'Return'       : u'Zurück',
            u'Skip mode'    : u'Skip Modus',
            u'Auto mode'    : u'Auto Modus',
            u'Version '     : u'Version ',

            u'Choose a language'    : u'Wähle eine Sprache',
            u'Cancel'               : u'Abbrechen',

            u'Fullscreen'           : u'Vollbildschirm',
            u'Transitions'          : u'Überblendungen',
            u'OpenGL'               : u'OpenGL',
            u'Skip unread dialog'   : u'Ungelese Texte skippen',
            u'Skip after Choices'   : u'Nach Wahl skippen',
            u'Auto-Forward Time'    : u'Autom. weiter',
            u'Text Speed'           : u'Textgeschwindigkeit',
            u'Music'                : u'Musik',
            u'Voice'                : u'Sprache',
            u'Sound'                : u'Geräusch',
            u'Test'                 : u'Test',
            u'Rollback'             : u'Rollback',

            u'Auto'                 : u'Auto',
            u'Quick'                : u'Quick',
            u'Empty Slot'           : u'Empty Slot',
            u'Create new save state': u'Neuen Spielstand erstellen',

            u'Yes'  : u'Ja',
            u'No'   : u'Nein',

            u'All'  : u'Alle',
            u'Some' : u'Einige',
            u'None' : u'Keine',

            u'Are you sure?'
            : u'Sicher?',

            u'Are you sure you want to quit?'
            : u'Wirklich beenden?',

            u'Are you sure you want to overwrite your save?'
            : u'Willst du diesen Spielstand wirklich überschreiben?',

            u'Are you sure you want to return to the main menu?\nThis will lose unsaved progress.'
            : u'Wirklich zum Hauptmenü?\nNicht gespeicherter Spielstand wird verlorengehen.',

            u'Are you sure you want to delete this save?'
            : u'Willst du diesen Spielstand wirklich löschen?',

            u'Loading will lose unsaved progress.\nAre you sure you want to do this?'
            : u'Der aktuelle Spielstand geht beim Laden verloren.\nBist du dir sicher?',

            u'Save Failed.'
            : u'Speichern fehlgeschlagen.'
            })

    set_language()
