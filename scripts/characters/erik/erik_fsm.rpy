init -1 python:
    M_erik = Machine('erik',
                     default_loc=[[L_school_scienceclassroom,
                                   L_erikhouse_erikroom,
                                   L_erikhouse_erikroom,
                                   L_erikhouse_erikroom],
                                  [L_erikhouse_erikroom,
                                   L_erikhouse_erikroom,
                                   L_erikhouse_erikroom,
                                   L_erikhouse_erikroom]],
                     vars={'bullying delay': 999999,
                           'card_outcome': False,
                           'confessed': -1,
                           'received orcette': False,
                           'in_flagrante': False,
                           'webcam help': False})

    M_erik.add_action(T_all_sleep, ('assign', ('in_flagrante', False)))

    def erik_orcette_arrival():
        game.mail['player'].reset()
        game.mail['player'].set('m_orcette_package')

    def erik_orcette_collect():
        game.mail['player'].take()

    def erik_contraceptive_pills_acquired():
        M_roz.trigger(T_erik_learn_pills)


init -3 python:
    T_erik_intro_meet = Trigger()
    T_erik_intro_done = Trigger()

    T_erik_cards_lost = Trigger()
    T_erik_cards_found = Trigger()
    T_erik_cards_return = Trigger()

    T_erik_card_acquired = Trigger()
    T_erik_card_given = Trigger()
    T_erik_card_tournament = Trigger()

    T_erik_orc_request = Trigger()
    T_erik_orc_ordered = Trigger()
    T_erik_orc_deliver = Trigger()
    T_erik_orc_collect = Trigger()
    T_erik_orc_intercept = Trigger()
    T_erik_orc_given = Trigger()

    T_erik_bully_visitor = Trigger()
    T_erik_bully_concern = Trigger()
    T_erik_bully_coax = Trigger()
    T_erik_bully_concuss = Trigger()
    T_erik_bully_recover = Trigger()
    T_erik_bully_debrief = Trigger()
    T_erik_bully_sleep = Trigger()

    T_erik_vr_request = Trigger()
    T_erik_vr_bought_headset = Trigger()
    T_erik_vr_bought_game = Trigger()
    T_erik_vr_given = Trigger()

    T_erik_feed_quiet = Trigger()
    T_erik_feed_missing = Trigger()
    T_erik_feed_found = Trigger()

    T_erik_thief_ignore = Trigger()
    T_erik_thief_spot = Trigger()
    T_erik_thief_catch = Trigger()
    T_erik_thief_thanks = Trigger()

    T_erik_poker_idea = Trigger()
    T_erik_poker_win = Trigger()
    T_erik_poker_fun = Trigger()

    T_erik_fork_guilt = Trigger()
    T_erik_fork_feedback = Trigger()
    T_erik_fork_match = Trigger()
    T_erik_fork_teach = Trigger()

    T_erik_learn_request = Trigger()
    T_erik_learn_kamasutra = Trigger()
    T_erik_learn_pills = Trigger()
    T_erik_learn_report = Trigger()
    T_erik_learn_threesome = Trigger()

