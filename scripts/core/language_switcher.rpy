# Summertime Saga Language Switcher Engine
# Author: myramm
# Seamless switching between English and Bahasa Indonesia

init -100 python:
    import renpy
    import zlib
    try:
        import cPickle as _pickle
    except ImportError:
        import pickle as _pickle

    _id_translations_cache = None

    def _load_id_translations():
        global _id_translations_cache
        if _id_translations_cache is None:
            try:
                f = renpy.file("scripts/tl_id.dat")
                raw = f.read()
                f.close()
                _id_translations_cache = _pickle.loads(zlib.decompress(raw))
            except Exception as e:
                _id_translations_cache = {}
        return _id_translations_cache

    def id_say_menu_text_filter(text):
        if not text:
            return text
        curr_lang = getattr(store._preferences, 'language', None)
        if curr_lang == 'indonesian':
            tl_map = _load_id_translations()
            if text in tl_map:
                return tl_map[text]
            if isinstance(text, str):
                try:
                    utext = text.decode('utf-8')
                    if utext in tl_map:
                        return tl_map[utext]
                except Exception:
                    pass
        return text

    # Register text filter for dialogue and interactive choices
    config.say_menu_text_filter = id_say_menu_text_filter

    # Hook UI string translation
    try:
        orig_translate_string = renpy.translation.translate_string

        def custom_translate_string(s, language=renpy.translation.Default):
            if not s:
                return s
            if language is renpy.translation.Default:
                lang = getattr(store._preferences, 'language', None)
            else:
                lang = language

            if lang == 'indonesian':
                tl_map = _load_id_translations()
                if s in tl_map:
                    return tl_map[s]
                if isinstance(s, str):
                    try:
                        us = s.decode('utf-8')
                        if us in tl_map:
                            return tl_map[us]
                    except Exception:
                        pass
            return orig_translate_string(s, language)

        renpy.translation.translate_string = custom_translate_string
    except Exception:
        pass

    # Register known language
    try:
        renpy.game.script.translator.languages.add('indonesian')
    except Exception:
        pass

    # Default to Bahasa Indonesia on fresh start
    if not hasattr(persistent, 'language_initialized') or not persistent.language_initialized:
        persistent.language_initialized = True
        if _preferences.language is None:
            _preferences.language = 'indonesian'
