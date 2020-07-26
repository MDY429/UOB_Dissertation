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
    - action_search_exercise

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
* partOfBody{"facility": "barbell"}
    - slot{"facility": "barbell"}
    - action_search_exercise
    - slot{"body": null}
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"suggest": null}
