import logging
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from rasa.core.trackers import DialogueStateTracker

logger = logging.getLogger(__name__)

class ActionCheckMuscle(Action):
    def name(self):
        return 'action_check_muscle'

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        logger.debug("---- [ActionCheckMuscle] ----")

        # Get slot value
        muscle = tracker.get_slot('muscle')
        facility = tracker.get_slot('facility')

        logger.debug("m:{}, f:{}".format(muscle, facility))

        if muscle == None:
            dispatcher.utter_message(template='utter_cannot_understand')
            return [SlotSet('muscle', None), SlotSet('facility', None), SlotSet('deny', None), FollowupAction('action_listen')]
        elif (muscle != None) and (facility != None):
            return [FollowupAction('action_search_exercise')]

        dispatcher.utter_message(template='utter_ask_facility')
        return []

class ActionCheckEquipment(Action):
    def name(self):
        return 'action_check_equipment'

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: DialogueStateTracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        logger.debug("---- [ActionCheckEquipment] ----")

        # Get slot value
        muscle = tracker.get_slot('muscle')
        facility = tracker.get_slot('facility')
        deny = tracker.get_slot('deny')
        intent= tracker.latest_message['intent'].get('name')

        logger.debug("m:{}, f:{}, d:{}, ent:{}".format(muscle, facility, deny, intent))

        if facility == None:
            if intent == 'negative' or deny != None:
                return [SlotSet('facility', 'bodyweight'), SlotSet('deny', None),FollowupAction('action_search_exercise')]
            else:
                dispatcher.utter_message(template='utter_ask_facility')
                return []
        
        return [FollowupAction('action_search_exercise')]

class ActionSearchExercise(Action):
    def name(self):
        return 'action_search_exercise'

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        logger.debug("---- [ActionSearchExercise] ----")
        
        # Get slot value
        muscle = tracker.get_slot('muscle')
        facility = tracker.get_slot('facility')

        logger.debug("m:{}, f:{}".format(muscle, facility))

        response = """ You want to find the {} exercise with {}.""".format(muscle, facility)

        dispatcher.utter_message(response)
        return [SlotSet('muscle', None), SlotSet('facility', None)]