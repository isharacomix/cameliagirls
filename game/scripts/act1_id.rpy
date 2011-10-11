# id
# Act 1 starts here.
init:
    # Declare language-specific characters used by this game.
    if persistent.lang == "indonesian":
        $ classroom = "Satu Kelas"
        $ teacher = "Guru"
        $ unknown = "Kelas"
label a1k1_start_id:
    scene black
    play music music_netbook1
    $ renpy.pause(1.0)
    scene bg sunrise
    with introfade
    nvl clear
    nvl show dissolve
    play countermusic sound_typing
    net "<Dear Cyllia...>"
    net "<Akhirnya aku tiba di sini di Akademi Putri Camelia...>"
    net "<Mulai hari ini, aku akan tinggal di asrama seperti yang orangtuaku inginkan...>"
    nvl hide dissolve
    stop countermusic
    scene bg academy
    with fade
    k_happy "Ah! Andai saja kau bisa merasakan betapa segarnya udara pagi ini..."
    k_relieved "Dan betapa indahnya matahari terbit..."
    k_genki "Aku tak sabar seperti apa cerita yang akan menantiku di sini..."
    stop music
    $ renpy.play(sound_collide)
    with vpunch
    nar "Sepertinya seseorang menabrakmu..."
    nar "...dan kau terjatuh"
    show miharu grief at Fling(-0.5, 0.35, 1.5, 1.5, 1.0, 730.0)
    u "Hiyaaaah!!"
    nar "Dia juga jatuh sih...."
    play music music_miharu1
    menu:
        "Kau baik-baik saja, tapi mungkin dia sakit?":
            jump a1k1_okay_id
        "Cewek BEGO, gak bisa lihat apa?!":
            jump a1k1_eyes_id
        "Hehe, keliatannya tukang ngelamun nih. Kerjain dikit ah...":
            jump a1k2_bone_id
label a1k1_okay_id:
    k_worried "Ow.... Ah! Apa kau baik-baik saja?"
    show miharu whimper at Rise(0.5, 1.0)
    u "Aku sangat minta ma'af dan ya aku baik-baik saja, makasih, kalo kamu?"
    k_relieved "Aku juga gak apa-apa"
    show miharu relieved
    u "Syukurlah...."
    show miharu uncomfortable at Bounce(1)
    u "Ah! Sial! Bakal telat nih!"
    show miharu smile
    u "Ma'af, tapi aku harus pergi.... jadi..."
    show miharu genki at ExitLeft(0.75)
    u "SAMPAI NANTI~!"
    k_nervous "Hah?"
    jump a1k1_who_id
label a1k1_eyes_id:
    k_furious "Hey! Situ buta ya?!"
    show miharu grief at Rise(0.5, 0.25)
    u "HIYAAAHHH~!!  AMPUN!!"
    show miharu uncomfortable at Bounce(1)
    u "Ah! Sial! Bakal telat nih!"
    show miharu nervous
    u "Ma'af banget ya, tapi aku harus pergi skarang..."
    show miharu grief at ExitLeft(0.5)
    u "SAMPAAAAAIIIIIIIII NANTIIIIIIIIII........!"
    k_shout "Hey! KEMBALI!"
    k_stare "...."
    k_unamused "....ah..... dia kabur deh....."
    jump a1k1_who_id
label a1k2_bone_id:
    k_sneaky "OWWW!! KAKIKU!!!! PATAH NIH!!!! AKU SEKARAT!!!!!"
    show miharu grief at Rise(0.5, 0.5)
    u "Gyaaaah!! Apa yang telah kuperbuat?!!!"
    show miharu dread at Bounce(2)
    u "Telepon rumah sakit~! Telepon rumah sakit~!"
    k_genki "Oi... aku cuma bercanda kok..."
    show miharu grief at Bounce(1)
    u "AH! AKU JUGA BAKAL TELAT!"
    show miharu confused at Bounce(2)
    u "Bagaimana ini~? Bagaimana ini~?"
    k_weird "Oi... denger nggak?"
    show miharu whimper
    u "Ya... *nangis*"
    k_smug "Ma'af... tapi aku sebenernya cuma bercanda kok..."
    show miharu grief at Bounce(4)
    u "GAK MUNGKIN! KAKIMU PATAH GARA-GARA AKU!"
    k_ehhh "Eh?!"
    show miharu cautious at Bow(1)
    u "Aku janji bakal tanggung jawab penuh! Tapi setelah aku pulang kerja.."
    k_weird "Errrr.... Baiklah...."
    show miharu uncomfortable
    u "Jadi mintalah seseorang untuk membawamu ke rumah sakit..."
    show miharu whimper at ExitLeft(0.75)
    u "Sampai nanti!"
    k_gasp "AH--!"
    k_unamused "..."
    k_sarcastic "Itu tadi 'Tabrak Lari' ya?"
    jump a1k1_who_id
label a1k1_who_id:
    k_sigh "...."
    show miharu smile at RunInDistance(-0.5, 1.5, 0.6, 0.75)
    nar "Gadis itu berlari, pergi meninggalkan sekolah"
    nar "Siapa gadis itu? Dalam pikirmu..."
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
    t "Oke anak-anak!"
    t "Seperti yang kijelaskan kemarin, hari ini kita bakal punya murid baru di kelas ini..."
    show aizawa grateful
    t "Masuklah, Nona Murid Pindahan! Perkenalkan dirimu!"
    show aizawa smile at ExitLeft(1.0)
    nar "kau berjalan masuk ke kelas dan mencoba menahan rasa gugup dari tatapan murid-murid yang ada"
    k_happy "Helo semuanya... Namaku Kana"
    k_genki "Salam kenal"
    show crowd nervous behind aizawa at Rise(0.50, 0.50)
    c "{=whispered}Salam kenal juga....{/=whispered}"
    show crowd nervous at Sit(0.75)
    nar "Tidakkah kedengarannya membosankan?"
    show aizawa sigh at EnterLeft(0.0, 0.5)
    t "*hah...*"
    show aizawa resign
    t "Perkenalan yang sangat umum...."
    show aizawa fatigue
    stop music
    k_nervous "Eh?!"
    nar "kau bisa mendengar para murid berbisik: 'ahhh... mulai lagi...'"
    show aizawa chastisecenter
    t "Mana EKSPRESINYA, Hana?! Apaan-apaan ITU ?!!!"
    show aizawa sadistic
    t "ULANGI!"
    show aizawa revenge
    play music music_aizawa2
    k_omg "EHHHHHH?!!!"
    k_nervous "...."
    k_genki "Apa ini semacam lelucon penyambutan anak baru atau apa....?"
    show aizawa reprimand at Bounce(2)
    t "Tentu saja bukan!"
    show aizawa maniac
    t "SEKARANG LAKUKAN ATAU MATI!!!"
    show aizawa astound at ExitLeft(0.25)
    k_swirl "GYAAHHHH~!! OKE! OKE!"
    k_nervous "ehem...."
    menu:
        "Kau memilih cara yang aman....":
            jump a1k1_hana_id
        "Dia ingin ekspresi lebih? TUNJUKKAN EKSPRESIMU!!":
            jump a1k1_sama_id
        "Oh! Ngomong aja apa yang terlintas pertama di benakmu....":
            jump a1k1_legend_id
label a1k1_hana_id:
    k_genki "Namaku Kana, bukan Hana"
    stop music
    play sound sound_deadsilence
    c "{=whispered}*........siiiiiiingg..........*{/=whispered}"
    nar "kau yakin habislah sudah....."
    show aizawa chortlecenter at EnterLeft(0.0, 0.75)
    t "Oke, lulus..."
    show aizawa schemecenter
    k_panic "GITU AJA?!!"
    jump a1k1_intro_id
label a1k1_sama_id:
    stop music
    k_creepy "{=whispered}fufufu...{/=whispered}"
    play music music_pompous1
    k_evil "AKULAH SI HEBAT DAN YANG MULIA KANA-SAMA!"
    k_villainous "TUNDUKLAH PADAKU, RAKYAT JELATA~!"
    stop music
    play sound sound_deadsilence
    c "{=whispered}*........siiiiiiingg..........*{/=whispered}"
    nar "\"aku kasihan padanya.....\", kau bisa mendengar itu dari seisi kelas"
    nar "sungguh memalukan"
    play music music_aizawa2
    show aizawa obsessed at EnterLeft(0.0, 0.25)
    t "BRAVO!!!!"
    show aizawa love
    t "BENAR-BENAR PERKENALAN YANG SANGAT HEBAT!!! AKU SAMPAI TERHARU!!!"
    show aizawa tearsofpride
    k_ehhh "EH?!!!!"
    show aizawa squeal
    t "Aku jadi suka padamu, saudaraku!"
    show aizawa savor
    k_waterfall "Apa yang terjadi di sini?!"
    k_angry "Dan lagian aku bukan saudaramu!"
    show aizawa sweetdream
    nar "kau lalu sadar bahwa si guru aneh ini sudah berhenti memperhatikanmu"
    jump a1k1_intro_id
