## intent:greet
- hi
- hi there
- hello
- hola
- hey what's up
- hey

## intent:goodbye
- thanks, bye

## intent:suggest
- Any [suggestion]{"entity": "suggest", "value": "Suggestion"}?
- Can you give me some [advice]{"entity": "suggest", "value": "Suggestion"}?
- Give me some [recommendation]{"entity": "suggest", "value": "Suggestion"}. Thanks

## intent:query
- tell me more please
- What do you have?
- Can you tell me more?
- what part do you have/

## intent:shoulder
- [rear delts]{"entity": "muscle", "value": "DeltoidPosterior"}
- [front delts]{"entity": "muscle", "value": "DeltoidAnterior"} thanks
- [side shoulder]{"entity": "muscle", "value": "DeltoidLateral"} please

## intent:partOfBody
- Tell me some [shoulder](body) exercise
- How about [neck](body) exercise?
- could you please tell me how to train my [shoulders]{"entity": "body", "value": "shoulder"}?
- of course [barbell](facility)

## intent:equipment
- I would like to use [barbell](facility)
- [cable](facility)
- yes, [dumbbell](facility)

## intent:neck
- yeh, [side neck]{"entity": "muscle", "value": "sternocleidomastoid"} please

## intent:chest
- oh nice, I want to choose [chest](body)
- ahhh [upper chest]{"entity": "muscle", "value": "PectoralClavicular"}

## synonym:DeltoidAnterior
- front delts

## synonym:DeltoidLateral
- side shoulder

## synonym:DeltoidPosterior
- rear delts

## synonym:Suggestion
- suggestion
- advice
- recommendation

## synonym:shoulder
- shoulders

## synonym:sternocleidomastoid
- side neck
