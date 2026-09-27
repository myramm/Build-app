init -5 python:
    class Telescope(object):
        def __init__(self, timer):
            self.randomize(timer)
        
        def randomize(self, timer):
            if timer.is_morning():
                self.erik = "telescope_erik_morning_{}".format(random.randint(1,2))
                self.mrsj = "telescope_mrsj_morning_{}".format(random.randint(1,2))
                self.mia = "telescope_mia_morning_{}".format(random.randint(1,2))
                self.helen = "telescope_helen_morning_1"
                self.backyard = "telescope_backyard_morning_1"
            elif timer.is_afternoon():
                if M_erik.finished_state(S_erik_orc_done):
                    self.erik = "telescope_erik_afternoon_{}".format(random.randint(1,4))
                else:
                    self.erik = "telescope_erik_afternoon_{}".format(random.randint(1,2))
                self.mrsj = "telescope_mrsj_afternoon_{}".format(random.randint(1,3))
                self.mia = "telescope_mia_afternoon_{}".format(random.randint(1,2))
                self.helen = "telescope_helen_afternoon_1"
                self.backyard = "telescope_backyard_afternoon_{}".format(random.randint(1,4))
            elif timer.is_dark():
                self.erik = "telescope_erik_night_{}".format(random.randint(1,2))
                self.mrsj = "telescope_mrsj_night_{}".format(random.randint(1,3))
                self.mia = "telescope_mia_night_{}".format(random.randint(1,3))
                self.helen = "telescope_helen_night_{}".format(random.randint(1,2))
                self.backyard = "telescope_backyard_night_1"

    class Game(object):
        language = "en"
        forced_season = False
        
        CA_FILE = os.path.join(config.gamedir, "scripts", "data", "cacert.pem")
        website_address = "https://my.kompasproductions.com"
        
        available_ui_message_screens = OrderedSet(*["ui_message{}".format(i) for i in range(10)])
        
        def __init__(self, language="en", difficulty=1):
            self.timer = DayTimer()
            self.language = language
            self.ui_lock = True
            self.cheat_mode = False
            self.xray = False
            self.anim_toggle = False
            self.cum = False
            self.animcounter = 0
            self.savegame_version = config.version
            self.mail = {"player": MailBoxManager("player", ["m_pizza_pamphlet", "m_newspaper"]),
                         "erik": MailBoxManager("erik", ["m_dad_letter", "m_magazine", "m_newspaper"]),
                         "mia": MailBoxManager("mia", ["m_pizza_pamphlet", "m_newspaper"])}
            self.possibly_in_shower = []
            self._in_shower = None
            self.sleep_lock = True
            self.seen_tv_channels = []
            self.new_message = False
            self.read_message = False
            self.telescope = Telescope(self.timer)
            self.clyde_big_berta = False
            self.force_unlock_map = False
            self.new_achievements = False
            self.in_dialogue = False
            self.difficulty = difficulty
            self.showroom_vehicle = 1
        
        def __getattr__(self, attr):
            """
                This getattr overloading ensures that something will always return
                when trying to access one of this class' attribute.

                If the attribute already has a value, then return that (classic behavior),
                otherwise, reinstantiate the class locally, and return the attribute
                as defined in the __init__ method.

                If there is still no attribute, will return None. This behavior can be changed
                by editing the line
                    return self.__class__().__dict__[attr]
                into
                    return self.__class__().__dict__[attr]
                which will throw a KeyError exception if the attribute doesn't exist.
            """
            val = self.__dict__.get(attr)
            if val is not None:
                return val
            else:
                try:
                    val = self.__class__().__dict__[attr]
                    self.__dict__[attr] = val
                    return val
                except KeyError:
                    return super(Game, self).__getattr__(attr)
        
        def randomize_shower(self):
            if M_anon.is_state(S_ano01_cops, S_ano02_food):
                return None
            
            if M_jenny.is_state(S_jenny_shower_spy):
                return M_jenny
            
            pool = {None, M_debbie, M_jenny}
            
            if M_debbie.pregnancy:
                pool.remove(M_debbie)
            
            if M_jenny.pregnancy.stage != 4 if M_jenny.pregnancy \
                else M_jenny.is_state(S_jenny_pool_talk) \
                  or M_jenny.is_state(S_jenny_go_to_her_room) \
                  or M_jenny.is_state(S_jenny_want_some_breakfast):
                
                
                pool.remove(M_jenny)
            
            return random.choice(tuple(pool))
        
        def sleep(self):
            if self.sleep_lock:
                raise OnSleepException()
            else:
                global erik_drunk
                erik_drunk = False
                
                self.timer.sleep()
                
                Machine.trigger(T_all_tick)
                Machine.machine_trigger(T_all_tick)
                Machine.trigger(T_all_sleep)
                Machine.machine_trigger(T_all_sleep)
                if self.timer._dow == 0:
                    Machine.trigger(T_all_new_week)
                    Machine.machine_trigger(T_all_new_week)
                
                
                if M_roxxy.finished_state(S_roxxy_picnic_done):
                    self.clyde_big_berta = random.randint(1,8)==1
                else:
                    self.clyde_big_berta = False
                
                
                MailBoxManager.randomize_all()
                
                
                self._in_shower = self.randomize_shower()
                
                
                PregnancyManager.increment_pregnancy()
                
                
                if M_rump.get("seen speech mall"):
                    M_rump.set("can see speech mall", False)
                
                
                if not 1 <= player.transport_level <= 3:
                    self.showroom_vehicle = random.randint(1, 3)
                elif self.showroom_vehicle != player.transport_level:
                    self.showroom_vehicle = player.transport_level
                
                
                if self.timer._dow == 0 and player.has_item('atm_card'):
                    player.calculate_interests()
                    if self.mail["player"].set("m_bank_statement"):
                        
                        self.mail["player"].randomize() 
                        self.mail["player"].reset() 
        
        @property
        def in_shower(self):
            if self.timer.is_morning():
                return self._in_shower
            else:
                return None
        
        def set_in_shower(self, machine):
            self._in_shower = machine
        
        def lock_ui(self):
            self.ui_lock = True
        
        def unlock_ui(self):
            self.ui_lock = False
        
        def unlock_sleep(self):
            self.sleep_lock = False
        
        def lock_sleep(self):
            self.sleep_lock = True
        
        def has_mail(self, character):
            if isinstance(character, Machine):
                character = character._name
            return self.mail[character] != ""
        
        @property
        def ui_locked(self):
            return (self.ui_lock or L_map.locked)
        
        @property
        def rump_n_cunt(self):
            return M_rump.rump_n_cunt
        
        def set_rump_n_cunt(self):
            M_rump.set('rump_n_cunt', True)
        
        def toggle_cheat_mode(self):
            self.cheat_mode = not self.cheat_mode
        
        def skip_first_day(self):
            M_player.trigger(T_jenny_hallway)
            
            L_map.unlock(False, False)
            L_erikhouse.unlock(False, False)
            M_player.trigger(T_debbie_breakfast)
            
            L_school_front.unlock(False, False)
            M_player.trigger(T_erik_intro_meet)
            
            L_miahouse.unlock(False, False)
            M_player.trigger(T_all_school_entrance)
            
            L_basketball_court.unlock(False, False)
            M_player.trigger(T_smith_intro)
            
            M_player.trigger(T_roxxy_teachers_berating)
            
            M_player.trigger(T_kevin_ambush)
            L_school_floor2.visited()
            L_gym_front.unlock(False, False)
            
            M_player.trigger(T_smith_go_to_locker)
            M_player.trigger(T_smith_unlocked_locker)
            M_player.trigger(T_smith_go_to_athletics)
            M_player.trigger(T_judith_changed)
            
            M_player.trigger(T_mc_lockerroom_change)
            L_school_boysroom.visited()
            
            L_pool.unlock(False, False)
            M_player.trigger(T_bridget_workout)
            
            L_library_front.unlock(False, False)
            M_player.trigger(T_bissette_improvement_challenge)
            
            M_player.trigger(T_eve_park_hangout)
            L_park.unlock(False, False)
            
            M_player.trigger(T_bissette_challenge_thoughts)
            M_player.trigger(T_all_tick)
            
            L_diane_yard.unlock(False, False)
            M_player.trigger(T_erik_intro_done)
            
            M_player.trigger(T_dia01_init)
            L_diane_garden.visited()
            
            M_player.trigger(T_dia01_find)
            player.get_item('shovel')
            M_player.trigger(T_dia01_give)
            M_player.trigger(T_dia01_work)
            M_diane.set("garden first time", False)
            M_player.trigger(T_all_tick)
            
            M_player.trigger(T_debbie_check)
            M_player.trigger(T_debbie_debt_help)
            M_player.trigger(T_all_tick)
            
            M_player.trigger(T_all_sleep)
            
            L_mall_parking_lot.unlock(False, False)
            L_beach.unlock(False, False)
            L_treehouse.unlock(False, False)
            L_hill.unlock(False, False)
            L_beachhouse_front.unlock(False, False)
            
            if not game.timer._game_day:
                game.timer._dow = 1
                game.timer._game_day = 1
        
        def force_unlock_ui(self):
            self.force_unlock_map = True
        
        def force_lock_ui(self):
            self.force_unlock_map = False
        
        @classmethod
        def dialog_select(cls, label_name):
            renpy.block_rollback()
            if cls.language != "en":
                lbl = label_name + "_" + cls.language
                if lbl in renpy.get_all_labels():
                    return lbl
            return label_name
        
        @classmethod
        def choose_label(cls, template):
            """
                randomly returns a label that match the template.

                template is a string that is the beginning of labels strings.
            """
            return random.choice(filter(lambda x: x.startswith(template), renpy.get_all_labels()))
        
        def main(self, clear_return_stack=True, location=None, call_location_lbl=False, call_screen_args=[]):
            renpy.scene(layer='screens')
            global player
            player.earnings = 0
            renpy.free_memory()
            renpy.display.render.free_memory()
            if clear_return_stack:
                return_stack = renpy.get_return_stack()
                
                renpy.set_return_stack(return_stack[-15:])
            
            if player.has_picked_up_item("seatrout") and player.has_picked_up_item("snapper") and player.has_picked_up_item("mackerel"):
                A_angler.unlock()
            if player.transport_level == 4:
                A_gt500.unlock()
            if player.inventory.savings == 25000:
                A_ready_for_college.unlock()
            if player.has_max_grades:
                A_passing_grade.unlock()
            if player.has_max_stats:
                A_overpowered.unlock()
            if player.stats.dex() == 10:
                A_slick_mofo.unlock()
            if player.stats.str() == 10:
                A_cedric_got_nothing.unlock()
            if player.inventory.total_interests >= 50000:
                A_sound_investment.unlock()
            if self.timer.game_day() >= 365:
                A_happy_birthday.unlock()
            if M_eve.biggus_dickus and A_eve_tat_too_point_oh.is_unlocked:
                A_full_ackbar.unlock()
            
            unlock_achievement = True
            for loc in [l for l in store.locations.values() if "locker" in l.name.lower() and l.is_child_of(L_school_hall)]:
                if loc.is_visited:
                    continue
                else:
                    unlock_achievement = False
            if unlock_achievement:
                A_whats_in_there.unlock()
            
            if player.has_item("seatrout"):
                M_diane.trigger(T_diane_got_dinner_fish)
            
            if L_home_livingroom.is_here(M_diane):
                M_diane.outfit.is_naked = 0
            elif not M_diane.finished_state(S_diane_d9_intro):
                M_diane.outfit.is_naked = 0
            elif M_diane.between_states(S_diane_d9_intro, S_diane_return_outfit_package) or M_diane.is_state(S_diane_d9_intro):
                M_diane.outfit.is_naked = 0
            
            if location is None:
                player.location.call_screen(*call_screen_args)
                if call_location_lbl:
                    player.location.call()
            else:
                location.call_screen(*call_screen_args)
                if call_location_lbl:
                    location.call()
        
        @classmethod
        def can_show(cls, name, layer="master"):
            return renpy.can_show(name, layer) is not None or renpy.loadable(name)
        
        def copy(self):
            game = Game()
            for attribute, value in [(k, v) for k, v in self.__dict__.items()]:
                try:
                    game.__dict__[attribute] = value
                except KeyError:
                    pass
            return game
        
        @classmethod
        def season(cls):
            if cls.forced_season is not False:
                return cls.forced_season
            today = datetime.date.today()
            today = today.month + today.day / 100.0
            if 10.15 <= today <= 10.31:
                return 'halloween'
            if 12.15 <= today <= 12.30:
                return 'christmas'
            return None
        
        @classmethod
        def period_index(cls):
            return {None: 0,
                    'christmas': 1,
                    'halloween': 2}[cls.season()]
        
        @classmethod
        def is_christmas(cls):
            return cls.season() == 'christmas'
        
        @classmethod
        def is_halloween(cls):
            return cls.season() == 'halloween'
        
        @property
        def get_period_str(self):
            season = self.season()
            if not season:
                season = 'normal'
            season = season.title()
            if self.forced_season is not False:
                season += ' (debug)'
            return season
        
        @classmethod
        def toggle_debug_period(cls):
            cls.forced_season = {'christmas': False,
                                 'halloween': 'christmas',
                                 False: None,
                                 None: 'halloween'}[cls.forced_season]
        
        @classmethod
        def get_available_ui_message_screen(cls):
            try:
                screen = cls.available_ui_message_screens.pop()
                return screen
            except KeyError:
                cls.available_ui_message_screens = OrderedSet(*['ui_message{}'.format(i) for i in range(10)])
                return cls.get_available_ui_message_screen()
        
        def rails(self):
            return (M_anon.is_state(S_ano01_cops,
                                    S_ano02_food,
                                    S_ano04_tony,
                                    S_ano10_tina,
                                    S_ano12_oops,
                                    S_ano12_done,
                                    S_ano21_news,
                                    S_ano21_done,
                                    S_ano22_ally,
                                    S_ano27_yumi,
                                    S_ano28_food) or
                    M_jenny.is_state(S_jen0m_food) or
                    M_nadya.is_state(S_nad01_thug) or
                    M_diane.is_state(S_diane_debbie_drop_off,
                                     S_diane_check_shed_light,
                                     S_diane_peeking_masturbate,
                                     S_diane_get_dirty_with_debbie) or
                    M_iwanka.is_state(S_iwa01_pier) or
                    M_odette.is_state(S_ode02_warn) or
                    M_eve.is_state(S_eve_visit_garage,
                                   S_eve_big_sis_check_garage) or
                    M_consuela.is_state(S_con02_job1,
                                        S_con02_job2,
                                        S_con02_job3))


init python hide:
    '''
    Patch to circumvent errors occuring during a load containing
    dynamically scoped values associated with the return stack.
    '''

    from renpy.execution import Context, Delete


    def pop(self):
        if not self.dynamic_stack:
            return
        
        store = renpy.store.__dict__
        
        dynamic = self.dynamic_stack.pop()
        
        for k, v in dynamic.iteritems():
            if isinstance(v, Delete):
                store.pop(k, None)
            else:
                store[k] = v


    Context.pop_dynamic = pop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
