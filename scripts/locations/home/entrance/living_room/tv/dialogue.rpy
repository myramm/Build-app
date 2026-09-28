label tv_daytime:
    scene expression player.location.background_blur
    show anon f_thinking with dissolve
    anon @ -m_talk "( Urgh! Daytime TV? But I'm not sick... )"
    anon f_worried @ -m_talk "( And I can't watch porn during the day, {b}[deb_name]{/b} could catch me. )"
    anon f_surprised_forward @ -m_talk "( I am NOT having that conversation {i}again{/i}! )"
    hide anon with dissolve
    return

label tv_tired:
    scene expression player.location.background_blur
    show anon f_tired with dissolve
    anon @ -m_talk "( I don't have the energy... I think I should go to bed. )"
    hide anon with dissolve
    return

label tv_commentary(chan, flag):
    if chan == 0 and not M_player.once(flag):
        anon "( Hmm... Let's see what's on TV. )"
    elif chan == 1 and not M_player.once(flag):
        anon "( Local news. Boring! )"
    elif chan == 2 and not M_player.once(flag):
        anon "( That's the kind of sport I could get into. )"
    elif chan == 3 and not M_player.once(flag):
        anon "( Hey, it's {b}Mayor Rump{/b}! )"
    elif chan == 4 and not M_player.once(flag):
        anon "..."
        anon "( These nature channels are so strange... )"
    elif chan == 5 and not M_player.once(flag):
        anon "( Who watches this stuff? )"
    elif chan == 6 and not M_player.once(flag):
        anon "( This channel's a dud. )"
    elif chan == 7 and not M_player.once(flag):
        anon "( Man, I wish I could access this channel. )"
        anon "( {b}[jen_name]{/b} watches a lot of porn... )"
        anon "( I wonder if {b}she has a subscription{/b}? )"
    elif chan == 7 and tv_authed:
        anon "( Oh, lesbians! )"
        scene onlayer screens
        jump tv_event
    elif chan == 'rump_arrest' and not M_player.once(flag):
        anon "( I wonder how long they're going to keep replaying this footage... )"
        anon "( ... He does give good perp-walk though! )"
    elif chan == 'rump_cellmate' and not M_player.once(flag):
        anon "( Huh. )"
        anon "( I suppose that answers where {b}Kim{/b} wound up. )"
        anon "( He must think he's the mayor's apprentice or something... )"
    elif chan == 'rump_jumpsuit' and not M_player.once(flag):
        anon "( !!! )"
        anon "( Is he giving a press conference?! )"
        anon "( From jail?! )"
    return


label tv_event(rn=0):
    call tv_event_intro
    $ rn = 2 if M_jenny.get('force_couch_sex') else random.randint(1, 10)
    if rn <= 4 and M_jenny.finished_state(S_jenny_catch_her_jilling) and not M_jenny.pregnancy:
        call tv_event_jenny
    elif rn <= 8:
        call tv_event_solo
    else:
        call tv_event_debbie
    $ game.timer.tick()
    $ game.main()


label tv_event_intro:
    scene location_home_livingroom_couch01
    show anon b_couch_sit_watching f_couch_sit_watching_straight a_boner_covered
    with fade
    anon "( Everyone's asleep... This is the perfect opportunity to rub one out! )"
    show anon a_boner_pull1 with dissolve
    pause
    show anon a_boner_pull2 with dissolve
    show anon a_boner with dissolve
    pause
    show anon a_boner_jerk with dissolve
    anon "( Damn these chicks are hot! )"
    show anon f_couch_sit_watching_jerking
    anon "( I'm getting close! )"
    return


label tv_event_solo:
    anon a_boner_cum2 "HNNGGG!!!" with flash
    show anon a_boner_cum o_couch_boner_cum
    pause
    anon a_boner_cum2 o_couch_boner_cum2 "( Phew, that felt awesome! )"
    show anon f_couch_sit_watching_straight
    pause
    anon "( I guess I'd better go and get cleaned up. )"
    hide anon with dissolve
    return


label tv_event_debbie:
    scene home_livingroom_couch02
    show anon b_couch_sit_watching f_couch_sit_watching_jerking a_boner_jerk
    with fade
    debbie "{b}[firstname]{/b}?"
    show anon b_couch_sit f_couch_sit_down_surprised a_boner_jerk1 with dissolve
    anon "( Oh, crap! )"
    show anon f_couch_sit_right
    anon @ -m_talk "( {b}[deb_name]{/b} is coming! )"
    show old_debbie 126 at Position (xpos=917,ypos=694)
    hide anon
    show player 303 at left
    with dissolve
    debbie "Is somebody out here?!"
    show old_debbie 127 at Position (xpos=872,ypos=540) with dissolve
    debbie "Hello?!"
    debbie "Oh, they left the TV-"
    show old_debbie 128 at Position (xpos=862,ypos=511) with dissolve
    debbie "!!!"
    show old_debbie 132 at Position (xpos=680,ypos=768) with dissolve
    debbie "Oh, my."
    pause
    debbie "Who in the world was-"
    pause
    debbie "Wow, they're really going at it..."
    pause
    debbie "I shouldn't be watching this!"
    debbie "{b}[firstname]{/b} or {b}[jen_name]{/b} could walk in here any second!"
    show old_debbie 133 at Position (xpos=812,ypos=767) with dissolve
    pause
    hide old_debbie with dissolve
    pause
    scene expression player.location.background_blur with None
    show anon f_worried
    anon "That was close!"
    anon "I'd better just go to bed..."
    hide anon with dissolve
    hide home_livingroom_couch01
    return


