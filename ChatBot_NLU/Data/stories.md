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

## story 05
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
* query
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
* partOfBody{"body": "chest"}
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

## interactive_story_1
* greet
    - utter_greet
* partOfBody{"body": "shoulder"}
    - slot{"body": "shoulder"}
    - action_check_body
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"deny": null}
    - slot{"suggest": null}
* query
    - action_check_muscle
* shoulder{"muscle": "DeltoidAnterior"}
    - slot{"muscle": "DeltoidAnterior"}
    - action_check_muscle
    - slot{"deny": null}
    - slot{"suggest": null}
* query
    - action_check_equipment
* equipment{"facility": "cable"}
    - slot{"facility": "cable"}
    - action_check_equipment
    - slot{"facility": "Cable"}
    - followup{"name": "action_search_exercise"}
    - action_search_exercise
    - slot{"body": null}
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"deny": null}
    - slot{"suggest": null}

## interactive_story_1
* greet
    - utter_greet
* partOfBody{"body": "back"}
    - slot{"body": "back"}
    - action_check_body
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"deny": null}
    - slot{"suggest": null}
* query
    - action_check_muscle
* back{"muscle": "upper trapezius"}
    - slot{"muscle": "upper trapezius"}
    - action_check_muscle
    - slot{"deny": null}
    - slot{"suggest": null}
* equipment{"facility": "cable"}
    - slot{"facility": "cable"}
    - action_check_equipment
    - action_search_exercise
    - slot{"body": null}
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"deny": null}
    - slot{"suggest": null}

## interactive_story_1
* greet
    - utter_greet
* query
    - action_check_body
    - followup{"name": "action_listen"}
* support{"suggest": "Suggestion"}
    - slot{"suggest": "Suggestion"}
    - action_check_body
    - reset_slots
    - followup{"name": "action_restart"}
    - action_restart

## interactive_story_2
* query
    - action_check_body
    - followup{"name": "action_listen"}
* partOfBody{"body": "chest"}
    - slot{"body": "chest"}
    - action_check_body
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"deny": null}
    - slot{"suggest": null}
* partOfBody{"body": "forearms"}
    - slot{"body": "forearms"}
    - action_check_body
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"deny": null}
    - slot{"suggest": null}
* partOfBody{"body": "thighs"}
    - slot{"body": "thighs"}
    - action_check_body
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"deny": null}
    - slot{"suggest": null}
* waist{"waist": "RectusAbdominis"}
    - action_check_muscle
    - slot{"muscle": null}
* thighs{"muscle": "Hamstrings"}
    - slot{"muscle": "Hamstrings"}
    - action_check_muscle
    - slot{"deny": null}
    - slot{"suggest": null}
* thighs{"muscle": "Quadriceps"}
    - slot{"muscle": "Quadriceps"}
    - action_check_muscle
    - slot{"deny": null}
    - slot{"suggest": null}
* query
    - action_check_equipment
* equipment{"facility": "sled"}
    - slot{"facility": "sled"}
    - action_check_equipment
    - followup{"name": "action_search_exercise"}
    - action_search_exercise
    - reset_slots
    - followup{"name": "action_restart"}
    - action_restart

## interactive_story_1
* query
    - action_check_body
    - followup{"name": "action_listen"}
* partOfBody{"body": "calves"}
    - slot{"body": "calves"}
    - action_check_body
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"deny": null}
    - slot{"suggest": null}
* negative{"deny": "no"}
    - slot{"deny": "no"}
    - action_check_muscle
    - slot{"muscle": "TibialisAnterior"}
    - slot{"deny": null}
    - slot{"suggest": null}
    - followup{"name": "action_listen"}
* negative{"deny": "no"}
    - slot{"deny": "no"}
    - action_check_equipment
    - slot{"facility": "lever"}
    - slot{"suggest": null}
    - slot{"deny": null}
    - followup{"name": "action_search_exercise"}
    - action_search_exercise
    - reset_slots
    - followup{"name": "action_restart"}
    - action_restart

## interactive_story_2
* query
    - action_check_body
    - followup{"name": "action_listen"}
* partOfBody{"body": "thighs"}
    - slot{"body": "thighs"}
    - action_check_body
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"deny": null}
    - slot{"suggest": null}
* negative{"deny": "NO"}
    - slot{"deny": "NO"}
    - action_check_muscle
    - slot{"muscle": "Hamstrings"}
    - slot{"deny": null}
    - slot{"suggest": null}
    - followup{"name": "action_listen"}
* query
    - action_check_equipment
* equipment{"facility": "trapbar"}
    - slot{"facility": "trapbar"}
    - action_check_equipment
    - followup{"name": "action_search_exercise"}
    - action_search_exercise
    - reset_slots
    - followup{"name": "action_restart"}
    - action_restart

## interactive_story_3
* equipment{"muscle": "PectoralClavicular", "facility": "barbell"}
    - slot{"facility": "barbell"}
    - slot{"muscle": "PectoralClavicular"}
    - action_check_equipment
    - followup{"name": "action_search_exercise"}
    - action_search_exercise
    - reset_slots
    - followup{"name": "action_restart"}
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* partOfBody{"body": "hips"}
    - slot{"body": "hips"}
    - action_check_body
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"deny": null}
    - slot{"suggest": null}
* support{"suggest": "Suggestion"}
    - slot{"suggest": "Suggestion"}
    - action_check_muscle
    - slot{"muscle": "HipAbductor"}
    - slot{"deny": null}
    - slot{"suggest": null}
    - followup{"name": "action_listen"}
* equipment{"facility": "bodyweight"}
    - slot{"facility": "bodyweight"}
    - action_check_equipment
    - followup{"name": "action_search_exercise"}
    - action_search_exercise
    - reset_slots
    - followup{"name": "action_restart"}
    - action_restart

## interactive_story_2
* partOfBody{"body": "upperarms"}
    - slot{"body": "upperarms"}
    - action_check_body
    - slot{"muscle": null}
    - slot{"facility": null}
    - slot{"deny": null}
    - slot{"suggest": null}
* upperarms{"muscle": "Biceps"}
    - slot{"muscle": "Biceps"}
    - action_check_muscle
    - slot{"deny": null}
    - slot{"suggest": null}
* support{"suggest": "Suggestion"}
    - slot{"suggest": "Suggestion"}
    - action_check_equipment
    - slot{"facility": "barbell"}
    - slot{"suggest": null}
    - slot{"deny": null}
    - followup{"name": "action_search_exercise"}
    - action_search_exercise
    - reset_slots
    - followup{"name": "action_restart"}
    - action_restart