label a1k1_legend_id:
    k_squeal "I am Legend!"
    stop music
    play sound sound_embarrass
    c "*........grauuuu..........*"
    nar "\"Oh kenapa aku mengatakan sesuatu yang GOBLOK yang terlintas pertama dalam pikiranku?\" pikirmu"
    show aizawa orly at EnterLeft(0.0, 1.0)
    t "Ahh... ternyata kau suka menonton film si Smith itu..."
    show aizawa snicker
    k_panic "Bukan begitu....!"
    show aizawa chortlecenter
    t "Awww, tidak perlu malu... semua remaja puber pada umumnya juga menyukai si Smith itu."
    show aizawa schemecenter
    show crowd angry behind aizawa at Rise(0.5, 0.25)
    c "JANGAN NGOMONG YANG GAK BERTANGGUNG JAWAB DEH!!"
    show crowd angry at Sit(0.25)
    jump a1k1_intro_id
label a1k1_intro_id:
    show aizawa cute
    t "Baiklah.... sekarang saatnya bagiku untuk memperkenalkan diri..."
    show aizawa smile
    stop music fadeout 1
    play sound sound_spotlight
    show ambient darken behind aizawa
    show prop spotlight at Appear(0.0, 0.0, 0.0, 0.0)
    nar "lampu sorot?"
    play music sound_drumroll
    show aizawa awesome
    t "AKULAH SI HEBAT~!"
    show aizawa evilchuckle
    t "FABULOUS~!"
    show aizawa love
    t "MAGNIFICENT~!"
    show aizawa impressed
    t "MENG-INSPIRASI~!"
    show aizawa happy
    t "LEGENDARIS~!"
    show aizawa pleasantdream
    t "dan yang terpenting dari semuanya..."
    show aizawa grateful
    t "CANTIK JELITA!"
    stop music
    play sound sound_drumtada
    show aizawa squeal at Bounce(1)
    t "BU GURU AIZAWA!!!"
    play music music_pompous2
    show aizawa smile at MoveTo(0.5, 1.0)
    hide ambient darken
    with dissolve
    hide prop spotlight
    with dissolve
    with Pause(1)
    show snowblossom
    with dissolve
    nar "dia berpose dengan gaya dramatis sedikit dekat denganmu..."
    show aizawa genki
    ta "Senang berkenalan denganmu yo!"
    show aizawa smile
    stop music fadeout 2
    hide snowblossom
    with dissolve
    k_weird "errr.... uh.... okay.... senang berkenalan dengan anda juga.... Bu Guru Aizawa...."
    queue music [ music_aizawa3, music_aizawa4, music_aizawa5 ]
    show aizawa lecture at MoveTo(0.0, 0.5)
    ta "BERDIRI, KETUA KELAS!"
    show aizawa meditate
    show freya lecture behind aizawa at Rise(1.0, 0.25)
    f "Namaku Freya!!"
    show aizawa complain
    show freya irritated
    ta "Kan sulit menghafal ribuan nama siswa,y'know..."
    show aizawa fatigue
    show freya shout at Bounce(3)
    f "Paling nggak kan hafal nama murid DI KELASMU SENDIRI dong!"
    show aizawa chortleleft
    show freya scowl
    ta "Kan aku bukan wali kelasmu, jadi gak ada urusan deh..."
    show aizawa schemeleft
    show freya annoyed
    show crowd shout behind freya at Rise(0.5, 0.25)
    c "KAU  {b}ITU{/b} WALI KELAS KAMI!"
    show crowd calm
    show aizawa confuzzled
    ta "Oh ya? Kupikir aku ini wali kelas 2-C deh...?"
    show aizawa confused
    show crowd angry
    show freya bored
    c "{b}INI{/b} 2-C!!"
    show crowd calm
    k_unamused "...."
    show aizawa resign
    nar "tiba-tiba keluar dari kelas dan memastikan papan tanda kelas..."
    show aizawa genki at Laugh(3)
    show freya pout
    ta "Hahaha! Gak usah pikirin hal kecil kayak begituan..."
    show aizawa smug
    show freya nag
    f "Apa yang kau maksud dengan 'hal kecil' ini?!"
    show aizawa awesome
    show freya upset
    ta "Terserah deh... Udah pada ngerjain PR kemarin belum?"
    show aizawa snide
    show crowd shout
    show freya angry
    c "PR apaan?"
    show crowd calm
    show aizawa evilchuckle
    ta "Kok nanya, tentu aja PR Sejarah Modern"
    show aizawa smug
    show freya calm at Bounce(1)
    show freya annoyed
    f "Tapi kan situ guru Bahasa Inggris kita"
    show aizawa dumbfounded at Laugh(2)
    ta "Eh? Ara! Lupa deh LOL!"
    show aizawa nervous
    show crowd shout
    show freya tired
    c "JANGAN NGE-'LOL' KITA DEH!"
    show crowd calm
    show aizawa sadistic
    show freya perturbed
    ta "Oh! Kumpulkan ajalah PR kalian yang ada..."
    show crowd angry
    show aizawa revenge
    show freya angry
    c "SEPERTI YANG KAMI BILANG, PR APAAN NIH?!"
    play countermusic sound_chatter fadein 0.25
    show crowd angry at VChatter
    show aizawa reel at MoveTo(0.25, 0.25)
    show freya defensive at MoveTo(0.75, 0.25)
    $ renpy.pause(0.25)
    show aizawa scream at HChatter(0.25, 0.28)
    show freya shout at HChatter(0.75, 0.72)
    nar "kau berharap untuk hari pertama yang normal, tapi baru saja kekacauan dimulai..."
    show crowd angry at Sit(0.25)
    show aizawa savor at ExitLeft(0.25)
    show freya bloodlust at ExitRight(0.25)
    $ renpy.pause(0.25)
    stop music fadeout 2
    stop countermusic fadeout 0.5
    scene bg cafeteria
    with fade
    outline "Jam Istirahat Siang"
    play music music_roughday fadein 2.0
    k_sigh "*menghela*"
    nar "kau merasa sangat lelah sampai-sampai gak sanggup menyendok makanamu"
    show freya nervouschuckle at EnterLeft(0.0, 0.5)
    f "Aku jadi merasa gak enak padamu."
    show freya nervous
    k_nervous "Kenapa?"
    show freya covet
    f "Ibu Aizawa"
    show freya bashful
    menu:
        "Baiklah.....kau mesti akui, kalau dia orang yang...":
            jump a1k1_interesting_id
        "Kau cemas kalau-kalau dia itu pelarian dari rumah sakit jiwa...":
            jump a1k1_crazy_id
        "Dia mungkin blak-blakan, tapi dia pasti memiliki hati yang baik.":
            jump a1k1_nice_id
label a1k1_interesting_id:
    k_sneaky "Dia orang yang.... menarik...."
    show freya glad
    f "Oke.... Mungkin bisa dikatakan dia itu... unik...."
    show freya smile
    k_sarcastic "Unik seperti binatang langka?"
    show freya cute at Bounce(1)
    f "Tepat!"
    jump a1k1_classified_id
label a1k1_crazy_id:
    k_painful "Dia GILA!"
    show freya nervouschuckle
    f "Ya begitulah..."
    jump a1k1_classified_id
label a1k1_nice_id:
    k_genki "Kurasa dia orang yang baik."
    show freya omg at Laugh(2)
    f "HAAAH?! OTAKMU DICUCI YA?!"
    show freya nervous
    k_oops "...?"
    jump a1k1_classified_id
