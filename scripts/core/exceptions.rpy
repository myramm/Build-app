init python:
    class SummertimeSagaException(Exception):
        def __init__(self, message = "SummertimeSagaException triggered"):
            self.message = message
            self.type = type(self).__name__
        def __str__(self):
            rv = self.type + " : " + self.message
            logger.error(rv)
            return rv
        
        def __repr__(self):
            rv = self.type + " : " + self.message
            logger.error(rv)
            return rv

    class OnSleepException(SummertimeSagaException):
        def __init__(self, message = "OnSleepException triggered"):
            self.message = message
            self.type = type(self).__name__

    class FSMException(SummertimeSagaException):
        def __init__(self, message = "FSM Exception Triggered"):
            self.message = message
            self.type = type(self).__name__

    class DuplicateStateAddedException(FSMException):
        def __init__(self, message = "Duplicate State added."):
            self.message = message
            self.type = type(self).__name__

    class DuplicateTriggerAddedException(FSMException):
        def __init__(self, message = "Duplicate Trigger added."):
            self.message = message
            self.type = type(self).__name__

    class SummertimeSagaInitException(SummertimeSagaException):
        pass

    class OrphanedStateException(FSMException):
        def __init__(self, message = "State Orphaned."):
            self.message = message
            self.type = type(self).__name__

    class MisnamedTriggerException(FSMException):
        pass

    class LocationException(SummertimeSagaException):
        pass

    class LocationNotFoundError(LocationException):
        pass

    class MachineNotFoundError(FSMException):
        pass

    class StateNotFoundError(FSMException):
        pass

    class TriggerNotFoundError(FSMException):
        pass

    class FSMActionError(FSMException):
        def __init__(self, message = "Action Exception Triggered"):
            self.message = message
            self.type = type(self).__name__

    class CannotCreateExtrasError(SummertimeSagaException):
        def __init__(self, message = "Can only create extras from private resources"):
            self.message = message
            self.type = type(self).__name__

    class MoveToArgumentError(SummertimeSagaException):
        def __init__(self, location):
            self.type = type(self).__name__
            self.message = "{} is not a valid argument for MoveTo screen Action. Type : {} ; Expected : Location".format(location, type(location))

    class ModLoaderError(SummertimeSagaInitException):
        def __init__(self, message="ModLoaderError occured"):
            self.message = message
            self.type = type(self).__name__
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
