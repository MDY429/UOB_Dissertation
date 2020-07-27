## story 01
* greet
    - utter_greet

## story 02
* goodbye
    - utter_goodbye

## story 03
* partOfBody
    - action_check_body
* thighs
    - action_check_muscle
* equipment
    - action_search_exercise

## story 04
* query
    - action_check_body
* partOfBody
    - action_check_body
* query
    - action_check_muscle
* hips
    - action_check_muscle
* equipment
    - action_check_equipment

## interactive_story_1
* greet
    - utter_greet
* partOfBody{"body": "shoulders"}
    - slot{"body": "shoulders"}
    - action_check_body
* shoulder{"muscle": "DeltoidPosterior"}
    - slot{"muscle": "DeltoidPosterior"}
    - action_check_muscle
* equipment{"facility": "barbell"}
    - slot{"facility": "barbell"}
    - action_check_equipment

## interactive_story_1
* greet
    - utter_greet
* partOfBody{"body": "shoulder"}
    - slot{"body": "shoulder"}
    - action_check_body
* shoulder{"muscle": "DeltoidAnterior"}
    - slot{"muscle": "DeltoidAnterior"}
    - action_check_muscle
* equipment{"facility": "barbell"}
    - slot{"facility": "barbell"}
    - action_search_exercise
    - slot{"body": null}
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"suggest": null}
* partOfBody{"body": "neck"}
    - slot{"body": "neck"}
    - action_check_body
* neck{"muscle": "sternocleidomastoid"}
    - slot{"muscle": "sternocleidomastoid"}
    - action_check_muscle
* equipment{"facility": "cable"}
    - slot{"facility": "cable"}
    - action_check_equipment
    - followup{"name": "action_search_exercise"}
    - action_search_exercise
    - slot{"body": null}
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"suggest": null}

## interactive_story_1
* greet
    - utter_greet
* partOfBody{"body": "shoulder"}
    - slot{"body": "shoulder"}
    - action_check_body
* shoulder{"muscle": "DeltoidLateral"}
    - slot{"muscle": "DeltoidLateral"}
    - action_check_muscle
* equipment{"facility": "dumbbell"}
    - slot{"facility": "dumbbell"}
    - action_check_equipment
    - followup{"name": "action_search_exercise"}
    - action_search_exercise
    - slot{"body": null}
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"suggest": null}

## interactive_story_1
* greet
    - utter_greet
* query
    - action_check_body
* chest{"body": "chest"}
    - slot{"body": "chest"}
    - action_check_body
* chest{"muscle": "PectoralClavicular"}
    - slot{"muscle": "PectoralClavicular"}
    - action_check_muscle
* equipment{"facility": "barbell"}
    - slot{"facility": "barbell"}
    - action_check_equipment
    - followup{"name": "action_search_exercise"}
    - action_search_exercise
    - slot{"body": null}
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"suggest": null}

## interactive_story_1
* greet
    - utter_greet
* partOfBody{"body": "hips"}
    - slot{"body": "hips"}
    - action_check_body
* back{"muscle": "TrapeziusUpper"}
    - slot{"muscle": "TrapeziusUpper"}
    - action_check_muscle
    - slot{"muscle": null}
    - followup{"name": "action_listen"}
* query
    - action_check_muscle
    - followup{"name": "action_listen"}
* hips{"muscle": "HipFlexors"}
    - slot{"muscle": "HipFlexors"}
    - action_check_muscle
* negative{"deny": "no"}
    - slot{"deny": "no"}
    - action_check_equipment
    - slot{"facility": "bodyweight"}
    - slot{"deny": null}
    - followup{"name": "action_search_exercise"}
    - action_search_exercise
    - slot{"body": null}
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"suggest": null}

## interactive_story_1
* greet
    - utter_greet
* partOfBody{"body": "shoulder"}
    - slot{"body": "shoulder"}
    - action_check_body
* query
    - action_check_muscle
    - followup{"name": "action_listen"}
* shoulder{"muscle": "DeltoidAnterior"}
    - slot{"muscle": "DeltoidAnterior"}
    - action_check_muscle
* negative{"deny": "no"}
    - slot{"deny": "no"}
    - action_check_equipment
    - slot{"facility": "bodyweight"}
    - slot{"deny": null}
    - followup{"name": "action_search_exercise"}
    - action_search_exercise
    - slot{"body": null}
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"suggest": null}
