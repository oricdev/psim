# Entity object


class Entity:
    def __init__(self, name, properties, values, units):
        self.name = name
        self.id = name
        # core properties (not bound with units
        self.core = {'id': self.id, 'name': name}
        self.props = {}
        for prop, val in zip(properties, values):
            self.props[prop] = val
        # object exists at startup (not dead)
        self.props['is_alive'] = True
        # init: bind to time-slot 0 (only properties are always saved on the flow to be able
        # to rebuild back based on time-slots
        self.data = {0: {self.props}}
        # Save units
        self.units = units
        # Effect formula against other entity which is actor(_receiver)
        # todo: review below
        self.effect_formula = "1+x{'x'}"

    def val(self, rel_time, prop_name):
        # If relative time is found, return the value of the required property
        if self.props.has_key(rel_time):
            if self.props[rel_time].has_key(prop_name):
                return self.props[rel_time][prop_name]
        return ""

    def live_next(self, prev_rel_time):
        """
        compute new property-values independently of other entities (passiv):
        - self-reduction effect, for radiation for instance over time, or as a defense against other activ entities
        :param prev_rel_time:
        :return:
        """
        # todo
        pass

    def calc_interactions(self, prev_rel_time, timegap, activ_entities):
        """
        Compute interactions of this entity received by all other actor-entities
        :param timegap:
        :param prev_rel_time:
        :param activ_entities:
        :return:
        """
        # todo: list of properties affected (x, y, z, etc.)
        global_interactions = {'x': 0}
        # compute global interactions on current object
        for actor in activ_entities:
            # todo: evaluate below interaction of actor on this entity
            # todo: actor.effectFormula
            effect = 1
            # todo: sum-up interactions by default, but in practise should be configurable
            # todo: ..for instance: radial waves (magnetic) may annihilate partially themselves if in opposition
            global_interactions['x'] += effect

        # at this stage, impacted properties are computes => save all properties for this time-slot
        self.save(prev_rel_time, timegap, global_interactions)

    def save(self, prev_rel_time, timegap, global_interactions):
        current_rel_time = prev_rel_time + timegap
        # replace each new value of property from global_interactions in the set of properties of the entity
        prev_dataset = self.data[prev_rel_time]
        for prop in global_interactions:
            prev_dataset[prop] = global_interactions[prop]

        # save updated data set for current time-slot
        self.data[current_rel_time] = prev_dataset
