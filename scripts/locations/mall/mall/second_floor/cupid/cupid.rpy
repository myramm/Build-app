label cupid_dialogue:
    $ player.go_to(L_cupid)
    if M_debbie.is_state(S_debbie_cupid_store):
        call expression game.dialog_select("cupid_mom_cupid_store")
        $ M_debbie.trigger(T_debbie_cupid_arrival)
    if M_daisy.is_state(S_daisy_get_new_flowers):
        call expression game.dialog_select("cupid_daisy_get_new_flowers")
    $ game.main()

label cupid_jewelery_display:
    scene expression player.location.background_blur
    if M_debbie.is_state(S_debbie_show_necklace):
        show anon f_worried with dissolve
        anon @ -m_talk "I already picked out a necklace..."

        anon @ -m_talk "I should {b}see what [deb_name] thinks{/b}."

        hide anon with dissolve
    elif M_debbie.is_state(S_debbie_dressing_room):
        show anon f_worried with dissolve
        anon @ -m_talk "I already got the necklace..."

        anon @ -m_talk "I wonder {b}what's taking [deb_name] so long{/b}..."

        hide anon with dissolve
    elif M_debbie.is_state(S_debbie_choose_gift):
        call expression game.dialog_select("necklace_display_mom_choose_gift")
        $ M_debbie.trigger(T_debbie_pick_necklace)
    $ game.main()

label cupid_dressingroom_dialogue:
    $ player.go_to(L_cupid_dressroom)
    if M_debbie.is_state(S_debbie_dressing_room):
        call expression game.dialog_select("cupid_dressroom_mom_dressing_room")
        $ M_player.set("jerk mom", True)
        $ M_debbie.trigger(T_debbie_dressing_room_check)
        $ player.go_to(L_cupid)

        $ game.timer.tick()
    $ game.main()

label cupid_store_bought_chocolates_eve_callback:
    scene expression player.location.background_blur with None
    show anon a_chocolat
    show eve
    with dissolve
    eve "Oh, let me try one!"

    anon f_worried "No, these are for your sister!"

    eve "Aww, c'mon... Just one?"

    eve "{b}Grace{/b} won't mind if I have a little sample."

    anon f_unimpressed "..."

    menu:
        "Alright but just one.":
            anon f_normal "Alright but just one."

            label cupid_store_bought_chocolates_eve_callback.double_back:
            eve @ f_laugh "Hehe, yay!"

            show anon a_idle
            show eve a_chocolat f_normal_down
            with dissolve
            eve "Okay, which one do I want?"

            pause
            eve "This one looks yummy!"

            eve f_eat_good a_chocolat @ a_chocolat_eat f_eat "Om nom!"

            show anon a_chocolat
            show eve a_idle f_eat_bad
            with dissolve
            pause
            eve f_disgusted "Eugh!"

            eve "Aww, man... I got coconut!"

            show anon f_flirt_grin
            eve f_angry "I hate coconut!"

            anon @ -m_talk "..."
            eve "Bleh, now you have let me try one more!"

            anon f_snarky "Mustahil."

            eve "B-but coconut..."

            anon "Hey, you had your chance."

            anon "It's not my fault you chose poorly!"

            eve "Lame!"

            anon @ f_laugh "Haha!"

        "I'll buy you a box.":

            anon f_normal "I'll buy you a box."

            if player.has_money(50):

                eve @ f_laugh "Oh my god, you're amazing, {b}[firstname]{/b}!!"

                show anon a_idle
                show eve a_chocolat f_normal_down
                with dissolve
                eve "Okay, which one do I want?"

                pause
                eve "This one looks yummy!"

                eve f_eat_good a_chocolat @ a_chocolat_eat f_eat "Om nom!"

                pause
                show anon a_chocolat
                show eve a_cover_mouth f_sexy
                with dissolve
                eve "Oh, yeah... That's orgasmic!"

                anon @ f_laugh "hehe."

                eve f_happy "Thank you so much for this!"

                anon "Terima kasih kembali."

                $ player.spend_money(50)
                $ M_eve.dating.increment(3)
            else:
                anon f_sad_down "Is what I would say if I wasn't broke..."

                eve f_sad "Aduh."

                show anon f_tired
                pause
                anon f_normal @ f_eyeroll "Okay, fine... But just one!"

                jump cupid_store_bought_chocolates_eve_callback.double_back
            hide anon
            hide eve
            with dissolve
    if player.has_item("candle"):
        jump mall_eve_make_up_go_to_mall_has_chocolates_candles
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
