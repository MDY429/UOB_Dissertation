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

## interactive_story_0
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

## interactive_story_1
* greet
    - utter_greet
* inform{"muscle": "pectoralis major"}
    - slot{"muscle": "pectoralis major"}
    - action_check_muscle
* negative{"deny": "nope"}
    - slot{"deny": "nope"}
    - action_check_equipment
    - followup{"name": "action_search_exercise"}
    - slot{"facility": "bodyweight"}
    - slot{"deny": null}
    - action_search_exercise
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"deny": null}

## interactive_story_2
* inform{"muscle": "chest", "facility": "cable"}
    - slot{"facility": "cable"}
    - slot{"muscle": "chest"}
    - action_check_muscle
    - action_search_exercise
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"deny": null}

## interactive_story_3
* greet{"greet": "hey what's up"}
    - utter_greet
* inform{"muscle": "biceps"}
    - slot{"muscle": "biceps"}
    - action_check_muscle
* inform{"muscle": "triceps"}
    - slot{"muscle": "triceps"}
    - action_check_muscle
    - slot{"facility": null}
    - slot{"deny": null}
* inform{"facility": "dumbbell"}
    - slot{"facility": "dumbbell"}
    - action_check_equipment
    - action_search_exercise
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"deny": null}
