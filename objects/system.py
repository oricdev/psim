# System management
import numpy as np
from timeslot import *
from entity import Entity
from actors import Actors
from receivers import Receivers
from actorsreceivers import ActorsReceivers


class System:
    def __init__(self):
        self.time_start_experiment = current_milli_time()
        self.current_rel_time = 0
        # time-gap is defaulted to 1sec = 1000ms
        self.timegap = 1000
        # recording time-slots (relative time) and table of all objects' ids for each time-slot
        # (we use a dictionary for direct access/speed)
        self.times = {self.current_rel_time: {}}
        # .. but we also need to be able to fetch the nearest rel_time in case of de-synchronization
        # (due to time-gap changes=functionality such as acceleration or deceleration of ,time)
        self.t_times = []
        self.t_times.append(self.current_rel_time)
        # initialize groups of entities
        self.actors = Actors()
        self.load_actors()
        self.receivers = Receivers()
        self.load_receivers()
        self.actors_receivers = ActorsReceivers()
        self.load_actors_receivers()

    def load_actors(self):
        entity = Entity("soleil", ['x'], [0], ['m'])
        self.actors.add_entity(entity)

    def load_receivers(self):
        entity = Entity("terre", ['x'], [-2], ['m'])
        self.receivers.add_entity(entity)

    def load_actors_receivers(self):
        pass

    def get_state(self):
        current_state = {'time_start_experiment': self.time_start_experiment,
                         'system_rel_time': self.current_rel_time,
                         'timegap': self.timegap}
        list_actors = []
        for entity in self.actors.listEntities:
            list_actors.append(entity.name)
        current_state['actors'] = list_actors

        list_receivers = []
        for entity in self.receivers.listEntities:
            list_receivers.append(entity.name)
        current_state['receivers'] = list_receivers

        list_actors_receivers = []
        for entity in self.actors_receivers.listEntities:
            list_actors_receivers.append(entity.name)
        current_state['actors_receivers'] = list_actors_receivers
        return current_state

    def set_current_rel_time(self):
        self.current_rel_time += self.timegap

    def get_all_actors(self):
        """
        :return: Actors U Actors_receivers (all entities who has an effect on other passiv(receiver) entities
        """
        return np.vstack((self.actors.listEntities, self.actors_receivers.listEntities))

    def get_all_receivers(self):
        """
        :return: Receivers U Actors_receivers (all entities who has NO effect
        on any other entity (whatever activ or passiv)
        """
        return np.vstack((self.actors.listEntities, self.actors_receivers.listEntities))

    def compute_next_slot(self, prev_rel_time):
        # System point onto previous rel_time
        # compute data for all objects
        # .. adjust all entities
        self.actors.live_next(prev_rel_time)
        self.receivers.live_next(prev_rel_time)
        self.actors_receivers.live_next(prev_rel_time)
        # compute interactions of activ entities on each passiv entity
        activ_entities = self.get_all_actors()
        passiv_entities = self.get_all_receivers()
        for passiv_entity in passiv_entities:
            passiv_entity.calc_interactions(prev_rel_time, self.timegap, activ_entities)

    def get_data_for_slot_i(self, rel_time):
        # check if they were already computed; if yes, retrieve them back
        # data computed in entities for this slot :: update System with this time-slot
        # (if data required again later, no need to compute them again since each entity holds its own full history)
        if rel_time in self.times:
            return self.times[rel_time]
        # todo: if not computed with exact rel_time, try fetching low of high if available (approximation)
        # otherwise compute them (new)
        self.compute_next_slot(self.current_rel_time)
        data_for_this_slot = {}
        for entity in np.vstack((self.actors, self.receivers, self.actors_receivers)):
            # todo: extract only required fields for the GUI
            data_for_this_slot[entity.id] = entity.data[self.current_rel_time]

        return data_for_this_slot

    def get_data_next_n_slots(self, n):
        # gather all required properties for the n time-slots for all objects to feed the User Interface
        data_of_n_slots = {}

        for i in range(1, n):
            # data of next slot are based on data on previous time-slot
            prev_rel_time = self.current_rel_time
            self.set_current_rel_time()
            # note: in case of approximation in get_data_for_slot_i, we store anyway in System
            # for potentially further quick retrieval
            self.times[self.current_rel_time] = self.get_data_for_slot_i(prev_rel_time)
            data_of_n_slots[self.current_rel_time] = self.times[self.current_rel_time]
            self.add_to_t_time(self.current_rel_time)

        return data_of_n_slots

    def add_to_t_time(self, rel_time_to_add):
        """
        Insert rel_time_to_add accordingly in t_time (sorted)
        :param rel_time_to_add:
        :return:
        """
        self.t_times.append(rel_time_to_add)
        self.t_times.sort()
