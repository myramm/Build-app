default recovery_stack = []


init python early hide:
    '''
    Provide for wanting more than a single config.label_callback.
    '''

    def callback(label, abnormal):
        for callback in config.label_callbacks:
            callback(label, abnormal)


    config.label_callback = callback
    config.label_callbacks = []


init python early hide:
    '''
    Log visited labels for last ditch effort recovery purposes.
    '''

    exclude = {'after_load'}
    limit = 10


    def recover_log(label, abnormal):
        if label[0] == '_' or label.isupper() or label in exclude:
            return
        if label in recovery_stack:
            recovery_stack.remove(label)
        recovery_stack.append(label)
        del recovery_stack[:-limit]


    config.label_callbacks.append(recover_log)


init python hide:
    '''
    In the event that the return stack is not fully compatible with the
    current build, attempt to make the save recoverable, if not fully
    compatible.
    '''

    def recover():
        oldrs = renpy.get_return_stack()
        newrs = [l for l in oldrs if renpy.has_label(l)]
        
        if len(oldrs) == len(newrs):
            return 
        
        logger.warning('Return stack mutation detected!')
        
        if recovery_stack:
            known = next(l for l in reversed(recovery_stack) if renpy.has_label(l))
            newrs.insert(0, known)
        
        newrs.insert(0, player.location.label)
        renpy.set_return_stack(newrs)
        renpy.call_in_new_context('warn.recovery')


    config.after_load_callbacks.append(recover)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