init python:
    S_erik_start = State(_("An unavoidable encounter."))
    S_erik_intro_met = State(_("We should get to school!"))
    S_erik_intro_done = State(_("He can't have left already, I wonder where he is?"))

    S_erik_cards_ready = State(_("It'll be nice to hang out with Erik again. I should stop by after school."))
    S_erik_cards_lost = State(_("Erik needs help finding his Fappening Cards."))
    S_erik_cards_found = State(_("I should return these cards to Erik."))

    S_erik_card_needed = State(_("The Cock Crown of Thorns is for sale at Cosmic Cumics."))
    S_erik_card_acquired = State(_("Erik will be so happy when I present him with this new card!"))
    S_erik_card_done = State(_("Erik will be playing in a Fappening tournament this weekend. I hope it goes well!"))

    S_erik_orc_ready = State(_("I wonder how Erik did in his tournament."))
    S_erik_orc_order = State(_("Not sure how I got roped into this, but I guess I should visit the eGay website."))
    S_erik_orc_wait = State(_("The package should arrive on Tuesday."))
    S_erik_orc_arrived = State(_("Hopefully the package is waiting for me in the mailbox."))
    S_erik_orc_acquired = State(_("I better not give this to Erik at school. It could be embarrassing!"))
    S_erik_orc_inspected = State(_("I can't believe how cool Mrs J was. I should get the packge to Erik as soon as possible."))
    S_erik_orc_done = State(_("Ahh! Don't think about it. What Erik does behind that door is his business!"))

    S_erik_bully_ready = State(_("I hope Erik enjoyed his new toy..."), delay=1)
    S_erik_bully_visit = State(_("Mrs. Johnson is waiting for me downstairs."))
    S_erik_bully_promise = State(_("Who knew! Erik is getting bullied. I should speak to him about it."))
    S_erik_bully_fight = State(_("I wonder how Erik's getting on at school."))
    S_erik_bully_blackout = State(_("Owie :("))
    S_erik_bully_recovered = State(_("I still feel a bit groggy, I should head home."))
    S_erik_bully_tired = State(_("It's been a long day. I just want my bed."))
    S_erik_bully_done = State(_("I think I diverted attention enough. Erik should have an easier time of it now."), delay=2)

    S_erik_vr_ready = State(_("Erik's basement could be great for parties. I should scope it out at the weekend."))
    S_erik_vr_needed = State(_("A VR porn game? I'm not convinced, I\'ll always prefer those point and click visual novels..."))
    S_erik_vr_buy_headset = State(_("Well I suppose the game isn't any use without the headset."))
    S_erik_vr_buy_game = State(_("Wow! That headset was expensive, but it's no use without a game to play on it."))
    S_erik_vr_acquired = State(_("My pockets feel physically lighter now. I should get this stuff to Erik."))
    S_erik_vr_done = State(_("These parties had better be worth it..."))

    S_erik_feed_ready = State(_("I should talk to Erik about who to invite to the basement."), delay=2)
    S_erik_feed_curious = State(_("It's quiet. {i}Too{/i} quiet. I should try to find Erik."))
    S_erik_feed_search = State(_("It's unusual to hear voices in Mrs. Johnson\'s room, but perhaps she\'ll know where Erik is."))
    S_erik_feed_done = State(_("Whatever I was expecting... It wasn't that!"))

    S_erik_thief_ready = State(_("I should just play it cool. I'm sure Erik already feels extremely self-conscious."), delay=1)
    S_erik_thief_active = State(_("Those noises at night are quite annoying. I should probably investigate."))
    S_erik_thief_chase = State(_("It looked like the thief was trying to force his way into Mrs. Johnson's back door!"))
    S_erik_thief_caught = State(_("Woah! I feel like the world's greatest detective! Mister J\'s in jail now, what a joker!"))
    S_erik_thief_done = State(_("Mrs. Johnson said she'd find a way to thank me. I wonder what she has in mind..."))

    S_erik_poker_ready = State(_("I wonder what Mrs. Johnson is planning. I could drop by this evening and try to find out."), delay=1)
    S_erik_poker_invite = State(_("Mrs. Johnson said she'd be up for playing poker with us. I should extend an invitation."))
    S_erik_poker_party = State(_("I have to know what Mrs. Johnson was talking about. She's in the {b}backroom{/b}."))
    S_erik_poker_done = State(_("Wow!"))

    S_erik_fork_ready = State(_("Mrs. Johnson is one hell of a woman. I wonder how she's feeling."))
    S_erik_fork_talk = State(_("Mrs. Johnson is worried about Erik, things escalated pretty quickly after poker."))
    S_erik_fork_choice = State(_("Erik asked me to speak to Mrs. Johnson about what the three of us might do in future."))
    S_erik_fork_done = State(_("Mrs. Johnson needs some time to think about the situation."))

    S_erik_learn_ready = State(_("Perhaps Erik will have an idea about what Mrs. Johnson will do."))
    S_erik_learn_fetch = State(_("Right. The hospital should have contraceptive pills, then I can look for a Kama Sutra."))
    S_erik_learn_get_kamasutra = State(_("Contraceptive pills? Check! Now just need to find a copy of the Kama Sutra."))
    S_erik_learn_get_pills = State(_("Kama Sutra? Check! Now just need to find those contraceptive pills."))
    S_erik_learn_acquired = State(_("That's everything. I should get this stuff back to Mrs. Johnson."))
    S_erik_learn_prep = State(_("Mrs. Johnson needs time to prepare. I should seek her out in a day or two."))
    S_erik_learn_finale = State(_("It's time. Mrs. Johnson should be ready by now, time to visit her in the evening."))

    S_erik_end = State(_("Wow! I'm glad I got to experience that with Erik. Mrs. Johnson is a helluva woman!"))

