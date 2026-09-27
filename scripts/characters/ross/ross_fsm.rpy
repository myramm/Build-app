init -1 python:
    M_ross = Machine("ross", default_loc = [[L_school_artclassroom, L_school_artclassroom, L_school_rossoffice, L_NULL],
                                            [L_NULL, L_NULL, L_NULL, L_NULL]
                                            ],
                     vars = {"sex speed": .3,
                             "talked with chad": False,
                             "talked with jane": False,
                             "magazines remaining": 3,
                             "magazine kevin": False,
                             "magazine dewitt": False,
                             "magazine dexter": False,
                             "take porno fail": False,
                             "talked to grace": False,
                             "failed pick up boxes": False,
                             "waiting for contest": 0,
                             "smith office painting": False,
                             },
    )

init -3 python:
    T_ross_intro = Trigger()
    T_ross_molded_clay = Trigger()
    T_ross_find_partner = Trigger()
    T_ross_convinced_mia = Trigger()
    T_ross_find_art_pad = Trigger()
    T_ross_find_eve_backpack = Trigger()
    T_ross_got_eve_backpack = Trigger()
    T_ross_mia_drawn = Trigger()
    T_ross_find_magazines = Trigger()
    T_ross_found_magazines = Trigger()
    T_ross_found_all_magazines = Trigger()
    T_ross_made_collage = Trigger()
    T_ross_find_easels = Trigger()
    T_ross_has_easels = Trigger()
    T_ross_find_model = Trigger()
    T_ross_paint_for_smith = Trigger()

    T_ross_find_linens = Trigger()
    T_ross_find_paint = Trigger()
    T_ross_talk_to_grace = Trigger()
    T_ross_wait_for_contest = Trigger()
    T_ross_wait_for_contest_over = Trigger()
    T_ross_contest_over = Trigger()
    T_ross_sexual_body_painting = Trigger()
    T_ross_end = Trigger()

init python:

    S_ross_start = State()
    S_ross_grab_clay = State()
    S_ross_find_partner = State()
    S_ross_ask_mia_partner = State()
    S_ross_mia_is_partner = State()
    S_ross_find_art_pad = State()
    S_ross_find_eve_backpack = State()
    S_ross_get_eve_drawing = State()
    S_ross_collage = State()
    S_ross_find_magazines = State()
    S_ross_make_collage = State()
    S_ross_need_easels = State()
    S_ross_get_easels = State()
    S_ross_ask_model = State()
    S_ross_found_model = State()

    S_ross_need_linens = State()
    S_ross_get_linens = State()
    S_ross_get_paint = State()
    S_ross_get_paint_grace = State()
    S_ross_waiting_for_contest = State()
    S_ross_contest = State()

    S_ross_paint_with_body = State()
    S_ross_end = State()


    S_ross_start.add(T_ross_intro, S_ross_grab_clay)
    S_ross_grab_clay.add(T_ross_molded_clay, S_ross_find_partner)
    S_ross_find_partner.add(T_ross_find_partner, S_ross_ask_mia_partner)
    S_ross_ask_mia_partner.add(T_ross_convinced_mia, S_ross_mia_is_partner)
    S_ross_mia_is_partner.add(T_ross_find_art_pad, S_ross_find_art_pad)
    S_ross_find_art_pad.add(T_ross_find_eve_backpack, S_ross_find_eve_backpack)
    S_ross_find_eve_backpack.add(T_ross_got_eve_backpack, S_ross_get_eve_drawing)
    S_ross_get_eve_drawing.add(T_ross_mia_drawn, S_ross_collage, actions=["exec", "player.increase_grade_art()"])
    S_ross_collage.add(T_ross_find_magazines, S_ross_find_magazines,
                       actions = ["location", ["dewitt", {"place": L_school_teacherslounge,
                                                          "condition": "not M_ross.is_set('magazine dewitt')",
                                                          }
                                               ],
                                  "force", ["dewitt", {"tod": [0,1]}],
                                  ],
                       )
    S_ross_find_magazines.add(T_ross_found_magazines, S_ross_find_magazines,
                              actions = ["triggerOnZero", ["magazines remaining", T_ross_found_all_magazines]],
                              )
    S_ross_find_magazines.add(T_ross_found_all_magazines, S_ross_make_collage,
                              actions = ["unforce", "dewitt"],
                              )
    S_ross_make_collage.add(T_ross_made_collage, S_ross_need_easels, actions=["exec", "player.increase_grade_art()"])
    S_ross_need_easels.add(T_ross_find_easels, S_ross_get_easels)
    S_ross_get_easels.add(T_ross_has_easels, S_ross_ask_model)
    S_ross_ask_model.add(T_ross_find_model, S_ross_found_model)
    S_ross_found_model.add(T_ross_paint_for_smith, S_ross_need_linens)
    S_ross_need_linens.add(T_ross_find_linens, S_ross_get_linens, actions=["unlocklocation", L_church_front])
    S_ross_get_linens.add(T_ross_find_paint, S_ross_get_paint)
    S_ross_get_paint.add(T_ross_talk_to_grace, S_ross_get_paint_grace)

    S_ross_get_paint_grace.add(T_ross_wait_for_contest, S_ross_waiting_for_contest,
                               actions = ["assign", ["waiting for contest", 7],
                                          "set", "smith office painting",
                                          "exec", "player.increase_grade_art()",
                                         ]
                               )
    S_ross_waiting_for_contest.add(T_all_sleep, S_ross_waiting_for_contest, actions=["triggerOnZero", ["waiting for contest", T_ross_wait_for_contest_over]])
    S_ross_waiting_for_contest.add(T_ross_wait_for_contest_over, S_ross_contest)
    S_ross_contest.add(T_ross_contest_over, S_ross_paint_with_body)
    S_ross_paint_with_body.add(T_ross_sexual_body_painting, S_ross_end,
                               actions=["exec", "player.increase_grade_art()",
                                        "exec", A_painting_nude.unlock,
                                        'clear', ('player', 'is_virgin')])

    M_ross.set_priority(1)

    M_ross.add(S_ross_start, S_ross_grab_clay,S_ross_find_partner,
               S_ross_ask_mia_partner, S_ross_mia_is_partner,
               S_ross_find_art_pad, S_ross_find_eve_backpack,
               S_ross_get_eve_drawing, S_ross_collage, S_ross_find_magazines,
               S_ross_make_collage, S_ross_need_easels, S_ross_get_easels,
               S_ross_ask_model, S_ross_found_model, S_ross_need_linens,
               S_ross_get_linens, S_ross_get_paint, S_ross_get_paint_grace,
               S_ross_waiting_for_contest, S_ross_contest, S_ross_paint_with_body,
               S_ross_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
