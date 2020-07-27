import logging
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from rasa.core.trackers import DialogueStateTracker

import csv
import random

# reader = csv.DictReader(open('Exercise.csv'))
print('ttttttttt')
reader = csv.DictReader(open('BodyMap.csv'))
bodyMap = {}
for row in reader:
    if row['Body'] not in bodyMap:
        bodyMap[row['Body']] = set()
    bodyMap[row['Body']].add(row['muscle'])

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

        # if body != None:
        #     return [FollowupAction('action_check_muscle')]
        # bodyPart = ["neck", "shoulder", "back", "upper arms", "fore arms", "back", "chest", "waist", "hips", "thighs", "calves"]
        # bodyPart = bodyMap.keys()

        # print(tracker.get_latest_entity_values("body"))

        if suggest != None:
            rnd = random.choice(list(bodyMap.keys()))
            print(rnd)
            dispatcher.utter_message(template='utter_recommendation', variable = rnd)
            return [SlotSet('body', rnd), SlotSet('suggest', None)]
        elif tracker.latest_message['intent'].get('name') == 'query':
            respond = "You can choice following body: {}".format(bodyPart[0:])
            dispatcher.utter_message(respond)
            return []

        # if not isBody(body):
        #     dispatcher.utter_message(template='utter_cannot_understand')
        #     return [SlotSet('body', None), SlotSet('muscle', None), SlotSet('facility', None), SlotSet('suggest', None)]
        if body != None:
            reader = csv.DictReader(open('Exercise.csv'))
            for row in reader:
                # print("r:{}, boolean:{}".format(row, row['Body'].lower() == body.lower()))
                if row['Body'].lower() == body.lower():
                    dispatcher.utter_message(template='utter_check_muscle')
                    return []
                    # break
        dispatcher.utter_message(template='utter_cannot_understand')
        return [SlotSet('body', None), SlotSet('muscle', None), SlotSet('facility', None), SlotSet('suggest', None)]
        # dispatcher.utter_message(template='utter_check_muscle')
        # return []

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
            return []
        # elif muscle not in bodyMap[body]:
        #     dispatcher.utter_message(template='utter_cannot_find_muscle')
        #     return [SlotSet('muscle', None), SlotSet('facility', None), SlotSet('deny', None), FollowupAction('action_listen')]
        print(tracker.get_latest_entity_values("muscle"))
        if any(tracker.get_latest_entity_values("muscle")):
            print("AAAA")
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

        response1 = """ You want to find the {} exercise with {}.""".format(muscle, facility)

        reader = csv.DictReader(open('Exercise.csv'))
        sc = []
        try:
            for row in reader:
                if row['muscle'].lower() == muscle.lower() and row['equipment'].lower() == facility.lower():
                    print(row['resource'])
                    sc.append(row['resource'])

            print(sc[0:5])
        
            response1 = """FYI {}""".format(random.choice(sc))
        except:
            response1 = "sorry, we don't have this."
        # dispatcher.utter_message(response)
        dispatcher.utter_message(response1)
        return [SlotSet('body', None), SlotSet('muscle', None), SlotSet('facility', None), SlotSet('suggest', None)]

### functional method
def isBody(value):
    print("isBody: ", value)
    if value == None:
        return False
    for row in reader:
        print("r:{}, boolean:{}".format(row, row['Body'].lower() == value.lower()))
        if row['Body'].lower() == value.lower():
            return True
    return False