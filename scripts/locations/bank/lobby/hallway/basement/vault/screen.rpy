screen bank_vault():
    add L_bank_vault.background

    imagebutton:
        focus_mask True
        pos 688, 357
        idle 'objects/object_door_196.png'
        hover HoverImage('objects/object_door_196.png')
        action MoveTo(L_bank_basement)

    if not player.has_picked_up_item('case'):
        imagebutton:
            focus_mask True
            pos 119, 248
            idle 'objects/object_suitcase_01.png'
            hover HoverImage('objects/object_suitcase_01.png')
            action HideAll(), Jump('bank_vault_case')

    if M_anon.is_state(S_ano14_find):
        imagebutton:
            focus_mask True
            pos 61, 348
            idle 'objects/object_box_bank.png'
            hover HoverImage('objects/object_box_bank.png')
            action Jump('bank_vault_boxes')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
