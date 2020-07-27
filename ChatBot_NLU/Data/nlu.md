## intent:greet
- Hello
- hey
- hello
- hi
- heya
- howdy
- hey there
- hi there
- hihi

## intent:goodbye
- goodbye
- bye
- bye bye
- see ya
- see you later

## intent:partOfBody
- I want to train my [chest](body).
- I wanna know about [neck](body) exercise!
- Anything about [shoulders]{"entity": "body", "value": "shoulder"}?
- how to let my [upper arms]{"entity": "body", "value": "upperarms"} get bigger?
- Check exercise for [fore arms]{"entity": "body", "value": "forearms"}
- well [back](body) muscle
- [BACK]{"entity": "body", "value": "back"} training!!
- oh, how about [back](body) training?
- I would like to know about [waist](body).
- [hips](body) thanks.
- [Thighs]{"entity": "body", "value": "thighs"} exercise
- of course is [calves](body)
- tell me about [deltoid](body)
- want more about [shoulder](body) exercise
- May I know about [leg]{"entity": "body", "value": "thighs"} exercise?
- my [arm]{"entity": "body", "value": "upperarms"}
- tell me about [calf]{"entity": "body", "value": "calves"} training
- [Forearm]{"entity": "body", "value": "forearms"}
- [Neck]{"entity": "body", "value": "neck"}
- [Shoulder]{"entity": "body", "value": "shoulder"}
- [Chest]{"entity": "body", "value": "chest"}
- [Waist]{"entity": "body", "value": "waist"}
- How about [hip]{"entity": "body", "value": "hips"}?
- Any about [thigh]{"entity": "body", "value": "thighs"}?
- tell me some about [hips](body)
- i wanna know some [shoulder](body) exercise

## intent:equipment
- [barbell](facility)
- [bodyweight](facility)
- [cable](facility)
- maybe [dumbbell](facility)
- yes, [dumbbell](facility) please
- ahh probably [barbell](facility)
- I will go [smith machine]{"entity": "facility", "value": "smith"}
- how about [smith](facility)?
- i would like to use [trapbar](facility)
- [band](facility)

## intent:negative
- [no](deny)!!
- [no](deny) need
- [nope]{"entity": "deny", "value": "no"}!
- [no](deny) thanks
- [no](deny) thank you
- [nah]{"entity": "deny", "value": "no"}
- [uhuh]{"entity": "deny", "value": "no"}
- [nope]{"entity": "deny", "value": "no"}
- [nope]{"entity": "deny", "value": "no"}

## intent:neck
- [Sternocleidomastoid]{"entity": "muscle", "role": "neck", "value": "sternocleidomastoid"}
- [Splenius]{"entity": "muscle", "role": "neck", "value": "splenius"}
- [front neck]{"entity": "muscle", "role": "neck", "value": "sternocleidomastoid"}
- [side neck]{"entity": "muscle", "role": "neck", "value": "sternocleidomastoid"}
- [Neck Flexor]{"entity": "muscle", "role": "neck", "value": "sternocleidomastoid"}
- [Sterno mastoid]{"entity": "muscle", "role": "neck", "value": "sternocleidomastoid"}
- [rear neck]{"entity": "muscle", "role": "neck", "value": "splenius"}
- [Neck Extensor]{"entity": "muscle", "role": "neck", "value": "splenius"}

## intent:shoulder
- [Front Shoulder]{"entity": "muscle", "role": "shoulder", "value": "DeltoidAnterior"}
- [Front Delts]{"entity": "muscle", "role": "shoulder", "value": "DeltoidAnterior"}
- [Side Shoulder]{"entity": "muscle", "role": "shoulder", "value": "DeltoidLateral"}
- [Side Delts]{"entity": "muscle", "role": "shoulder", "value": "DeltoidLateral"}
- [Rear Shoulder]{"entity": "muscle", "role": "shoulder", "value": "DeltoidPosterior"}
- [Rear Delts]{"entity": "muscle", "role": "shoulder", "value": "DeltoidPosterior"}
- [Rotatory Cuff]{"entity": "muscle", "role": "shoulder", "value": "Supraspinatus"}
- [front shoulder]{"entity": "muscle", "role": "shoulder", "value": "DeltoidAnterior"}

## intent:UpperArms
- [Rear Arm]{"entity": "muscle", "role": "UpperArms", "value": "Triceps"} please
- well [triceps]{"entity": "muscle", "role": "UpperArms", "value": "Triceps"}
- [Front Arm]{"entity": "muscle", "role": "UpperArms", "value": "Biceps"}
- yes! [biceps]{"entity": "muscle", "role": "UpperArms", "value": "Biceps"} please
- [Biceps Cubiti]{"entity": "muscle", "role": "UpperArms", "value": "Biceps"}
- [Triceps Brachii]{"entity": "muscle", "role": "UpperArms", "value": "Triceps"}
- [Biceps Brachii]{"entity": "muscle", "role": "UpperArms", "value": "Biceps"}
- [brachialis]{"entity": "muscle", "role": "UpperArms", "value": "Brachialis"}
- [Side Arm]{"entity": "muscle", "role": "UpperArms", "value": "Brachialis"}
- [Lower Biceps]{"entity": "muscle", "role": "UpperArms", "value": "Brachialis"}
- [supinators]{"entity": "muscle", "role": "UpperArms", "value": "Supinators"}

