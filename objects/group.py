# Group of Entities: either Actors, Receivers, or ActorReceivers
from entity import Entity


class Group(object):
    def __init__(self):
        self.listEntities = []

    def live_next(self, prev_rel_time):
        """
        compute new property-values independently of other entities (passiv):
        - self-reduction effect, for radiation for instance over time, or as a defense against other activ entities
        :param prev_rel_time:
        :return:
        """
        for entity in self.listEntities:
            entity.liveNext(prev_rel_time)

    def get_all_entities(self): pass

    def get_all_other_entities(self, me): pass

    def add_entity(self, entity):
        # ex. of entity object
        # ..entity = Entity('a', ['x', 'y', 'z'], [0, 1, 1], ['m', 'm', 'm'])
        assert isinstance(entity, Entity)
        self.listEntities.append(entity)
