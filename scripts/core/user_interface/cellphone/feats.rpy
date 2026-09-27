init python hide in phone:
    from store import phone as exports

    from store import Achievement
    from store.util import struct


    def feats(achievements):
        count = 0
        total = 0
        feats = []
        
        for a, locked in achievements.iteritems():
            a = Achievement(a)
            
            if not a.enabled:
                continue
            
            desc = a.description
            if locked:
                if a.hidden:
                    desc = _('Achievement Hidden')
            else:
                count += 1
            
            total += 1
            
            feats.append((a.displayable, desc))
        
        return struct(count=count, total=total, feats=feats)


    exports.feats = feats


init python hide:
    def seen():
        if not game.new_achievements:
            return
        
        game.new_achievements = False


    phone.seen = seen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