## intent:ForeArms
- [brachioradialis]{"entity": "muscle", "role": "ForeArms", "value": "Brachioradialis"}
- [Upper outer Forearm]{"entity": "muscle", "role": "ForeArms", "value": "Brachioradialis"}
- [Supinator longus]{"entity": "muscle", "role": "ForeArms", "value": "Brachioradialis"}
- [Wrist Flexors]{"entity": "muscle", "role": "ForeArms", "value": "WristFlexors"}
- [Inner Forearm]{"entity": "muscle", "role": "ForeArms", "value": "WristFlexors"}
- [Hand Flexors]{"entity": "muscle", "role": "ForeArms", "value": "WristFlexors"}
- [Wrist Extensors]{"entity": "muscle", "role": "ForeArms", "value": "WristExtensors"}
- [Hand Extensors]{"entity": "muscle", "role": "ForeArms", "value": "WristExtensors"}
- [outer Forearm]{"entity": "muscle", "role": "ForeArms", "value": "WristExtensors"}
- [back Forearm]{"entity": "muscle", "role": "ForeArms", "value": "WristExtensors"}
- [pronators]{"entity": "muscle", "role": "ForeArms", "value": "Pronators"}

## intent:back
- [Latissimus Dorsi]{"entity": "muscle", "role": "back", "value": "LatissimusDorsi"}
- [middle back]{"entity": "muscle", "role": "back", "value": "BackGeneral"}
- [outer back]{"entity": "muscle", "role": "back", "value": "LatissimusDorsi"}
- [Lats]{"entity": "muscle", "role": "back", "value": "LatissimusDorsi"}
- [Lats little helper]{"entity": "muscle", "role": "back", "value": "LatissimusDorsi"}
- [Teres Major]{"entity": "muscle", "role": "back", "value": "LatissimusDorsi"}
- [upper trapezius]{"entity": "muscle", "role": "back", "value": "TrapeziusUpper"}
- [Upper Traps]{"entity": "muscle", "role": "back", "value": "TrapeziusUpper"}
- [Upper Shoulder]{"entity": "muscle", "role": "back", "value": "TrapeziusUpper"}
- [Levator Scapulae]{"entity": "muscle", "role": "back", "value": "TrapeziusUpper"}
- [middle Trapezius]{"entity": "muscle", "role": "back", "value": "BackGeneral"}
- [mid Trapezius]{"entity": "muscle", "role": "back", "value": "BackGeneral"}
- [upper back]{"entity": "muscle", "role": "back", "value": "BackGeneral"}
- [Traps]{"entity": "muscle", "role": "back", "value": "BackGeneral"}
- [Lower Traps]{"entity": "muscle", "role": "back", "value": "BackGeneral"}
- [Lower Trapezius]{"entity": "muscle", "role": "back", "value": "BackGeneral"}
- [Rhomboids]{"entity": "muscle", "role": "back", "value": "BackGeneral"}
- [mid back]{"entity": "muscle", "role": "back", "value": "BackGeneral"}
- [infraspinatus]{"entity": "muscle", "role": "back", "value": "Infraspinatus"}
- [Teres Minor]{"entity": "muscle", "role": "back", "value": "Infraspinatus"}
- [subscapularis]{"entity": "muscle", "role": "back", "value": "Subscapularis"}
- [upper shoulder]{"entity": "muscle", "role": "back", "value": "TrapeziusUpper"}

## intent:chest
- ahh maybe [Pectoralis Major]{"entity": "muscle", "role": "chest", "value": "PectoralSternal"}
- [Sternal]{"entity": "muscle", "role": "chest", "value": "PectoralSternal"}
- [Lower Pecs]{"entity": "muscle", "role": "chest", "value": "PectoralSternal"}
- [lower chest]{"entity": "muscle", "role": "chest", "value": "PectoralSternal"}
- [Clavicular]{"entity": "muscle", "role": "chest", "value": "PectoralClavicular"}
- oh i want to know [upper pecs]{"entity": "muscle", "role": "chest"}
- yes [upper chest]{"entity": "muscle", "role": "chest", "value": "PectoralClavicular"} please!
- [Pectoralis]{"entity": "muscle", "role": "chest", "value": "PectoralSternal"}
- well [Pectoralis Minor]{"entity": "muscle", "role": "chest", "value": "PectoralSternal"}
- [Serratus Anterior]{"entity": "muscle", "role": "chest", "value": "SerratusAnterior"}
- [Serratus Magnus]{"entity": "muscle", "role": "chest", "value": "SerratusAnterior"}
- tell me some [major chest]{"entity": "muscle", "role": "chest", "value": "PectoralSternal"} exercise