init python:

    S_erik_start.add(T_erik_intro_meet, S_erik_intro_met,
                     actions=('unlocklocation', L_school_front))
    S_erik_intro_met.add(T_all_school_entrance, S_erik_intro_done)
    S_erik_intro_done.add(T_erik_intro_done, S_erik_cards_ready,
                        actions=('location', {'place': L_erikhouse_basement},
                                 'force', {'tod': [1, 2]}))


    S_erik_cards_ready.add(T_erik_cards_lost, S_erik_cards_lost,
                             actions=('location', {'place': L_erikhouse_erikroom}))
    S_erik_cards_lost.add(T_all_sleep, S_erik_cards_lost,
                         actions=('unforce', None))
    S_erik_cards_lost.add(T_erik_cards_found, S_erik_cards_found)
    S_erik_cards_found.add(T_erik_cards_return, S_erik_card_needed,
                           actions=('condition', ('player.has_item("card02")',
                                                  ('trigger', T_erik_card_acquired), ())))


    S_erik_card_needed.add(T_erik_card_acquired, S_erik_card_acquired)
    S_erik_card_acquired.add(T_erik_card_given, S_erik_card_done)
    S_erik_card_done.add(T_all_sleep, S_erik_card_done,
                               actions=('condition', ('game.timer._dow == 6',
                                                      ('trigger', T_erik_card_tournament), ())))
    S_erik_card_done.add(T_erik_card_tournament, S_erik_orc_ready,
                         actions=('location', {'place': L_erikhouse_basement},
                                  'force', {'tod': [1, 2]}))


    S_erik_orc_ready.add(T_erik_orc_request, S_erik_orc_order,
                         actions=('unforce', None))
    S_erik_orc_order.add(T_erik_orc_ordered, S_erik_orc_wait)
    S_erik_orc_wait.add(T_all_sleep, S_erik_orc_wait,
                        actions=('condition', ('game.timer._dow == 0',
                                               ('trigger', T_erik_orc_deliver), ())))
    S_erik_orc_wait.add(T_erik_orc_deliver, S_erik_orc_arrived,
                        actions=('location', {'place': L_school_cafeteria},
                                 'force', {'tod': 1},
                                 'exec', erik_orcette_arrival))
    S_erik_orc_arrived.add(T_erik_orc_collect, S_erik_orc_acquired,
                           actions=('location', ('mrsj', {'place': L_erikhouse_entrance}),
                                    'force', ('mrsj', {'tod': 2}),
                                    'exec', erik_orcette_collect))
    S_erik_orc_acquired.add(T_erik_orc_intercept, S_erik_orc_inspected,
                            actions=('unforce', None,
                                     'unforce', 'mrsj'))
    S_erik_orc_inspected.add(T_erik_orc_given, S_erik_orc_done)
    S_erik_orc_done.add(T_all_sleep, S_erik_bully_ready)


    S_erik_bully_ready.add(T_erik_bully_visitor, S_erik_bully_visit,
                           actions=('location', {'place': L_erikhouse_erikroom},
                                    'force', {'flag': True},
                                    'location', ('mrsj', {'place': L_home_entrance}),
                                    'force', ('mrsj', {'flag': True})))
    S_erik_bully_visit.add(T_erik_bully_concern, S_erik_bully_promise,
                           actions=('unforce', 'mrsj'))
    S_erik_bully_promise.add(T_erik_bully_coax, S_erik_bully_fight,
                             actions=('location', {'place': [[L_school_hall,
                                                              L_school_hall,
                                                              None, None],
                                                             [None] * 4]},
                                      'force', {'tod': [0, 1]},
                                      'location', ('dexter', {'place': [[L_school_hall,
                                                                         L_school_hall,
                                                                         None, None],
                                                                        [None] * 4]}),
                                      'force', ('dexter', {'tod': [0, 1]})))
    S_erik_bully_fight.add(T_erik_bully_concuss, S_erik_bully_blackout,
                           actions=('unforce', None,
                                    'unforce', 'dexter'))
    S_erik_bully_blackout.add(T_erik_bully_recover, S_erik_bully_recovered,
                              actions=('location', ('mrsj', {'place': L_home_entrance}),
                                       'force', ('mrsj', {'flag': True}),
                                       'location', ('debbie', {'place': L_home_entrance}),
                                       'force', ('debbie', {'flag': True})))
    S_erik_bully_recovered.add(T_erik_bully_debrief, S_erik_bully_tired,
                               actions=('unforce', 'mrsj',
                                        'unforce', 'debbie'))
    S_erik_bully_tired.add(T_erik_bully_sleep, S_erik_bully_done)
    S_erik_bully_done.add(T_all_sleep, S_erik_vr_ready,
                          actions=('location', {'place': [[None] * 4,
                                                          [L_erikhouse_basement] * 4]},
                                   'force', {'tod': [0, 1, 2]}))


    S_erik_vr_ready.add(T_erik_vr_request, S_erik_vr_needed,
                        actions=('unforce', None,
                                 'condition', ('player.has_item("virtualsaga")',
                                               ('trigger', T_erik_vr_bought_headset), ()),
                                 'condition', ('player.has_item("game02")',
                                               ('trigger', T_erik_vr_bought_game), ())))
    S_erik_vr_needed.add(T_erik_vr_bought_headset, S_erik_vr_buy_game)
    S_erik_vr_needed.add(T_erik_vr_bought_game, S_erik_vr_buy_headset)
    S_erik_vr_buy_headset.add(T_erik_vr_bought_headset, S_erik_vr_acquired)
    S_erik_vr_buy_game.add(T_erik_vr_bought_game, S_erik_vr_acquired)
    S_erik_vr_acquired.add(T_erik_vr_given, S_erik_vr_done)
    S_erik_vr_done.add(T_mrsj_yoga_thanks, S_erik_feed_ready)


    S_erik_feed_ready.add(T_erik_feed_quiet, S_erik_feed_curious,
                          actions=('location', {'place': L_erikhouse_mrsjroom},
                                   'force', {'tod': 2},
                                   'location', ('mrsj', {'place': L_erikhouse_mrsjroom}),
                                   'force', ('mrsj', {'tod': 2})))
    S_erik_feed_curious.add(T_erik_feed_missing, S_erik_feed_search)
    S_erik_feed_curious.add(T_erik_feed_found, S_erik_feed_done)
    S_erik_feed_search.add(T_erik_feed_found, S_erik_feed_done)
    S_erik_feed_done.add(T_all_sleep, S_erik_thief_ready,
                         actions=('unforce', None,
                                  'unforce', 'mrsj'))


    S_erik_thief_ready.add(T_all_sleep, S_erik_thief_active)
    S_erik_thief_active.add(T_erik_thief_ignore, S_erik_thief_active)
    S_erik_thief_active.add(T_erik_thief_spot, S_erik_thief_chase)
    S_erik_thief_chase.add(T_all_sleep, S_erik_thief_active)
    S_erik_thief_chase.add(T_erik_thief_catch, S_erik_thief_caught,
                           actions=('location', ('mrsj', {'place': L_erikhouse_entrance}),
                                    'force', ('mrsj', {'tod': [0, 1, 2]})))
    S_erik_thief_caught.add(T_erik_thief_thanks, S_erik_thief_done,
                            actions=('unforce', 'mrsj'))
    S_erik_thief_done.add(T_all_sleep, S_erik_poker_ready)


    S_erik_poker_ready.add(T_erik_poker_idea, S_erik_poker_invite,
                           actions=('location', {'place': L_erikhouse_basement},
                                    'force', {'tod': 2}))
    S_erik_poker_invite.add(T_erik_poker_win, S_erik_poker_party,
                            actions=('location', {'place': L_erikhouse_backroom}))
    S_erik_poker_party.add(T_erik_poker_fun, S_erik_poker_done,
                           actions=('unforce', None))
    S_erik_poker_done.add(T_all_sleep, S_erik_fork_ready,
                          actions=('location', ('mrsj', {'place': L_erikhouse_entrance}),
                                   'force', ('mrsj', {'tod': [0, 1, 2]})))


    S_erik_fork_ready.add(T_erik_fork_guilt, S_erik_fork_talk,
                          actions=('unforce', 'mrsj'))
    S_erik_fork_ready.add(T_erik_fork_feedback, S_erik_fork_choice,
                          actions=('unforce', 'mrsj'))
    S_erik_fork_talk.add(T_erik_fork_feedback, S_erik_fork_choice)
    S_erik_fork_choice.add(T_erik_fork_match, S_erik_end)
    S_erik_fork_choice.add(T_erik_fork_teach, S_erik_fork_done)
    S_erik_fork_done.add(T_all_sleep, S_erik_learn_ready)


    S_erik_learn_ready.add(T_erik_learn_request, S_erik_learn_fetch,
                           actions=('condition', ('player.has_item("birth_control_pills")',
                                                  ('trigger', T_erik_learn_pills), ())))
    S_erik_learn_fetch.add(T_erik_learn_kamasutra, S_erik_learn_get_pills)
    S_erik_learn_fetch.add(T_erik_learn_pills, S_erik_learn_get_kamasutra)
    S_erik_learn_get_kamasutra.add(T_erik_learn_kamasutra, S_erik_learn_acquired)
    S_erik_learn_get_pills.add(T_erik_learn_pills, S_erik_learn_acquired)
    S_erik_learn_acquired.add(T_erik_learn_report, S_erik_learn_prep)
    S_erik_learn_prep.add(T_all_sleep, S_erik_learn_finale)
    S_erik_learn_finale.add(T_erik_learn_threesome, S_erik_end,
                            actions=('exec', A_sharing_is_caring.unlock))

