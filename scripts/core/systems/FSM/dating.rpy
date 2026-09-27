init -6 python:
    class DatingSystem(object):
        def __init__(self, name):
            self._data = store.dating_data.get(name, {})
            self._thresholds = self._data.get("thresholds", {})
            self._dating_points = 0
            self._times_actions_performed = defaultdict(int)
            self.name = name
        
        def copy(self):
            d = DatingSystem(self.name)
            for k, v in self.__dict__.items():
                d.__dict__[k] = copy(v)
            return d
        
        def update(self, category, item):
            data = self._data.get(category)
            if data is not None:
                self._times_actions_performed["{}/{}".format(category, item)] += 1
                for k in [x for x in data.keys() if "*" in x]:
                    
                    if item.startswith(k.split("*")[0]):
                        value = data.get(k, 0)
                        self.dating_points = self._get_value_increment(value, category, item)
                        return
                value = data.get(item, 0)
                self.dating_points = self._get_value_increment(value, category, item)
        
        @property
        def dating_points(self):
            return self._dating_points
        
        @dating_points.setter
        def dating_points(self, value):
            if isinstance(value, int):
                self._dating_points = value
                self.serialize()
        
        def increment(self, value):
            self.dating_points = self.dating_points + value
        
        def deserialize(self, obj):
            self._dating_points = int(obj.get("dating_points", 0))
            self._times_actions_performed.update(obj.get("times_actions_performed", {}))
            return
        
        def serialize(self):
            global fsm_data
            name = self.name
            data = {"dating_points": self._dating_points,
                    "times_actions_performed": self._times_actions_performed
            }
            fsm_data.machine_data[name]["dating"] = copy(data)
        
        def _get_value_increment(self, value, category, item):
            """
                Exponential decay for the value, the more you perform an action on a machine

                value = value * exp(-0.3 * t), t= n of times the action was performed.

                result is rounded, and cast as an integer.
            """
            t = self._times_actions_performed.get("{}/{}".format(category, item), 1)
            lam = 0.3
            try:
                value = float(value) * math.exp(-lam * t)
            except:
                pass
            value = int(round(value, 0))
            return self.dating_points + value
        
        @property
        def available_sex(self):
            return self.dating_points > self._thresholds.get("sex", 0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