label a1k1_classified_id:
    show freya glad
    f "Ngomong-ngomong...."
    f "Boleh aku bertanya sesuatu?"
    show freya smile
    k_happy "Tentu..."
    show freya sarcastic
    f "Kenapa kau pindah kemari, Kana?"
    show freya uneasy
    stop music fadeout 1
    k_sad "...?"
    k_oops "Emang ada yang salah ma sekolah ini ya?"
    $ renpy.pause(1.0)
    show freya bashful
    $ renpy.pause(0.5)
    show freya tender
    $ renpy.pause(0.25)
    show freya love
    f "Oh, bukan maksudku begitu sih. Cuma penasaran..."
    show freya cute
    f "Semua orang yang kutanya selalu memiliki alasan yang menarik kenapa bersekolah di sini..."
    show freya calm
    play music music_flashback1 fadein 2.0
    k_dream "Oh begitu... baiklah..."
    show freya curious at ExitLeft(0.25)
    $ renpy.pause(0.25)
    scene bg flashback1
    with flashbackfade
    k_happy "Orang tua ku mengirimku ke sini karena mereka pergi bisnis ke luar negeri"
    k_sad "... dan gak bakal kembali buat waktu yang lama."
    scene bg flashback2
    with flashbackfade
    k_happy "Aku tak punya keluarga lain di sini,"
    k_genki "... sehingga mereka mempercayakanku pada Kepala Sekolah karena ia sahabat karib kedua orang tuaku"
    scene bg flashback3
    with flashbackfade
    k_tired "Kalo sekarang dipikir-pikir, aku gak terlalu mempermasalahkan ini"
    k_happy "Tapi tetap..."
    k_dream "Aku yakin kalau aku akan mendapatkan pengalaman yang indah di Camelia ini"
    scene bg cafeteria
    with flashbackfade
    show freya sweetdream at EnterLeft(0.0, 0.5)
    f "*angguk angguk*"
    k_relieved "Bagaimana denganmu, Freya?"
    show freya pleasantdream
    f "Yah agak miriplah denganmu..."
    show freya sweetdream
    stop music
    k_nervous "..."
    play music music_roughday
    k_unamused "Dengan kata lain, tadi itu bukan cerita yang menarik sama sekali."
    show freya mock
    f "Yah paling nggak berasalah momen-nya..."
    show freya snicker
    k_sigh "*menghela nafas*"
    show freya tender at ExitLeft(0.25)
    $ renpy.pause(0.25)
    stop music fadeout 2
    scene bg classroom
    with fade
    outline "Sepulang Sekolah"
    play music music_aizawa4 fadein 2.0
    show aizawa pleasantdream at EnterLeft(0.0, 0.25)
    ta "Baiklah, sepertinya itu saja untuk hari ini."
    show aizawa glad
    ta "Kalau masih ada pertanyaan, simpan saja untuk--"
    play sound sound_doorslam
    show aizawa astound
    nar "Pintu mendadak terbuka"
    show aizawa amused at MoveTo(1.0, 0.25)
    show miharu grief behind aizawa at EnterLeft(0.0, 0.25)
    u "MA'AF TERLAMBAT! MA'AF!"
    k_shock "AH! KAMU!"
    show aizawa naive
    show miharu confused
    u "Kamu..?"
    u ".....siapa.....?"
    show miharu nervous
    show aizawa inquisitive
    k_sneaky "Kita \”ketemu\” di gerbang depan, ingat?"
    show miharu wonder
    show aizawa snide
    u "ahhhh...."
    show miharu curious
    show aizawa cool
    u "...."
    show miharu excited at Bounce(1)
    show aizawa evilsmile
    u "ah! KAMU!"
    queue music [ music_aizawa3, music_aizawa4, music_aizawa5 ]
    stop countermusic fadeout 3.0
    show aizawa evilchuckle at Bounce(3)
    show miharu smile
    ta "Ah, jadi kalian sudah kenal sebelumnya?"
    show aizawa evilsmile
    k_angry "NGGAK!"
    show aizawa grateful
    ta "Terus kok mesra banget?"
    show aizawa drunksmile
    k_stare "Ini mesra?"
    show miharu cute
    show aizawa awesome
    ta "Omong-omong.... Akhirnya kamu datang juga, Miharu. Sayangnya kami baru selesai."
    show miharu sad at Bow(1)
    show aizawa snide
    m "Ma'af..."
    show aizawa genki at Laugh(3)
    ta "Hahahaha! Ga masalah... Aku kan orang baik. Kamu kumaafkan..."
    show crowd angry behind miharu at Rise(0.50, 0.25)
    show miharu happy
    show aizawa smile
    c "ORANG BAIK?!!"
    show crowd angry at Sit(0.25)
    show miharu cute
    show aizawa happy
    ta "Nanti mampir aja ke Ruang Staff, yah... Buat ngambil kopian materinya."
    show miharu genki at Bow(1)
    show aizawa smile
    m "Terimakasih banyak! Ibu Aizawa memang yang terbaik!"
    show miharu smile at ExitLeft(0.25)
    show aizawa squeal at Laugh(3)
    ta "Hahaha!"
    show aizawa savor
    show crowd nervous behind aizawa at Rise(0.50, 0.25)
    c "Ini pasti bercanda..."
    show crowd nervous at Sit(0.25)
    show aizawa orly
    ta "Oke semuanya, jangan lupa ngerjain PR ya..."
    show aizawa snicker at ExitRight(0.25)
    show crowd angry behind aizawa at Rise(0.50, 0.25)
    c "TAPI IBU NGGAK NGASIH PR SAMA SEKALI!!!"
    show freya chide at Rise(0.50, 0.25)
    f "*uhh* Guru yang merepotkan..."
    show crowd calm
    show freya annoyed at Sit(0.25)
    $ renpy.music.set_volume(0.25, 1, channel="music")
    play countermusic sound_chatter fadein 1.0
    show crowd calm at VChatter
    nar "Setelah guru keluar dari ruang kelas..."
    nar "Teman-temanmu mulai membereskan barang-barang mereka sambil mengobrol..."
    nar "...dan suara mereka terasa menentramkan"
    stop countermusic fadeout 2.0
    $ renpy.music.set_volume(1, 1, channel="music")
    m "Ah Freya!"
    play countermusic music_miharu3 fadein 3.0
    stop music fadeout 3.0
    show crowd calm at Sit(0.25)
    show miharu happy at EnterLeft(0.0, 0.25)
    show freya cool at EnterRight(1.0, 0.25)
    m "Ma'af merepotkan lagi, tapi bolehkah aku melihat catatanmu?"
    m "Ntar aku gambarin sesuatu deh!"
    show freya cute
    f "Ah, nggak perlu. Aku akan senang membantu..."
    show miharu genki at Bounce(1)
    show freya calm
    m "Kamu teman yang baik, yang paling baik yang pernah kukenal!"
    show freya curious
    show prop bookworm at Appear(0.15, 0.4, 0.0, 0.0)
    with dissolve
    $ renpy.pause(0.5)
    show miharu relieved
    show freya angry
    m "Untuk itu, gambar ini--"
    show prop bookworm at MoveTo(0.8,1.0)
    $ renpy.pause(1.0)
    show freya psycho at Bounce(3)
    show prop bookworm at Fling(0.8, 0.4, -0.30, 0.35, 0.35, 1095)
    $ renpy.pause(0.15)
    show miharu grief at Fling (0.0, 0.0, -1.0, -0.5, 0.5, 790)
    $ renpy.play(sound_collide)
    stop countermusic
    hide prop bookworm
    f "Nggak butuh! Udahlah, ini catatannya!"
    hide miharu
    queue music [ music_miharu1, music_miharu3 ]
    show freya disturbed
    $ renpy.pause(1.00)
    show freya meditate
    $ renpy.pause(0.50)
    nar "Kau pikir... Nggak, kamu yakin itu bukan khayalanmu saja..."
    show freya glad at Bounce(1)
    f "Ah! Hampir lupa Kana, ini Miharu. Dia akan jadi teman sekamarmu."
    show freya smile at ExitRight(0.25)
    show miharu happybandage at EnterLeft(0.5, 0.5)
    m "Jadi dia murid pindahan itu."
    show miharu uncomfortablebandage
    m "Ma'af telah menyusahkanmu pagi ini."
    menu:
        "Manis sekali, dia masih mikirin tentang kamu.":
            jump a1k1_forget_id
        "Oh tidak! Dia tidak bisa lari begitu saja!":
            jump a1k1_hell_id
label a1k1_forget_id:
    k_relieved "Sudahlah, aku sudah melupakannya."
    show miharu relievedbandage
    m "Kamu orang yang baik..."
    k_genki "Senang berkenalan denganmu, Miharu."
    jump a1k1_conclusion_id
label a1k1_hell_id:
    play sound sound_thunder
    show lightning
    show miharu dreadbandage
    k_furious "Mana bisa aku melupakan HAL ITU?!"
    hide lightning
    show miharu griefbandage at Bow(1)
    m "Hiyaaaaaaahhhh...!! Ampuuuunnn..!!"
    k_scheme "Ah, biarlah itu berlalu, jadi..."
    show miharu curiousbandage
    k_genki "Senang berkenalan denganmu, Miharu."
    jump a1k1_conclusion_id