label tv_event_jenny:
    show jenny b_couch_behind
    with fade
    jenny "Surprise, perv!"
    show anon f_couch_sit_down_surprised b_couch_sit a_boner
    anon "!!!" with hpunch
    show anon f_couch_sit_right a_boner_covered_shirt with dissolve
    anon "You scared me!"
    if M_diane.finished_state(S_diane_couch_crashing):
        jenny "Where's {b}Diane{/b}?"
        anon "I dunno, she must be working late or something..."
    show jenny b_couch_sit f_upset a_rest with dissolve
    jenny "Who said you could use my Pink Channel account?"
    anon "I didn't think you would mind-"
    jenny "Ugh, lesbians..."
    show jenny f_grin
    jenny "Don't you think that's kinda boring?"
    anon "Not really."
    jenny "It just seems kinda pointless when there's no dick involved..."
    anon "..."
    show jenny f_surprised
    jenny "Oh my god, were you jerking it?!"
    show jenny f_sexy
    anon "N-no..."
    jenny "Yes, you were."
    show jenny f_laugh
    jenny "Look at your dick, it's rock hard!"
    show jenny f_sexy
    pause
    jenny "You know, if you ask me real nice... I might just help you out with that."
    anon "R-really?"
    jenny "Yeah, but only if you beg me for it."
    if M_jenny.get("dominance") <= 0:
        anon "..."
        anon "P-please?"
        show jenny f_eyeroll
        jenny "Oh c'mon, that was pathetic!"
        show jenny f_sexy
        anon "..."
        jenny "Say this:"
        jenny "Please, {b}Princess [jen_name]{/b}."
        anon "Please, {b}Princess [jen_name]{/b}."
        jenny "I know, I'm just a pathetic little loser..."
        anon "{i}*Sigh*{/i} I know, I'm just a pathetic little loser..."
        jenny "... Not even worthy of your feet."
        anon "... Not even worthy of your feet."
        show jenny f_laugh
        jenny "Hahahaah!"
        show jenny f_sexy
        anon "Shh, you're going to wake up {b}[deb_name]{/b}!"
        jenny "Yeah, yeah... Alright, get it out, loser."
        show jenny f_sexy_down
        show anon a_boner with dissolve
        pause
        show anon f_couch_sit_down a_sides
        $ M_jenny.set('sex speed', .3)
        show jenny a_empty
        show expression AnimatedImage("jenny_couch_dick_rub", [1,2,3], M_jenny) as jenny_couch_dick_rub zorder 3 at Position(xalign = 0.0, yoffset = 0)
        with dissolve
    else:
        anon f_couch_sit_right "Screw you!"
        show jenny f_upset
        jenny "What?!"
        anon "I'm not begging you for anything."
        show jenny f_angry
        jenny "Don't talk to me like that!"
        anon "Shh, you're going to wake up {b}[deb_name]{/b}!"
        jenny "Grr!"
        show anon a_boner with dissolve
        anon "Just go away and let me finish."
        show jenny f_angry_pouting
        jenny "..."
        show jenny f_upset
        jenny "You are such an asshole!"
        anon "You're the one who's trying to make me beg for it!"
        jenny "Whatever."
        show jenny f_gross_down
        pause
        show jenny f_upset
        jenny "{i}*Sigh*{/i} Here..."
        show jenny f_sexy_down
        show anon f_couch_sit_down a_sides
        $ M_jenny.set('sex speed', .3)
        show jenny a_empty
        show expression AnimatedImage("jenny_couch_dick_rub", [1,2,3], M_jenny) as jenny_couch_dick_rub zorder 3 at Position(xalign = 0.0, yoffset = 0)
        anon "!!!" with hpunch
        anon "I thought you didn't want to-"
        show jenny f_sexy_down
        jenny "Just shut up!"
        jenny "I walked all the way down here, I might as well have some fun."
        pause
    show jenny f_sexy_down
    jenny "How does that feel?"
    anon "So good!"
    pause
    jenny "You are such a pervert, you know that?"
    jenny "Getting off to my feet?"
    anon "This was your idea..."
    show jenny f_laugh
    jenny "Hahahaah!"
    show jenny f_sexy_down
    $ M_player.set("masturbated tv", True)
    jump jenny_couch_fj_loop
    return


label tv_auth_pass:
    anon @ -m_talk "( !!! )"
    anon @ -m_talk "( It worked! )"
    return

label tv_auth_fail:
    show text _ ('WRONG PASSWORD') as tv_warn at Transform(anchor=(.5, .5), pos=(525, 412))
    anon @ -m_talk "( Huh. No good... )"
    anon @ -m_talk "( Maybe {b}[jen_name]{/b} has a subscription. )"
    anon @ -m_talk "( I bet they send access codes via {b}email{/b}. )"
    hide tv_warn
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
