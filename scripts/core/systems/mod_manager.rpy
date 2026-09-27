init -1 python:
    def safe_parse_dict(dct, *keys, **kwargs):
        default = kwargs.get('default', None)
        list_to_append = kwargs.get('list_to_append', None)
        def _p(dct, k, default):
            try:
                return dct[k]
            except KeyError, e:
                if list_to_append is not None:
                    list_to_append.append(e.args[0])
                if default is not None:
                    return default
                elif list_to_append is not None:
                    return None
                raise e
        rv = dct
        for k in keys:
            try:
                rv = _p(rv, k, default)
            except TypeError:
                logger.warning("Extra positionnal argument passed, is default properly named in the arguments")
                return rv
        return rv

    class SayTextFilter(object):
        def __init__(self):
            self.to_call = []
            pass
        
        def __add__(self, other):
            if callable(other):
                self.to_call.append(other)
                return self
            else:
                raise Exception(repr(other)+ " is not a callable")
        
        def __iadd__(self, other):
            return self.__add__(other)
        
        def __call__(self, text):
            if not self.to_call:
                return text
            for function in self.to_call:
                ret = function(text)
                if ret != text:
                    return ret
    config.say_menu_text_filter = SayTextFilter()

    class ModManager(object):
        registered_mods = []
        enabled_mods = []
        mods =[]
        mods_hash_table = {}
        
        @classmethod
        def register(cls, modname):
            cls.registered_mods.append(modname)
        
        @classmethod
        def enable(cls, modname):
            if modname in cls.registered_mods:
                cls.enabled_mods.append(modname)
        
        @classmethod
        def get_screens(cls, screen_name=None):
            rv = []
            if screen_name is None:
                screens = renpy.sort_screens()
                for screen in screens:
                    if renpy.get_screen(screen):
                        screen_name = screen
            for mod in cls.mods:
                rv.append(mod.screens[screen_name])
            return rv
        
        @classmethod
        def get_labels(cls, label_name=None):
            rv = []
            if label_name is None:
                rs = renpy.get_return_stack()
                for lbl in reversed(rs):
                    if isinstance(lbl, unicode) or isinstance(lbl, str):
                        label_name = lbl
            for mod in cls.mods:
                rv.append(mod.labels[label_name])
            return rv
        
        @classmethod
        def get_lock_check_labels(cls):
            return [mod.global_lock_check_label for mod in cls.mods]
        
        @classmethod
        def init_mods(cls):
            for modname in cls.enabled_mods:
                cls.mods = Mod(modname).parse_load_order(cls.mods)
            for mod in cls.mods:
                config.say_menu_text_filter += mod.text_filter
                cls.mods_hash_table[mod.name] = mod
        
        @classmethod
        def update_stores(cls):
            global store
            for mod in cls.mods:
                store.items.update(mod.items)
                phone.data.update(mod.text_messages)
                store.achievements_json.update(mod.achievements)
        
        @classmethod
        def call_init_mods(cls):
            for mod in cls.mods:
                mod.call_init()
        
        @classmethod
        def call_main_functions(cls):
            for mod in cls.mods:
                mod.main()
        
        @classmethod
        def mods_search_prefixes(cls):
            rv = []
            for mod in cls.mods:
                rv.append("mods/{}/".format(mod.folder_name))
            return rv
        
        @classmethod
        def get_mod(cls, modname):
            try:
                return cls.mods_hash_table[modname]
            except KeyError:
                raise ModLoaderError("Cannot get mod {}.".format(modname))
        
        @classmethod
        def get_mod_index(cls, modname):
            try:
                return cls.mods.index(cls.get_mod(modname))
            except ModLoaderError:
                raise ModLoaderError("Cannot get mod index {} because the mod can't be retrieved.".format(modname))
            except ValueERror, e:
                raise e
        
        @classmethod
        def get_all_mods_fsm_actions(cls):
            rv = {}
            for mod in cls.enabled_mods:
                rv.update(mod.custom_fsm_actions)
            return rv

    class Mod(object):
        def __init__(self, modname):
            try:
                json_file = renpy.file("mods/{}_manifest.json".format(modname))
                data = json.load(json_file)
                json_file.close()
            except FileNotFoundError:
                raise ModLoaderError("mods/{}_manifest.json".format(modname) + " not found, is it misplaced, or named improperly?")
            missing_keys = []
            self.name = safe_parse_dict(data, "name", default=modname)
            self.version = safe_parse_dict(data, "version", list_to_append=missing_keys)
            self.load_order = safe_parse_dict(data, "load_order", default="inf")
            self.main_name = safe_parse_dict(data, "main_function_name", list_to_append=missing_keys)
            self.init_label_name = safe_parse_dict(data, "init_label_name", list_to_append=missing_keys)
            self.items = safe_parse_dict(data, "items", list_to_append=missing_keys)
            self.text_messages = safe_parse_dict(data, "text_messages", list_to_append=missing_keys)
            self.screens = safe_parse_dict(data, "screen_hooks", list_to_append=missing_keys)
            self.labels = safe_parse_dict(data, "label_hooks", list_to_append=missing_keys)
            self.achievements = safe_parse_dict(data, "achievements", list_to_append=missing_keys)
            self._text_filter = safe_parse_dict(data, "text_filter", default=lambda x:x)
            self.folder_name = safe_parse_dict(data, "folder_name", default=self.name)
            self.global_lock_check_label = safe_parse_dict(data, "global_lock_check_label", default="modmanager_default_lock_check")
            
            if modname.lower() != self.name.lower():
                raise ModLoaderError("Mod named {0} does not match manifest name modname: {0}, manifest:{1}".format(modname, self.name))
            logger.warning(missing_keys, mod=modname)
            self.missing_keys = missing_keys
            self.custom_fsm_actions = {}
        
        def parse_load_order(self, current_load_order):
            current_load_order = copy(current_load_order)
            if self.load_order[0] == "<":
                current_load_order.insert(int(self.load_order[1:])-1, self)
            elif self.load_order[0] == ">":
                current_load_order.insert(int(self.load_order[1:])+1, self)
            elif self.load_order[0] == "=":
                current_load_order.insert(int(self.load_order[1:]), self)
            elif self.load_order == "-inf":
                current_load_order.insert(0, self)
            elif self.load_order == "inf":
                current_load_order.append(self)
            return current_load_order
        
        def call_init(self):
            if self.init_label_name is not None:
                renpy.call_in_new_context(self.init_label_name)
        
        def main(self):
            if "main_function_name" in self.missing_keys:
                return
            try:
                globals()[self.main_name]()
            except KeyError:
                raise ModLoaderError("Error when trying to call main function named {}. Did you properly name it in the manifest?".format(self.main_name))
        
        @property
        def text_filter(self):
            if callable(self._text_filter):
                return self._text_filter
            try:
                return globals()[self._text_filter]
            except KeyError:
                raise ModLoaderError("No Function named {} found in the global namespace. Is it defined properly?".format(self._text_filter))

init 990 python:
    ModManager.init_mods()
    ModManager.update_stores()
    config.search_prefixes.extend(ModManager.mods_search_prefixes())

label INIT_MODS:
    $ ModManager.call_init_mods()

screen mods_screens_hook(screen=None, locals={}):
    for scr in ModManager.get_screens(screen):
        python:
            renpy.use_screen(scr, **locals)

label mods_labels_hook():
    python:
        for lbl in ModManager.get_labels(player.location.label):
            renpy.call_in_new_context(lbl)
    return

label modmanager_default_lock_check(destination=None):
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