label a1k1_conclusion_id:
    show miharu excitedbandage
    m "Senang berkenalan denganmu, Kana."
    show freya cute at EnterRight(1.0, 0.25)
    show miharu cutebandage
    f "Yah...."
    f "Kukira sudah saatnya kita kembali ke asrama."
    show freya calm at ExitRight(0.25)
    show miharu smilebandage at ExitRight(0.5)
    $ renpy.pause(0.5)
    stop music fadeout 3.0
    scene bg dorm
    with introfade
    outline "Asrama Camelia"
    play music music_mellow
    scene bg dormhall
    with dissolve
    show freya keen at EnterRight(0.5, 0.75)
    f "Ini asrama kita. Semua murid Camelia tinggal disini."
    f "Ada tiga lantai di asrama ini, ditambah ruang bawah tanah yang nggak boleh dimasuki."
    show freya cute at MoveTo(1.0, 0.5)
    f "Pencatatan, telepon, dan kafetaria di lantai satu..."
    show freya curious at MoveTo(0.0, 0.75)
    f "Dan kamar-kamar kita, toilet, serta kamar mandi di dua lantai diatasnya."
    show freya love at MoveTo(0.5, 0.5)
    f "Ada empat ranjang di setiap kamar."
    f "...Yang artinya, kamu berbagi kamar dengan empat orang."
    show freya glad at MoveTo(0.0, 0.5)
    f "Kamarmu #327, di lantai tiga, belok kanan dua kali setelah tangga."
    show freya smile at MoveTo(0.5, 0.25)
    show miharu smug at EnterLeft(0.0, 0.25)
    f "Dan Miharu ini teman sekamarmu."
    show freya smile at MoveTo(0.0, 0.25)
    show miharu smile at ExitLeft(0.25)
    $ renpy.pause(0.75)
    show freya keen
    f "Ada pertanyaan?"
    show freya cool
    menu:
        "Wow! Dia bicara banyak...":
            jump a1k1_enough_id
        "Tunggu! TIGA orang lagi?!!":
            jump a1k1_two_id
label a1k1_enough_id:
    k_nervous "Kurasa itu saja..."
    show freya glad
    f "Bagus."
    jump a1k1_fine_id
label a1k1_two_id:
    k_nervous "Kau tahu siapa dua orang lagi?"
    show freya sarcastic
    f "Yah...."
    f "Dua senior bernama Reina dan Q.U.E.E.N"
    show freya weary
    k_baka "<Queen>? Nama asli?"
    show freya yearn
    f "Ya, sekarang."
    show freya love
    f "Oh ya, kalau nulis namanya, jangan lupa pakek huruf besar semua."
    show freya tender
    k_genki "Kenapa? Dia pemimpin atau gimana?"
    $ renpy.pause(0.75)
    show freya suspicious
    f "Percayalah. Lakukan saja."
    show freya snide
    k_baka "Ha?"
    show freya evil
    f "Kecuali kamu mau tau alasannya, dengan cara yang lebih sakit."
    show freya cynical
    k_gasp "....!!"
    $ renpy.pause(1.0)
    jump a1k1_fine_id
label a1k1_fine_id:
    show freya glad
    f "Yah, kalau butuh bantuan, ada pertanyaan, atau mau main..."
    show freya cute
    f "Datang saja ke kamarku, #156, di lantai pertama."
    show freya calm
    k_happy "Baik, terimakasih!"
    show freya smile at ExitRight(0.75)
    nar "Freya melangkah pergi"
    k_genki "Yah, sepertinya sudah waktunya kita ke kamar."
    k_smile "...."
    show miharu confused at EnterLeft(0.0, 0.25)
    m "...?"
    k_sarcastic "...uh... Oke, sejujurnya aku tidak ingat apa yang Freya bilang."
    show miharu relieved
    k_waterfall "Duluan deh."
    show miharu glad at Bounce(1)
    m "Baiklah! Ikut aku..."
    scene bg dormhall1
    with dissolve
    $ renpy.pause(0.25)
    show miharu chibi1 at Bobble(1.15, 0.6, -0.15, 0.6, 0.35, 2.0)
    nar "dan begitulah"
    scene bg dormhall2
    with dissolve
    show miharu chibi1 at Bobble(-0.15, 0.0, 1.15, 0.2, 0.25, 3.0)
    nar "tidak terlalu mengagetkan, Miharu adalah jenis yang buta arah."
    scene bg dormhall3
    with dissolve
    show miharu chibi1 at Fling(1.15, 0.7, -0.15, 0.3, 2.00, 365.0)
    nar "Dan kamu menyusuri koridor yang seperti labirin selama 15 menit mengikuti gadis itu"
    scene black
    with dissolve
    stop music fadeout 3.0
    nar "...sampai akhirnya kau sampai di kamarmu."
    scene bg dormroom
    with dissolve
    play music music_quirky
    show miharu genki at EnterLeft(0.0, 0.25)
    m "Inilah dia! Kamarku istanaku!"
    k_swirl "UHH!!! Aku tidak bisa jadi Tour Guide..."
    show miharu smile at ExitLeft(0.25)
    nar "kamu ingin berbaring, tapi kamu tidak tahu yang mana ranjangmu"
    show prop haku at Appear(0.45, 0.2, 0.0, 0.0)
    with dissolve
    nar "Dan kamu melihat kamar itu penuh dengan barang-barang yang menarik"
    k_squeal "Ah! Bonekanya lucu!"
    k_happy "Milikmu?"
    show miharu happy at EnterLeft(0.0, 0.25)
    m "Bukan. Itu punyanya Q.U.E.E.N"
    k_ehhh "Eh?!!"
    nar "Jadi si \Q.U.E.E.N.\ ini suka ginian?"
    nar "Orangnya kayak gimana sih?"
    k_sarcastic "Ah, sudahlah. Itu urusan nanti."
    show miharu smile at ExitRight(0.75)
    $ renpy.pause(0.25)
    show prop haku at ExitRight(0.50)
    nar "Kalian berdua masuk"
    nar "Sementara Miharu melihat-lihat, kamu mulai membongkar tas."
    nar "Setelah mengeluarkan baju, foto, dan beberapa dekorasi lain"
    nar "...kamu mengeluarkan netbookmu dan menaruhnya diatas meja."
    show miharu genki at EnterRight(1.0, 0.25)
    m "Wuih! Lucu banget!"
    show miharu worried
    m "Tas yang sama dengan pas nabrak tadi pagi?"
    k_genki "Yep."
    show miharu concern
    m "....Apa baik-baik saja?"
    k_smile "Mmm?"
    show miharu curious at MoveTo(0.85, 0.25)
    m "Itu, yang kecil..."
    k_glad "Oh, netbook? Baik kok."
    show prop netbook at Appear(0.5, 0.5, 0.5, 0.5)
    with dissolve
    nar "kau mengangkatnya dari atas meja dan memutar-mutarnya dengan mudah"
    show miharu wonder
    nar "sebenarnya sangat ringan, tapi Miharu melihatmu sepertinya sangat kuat untuk bisa mengangkatnya"
    show prop netbook at Shake(0.4, 2)
    k_genki "Lihat? Tidak ada goresan."
    show miharu relieved at Bounce(1)
    m "Oh! Syukurlah!"
    k_happy "Yap, si kecil ini kuat kok."
    show prop netbook at Heft(0.4, 3)
    show miharu cute
    k_smug "Sudah sekitar 10 kali kujatuhkan, tapi tetap bisa nyala."
    show miharu genki
    m "Keren! Warnanya juga lucuuu banget!"
    show miharu excited
    m "Mahal yah, pastinya..."
    show miharu cute
    k_happy "Nggak juga. Untuk yang ini aku menghabiskan sekitar... Rp. 1.500.000"
    k_relieved "Cukup bagus untuk sebuah komputer, dan aku tau ada yang lebih murah."
    show miharu genki at Bounce(1)
    m "Hebat! Murah banget! Lebih murah dari yang kukira!"
    hide prop netbook
    with dissolve
    show miharu smile
    k_smile "hehe..."
    show miharu grief at MoveTo(0.5, 0.25)
    m "Omong-omong tentang murah, saat ini aku lagi bokek dan kelaparan."
    k_oops "?!"
    show miharu excited at Bounce(4)
    m "...jadi ayo kita makan di Bombshelter malam ini!"
    show miharu cute
    k_nervous ".........\"Bombshelter\"?"
    show miharu happy
    m "Itu sebutan buat kafetaria asrama."
    show miharu cute
    k_weird "Um... baiklah...."
    nar "hari ini kamu sudah mengalami banyak keanehan. Satu lagi nggak masalah lah."
    k_nervous "Ayo.... Ayo pergi makan kalau begitu."
    show miharu glad at Bounce(2)
    $ renpy.pause(0.25)
    show miharu smile at ExitLeft(0.5)
    $ renpy.pause(0.5)
    stop music fadeout 3.0
    scene bg bombshelter
    with slowdissolve
    outline "The Bombshelter"
    play music music_bombshelter1 fadein 2.0
    nar "Sekarang kau tahu kenapa disebut \”Bombshelter\”"
    nar "Dinding tebal, lampu redup, tanpa jendela, dan dekorasi minim"
    nar "Lebih mirip perlindungan serangan udara ketimbang tempat makan."
    nar "Pantes murah..."
    show miharu genki at Rise(0.5, 0.25)
    m "Leganya! Aku belum makan apa-apa dari pagi!"
    show miharu smile
    nar "Pepatah \”Lapar adalah bumbu terbaik\” sepertinya benar adanya."
    play sound sound_thunderstep
    with vpunch
    nar "...secara ini salah satu makanan paling nggak enak seumur hidupmu."
    show reina silhoutte behind miharu at EnterRight(0.7, 2.5)
    play sound sound_thunderstep
    with vpunch
    show ambient darken
    with slowdissolve
    play sound sound_thunderstep
    with vpunch
    nar "belum apa-apa, mendadak,"
    show miharu wonder
    nar "...kamu dikagetkan dengan sosok tinggi yang muncul dan mendadak memeluk Miharu"
    show reina relievedblush
    show ambient darkenhole
    with dissolve
    u "Miharu sayang! Sudah lama ya!"
    show miharu happy
    show reina tenderblush
    m "\”Sudah lama\”?"
    show reina relievedblush
    u "Ya, sejak pagi."
    show reina desire
    u "Tapi tanpamu, serasa lima tahun!"
    hide ambient darkenhole
    show miharu cute
    show reina lovestarved
    k_sigh "Ehem!"
    show reina stare
    k_sarcastic "Ma'af mengganggu, tapi, boleh tau, siapa ya?"
    show reina calm at Bounce(1)
    show reina oppose
    u "Cintanya."
    show miharu uncomfortable
    show reina frown
    nar "GLEK! Jujur sekali!"
    show miharu genki at Laugh(3)
    show reina lust
    m "Hahaha! Apanya yang \”Cintanya\”? Kita kan teman sekamar..."
    show miharu smile
    show reina hentai
    k_nervous "Eh?"
    show miharu happy
    show reina fantasize
    m "Ya, ini Reina, teman sekamar kita."
    show miharu cute
    show reina blush
    k_omg "EHHH?!"
    show miharu smile at Sit(0.25)
    show reina taunt at MoveTo(0.5, 0.75)
    r "Oke... Jadi ini murid pindahan itu."
    show reina mock
    r "mmmmm... Lupa, Kana, atau Hana?"
    play sound sound_wind
    show ambient icy
    with dissolve
    show reina fufufu
    nar "Kamu merinding atas tatapan dingin plus cemburu itu."
    show reina sinister
    k_nervous "....Kana."
    hide ambient icy
    with dissolve
    show reina reluctant
    r "Ah, ya... Kana."
    show reina evil
    r "Aku Reina. Senang berkenalan denganmu."
    show reina smug
    k_nervous "Uh... Senang berkenalan juga... Kak Reina."
    show reina chastise
    r "Panggil \”Reina\” saja..."
    show reina happydream at MoveTo(0.7, 0.25)
    show miharu calm at Rise(0.5, 0.25)
    nar "Dan dia kembali memeluk Miharu"
    show reina kawaii
    r "Jadi, makan apa lagi nih, Miharu sayang?"
    r "Kutraktir deh."
    show reina kawaiismile
    $ renpy.pause(0.5)
    show miharu genki at Bounce(3)
    show prop foodbubble1 at Appear(0.30, 0.18, 0.5, 0.5)
    show prop foodbubble1 at Heft(0.55, 20)
    m "Ah, baik sekali! Terimakasih! Aku mau bihun goreng!"
    hide prop foodbubble1
    show miharu smile
    show reina happy
    r "Apa sih yang nggak buat kamu..."
    show prop foodbubble2 at Appear(0.25, 0.60, 0.5, 0.5)
    show prop foodbubble2 at Heft(0.55, 20)
    show miharu calm
    show reina smile
    k_genki "Aku nasgor dong."
    show prop foodbubble2 at Fling(0.25, 0.60, -0.5, 0.7, 0.5, 730)
    show miharu worried
    show reina suspicious
    r "Nggak nanya."
    hide prop foodbubble2
    show reina angry
    k_sneaky "Heh?"
    show miharu genki at Laugh(3)
    show reina bashfulleft
    m "Hahaha! Jangan gitu ah, Reina"
    show miharu glad
    show reina enchanted
    m "Nanti banyak yang salah paham. Hahahaha..."
    show miharu smile
    show reina awkward
    nar "Miharu pikir Reina bercanda, tapi terlihat jelas ia serius."
    show reina lecherous
    nar "Sangat jelas ia melihat Miharu. Bukan yang lain."
    show reina naughtydream
    nar "Kalau begitu... bagaimana kalau... mungkin..."
    show miharu confused
    show reina mesmerized
    k_sigh "Ah, sudahlah, aku ambil sendiri."
    show miharu happy at MoveTo(0.0, 0.5)
    show reina embarrassed at Bounce(1)
    m "Yah, kalau begitu samaanlah."
    show reina gulp at Bounce(3)
    $ renpy.pause(0.15)
    show reina overprotect at MoveTo(0.15, 0.25)
    show miharu cute
    r "TIDAK, TUNGGU!"
    show reina tense
    nar "hehe, gitu dong."
    show reina awkward
    r "Iya, iya, dua-duanya kutraktir deh."
    show miharu genki at Bow(1)
    show reina nervousblush
    m "Benarkah?! Terimakasih banyaaak!"
    show miharu smile
    show reina genki
    r "Nggak masalah, Miharu sayang."
    show ambient reinaglare
    with dissolve
    show reina evil
    nar "belum sempat merasa menang, tiba-tiba senyuman jahat sekilas terlontar kepadamu"
    nar "merinding, kamu ketakutan apa yang akan terjadi."
    hide ambient reinaglare
    show prop foodbubble3 at Appear(0.85, 0.25, 0.5, 0.5)
    show prop foodbubble3 at Heft(0.55, 20)
    show miharu curious
    show reina shock
    ta "Dan bawa juga ayam gorang kalasan sekalian yah! Makasih!"
    hide prop foodbubble3
    nar "........."
    nar "Kamu menengok kaget kearah datangnya suara"
    menu:
        "Haruskah kamu berteriak keras...?":
            jump a1k1_kya_id
        "...atau SANGAT keras?":
            jump a1k1_gya_id
