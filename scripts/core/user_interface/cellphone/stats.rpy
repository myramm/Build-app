init python in phone:
    class CellPhoneStatsApp(renpy.Displayable):
        def __init__(self, stats, **properties):
            super(CellPhoneStatsApp, self).__init__(**properties)
            self.base = renpy.displayable('cellphone/phone_stats_base.png')
            self.stats_str = renpy.displayable('cellphone/phone_stats_tally_str.png')
            self.stats_dex = renpy.displayable('cellphone/phone_stats_tally_dex.png')
            self.stats_chr = renpy.displayable('cellphone/phone_stats_tally_chr.png')
            self.stats_int = renpy.displayable('cellphone/phone_stats_tally_int.png')
            self.x_start = 79
            self.stats = stats
        
        def render(self, width, height, st, at):
            render = renpy.render(self.base, width, height, st, at)
            str_r = renpy.render(self.stats_str, width, height, st, at)
            dex_r = renpy.render(self.stats_dex, width, height, st, at)
            chr_r = renpy.render(self.stats_chr, width, height, st, at)
            int_r = renpy.render(self.stats_int, width, height, st, at)
            
            for count in xrange(self.stats.str()):
                x = self.x_start + count * 19
                render.blit(str_r, (x, 11))
            for count in xrange(self.stats.dex()):
                x = self.x_start + count * 19
                render.blit(dex_r, (x, 11 + 58))
            for count in xrange(self.stats.chr()):
                x = self.x_start + count * 19
                render.blit(chr_r, (x, 11 + 58 * 2))
            for count in xrange(self.stats.int()):
                x = self.x_start + count * 19
                render.blit(int_r, (x, 11 + 58 * 3))
            
            return render
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
