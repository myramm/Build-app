label check_pregnancies:
label _check_all_pregnancies:
    python hide:
        calls = []
        texts = []
        monos = []

        for machine in pregnant_machines():
            manager = machine.pregnancy
            stage = manager.stage
            
            abort = machine.get('abort_wait', None)
            days = manager.days_elapsed
            first = manager.first_baby
            name = machine._name
            
            if stage == 1:
                summoned = manager.text_announcement_seen
                if not summoned:
                    phone = '{}_pregnancy_summon'.format(name)
                    if not first:
                        phone += '.repeat'
                    
                    if renpy.has_label(phone):
                        manager.set('text_announcement_seen')
                        calls.append(phone)
                        continue
                
                notified = manager.announced_pregnancy
                if not notified:
                    phone = '{}_pregnancy_notify'.format(name)
                    if not first:
                        phone += '.repeat'
                    
                    if renpy.has_label(phone):
                        manager.set('text_announcement_seen')
                        manager.set('announced_pregnancy')
                        calls.append(phone)
                        continue
                    
                    if not summoned and not game.new_message:
                        manager.set('text_announcement_seen')
                    
                    if not manager.text_announcement_seen:
                        texts.append("{}_pregnant_announcement_1".format(name))
                    elif abort and abort + 6 <= days:
                        manager.abort_baby()
                    else:
                        monos.append("{}_pregnant_announcement_2".format(name))
                    continue
            
            if manager.character_bedridden:
                informed = manager.text_labor_seen
                if not informed:
                    phone = '{}_pregnancy_labour'.format(name)
                    if not first:
                        phone += '.repeat'
                    
                    if renpy.has_label(phone):
                        manager.set('text_labor_seen')
                        calls.append(phone)
                        continue
                
                visited = manager.seen_in_labor
                if not visited:
                    if not informed and not game.new_message:
                        manager.set('text_labor_seen')
                    
                    if not manager.text_labor_seen:
                        texts.append("{}_pregnant_labor_1".format(name))
                    else:
                        monos.append("{}_pregnant_labor_2".format(name))
                    continue

        store.res = list(reversed(texts[:1] + calls + monos))

    while res:
        $ renpy.dynamic(label=res.pop())
        call expression label from _check_all_pregnancies.resume
        python hide:
            name, _, type = label.partition('_')
            if type.startswith('pregnancy_notify') and not _return:
                machines[name].pregnancy.abort_baby()
        if label.endswith('_pregnant_labor_2'):
            $ L_hospital.unlock()
            $ L_annie_front.unlock()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