label a1k1_kya_id:
    show miharu uncomfortable
    k_swirl "KYAAAA!!"
    show reina huh at Bounce(1)
    r "ARGH?!!"
    show aizawa calm at EnterRight(1.0, 0.25)
    show miharu confused
    show reina chide
    ta "Reaksi apaan tuh?!"
    jump a1k1_reaction_id
label a1k1_gya_id:
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
    ta "A-ha! Itu baru reaksi dari hati yang paling dalam, LOL!"
    hide redsiren
    stop sound
    jump a1k1_reaction_id
label a1k1_reaction_id:
    show miharu glad at Bow(1)
    show aizawa snide
    show reina frustrated
    m "Selamat malam, Bu Aizawa."
    show miharu smile
    show aizawa grateful
    ta "Ah! Selamat malam, Miharu!"
    show miharu happy
    show aizawa amused
    show reina impatient
    m "Tumben datang, perlu sesuatu, Bu Aizawa?"
    show miharu cute
    show aizawa cute
    ta "Lha, tentu buat makan malam gratis...~"
    show aizawa smug
    show miharu confused at ExitLeft(1.00)
    show reina smile at MoveTo(-0.4, 0.75)
    $ renpy.pause(1.25)
    hide miharu
    show reina angry at MoveTo(0.5, 0.15)
    show aizawa baka
    $ renpy.pause(0.25)
    show reina shout at Bounce(3)
    r "Anda bukan murid, ingat?! Jadi bayar sendiri dong!"
    show aizawa complain at Laugh(2)
    show reina angry
    ta "Ckk ckk! Nggak sopan, aku juga murid loh..."
    show aizawa fatigue
    show reina chastise
    r "Jaman {b}Stinky{/b} belum bubar..."
    show aizawa meditate
    play sound sound_gong
    show ambient zen behind reina at Appear(0.0, 0.0, 0.0, 0.0)
    with slowdissolve
    show aizawa lecture
    show reina bored
    ta "Anak muda, dalam kehidupan, belajar itu sampai ke liang lahat."
    show aizawa pity
    show reina calm at Bounce(1)
    show ambient zen behind reina at Fling(0.0, 0.0, 0.0, 2.5, 0.75, 365)
    show reina nag
    r "Jangan berfilosofi!"
    show reina complain
    r "Ibu kan tamat lima tahun lalu!"
    hide ambient zen
    show aizawa yelp at Bounce(2)
    show reina chide
    ta "Awww! Jahat!"
    show aizawa accuse
    ta "Diatas ketinggian non? Kurang oksigen jadi rese?"
    show reina blush
    show aizawa stare
    stop music
    r "........."
    show reina shameshiftleft at MoveTo(0.25, 0.5)
    $ renpy.pause(1.0)
    show aizawa revenge
    show reina shameshiftleft at MoveTo(0.15, 0.25)
    $ renpy.pause(0.5)
    show reina shameshiftleft at MoveTo(0.0, 0.25)
    $ renpy.pause(0.75)
    play music music_crazyfight1
    show reina shameleft
    r "Tapi kita... {p}... {p}...{=whispered}tingginya kan sama....{/=whispered}"
    show aizawa orly at Laugh(4)
    show reina shameright
    ta "Oh-hohoho! Dulu iya kaleee..."
    show aizawa squeal
    show reina furiousblush
    ta "Tapi situ sekarang kan {b}GEDE{/b} banget"
    show angrytwitch at Appear(0.4, 0.1, 0.5, 0.5)
    show aizawa evilchuckle
    ta "Paling tinggi dan paling ganteng diantara cowok-cowok!"
    show aizawa genki at Laugh(4)
    show reina impatient
    ta "Haha! Hati-hati wahai pangeran, ntar aku jatuh cinta!"
    show aizawa amused
    hide angrytwitch
    $ renpy.pause(2.5)
    show reina taunt at Laugh(3)
    r "fufufu! Coba aja..."
    show aizawa astound
    show reina mock
    r "Karena kalau sampai cewek se {b}LEBAY{/b} ini bisa naksir orang..."
    show aizawa unamused
    show angrytwitch at Appear(0.9, 0.1, 0.5, 0.5)
    show reina evil
    r "Tipenya nggak jauh-jauh dari aku."
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
    ta "Adu mulut!!"
    $ renpy.pause(2.0)
    nar "Walaupun menyenangkan melihat pertarungan itu"
    nar "...kamu ingin menghentikannya sebelum aura yang nggak enak memenuhi kafetaria."
    stop music
    stop countermusic
    m "Baiklah, cukup!"
    show reina gulp at MoveTo(0.25, 0.25)
    show aizawa confuzzled at MoveTo(0.75, 0.25)
    nar "untungnya Miharu menyela."
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
    m "Damai, oke? Ingat, kita ini manusia."
    m "Kita harus saling tolong menolong dan menjaga hubungan baik dengan sesama"
    show reina bored
    m "Karena tidak ada keuntungan dari saling menyerang satu sama lain."
    show reina chide
    r "DEMIKIAN!"
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
    r "Aku puas jika dendam ini akan terbalaskan..."
    show reina scold at Bounce(1)
    r "...Atas kue ulang tahun mematikannya yang hampir membunuhku tahun lalu!"
    show aizawa moronic
    show reina angry
    play music music_ridiculous fadein 2.0
    show prop blackforest1 behind reina at Appear(0.5, 0.4, 0.5, 0.5)
    with dissolve
    ta "Kejam! Aku susah payah membuatnya!"
    show aizawa yelp at Bounce(2)
    show reina threaten
    ta "Aku menyiapkannya selama tiga hari!"
    show reina reprimand at Bounce(1)
    show aizawa pity
    r "Dan kau membiarkannya diluar selama empat hari!"
    play countermusic sound_poison fadein 2.0
    show prop blackforest2 behind reina
    with slowdissolve
    show aizawa dumbfounded
    show reina pout
    r "Kau bahkan tidak merasa bersalah mengirimkan aku kue penuh jamur!"
    show reina pout at Bounce(2)
    show aizawa nervous
    r "Dan kau bilang itu Black Forest gaya baru!"
    show miharu excited at EnterLeft (0.2, 0.25)
    show reina mope
    m "Haha! Ah! Aku ingat..."
    stop countermusic
    hide prop blackforest2
    with dissolve
    show overlay hospital
    with dissolve
    show miharu happy
    show aizawa chastiseright
    show reina hopeless
    m "Kita semua pingsan setelah memakan itu dan dibawa ke rumah sakit akibat keracunan makanan."
    show miharu glad
    show aizawa schemeright
    show reina speechless
    m "Setelah itu, Bu Aizawa dikenal sebagai \“Koki Kematian\”."
    hide overlay hospital
    with dissolve
    show aizawa chortleright at Laugh(2)
    show miharu smile
    show reina impatient
    ta "Sudahlah, pendidikan keras seperti itu perlu..."
    show aizawa orly
    ta "...supaya nantinya engkau tumbuh menjadi orang dewasa yang kuat dan sehat."
    show aizawa nervous
    stop music
    $ renpy.pause(2.50)
    show reina ippenshindemiru
    r "JANGAN NGE... {p}\"LOL\"... {p}{b}AKU!!!{/b}"
    play music music_crazyfight3 fadein 1.0
    play countermusic sound_war fadein 2.0
    show miharu grief at Sit(0.25)
    show reina scold at MoveTo(0.25, 0.25)
    show aizawa shock at MoveTo(0.75, 0.25)
    $ renpy.pause(0.25)
    show reina shout at HChatter(0.25, 0.28)
    show aizawa scream at HChatter(0.75, 0.72)
    $ renpy.pause(2.0)
    nar "*duh*... bisa dilihat kenapa Reina marah..."
    hide miharu
    show ambient fire behind reina
    with dissolve
    nar "sekarang, adu mulut ini semakin keras..."
    show crowd calm behind ambient
    with dissolve
    nar "pastinya, sebentar lagi ini bakalan jadi tontonan semua murid"
    k_unamused "Ugh! Berhentilah, ini memalukan!"
    show miharu nervous behind aizawa at EnterLeft (0.5, 0.25)
    $ renpy.pause(0.25)
    show miharu dread behind aizawa at HChatter(0.5, 0.52)
    m "Berhentilah!"
    show miharu grief at QuickFling (-1.0, -0.5, 0.5, 550)
    show prop chair behind crowd at Appear(0.1, 0.8, 0.5, 0.5)
    show prop chair behind crowd at SetPosition(0.2, -45.0)
    show prop chair behind crowd at SendTo(0.1, 0.45, 1.0)
    nar "Tapi mereka tetap bertengkar... Sepertinya tidak ada yang bisa menghentikan."
    hide miharu
    show angrytwitch at Appear(0.15, 0.35, 0.5, 0.5)
    u "{b}Denger nggak apa yang Miharu bilang?!{/b} "
    u "{b}HENTIKAN KEBODOHAN INI SEKARANG!!!{/b}"
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
    nar "kau kaget mendengar suara yang demikian keras dan kursi yang terlontar dari kerumunan"
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
    nar "dan kemudian, sesosok gadis muncul dan berjalan kearah mereka"
    show angrytwitch at Appear(0.35, 0.35, 0.5, 0.5)
    u "Yah yah... Sepertinya kalian sudah merusak mood-ku"
    hide angrytwitch
    u "Padahal yang kubutuhkan adalah sedikit ketenangan untuk menikmati makan malam..."
    u "*Duh* dan sekarang... terutama karna anda, Bu Aizawa..."
    show aizawa complain behind crowd at SendTo(0.8, 0.5, 0.15)
    ta "AKU LAGI?!"
    show aizawa complain behind crowd at SendTo(0.8, 0.8, 0.25)
    u "...dan sekarang sudah tidak ada lagi."
    hide reina
    hide aizawa
    show queen frown behind crowd at Heft(0.45, 3)
    u "Ini tidak bisa dibiarkan!"
    nar "Menghindari terseret ke babak baru drama ini, kamu berbisik ke Miharu..."
    k_sarcastic "{=whispered}Dia korban Black Forest itu juga?{/=whispered} "
    show miharu concern at EnterLeft(0.0, 0.25)
    m "{=whispered}Yup...{/=whispered}"
    show miharu doubt
    k_sneaky "{=whispered}Siapa dia?{/=whispered} "
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
    nar "Kamu merinding karena memotong pembicaraan Q.U.E.E.N. "
    hide queen
    show queen lecture at EnterRight(1.0, 0.25)
    show miharu nervous at MoveTo(-0.3, 0.25)
    q "SIAPA?!!"
    show queen frown
    nar "...dan kamu takut saat dia mulai berbalik melihat siapa yang memotongnya tadi"
    nar "untungnya, sebuah suara dari kerumunan menyelamatkanmu"
    show freya berate at EnterLeft(0.0, 0.25)
    f "Jangan mulai lagi deh, Q.U.E.E.N."
    show freya glare
    k_incredulous "Freya! Kamu disini juga!"
    show freya irked
    f "Iyalah, satu asrama kan makannya disini."
    show freya troubled
    show queen bored
    nar "Semuanya? Miskin..."
    show freya fury at MoveTo(0.5, 0.25)
    $ renpy.pause(0.25)
    show freya shout at Bounce(4)
    $ renpy.pause(0.5)
    show miharu confused at MoveTo(0.0, 1.0)
    f "{b}Oke, okee... Bubar! Sudah tidak ada yang perlu dilihat!{/b} "
    show freya irritated
    hide crowd nervous
    with dissolve
    nar "Kerumunan membubarkan diri diiringi gerutu yang serempak"
    show freya obligated at Sit (0.25)
    $ renpy.pause(1.0)
    show freya reprimand at Rise(0.5, 0.25)
    show aizawa aho at Rise(0.7, 0.25)
    $ renpy.pause(0.25)
    show miharu cute
    show queen frown
    f "Dan Bu Aizawa, aku tidak tahu berapa kali harus bilang ini,"
    show freya scold at Bounce(1)
    show aizawa confused
    f "Bukankah seharusnya anda sudah pulang sekarang?"
    show freya shout at Bounce(3)
    show aizawa confuzzled
    f "Dewasalah, dan berilah contoh yang baik kepada murid!"
    show miharu smile
    show aizawa cry
    show freya irritated
    ta "Tapi aku belum bayar uang sewa, belum bisa pulang..."
    show aizawa weep
    show freya lecture
    show queen calm
    f "Lalu, gaji anda?"
    show aizawa whimper
    show freya irritated
    ta "Oh, tentu, gaji selalu tepat waktu."
    show aizawa aho
    show freya leer
    ta "Tapi... Anu, itu... Biasalah, belanja..."
    show miharu uncomfortable
    show queen bored
    ta "...dan saat sadar, udah abis."
    show aizawa orly at Laugh(8)
    show freya angry
    show queen boredleft
    ta "Dan uang sewa tiga bulan belum kebayar LOL!"
    show aizawa nervous
    stop music
    play sound sound_deadsilence
    show miharu nervous
    nar "Dan semuanya terdiam"
    play music music_ridiculous fadein 5.0
    show freya defensive
    k_unamused "Serius..."
    show reina chide behind miharu at EnterLeft(-0.4, 0.25)
    r "Ngasal..."
    show miharu sad at Bow(1)
    show reina leer
    m "Ibu yang malang--"
    show queen chideleft at Bounce(1)
    show miharu dread
    q "Bodoh."
    show aizawa calm at Laugh(3)
    show miharu confused
    show aizawa genki
    show freya annoyed
    show reina angry
    show queen boredleft
    ta "Haha! Iya sih! Kepala sekolah juga bilang gitu!"
    show aizawa happy
    ta "Makanya beliau mengizinkan aku tinggal disini sementara."
    show miharu nervous
    show aizawa megasigh
    show freya evildream
    show angrytwitch at Appear(0.47, 0.18, 0.5, 0.5)
    show reina scowl
    show queen stareleft
    ta "*duh* seandainya dia sedikit kasihan padaku..."
    show aizawa pleasantdream at Laugh(2)
    show reina chastise
    show queen stareright
    ta "...dan memberikan mansionnya, atau malah apartemen kek..."
    show reina speechless
    show aizawa sweetdream
    hide angrytwitch
    $ renpy.pause(2.0)
    show freya psycho at Bounce(6)
    show miharu sigh
    show aizawa gasp
    f "{b}MALU DIKIT DONG!!!{/b}"
    show aizawa cry
    play sound sound_stomachgrowl
    show freya shock
    show reina shock
    show queen stareleft
    $ renpy.pause(0.75)
    show miharu uncomfortable at Bounce(1)
    show freya surprised
    show queen meditate
    m "Ah! Jadi ingat!"
    show miharu grief at Bounce(2)
    show aizawa weep
    show reina gulp
    m "Bihun, mana bihun?"
    show freya complain at MoveTo(0.35, 0.25)
    show miharu dread
    show reina embarrassed
    f "HUBUNGANNYA APA COBA?!"
    show reina awkward at Bounce(1)
    show aizawa whimper
    show freya bored
    r "Ack! Lupa!"
    show miharu sad
    show aizawa weep
    show reina nervousblush
    m "Nyuuuu....."
    show miharu doubt
    show aizawa whimper
    show reina shoo
    r "Ma'af, sebentar diambil...!"
    show aizawa weep
    show reina shoofrown at ExitLeft(0.5)
    show prop foodbubble4 at Appear(0.65, 0.5, 0.5, 0.5)
    show prop foodbubble4 at Heft(0.55, 20)
    show freya sigh
    show queen mumble
    q "Jangan lupa nasi gorengnya. Yang spesial."
    show aizawa whimper
    show reina huh at EnterLeft(-0.4, 0.25)
    hide prop foodbubble4
    show miharu confused
    show queen meditate
    r "Kapan~? Ugh~! Oh baiklah!"
    show prop foodbubble5 at Appear(0.5, 0.45, 0.5, 0.5)
    show prop foodbubble5 at Heft(0.55, 20)
    show aizawa tearsofjoy at Laugh(2)
    show miharu uncomfortable
    show freya perturbed
    show reina furious
    ta "Dan kalasan juga, hehe!"
    show prop foodbubble5 at QuickFling(1.5, 0.3, 0.5, 365)
    show reina reprimand at Bounce(3)
    show miharu nervous
    show aizawa moronic
    show freya perplexed
    show queen calm
    r "{b}DIAM! AMBIL SENDIRI!!!{/b}"
    show aizawa cry at Bow(1)
    show miharu smile
    show freya irked
    show reina furious
    ta "Hauu... *srooot*"
    show aizawa whimper
    show reina impatient at ExitLeft(0.25)
    show freya mocksideways
    nar "Reina pergi, meninggalkanmu yang berpikir apakah dia masih ingat pesananmu"
    show miharu smile at ExitLeft(0.25)
    show aizawa weep at Sit(0.25)
    show freya mocksideways at ExitRight(0.25)
    show queen calm at ExitRight(0.25)
    $ renpy.pause(0.25)
    stop music fadeout 3.0
    scene bg dormroom
    with dissolve
    outline "KEMBALI KE KAMAR"
    play music music_quirky
    show miharu genki at Rise(0.0, 1.0)
    m "Ah~! Kenyaaang...!"
    show miharu smile at VChatter
    k_painful "Ya iyalaah!"
    show miharu glad at ExitLeft(0.25)
    $ renpy.pause(0.25)
    show prop nasgor at Appear(0.5, 0.5, 0.5, 0.5)
    with dissolve
    nar "Reina ingat nasi goreng pesananmu dan tampaknya pesananmu layak makan"
    show prop nasgormini
    with dissolve
    nar "kecuali porsinya yang hanya tiga suap"
    nar "untungnya, kau sudah makan sebelumnya"
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
    nar "dilain itu, Miharu sendiri pesanannya sekitar 10 mangkok bihun goreng,"
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
    nar "...dan hebatnya, semuanya habis disantap."
    nar "\”Metabolismenya dia gimana ya?\” pertanyaan itu berputar-putar di kepalamu"
    hide miharu
    show queen talk at EnterRight(1.0, 0.25)
    q "Kalau nggak salah inget, namamu Hana bukan?"
    show queen calm
    k_nervous "Uh... Kana..."
    show queen talk
    q "Menyesal salah, tapi senang bertemu denganmu."
    show queen calm
    stop music fadeout 2.0
    menu:
        "Santai saja.":
            jump a1k1_nice1_id
        "Oh, dia asyik kok.":
            jump a1k1_hermajesty_id
