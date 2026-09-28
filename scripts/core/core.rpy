init -20 python:
    class PlayTimer:
        def __str__(self):
            delta = datetime.timedelta(seconds=renpy.get_game_runtime())
            mins = delta.seconds // 60
            return '{}d, {}h, {}m'.format(delta.days, mins / 60, mins % 60)

    playtime = PlayTimer()

    def call_action(action):
        if callable(action):
            action()

    def get_label(machine, location, state, variable=None):
        if variable is None:
            return "_".join(str(location), str(machine), str(state))
        else:
            return "_".join(str(location), str(machine), str(state), variable)

    def randomizer(name = "", start = 0, end = 99):
        rand = renpy.random.randint(start, end)
        if name == "":
            return rand
        if not re.search('\{}', name):
            name = name + '{}'
        tmp = name.format(rand)
        return tmp

    def choice_randomizer(list):
        r = random.uniform(0, sum([v[1] for v in list]))
        s = 0.0
        for k, w in list:
            s += w
            if r < s:
                return k
        return k

    def get_returnable_books():
        books = []
        if player.has_item("french_dictionary") and player.has_item("french_love") and M_bissette.is_state(S_bissette_end):
            books.append("french_dictionary")
            books.append("french_love")
        if player.has_item("old_book") and M_aqua.is_state((S_aqua_trade, S_aqua_fishing, S_aqua_chase,
                   S_aqua_squid_gaurd, S_aqua_maze, S_aqua_lair, S_aqua_found,
                   S_aqua_mating_proposal, S_aqua_valor_test, S_aqua_mate,
                   S_aqua_seasucc_intro, S_aqua_seasucc_mushroom, S_aqua_end)):
            books.append("old_book")
        if player.has_item("breeding_guide") and M_diane.finished_state(S_diane_return_production_book):
            books.append("breeding_guide")
        return books

    def splice_string(string, every=30):
        lines = []
        for i in xrange(0, len(string), every):
            lines.append(string[i:i+every])
        return '\n'.join(lines)

    def insert_newlines(string, every=30):
        lines = textwrap.wrap(string, every)
        return "\n".join(lines), len(lines)

    def clamp(number, lower, upper):
        assert lower < upper, "Error in clamp call, lower bound is greater than upper bound"
        return lower if number < lower else upper if number > upper else number

    def gauss(mean, deviation, lower, upper):
        return int(clamp(random.gauss(mean, deviation), lower, upper))

    def replace_bracket(string):
        def replace(match):
            return globals()[match.group(0)]
        if "[" in string:
            re.sub(r"(\[\w+\])", replace, string)
            return string
        else:
            return string

    def is_string(variable):
        return isinstance(variable, str) or isinstance(variable, unicode)


    try:
        import cPickle as _pickle
    except ImportError:
        import pickle as _pickle
    pick = _pickle.dumps


    def test(obj, prt=True):
        def tstlst(lst, prt):
            for i, v in enumerate(lst):
                if prt:
                    print i, v
                else:
                    print i
                pick(v)
        def tstcls(cls, prt):
            for k, v in cls.__dict__.items():
                if prt:
                    print k, v
                else:
                    print k
                pick(v)
        def tstdct(dct, prt):
            for k, v in dct.items():
                if prt:
                    print k, v
                else:
                    print k
                pick(v)
        if isinstance(obj, list) or isinstance(obj, tuple):
            tstlst(obj, prt)
        elif isinstance(obj, dict):
            tstdct(obj, prt)
        elif isinstance(obj, object):
            tstcls(obj, prt)

    def randomchoices(population, weights=[]):
        if len(weights) < len(population):
            weights.extend([1]*(len(population)-len(weights)))
        
        sumpop = [[population[i]]*weights[i] for i in range(len(population))]
        rv = []
        for spop in sumpop:
            rv.extend(spop)
        random.shuffle(rv)
        return random.choice(rv)

    def is_game_unpacked(check_rpy=True, check_rpa=True, check_rpyc=True, check_img=True, return_rv=False):
        global archives
        if "renpy" in os.getcwd().split(r"/")[-1] and config.developer:
            return "DEV"
        else:
            rv = []
            if check_rpy:
                rv.extend(glob.glob("**/*.rpy"))
            if check_rpa:
                rpas = glob.glob("**/*.rpa")
                allowed_rpas = ["{}.rpa".format(name) for name in archives]
                for rpa in rpas:
                    for allowed_rpa in allowed_rpas:
                        if allowed_rpa in rpa:
                            try:
                                rpas.remove(rpa)
                            except ValueError:
                                pass
                rv.extend(rpas)
            if check_img:
                rv.extend(glob.glob("**/*.png"))
                rv.extend(glob.glob("**/*.jpg"))
                rv.extend(glob.glob("**/*.webp"))
                rv.extend(glob.glob("**/*.jpeg"))
            if check_rpyc:
                rv.extend(glob.glob("**/*.rpyc"))
            if return_rv:
                return rv
            else:
                return not (len(rv)==0)

    def get_sex_speeds(n_frames):
        """
            Gets the minimum and maximum sex speeds given a number of frames for the animation.

            :param n_frames: (int) number of frames in the scene

            :return: (tuple(float)) 3 significant digits, a tuple (slowest, fastest) for the sex speeds.
        """
        slow = 0.25 / n_frames
        slow = round(slow, 3)
        fast = 0.75 / n_frames
        fast = round(fast, 3)
        return slow, fast

    def get_sex_speed_increment(n_frames, n_increments=2):
        """
            Gets the increment of speed for the sex scene.

            :param n_frames: (int) number of frames in the scene
            :param n_increments: (int) number of increments to increase/decrease the sex speed

            :return: (float) 3 significant digits, the increment for the sex speed.
        """
        slow, fast = get_sex_speeds(n_frames)
        return round((fast - slow) / n_increments, 3)

    def get_average_sex_speed(n_frames, n_increments=2):
        """
            Gets the average sex speed (useful to initialize it to a set value)
            that is a multiple of the number of increments

            :param n_frames: (int) number of frames in the scene
            :param n_increments: (int) number of increments to increase/decrease the sex speed

            :return: (float) 3 significant digits, the average speed for the scene.
        """
        slow, fast = get_sex_speeds(n_frames)
        inc = 1000 * get_sex_speed_increment(n_frames, n_increments)
        slow = int(slow * 1000)
        fast = int(fast * 1000)
        return float(xrange(slow, fast, inc)[int(n_increments / 2)]) / 1000

    def screen_to_world_coords(xpos, ypos):
        
        width, height = 1920., 1080.
        x, y = float(x), float(y)
        return (x/width, y/height)

    def get_size(image, bounding_rect = False):
        """
            Gets the size of an image (pass in the image string)
            returns a tuple (width, height) which is the size of the image
            optional parameter : bounding_rect, if true returns the brect of the image as a (x, y, width, height) tuple
        """
        file_ = renpy.file("images/" + image.lstrip("/"))
        surface = pygame.image.load(file_)
        file_.close()
        if not bounding_rect:
            return surface.get_width(), surface.get_height()
        else:
            rect = surface.get_bounding_rect()
            return rect.x, rect.y, rect.w, rect.h
        pass

    def coordinates_in_screen(x, y):
        return (0 <= x <= 1024) and (0 <= y <= 768)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
