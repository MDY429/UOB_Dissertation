import logging
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

logger = logging.getLogger(__name__)

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
        
        logger.debug("1,{}".format(facility))
        
        # If facility is None --> set to bodyweight
        if facility == None:
            logger.debug("2,{}".format(facility))
            facility = tracker.get_slot('deny')
            logger.debug("3,{}".format(facility))
            
            if  facility != None:
                logger.debug("11,{}".format(facility))
                tracker.slots['facility'] = 'bodyweight'
                logger.debug("12,{}".format(tracker.get_slot('facility')))
            else:
                logger.debug("22,{}".format(facility))
                dispatcher.utter_template('utter_ask_facility2', tracker)
                return [SlotSet('facility', None), SlotSet('deny', None)]
        

        response = """ You want to find the {} exercise with {}.""".format(muscle, tracker.get_slot('facility'))

        dispatcher.utter_message(response)
        return [SlotSet('muscle', None), SlotSet('facility', None), SlotSet('deny', None)]