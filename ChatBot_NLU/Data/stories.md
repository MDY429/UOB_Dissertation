## story 01
* greet
    - utter_greet

## story 02
* goodbye
    - utter_goodbye

## story 03
* inform
    - action_check_muscle

## story 04
* inform
    - action_check_muscle
* inform
    - action_check_equipment

## interactive_story_1
* greet
    - utter_greet
* inform{"muscle": "chest"}
    - slot{"muscle": "chest"}
    - action_check_muscle
* inform{"facility": "bodyweight"}
    - slot{"facility": "bodyweight"}
    - action_check_equipment
    - action_search_exercise
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"deny": null}
