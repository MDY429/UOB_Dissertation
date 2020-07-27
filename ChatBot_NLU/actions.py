import logging
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, AllSlotsReset
from rasa.core.trackers import DialogueStateTracker

import csv
import random

bodyMap = {}
exerciseList = []

logger = logging.getLogger(__name__)

class ActionCheckBody(Action):
    def name(self):
        return 'action_check_body'

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        logger.debug("---- [ActionCheckBody] ----")

        # Get slot value
        body = tracker.get_slot('body')
        suggest = tracker.get_slot('suggest')
        muscle = tracker.get_slot('muscle')
        facility = tracker.get_slot('facility')

        logger.debug("b:{}, s:{}, m:{}, f:{}".format(body, suggest, muscle, facility))

        # Need a exercise suggestion.
        if suggest != None:
            rnd = random.choice(exerciseList)
            msg = "I recommend to do some {} exercise with {}!!\nFYI {}".format(rnd['Body'],rnd['equipment'], rnd['resource'])
            dispatcher.utter_message(msg)
            return [AllSlotsReset()]
        # Body part question
        elif tracker.latest_message['intent'].get('name') == 'query':
            respond = "You can choice following body: {}".format(list(bodyMap.keys())[0:])
            dispatcher.utter_message(respond)
            return [FollowupAction('action_listen')]

        # Check body is vaildated.
        if body != None:
            if body.lower() in [item.lower() for item in list(bodyMap.keys())]:
                dispatcher.utter_message(template='utter_check_muscle')
                return []

        dispatcher.utter_message(template='utter_cannot_understand')
        return [AllSlotsReset(), FollowupAction('action_restart')]

class ActionCheckMuscle(Action):
    def name(self):
        return 'action_check_muscle'

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        logger.debug("---- [ActionCheckMuscle] ----")

        # Get slot value
        body = tracker.get_slot('body')
        muscle = tracker.get_slot('muscle')
        facility = tracker.get_slot('facility')

        logger.debug("b:{}, m:{}, f:{}".format(body, muscle, facility))

        if (muscle != None) and (facility != None):
            return [FollowupAction('action_search_exercise')]
        elif tracker.latest_message['intent'].get('name') == 'query':
            respond = "{} has following muscles: {}".format(body, bodyMap[body])
            dispatcher.utter_message(respond)
            return [FollowupAction('action_listen')]

        if any(tracker.get_latest_entity_values('muscle', entity_role = body.lower())):
            dispatcher.utter_message(template='utter_ask_facility')
        else:
            dispatcher.utter_message(template='utter_wrong_muscle')
            return [SlotSet('muscle', None), FollowupAction('action_listen')]
        
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
                return [SlotSet('facility', None), FollowupAction('action_listen')]
        
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

        try:       
            response = """FYI {}""".format(random.choice(searchExercise(muscle, facility)))
        except:
            response = "sorry, we don't have this."
        dispatcher.utter_message(response)
        return [SlotSet('body', None), SlotSet('muscle', None), SlotSet('facility', None), SlotSet('suggest', None)]

### Sub Method ###
def readBodyMap():
    logger.debug('BodyMap.csv')
    reader = csv.DictReader(open('BodyMap.csv'))
    for row in reader:
        if row['Body'] not in bodyMap:
            bodyMap[row['Body']] = set()
        bodyMap[row['Body']].add(row['muscle'])

def readExerciseMap():
    logger.debug('Exercise.csv')
    reader = csv.DictReader(open('Exercise.csv'))
    for row in reader:
        exerciseList.append(row)

def searchExercise(muscle, facility):
    logger.debug('Searching {} with {}'.format(muscle, facility))
    src = []
    for e in exerciseList:
        if e['muscle'].lower() == muscle.lower() and e['equipment'].lower() == facility.lower():
            src.append(e['resource'])
    return src

readBodyMap()
readExerciseMap()