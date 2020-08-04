import logging
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, AllSlotsReset
from rasa.core.trackers import DialogueStateTracker

import csv
import random

bodyMap = {}
muscleMap = {}
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

        try:
            # Need a exercise suggestion.
            if suggest != None:
                rnd = random.choice(exerciseList)
                msg = "I recommend to do some {} exercise with {}!!\nFYI {}".format(rnd['Body'],rnd['equipment'], rnd['resource'])
                dispatcher.utter_message(msg)
                return [AllSlotsReset(), FollowupAction('action_restart')]
            # Body part question
            elif tracker.latest_message['intent'].get('name') == 'query':
                respond = "You can choice following body: {}".format(list(bodyMap.keys())[0:])
                dispatcher.utter_message(respond)
                return [FollowupAction('action_listen')]

            # Check body is vaildated.
            if body != None and body.lower() in [item.lower() for item in list(bodyMap.keys())]:
                dispatcher.utter_message(template='utter_check_muscle')
                return [SlotSet('muscle', None), SlotSet('facility', None), SlotSet('deny', None), SlotSet('suggest', None)]

            dispatcher.utter_message(template='utter_cannot_understand')
            respond = "Please check the spelling of body part\n"
            respond = respond +"\tFollowing is the body list: {}\n".format(list(bodyMap.keys())[0:])
            respond = respond + "Which part of body exercise you want to know?"
            dispatcher.utter_message(respond)
            return [AllSlotsReset(), FollowupAction('action_restart')]

        except:
            dispatcher.utter_template('utter_system_wrong')
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
        intent = tracker.latest_message['intent'].get('name')

        logger.debug("b:{}, m:{}".format(body, muscle))

        try:
            # Need muscle suggestion
            if body != None and (intent == 'negative' or tracker.get_slot('deny') != None or tracker.get_slot('suggest') != None):
                rnd = random.choice(list(bodyMap[body.lower()]))
                dispatcher.utter_message(template='utter_random_muscle', variable=rnd)
                dispatcher.utter_message(template='utter_ask_facility')
                return [SlotSet('muscle', muscleMap[rnd][0]), SlotSet('deny', None), SlotSet('suggest', None), FollowupAction('action_listen')]
            # Need to know what muscles in body.
            elif intent == 'query':
                if muscle != None:
                    return[FollowupAction('action_check_equipment')]
                dispatcher.utter_template('utter_query_muscle', tracker, body=body)
                dispatcher.utter_message(" - {}".format(bodyMap[body.lower()]))
                return []
            # Ask muscle directly.
            elif body == None and any(tracker.get_latest_entity_values('muscle')):
                print(tracker.latest_message)
                body = tracker.latest_message['entities'][0].get('role')
                dispatcher.utter_message(template='utter_ask_facility')
                return [SlotSet('body', body), SlotSet('deny', None), SlotSet('suggest', None)]

            # Vaildate muscle
            if any(tracker.get_latest_entity_values('muscle', entity_role = str(body).lower())):
            # if (tracker.latest_message.get("entities", [])[0]['role'] == body.lower()) == True:
                dispatcher.utter_message(template='utter_ask_facility')
                return [SlotSet('deny', None), SlotSet('suggest', None)]
            
            # Vaildate muscle fail
            dispatcher.utter_template('utter_wrong_muscle', tracker)
            return [SlotSet('muscle', None)]
        except:
            dispatcher.utter_template('utter_system_wrong')
            return [AllSlotsReset(), FollowupAction('action_restart')]

class ActionCheckEquipment(Action):
    def name(self):
        return 'action_check_equipment'

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        logger.debug("---- [ActionCheckEquipment] ----")

        try:
            # Get slot value
            muscle = tracker.get_slot('muscle')
            facility = tracker.get_slot('facility')
            deny = tracker.get_slot('deny')
            intent= tracker.latest_message['intent'].get('name')

            logger.debug("m:{}, f:{}, d:{}, ent:{}".format(muscle, facility, deny, intent))

            # Need to know equipments 
            if tracker.latest_message['intent'].get('name') == 'query':
                dispatcher.utter_template('utter_query_equipment', tracker)
                dispatcher.utter_message(" - {}".format(equipmentMapping(muscle)))
                return []
            # Need suggestion
            elif intent == 'negative' or deny != None or tracker.get_slot('suggest') != None:
                rnd = random.choice(list(equipmentMapping(muscle)))
                respond = 'Let us use {} to do some exercise!!'.format(rnd)
                dispatcher.utter_message(respond)
                return [SlotSet('facility', rnd), SlotSet('suggest', None), SlotSet('deny', None),FollowupAction('action_search_exercise')]

            if facility != None and facility.lower() in equipmentMapping(muscle):
                    return [FollowupAction('action_search_exercise')]
            else:
                rnd = random.choice(list(equipmentMapping(muscle)))
                respond = 'Sorry, there is no exercise go with this equipment. But we recommend use {} to replace.'.format(rnd)
                dispatcher.utter_message(respond)
                return [SlotSet('facility', rnd), FollowupAction('action_search_exercise')]
            # else:
            #     respond = 'Oh, please check your equipment is correct.'
            #     dispatcher.utter_message(respond)
            #     dispatcher.utter_template('utter_cannot_understand', tracker)
            #     return [SlotSet('facility', None)]
            # return [FollowupAction('action_search_exercise')]
        except:
            dispatcher.utter_template('utter_system_wrong')
            return [AllSlotsReset(), FollowupAction('action_restart')]

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
            response = "sorry, we cannot find the related exercise for you.\n"
            response = "But we recommend you to do this\n"
            rnd = random.choice(exerciseList)
            response = response + "I recommend to do some {} exercise with {}!!\nFYI {}".format(rnd['Body'],rnd['equipment'], rnd['resource'])
        dispatcher.utter_message(response)
        return [AllSlotsReset(), FollowupAction('action_restart')]

### Sub Method ###
def readBodyMap():
    logger.debug('BodyMap.csv')
    input_csv = []
    reader = csv.DictReader(open('BodyMap.csv'))
    for row in reader:
        input_csv.append(row)

    for row in input_csv:
        b = row['Body'].lower()
        if b not in bodyMap:
            bodyMap[b] = set()
        bodyMap[b].add(row['muscle'])

    for row in input_csv:
        if row['muscle'] not in muscleMap:
            muscleMap[row['muscle']] = []
        muscleMap[row['muscle']].append(row['value'])

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

def equipmentMapping(muscle):
    logger.debug('Searching {} for equipment'.format(muscle))
    src = set()
    for e in exerciseList:
        if e['muscle'].lower() == muscle.lower() and e['equipment'] not in src:
            src.add(e['equipment'].lower())
    return src

def equipmentList():
    return ['Barbell', 'Cable', 'Dumbbell', 'Smith', 'Lever', 'Suspended', 'BodyWeight', 'Sled',
            'Weight', 'Weight', 'Band Resistive', 'Assisted', 'TrapBar', 'SafetyBarbell', 'MedicineBall']

readBodyMap()
readExerciseMap()
