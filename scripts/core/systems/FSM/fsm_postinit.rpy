init -2 python:
    for name, var in globals().items():
        if name.startswith("T_"):
            var._name = name

init 990 python:
    for name, var in globals().items():
        if name.startswith("S_"):
            var._name = name
    instantiate_machines()
    check_misnamed_triggers()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
