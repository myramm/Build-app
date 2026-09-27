label scene_sara_terry:
    scene location_beach_tower_sex
    show location_beach_tower_sex_overlay as bench
    call scene_sara_terry.animation
    terry "Oh, kamu harpy surgawi!"

    anon "( !!! )"
    terry "Calypso sendiri akan iri dengan pesonamu."

    sara "Mhmm!"

    anon "( {b}Kapten C Terry{/b}??? )"

    pause
    terry "Terlempar seperti lautan di tengah badai!"

    sara "Jibe ho, sayangku!"

    terry "Rak dayung kanan..."

    $ M_sara.set('sex speed', 1. / 14)
    terry "... Sulit untuk dipindahkan!"

    pause
    anon "(Apa-apaan ini-)"

    terry "Dia akan meledak!"

    sara "Bawa dia ke pelabuhan, kapten!"

    $ M_sara.set('sex speed', 1. / 16)
    terry "Oh, dia sedang ejakulasi!"

    pause
    terry "Muat senjatanya!"

    anon "(Saya sangat senang untuk mereka tetapi ini adalah pembicaraan seks yang sangat aneh...)"

    anon "(...Biarkan aku mengambil ini dan...)"


    scene location_beach_tower_floor
    with fade
    terry "OOOHHH, AKU KLUB HAULIN'!!!"

    anon "(... Oh oke, ini pasti waktunya berangkat!! )"

    return


label scene_sara_terry.animation:
    $ M_sara.set('sex speed', 1. / 12)
    show sara_sex_terry behind bench
    with fade
    return


label scene_sara_terry.replay:
    jump scene_sara_terry
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
