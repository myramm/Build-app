init -900 python:
    class Set(object):
        def __init__(self, *items):
            self.items = list(set(items))
        
        def __len__(self):
            return len(self.items)
        
        def __getitem__(self, index):
            return self.items[index]
        
        def __setitem__(self, index, item):
            if item not in self.items:
                self.items[index] = item
            else:
                raise ValueError
        
        def __delitem__(self, index):
            del self.items[index]
        
        def __iter__(self):
            return self
        
        def __contains__(self, item):
            return item in self.items
        
        def __nonzero__(self):
            return self.__bool__()
        
        def __bool__(self):
            return len(self) != 0
        
        def __reversed__(self):
            return reversed(self.items)
        
        def __str__(self):
            return "{" + ", ".join(self.items) + "}"
        
        def __repr__(self):
            return "Set(" + str(self) + ") at " + id(self)
        
        def next(self):
            for item in self.items:
                yield item
        
        def append(self, item):
            self.items.insert(len(self), item)
        
        def insert(self, index, item):
            if item not in self.items:
                self.items.insert(index, item)
        
        def pop(self, index=None):
            if index is None:
                index = len(self)
            return self.items.pop(index)
        
        def extend(self, other_list):
            other_list = list(set(other_list))
            self.items.extend(other_list)
            self.items = list(set(other_list))
        
        def remove(self, item):
            self.items.remove(item)
        
        def sort(cmp=None, key=None, reverse=False):
            self.items.sort(cmp, key, reverse)

    class LastUpdatedOrderedDict(OrderedDict):
        'Store items in the order the keys were last added'
        def __setitem__(self, key, value):
            if key in self:
                del self[key]
            OrderedDict.__setitem__(self, key, value)
        
        @property
        def listkeys(self):
            return list(self.keys())
        
        @property
        def listvalues(self):
            return list(self.values())
        
        @property
        def lastkey(self):
            return self.listkeys[-1]
        
        @property
        def lastvalue(self):
            return self.listvalues[-1]
        
        @property
        def isempty(self):
            return len(self.listkeys) == 0

    class OrderedSet(object):
        def __init__(self, *items):
            self.items = []
            for item in items:
                if item not in self.items:
                    self.items.append(item)
        
        def __getitem__(self, item):
            return self.items[item]
        
        def __repr__(self):
            return "OrderedSet(" + str(self.items) + ") at id " + str(id(self))
        
        def add(self, item):
            if item not in self.items:
                self.items.append(item)
        
        def remove(self, item):
            self.items.remove(item)
        
        def pop(self, index=-1):
            try:
                return self.items.pop(index)
            except IndexError:
                raise KeyError('pop from an empty OrderedSet')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