## intent:waist
- [belly waist]{"entity": "muscle", "role": "waist", "value": "RectusAbdominis"}
- [Abdominal]{"entity": "muscle", "role": "waist", "value": "RectusAbdominis"}
- [abs]{"entity": "muscle", "role": "waist", "value": "RectusAbdominis"}
- [Rectus Abdominis]{"entity": "muscle", "role": "waist", "value": "RectusAbdominis"}
- [Transverse Abdominis]{"entity": "muscle", "role": "waist", "value": "Transverse"}
- [Transverse Abs]{"entity": "muscle", "role": "waist", "value": "Transverse"}
- i want to know [obliques]{"entity": "muscle", "role": "waist", "value": "Obliques"}
- [Upper Hips]{"entity": "muscle", "role": "waist", "value": "Obliques"}
- [Side Waist]{"entity": "muscle", "role": "waist", "value": "Obliques"}
- [Quadratus Lumborum]{"entity": "muscle", "role": "waist", "value": "Obliques"}
- [Deep Low Back Lateral Flexor]{"entity": "muscle", "role": "waist", "value": "Obliques"}
- i choose [Erector Spinae]{"entity": "muscle", "role": "waist", "value": "ErectorSpinae"}

## intent:hips
- tell me [Gluteus Maximus]{"entity": "muscle", "role": "hips", "value": "GluteusMaximus"}
- [butt]{"entity": "muscle", "role": "hips", "value": "GluteusMaximus"}
- [Glutes]{"entity": "muscle", "role": "hips", "value": "GluteusMaximus"}
- [rear hips]{"entity": "muscle", "role": "hips", "value": "GluteusMaximus"}
- tell more about [Gluteus Medius]{"entity": "muscle", "role": "hips", "value": "HipAbductor"}
- [Hip Abductor]{"entity": "muscle", "role": "hips", "value": "HipAbductor"}
- [Gluteus Minimus]{"entity": "muscle", "role": "hips", "value": "HipAbductor"}
- [Tensor Fasciae Latae]{"entity": "muscle", "role": "hips", "value": "HipAbductor"}
- [Tensor Fasciae Femoris]{"entity": "muscle", "role": "hips", "value": "HipAbductor"}
- [Iliopsoas]{"entity": "muscle", "role": "hips", "value": "HipFlexors"}
- sure [hip flexors]{"entity": "muscle", "role": "hips", "value": "HipFlexors"} please
- [Sartorius]{"entity": "muscle", "role": "hips", "value": "HipFlexors"}
- [Rotator Hip]{"entity": "muscle", "role": "hips", "value": "HipExternalRotator"}
- [Hip External Rotators]{"entity": "muscle", "role": "hips", "value": "HipExternalRotator"}
- ok, i choose [sartorius]{"entity": "muscle", "role": "hips", "value": "HipFlexors"}

## intent:thighs
- How about [inner thigh]{"entity": "muscle", "role": "thighs", "value": "HipAdductors"}?
- [quadriceps]{"entity": "muscle", "role": "thighs", "value": "Quadriceps"}
- need to know [front  thigh]{"entity": "muscle", "role": "thighs", "value": "Quadriceps"}
- [Quads]{"entity": "muscle", "role": "thighs", "value": "Quadriceps"}
- [hamstrings]{"entity": "muscle", "role": "thighs", "value": "Hamstrings"}
- [rear thigh]{"entity": "muscle", "role": "thighs", "value": "Hamstrings"}
- [Gracilis]{"entity": "muscle", "role": "thighs", "value": "HipAdductors"}
- [Pectineus]{"entity": "muscle", "role": "thighs", "value": "HipAdductors"}
- [Adductors]{"entity": "muscle", "role": "thighs", "value": "HipAdductors"}

## intent:calves
- [gastrocnemius]{"entity": "muscle", "role": "calves", "value": "Gastrocnemius"}
- [soleus]{"entity": "muscle", "role": "calves", "value": "Soleus"}
- [Tibialis Anterior]{"entity": "muscle", "role": "calves", "value": "TibialisAnterior"}
- [Shin]{"entity": "muscle", "role": "calves", "value": "TibialisAnterior"}
- [Tibias]{"entity": "muscle", "role": "calves", "value": "TibialisAnterior"}
- [Tibialis Anticus]{"entity": "muscle", "role": "calves", "value": "TibialisAnterior"}

