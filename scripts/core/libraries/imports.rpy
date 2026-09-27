init -990 python:
    renpy.not_infinite_loop(1000)
    import os
    import pygame
    import sys
    from time import time, clock
    from copy import copy, deepcopy
    import datetime
    import re
    import random
    import math
    from collections import defaultdict, OrderedDict, Counter
    from collections import Iterable
    import weakref
    import codecs
    import hashlib
    import json
    import itertools
    import operator
    import textwrap
    import bisect
    import glob
    import logging
    try:
        import android

    except ImportError:
        android = None


init python early hide:
    try:
        from contextlib import suppress
    except ImportError:
        class suppress():
            '''Backported from cpython 3.x'''
            
            def __init__(self, *excs):
                self._excs = excs
            
            def __enter__(self):
                pass
            
            def __exit__(self, exctype, excinst, exctb):
                return exctype is not None and issubclass(exctype, self._excs)

    store.suppress = suppress
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
