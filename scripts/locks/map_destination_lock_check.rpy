label map_destination_lock_check:
    scene expression player.location.background_blur

    if M_anon.is_state(S_ano02_warn) and player.location in L_home.get_all_children_inclusive() and game.timer.is_morning():
        $ player.go_to(L_home)
        jump home_front_dialogue

    elif M_anon.is_state(S_ano03_done):
        show anon f_tired a_sides with dissolve
        anon @ -m_talk "( Nope. Too tired to think. I'm done for today. It's nap time. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano16_tree) and player.location == L_treehouse:
        show anon f_grin with dissolve
        anon @ -m_talk "( I kinda want to know what {b}Erik{/b} has in store for me. )"
        anon @ -m_talk "( I mean what's the worst that could await me? )"
        anon @ f_normal_out -m_talk "( !!! )" with hpunch
        anon f_worried @ -m_talk "( No... )"
        anon f_laugh @ -m_talk "( No... That's just silly. )"
        anon f_normal @ -m_talk "( No. That's just silly. I should head {b}up to the treehouse{/b}. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano27_tony) and player.location == L_pizzeria_exterior:
        show anon f_worried with dissolve
        anon @ -m_talk "( Looks empty ... Did I beat them here? )"
        anon f_thinking @ -m_talk "( I guess I should try the door, just in case. )"
        hide anon with dissolve

    elif M_diane.is_state(S_dia01_init) and player.location == L_diane_yard:
        show anon with dissolve
        anon @ -m_talk "( I only just got here, I should try to find {b}Diane{/b}. )"
        hide anon with dissolve

    elif M_diane.is_state(S_dia01_find) and player.location == L_home:
        show anon with dissolve
        anon @ -m_talk "( Time to g- )"
        anon f_surprised @ -m_talk "( Woah! I almost forgot to {b}look for the shovel in the garage{/b}! )"
        hide anon with dissolve

    elif M_diane.is_state(S_dia01_give) and player.location == L_diane_yard:
        show anon with dissolve
        anon @ -m_talk "( {b}Diane{/b}'s waiting for me, I should find her before I leave! )"
        hide anon with dissolve

    elif M_debbie.is_state(S_debbie_overheard) and player.location != L_diane_yard and game.timer.is_evening():
        show anon f_tired with dissolve
        anon @ -m_talk "( Nope, I'm not doing anything but crawling into bed. )"
        hide anon with dissolve

    elif M_debbie.is_state(S_debbie_lawn_delay) and game.timer.is_evening():
        show anon f_unimpressed with dissolve
        anon @ -m_talk "( Really? Just accept we're on rails and {b}click the bed{/b}. )"
        pause .5
        show anon f_sad_down with dissolve
        anon @ -m_talk "( Sorry, I'm just tired. Please let me sleep... I promise tomorrow, no rails, okay? )"
        anon f_yawn @ -m_talk "{i}*Yawn*{/i}"
        anon f_shy_down of_blush @ -m_talk "( Love you really... Now, night-night. Just {b}click the bed for me{/b}? Pretty please? )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano20_cops) and player.location == L_police_front:
        show anon f_worried with dissolve:
            flip
        anon @ -m_talk "( Hopefully {b}Harold{/b} is inside working late. )"
        anon @ -m_talk "( With all this evidence there's no way he can't do anything. )"
        hide anon with dissolve

    elif player.location == L_police_front and M_eve.is_state(S_eve_police_trouble) and game.timer.is_dark():
        show anon f_worried at Transform(xanchor=.75, xpos=.5, xzoom=-1) with dissolve
        anon @ -m_talk "( I should {b}talk to Eve and Grace{/b}. )"
        anon @ -m_talk "( Make sure they're okay... )"
        hide anon with dissolve
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