label a1k1_nice1_id:
    play music music_queen1
    k_glad "Ah! Jadi ingat!"
    k_genki "Senang bertemu denganmu, Q.U.E.E.N."
    show queen mumble at Laugh(1)
    q "Kau benar menyebut namaku. Gadis pintar."
    jump a1k1_question_id
label a1k1_hermajesty_id:
    play music music_royalty
    k_dream "*membungkuk* Kehormatan buat hamba, Kanjeng Ratu."
    show queen mumble at Laugh(3)
    q "Oh-hoho! Bagus sekali!"
    show queen rebuke
    q "Tapi walaupun aku memang <queen>, aku tidak merasa perlu panggilan lain."
    show queen annoyed
    k_nervous "Oh... maaf..."
    show queen mumble at Laugh(2)
    q "Hoho! Tidak apa-apa. Kamu anak baru. Tidak masalah"
    show queen comment
    q "Tapi kali ini saja..."
    show queen stare
    k_gasp "?!!"
    k_nervous "Hehe, um.."
    jump a1k1_question_id
label a1k1_question_id:
    show queen calm
    k_happy "Boleh aku bertanya?"
    show queen talk
    q "Diizinkan."
    show queen calm
    k_glad "Apa \”Q.U.E.E.N\” ini nama asli?"
    show queen chide
    q "Bagimu, ya."
    show queen bored
    nar "\”Itu tidak menjawab pertanyaanku!\” batinmu"
    show miharu genki at EnterLeft(0.0, 0.25)
    show queen stareleft
    m "Yep! Q.U.E.E.N. Ya Q.U.E.E.N.!"
    show miharu glad at Laugh(2)
    m "Tidak perlu dibantah, hehe!"
    stop music fadeout 2.0
    show queen stareright at ExitRight(0.5)
    show miharu doubt at MoveTo(-0.3, 1.0)
    nar "Saat perhatian Q.U.E.E.N. Teralih, miharu berbisik..."
    show miharu concern
    m "{=whispered}Jangan tanya deh, atau bakalan kena kutukan boneka itu....{/=whispered}"
    show miharu doubt
    k_ehhh "{=whispered}Huh?{/=whispered}"
    show miharu concern
    m "{=whispered}Haku. Boneka kesayangannya.{/=whispered} "
    show miharu dread
    m "{=whispered}Itu bukan boneka biasa. Itu boneka santet.{/=whispered} "
    play music music_haku
    menu:
        "Oh yaaa.":
            jump a1k1_kidding_id
        "Ampun dah. Nambah lagi orang seremnya.":
            jump a1k1_scary_id