init python:
    M_erik.add(
        S_erik_start, S_erik_intro_met, S_erik_intro_done,
        S_erik_cards_ready, S_erik_cards_lost, S_erik_cards_found,
        S_erik_card_needed, S_erik_card_acquired, S_erik_card_done,
        S_erik_orc_ready, S_erik_orc_order, S_erik_orc_wait,
            S_erik_orc_arrived, S_erik_orc_acquired,
            S_erik_orc_inspected, S_erik_orc_done,
        S_erik_bully_ready, S_erik_bully_visit, S_erik_bully_promise,
            S_erik_bully_fight, S_erik_bully_blackout, S_erik_bully_recovered,
            S_erik_bully_tired, S_erik_bully_done,
        S_erik_vr_ready, S_erik_vr_needed, S_erik_vr_buy_headset,
            S_erik_vr_buy_game, S_erik_vr_acquired, S_erik_vr_done,
        S_erik_feed_ready, S_erik_feed_curious,
            S_erik_feed_search, S_erik_feed_done,
        S_erik_thief_ready, S_erik_thief_active, S_erik_thief_chase,
            S_erik_thief_caught, S_erik_thief_done,
        S_erik_poker_ready, S_erik_poker_invite,
            S_erik_poker_party, S_erik_poker_done,
        S_erik_fork_ready, S_erik_fork_talk,
            S_erik_fork_choice, S_erik_fork_done,
        S_erik_learn_ready, S_erik_learn_fetch, S_erik_learn_get_kamasutra,
            S_erik_learn_get_pills, S_erik_learn_acquired,
            S_erik_learn_prep, S_erik_learn_finale,
        S_erik_end)

    M_erik.set_priority(1)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