## intent:support
- Any [suggestion]{"entity": "suggest", "value": "Suggestion"}?
- Could you give me some [advice]{"entity": "suggest", "value": "Suggestion"}?
- Please [suggest]{"entity": "suggest", "value": "Suggestion"} some.
- Tell me some [idea]{"entity": "suggest", "value": "Suggestion"} please
- I have [no idea]{"entity": "suggest", "value": "Suggestion"} about this.
- Can you [recommend]{"entity": "suggest", "value": "Suggestion"} it?
- What do you [recommend]{"entity": "suggest", "value": "Suggestion"}?
- Give me some [recommendation]{"entity": "suggest", "value": "Suggestion"}. Thanks

## intent:query
- Can you tell me more?
- What do you have?
- What muscles in chest?
- how do I know what muscle on shoulder?
- tell me more please
- what muscle does hip have?
- Can you tell me what part do you have?
- what do you have

## synonym:BackGeneral
- middle back
- middle Trapezius
- mid Trapezius
- upper back
- Traps
- Lower Traps
- Lower Trapezius
- Rhomboids
- mid back

## synonym:Biceps
- Front Arm
- biceps
- Biceps Cubiti
- Biceps Brachii

## synonym:Brachialis
- brachialis
- Side Arm
- Lower Biceps

## synonym:Brachioradialis
- brachioradialis
- Upper outer Forearm
- Supinator longus

## synonym:DeltoidAnterior
- Front Shoulder
- Front Delts

## synonym:DeltoidLateral
- Side Shoulder
- Side Delts

## synonym:DeltoidPosterior
- Rear Shoulder
- Rear Delts

## synonym:ErectorSpinae
- Erector Spinae

## synonym:Gastrocnemius
- gastrocnemius

## synonym:GluteusMaximus
- Gluteus Maximus
- butt
- Glutes
- rear hips

## synonym:Hamstrings
- hamstrings
- rear thigh

## synonym:HipAbductor
- Gluteus Medius
- Hip Abductor
- Gluteus Minimus
- Tensor Fasciae Latae
- Tensor Fasciae Femoris

## synonym:HipAdductors
- inner thigh
- Gracilis
- Pectineus
- Adductors

## synonym:HipExternalRotator
- Rotator Hip
- Hip External Rotators

## synonym:HipFlexors
- Iliopsoas
- hip flexors
- Sartorius
- sartorius

## synonym:Infraspinatus
- infraspinatus
- Teres Minor

## synonym:LatissimusDorsi
- Latissimus Dorsi
- outer back
- Lats
- Lats little helper
- Teres Major

## synonym:Obliques
- obliques
- Upper Hips
- Side Waist
- Quadratus Lumborum
- Deep Low Back Lateral Flexor

## synonym:PectoralClavicular
- Clavicular
- upper chest

## synonym:PectoralSternal
- Pectoralis Major
- Sternal
- Lower Pecs
- lower chest
- Pectoralis
- Pectoralis Minor
- major chest

## synonym:Pronators
- pronators

## synonym:Quadriceps
- quadriceps
- front  thigh
- Quads
- front thigh

## synonym:RectusAbdominis
- belly waist
- Abdominal
- abs
- Rectus Abdominis

## synonym:SerratusAnterior
- Serratus Anterior
- Serratus Magnus

## synonym:Soleus
- soleus

## synonym:Subscapularis
- subscapularis

## synonym:Suggestion
- suggestion
- advice
- suggest
- idea
- no idea
- recommend
- recommendation

## synonym:Supinators
- supinators

## synonym:Supraspinatus
- Rotatory Cuff

## synonym:TibialisAnterior
- Tibialis Anterior
- Shin
- Tibias
- Tibialis Anticus

## synonym:Transverse
- Transverse Abdominis
- Transverse Abs

## synonym:TrapeziusUpper
- upper trapezius
- Upper Traps
- Upper Shoulder
- Levator Scapulae
- upper shoulder

## synonym:Triceps
- Rear Arm
- triceps
- Triceps Brachii

## synonym:WristExtensors
- Wrist Extensors
- Hand Extensors
- outer Forearm
- back Forearm

## synonym:WristFlexors
- Wrist Flexors
- Inner Forearm
- Hand Flexors

## synonym:back
- BACK

## synonym:calves
- calf

## synonym:chest
- Chest

## synonym:forearms
- fore arms
- Forearm

## synonym:hips
- hip

## synonym:neck
- Neck

## synonym:no
- nope
- nah
- uhuh

## synonym:shoulder
- shoulders
- Shoulder

## synonym:smith
- smith machine

## synonym:splenius
- Splenius
- rear neck
- Neck Extensor

## synonym:sternocleidomastoid
- Sternocleidomastoid
- front neck
- side neck
- Neck Flexor
- Sterno mastoid

## synonym:thighs
- Thighs
- leg
- thigh

## synonym:upperarms
- upper arms
- arm

## synonym:waist
- Waist
