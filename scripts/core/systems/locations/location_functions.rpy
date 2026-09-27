init -5 python:
    def get_path_to_location(origin, destination):
        """
            Function get_path_to_location(Location: origin, Location: destination)

            Temporary locks all locations from origin to destination that are
            not on the path to that destination.

            Returns a list of locations, which is the path to take.
        """
        children = origin.get_all_children()
        path = []
        for child in children:
            child.temporary_locked = True
        while destination != origin:
            destination.temporary_locked = False
            path.append(destination)
            destination = destination.parents[0]
        return path

    def locations_label_check(prt=False):
        wrong_labels = [loc.label for loc in store.locations.values() if not renpy.has_label(loc.label)]
        padded = sorted(wrong_labels)
        padded.extend([""] * (len(wrong_labels) % 4))
        if wrong_labels:
            if not prt:
                logger.debug("LOCATION LABEL CHECK :")
            else:
                print("DEBUG : LOCATION LABEL CHECK :")
        for i in xrange(0, len(padded), 4):
            if prt:
                print("DEBUG : " + ", ".join(padded[i:i+4]))
            else:
                logger.debug(", ".join(padded[i:i+4]))
        return wrong_labels

    def locations_background_names_check(prt=False):
        dont_care_locs = (L_NULL, L_apt_other, L_map, L_rump_office,
                          L_school_utilitycloset, L_trailer_shootingrange)
        wrong = []
        for loc, data in background_names.items():
            if data == [] and loc not in dont_care_locs and loc._bg not in ("ground", ""):
                s = 'EXPECTED FORMAT for location {}: location_{}_(period)_(tod)_(attr)'.format(loc, loc._bg)
                wrong.append(s)
        if wrong:
            if not prt:
                logger.debug("LOCATION BACKGROUND NAMES CHECK :")
            else:
                print("DEBUG : LOCATION BACKGROUND NAMES CHECK :")
        for s in wrong:
            if prt:
                print("DEBUG : " + s)
            else:
                logger.debug(s)

    def dianes_shed_exit_location():
        if M_diane.finished_state(S_diane_barn_news):
            return L_diane_barn_garden
        else:
            return L_diane_garden

    def church_graveyard_exit_location():
        if not L_church_front.locked:
            return L_church_front
        elif M_diane.finished_state(S_diane_barn_news):
            return L_diane_barn_garden
        elif M_diane.finished_state(S_diane_couch_crashing):
            return L_diane_barn_bulding
        else:
            return L_diane_garden
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