label a1k1_kidding_id:
    show ambient haunted behind miharu
    with slowdissolve
    show miharu nervous
    k_sarcastic "{=whispered}bercanda kan?{/=whispered}"
    show hauntedtwirl behind miharu
    with dissolve
    show miharu confused
    m "{=whispered}Serius!{/=whispered} "
    show creepyqueenhaku behind miharu
    with dissolve
    show miharu dread
    m "{=whispered}Namanya SHI NO HAKUSHAKU!{/=whispered} "
    m "{=whispered}Bangsawan Kematian!{/=whispered} "
    show miharu nervous
    k_sneaky "{=whispered}Huh~?!!{/=whispered}"
    jump a1k1_proof_id
label a1k1_scary_id:
    k_incredulous "Whoa!! SEREM~!!"
    show miharu worried
    m "{=whispered}Ya, kan?{/=whispered} "
    jump a1k1_proof_id
label a1k1_proof_id:
    show miharu dread
    m "{=whispered}Dan Reina sudah pernah kena~{/=whispered} "
    k_panic "{=whispered}REINA?!!{/=whispered} "
    hide ambient haunted
    hide hauntedtwirl
    hide creepyqueenhaku
    show queen hakuchideleft at EnterRight(1.0, 0.5)
    show miharu nervous
    q "Oh oh... Ada yang ngomong di belakang kah?"
    show miharu uncomfortable at MoveTo(0.0, 0.25)
    show queen hakuboredleft
    m "Ah, nggak.. nggak~!"
    show miharu whimper
    k_nervous "Haha! Uh... Kok bilang gitu?"
    show queen hakuannoyed at Bounce(1)
    show miharu doubt
    q "Hmpf! "
    stop music fadeout 1.0
    play sound sound_doorslam
    $ renpy.pause(0.5)
    nar "Dan kemudian Reina masuk"
    play music music_reina1 fadein 2.0
    queue music [ music_reina2, music_reina1 ]
    show miharu cute
    nar "Dan untuk pertama kalinya, kamu senang melihatnya"
    show reina relieved behind miharu at EnterLeft(0.5, 0.5)
    show miharu happy
    show queen hakucalm
    r "Ahhh~! Akhirnya pulang~!!"
    show miharu genki at Laugh(2)
    show reina tenderblush
    m "Selamat datang, teehee~!"
    show reina coo at MoveTo(0.1, 0.25)
    show miharu cute
    r "Miharu sayang, rindu yah?"
    show queen hakustareleft
    nar "seperti saat jam makan malam belum cukup saja,"
    show miharu smile at ExitLeft(0.75)
    show reina hentai at ExitLeft(0.75)
    nar "...sekarang dia kembali memeluk Miharu di kamar"
    show lotsoflove
    nar "dan kamu berharap ini tidak berlangsung semalaman"
    show queen hakustare
    k_nervous "Reina... Sedikit terobsesi dengan Miharu yah...?"
    show queen hakucomment
    q "Bukan urusanku."
    q "Yah, tapi bisa dibilang begitulah."
    show queen hakuboredleft at MoveTo(0.7, 1.0)
    nar "Kamu ingin bertanya lagi, tapi ia mengalihkan pandangannya ke \”pasangan\” itu"
    show queen hakuchideleft at Bounce(2)
    q "Aku tidak ingin mengganggu, tapi dari mana saja kamu Rei?!"
    hide lotsoflove
    show reina complain at EnterLeft(-0.4, 0.25)
    show queen hakuboredleft
    r "Nyuci piring. Jadwalku hari ini."
    show reina threaten at Bounce(6)
    r "Dan kerjaannya DOBEL karna ngerjain kerjaanmu juga!"
    show queen hakucommentleft at Laugh(1)
    show reina furious
    q "Ah, begitu. Terimakasih. Lanjutkan."
    show reina suspicious at Bounce(3)
    show queen hakustareleft
    r "*menggerutu*"
    show miharu sigh at EnterLeft(0.0, 0.5)
    show reina curious
    show queen hakucalm
    m "*Hoahm* Sudah malam, sudah saatnya tidur."
    show reina yawn at Bow(1)
    show miharu tired
    r "Yah, capek juga setelah yang tadi *hoahm*"
    show queen hakumumble at Bounce(1)
    show reina tired
    q "Jika demikian baiklah. Mari kita semua tidur!"
    show reina sleepy at ExitLeft(0.5)
    show miharu sigh at ExitLeft(0.5)
    show queen hakumeditate at ExitRight(0.5)
    $ renpy.pause(0.5)
    stop music fadeout 3.0
    scene black
    with dissolve
    nar "dan kemudian semuanya sudah selesai menggosok gigi, berpiyama, dan ditempat tidurnya masing-masing."
    nar "Termasuk kamu."
    scene bg dormroom2
    with dissolve
    q "Mimpi indah semuanya."
    m "Terimakasih Q.U.E.E.N.! Selamat malam semua!"
    r "Selamat malam, untuk Miharu sayang."
    q "Aku tidak?"
    r "Tidak. Malammu tidak selamat. Hehe."
    q "Bodoh."
    k_genki "Selamat malam semua! Senang bertemu kalian semua hari ini!"
    m "Senang bertemu denganmu juga! Sampai jumpa besok pagi!"
    r "Pagi-pagi sekali, atau dijatuhkan dari ranjang!"
    q "Mungkin."
    k_nervous "hehe... uh, baiklah..."
    nar "Reina dan Q.U.E.E.N berbalik dan tertidur dengan cepat"
    nar "Miharu bergeser sedikit untuk mematikan lampu"
    play sound sound_lightswitch
    scene bg dormroom3
    nar "dan gelap..."
    nar "...sampai gadis itu melihat pendaran cahaya dari netbook yang sedang kau gunakan diatas ranjang"
    play music music_calm1 fadein 5.0
    m "Oh, nggak tidur?"
    k_smile "Sebentar lagi. Ada yang harus dilakukan."
    m "Baiklah... Jangan begadang. Selamat malam."
    k_relieved "Malam..."
    nar "dan beberapa detik kemudian, Miharu sudah tertidur"
    show prop unr1 at DissolveAppear(0.09, 0.3, 0.0, 0.0, 0.5)
    show overlay netbook at DissolveAppear(0.03, 0.2, 0.0, 0.0, 0.5)
    nar "untungnya keyboard dan trackpad netbookmu tipe yang bersuara halus"
    show prop unr2
    with quickdissolve
    nar "jadi kau bisa mengetik dan ngenet tanpa membangunkan orang"
    show prop unr3
    with quickdissolve
    nar "kau melihat berita hari ini, proyek yang kau kerjakan"
    show prop unr5
    with quickdissolve
    nar "artwork baru, game, musik,"
    show prop unr4
    with quickdissolve
    nar "...dan situs-situs yang biasa kau kunjungi"
    show prop unr6
    with quickdissolve
    stop music fadeout 3.0
    nar "kau membuka webmail dan menemukan sedikit email-email singkat"
    play music music_netbook1 fadein 5.0
    scene bg email1
    with dissolve
    nar "setelah semuanya beres, berarti tinggal satu email yang harus direply"
    nvl clear
    nvl show dissolve
    play countermusic sound_typing
    net "<Dear Cyllia...>"
    net "<Ini hari pertamaku di kelas, dan ANJRIT! Udah kayak dimensi lain LOL!>"
    net "<aku bertemu guru yang rada edan, kayaknya baru aja keluar dari lingkungan sarap.> >.<"
    net "<dan aku terus bertemu dengan orang-orang yang aneh dan unik juga.>"
    net "<Lebih lagi, aku juga berbagi kamar dengan TIGA dari orang-orang itu LOL!> ^^;"
    net "<Meskipu begitu... Aku tetap ingin berpikiran positif...>"
    net "<Jika aku lebih mengenal mereka nantinya, aku yakin mereka orang-orang yang baik dan hebat.>"
    net "<Atau mungkin aku yang ikutan jadi gila, hahaha....!> ^___^'"
    stop music fadeout 3.0
    net "<Yah, kukira itu saja untuk hari ini. Akan kuceritakan lagi nanti.>"
    net "<Besok adalah hari yang berat, jadi, doakan aku!>^^"
    nvl hide nodissolve
    show ambient darken
    $ mouse_visible = False
    play music music_ED1a fadein 25.0
    queue music [ music_ED1b, music_silence ]
    $ floatingtext1 = Text("<Selamat malam...!>\n\n...\n\n<LOL! Aku lupa kalau disana siang hari!>\n<Selamat siang kalau begitu!> ^____^\n\n<Salam hangat,>\nKana-chan ^____^v\n\n\nPS:\n<.....Seperti biasa, maaf, Inggrisku buruk.> ^^;", slow=True, slow_speed=10, style="emailed")
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
    
