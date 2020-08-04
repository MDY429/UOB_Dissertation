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
- [shoulder](body) exercise
- How to train neck(body)?
- [BACK]{"entity": "body", "value": "back"} training!!
- oh, how about [back](body) training?
- I would like to know about [waist](body).
- [hips](body) thanks.
- [Thigh]{"entity": "body", "value": "thighs"} training
- [Thighs]{"entity": "body", "value": "thighs"}
- of course is [calves](body)
- tell me about [deltoid](body)
- want more about [shoulder](body) exercise
- May I know about [leg]{"entity": "body", "value": "thighs"} exercise?
- my [arm]{"entity": "body", "value": "upperarms"}
- [arms]{"entity": "body", "value": "upperarms"}
- [Upper arms]{"entity": "body", "value": "upperarms"}
- [upper arm]{"entity": "body", "value": "upperarms"}
- tell me about [calf]{"entity": "body", "value": "calves"} training
- [Forearm]{"entity": "body", "value": "forearms"}
- [fore arms]{"entity": "body", "value": "forearms"}
- [fore arm]{"entity": "body", "value": "forearms"}
- [Neck]{"entity": "body", "value": "neck"}
- [Shoulder]{"entity": "body", "value": "shoulder"}
- [Chest]{"entity": "body", "value": "chest"}
- [Waist]{"entity": "body", "value": "waist"}
- How about [hip]{"entity": "body", "value": "hips"}?
- Any about [thigh]{"entity": "body", "value": "thighs"}?
- tell me some about [hips](body)
- i wanna know some [shoulder](body) exercise
- [shoulders]{"entity": "body", "value": "shoulder"}
- i wonder know about [back](body) exercise
- [back](body)
- Any good for [legs]{"entity": "body", "value": "thighs"}
- [chest](body) please
- Oops, I change to [forearms](body).
- alright, change my mind again, [legs]{"entity": "body", "value": "thighs"}!!

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
- any with [cable](facility)?
- [Barbell]{"entity": "facility", "value": "barbell"}
- [Cable]{"entity": "facility", "value": "cable"}
- [Dumbbell]{"entity": "facility", "value": "dumbbell"}
- [Smith]{"entity": "facility", "value": "smith"}
- [Lever]{"entity": "facility", "value": "lever"}
- [Suspended]{"entity": "facility", "value": "suspended"}
- [BodyWeight]{"entity": "facility", "value": "bodyweight"}
- [Body Weight]{"entity": "facility", "value": "bodyweight"}
- [body weight]{"entity": "facility", "value": "bodyweight"}
- [Sled]{"entity": "facility", "value": "sled"}
- [Weight]{"entity": "facility", "value": "weight"}
- [weight](facility)
- [Band]{"entity": "facility", "value": "band"} Resistive
- [Assisted]{"entity": "facility", "value": "assisted"}
- [TrapBar]{"entity": "facility", "value": "trapbar"}
- [SafetyBarbell]{"entity": "facility", "value": "safetybarbell"}
- [MedicineBall]{"entity": "facility", "value": "medicineball"}
- [Medicine Ball]{"entity": "facility", "value": "medicineball"}
- [medicine ball]{"entity": "facility", "value": "medicineball"}
- [medicineball](facility)
- [sled](facility)

## intent:negative
- [no](deny)!!
- [no](deny) need
- [nope]{"entity": "deny", "value": "no"}!
- [no](deny) thanks
- [no](deny) thank you
- [nah]{"entity": "deny", "value": "no"}
- [uhuh]{"entity": "deny", "value": "no"}
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
- [Anterior Shoulder]{"entity": "muscle", "role": "shoulder", "value": "DeltoidAnterior"}
- [Side Shoulder]{"entity": "muscle", "role": "shoulder", "value": "DeltoidLateral"}
- [Side Delts]{"entity": "muscle", "role": "shoulder", "value": "DeltoidLateral"}
- [Lateral Shoulder]{"entity": "muscle", "role": "shoulder", "value": "DeltoidLateral"}
- [Rear Shoulder]{"entity": "muscle", "role": "shoulder", "value": "DeltoidPosterior"}
- [Rear Delts]{"entity": "muscle", "role": "shoulder", "value": "DeltoidPosterior"}
- [Posterior Shoulder]{"entity": "muscle", "role": "shoulder", "value": "DeltoidPosterior"}
- [Rotatory Cuff]{"entity": "muscle", "role": "shoulder", "value": "Supraspinatus"}
- [front shoulder]{"entity": "muscle", "role": "shoulder", "value": "DeltoidAnterior"}
- thanks, how about [anterior shoulder]{"entity": "muscle", "role": "shoulder", "value": "DeltoidAnterior"}?

## intent:upperarms
- [Rear Arm]{"entity": "muscle", "role": "upperarms", "value": "Triceps"} please
- well [triceps]{"entity": "muscle", "role": "upperarms", "value": "Triceps"}
- [Front Arm]{"entity": "muscle", "role": "upperarms", "value": "Biceps"}
- yes! [biceps]{"entity": "muscle", "role": "upperarms", "value": "Biceps"} please
- [Biceps Cubiti]{"entity": "muscle", "role": "upperarms", "value": "Biceps"}
- [Triceps Brachii]{"entity": "muscle", "role": "upperarms", "value": "Triceps"}
- [Biceps Brachii]{"entity": "muscle", "role": "upperarms", "value": "Biceps"}
- [brachialis]{"entity": "muscle", "role": "upperarms", "value": "Brachialis"}
- [Side Arm]{"entity": "muscle", "role": "upperarms", "value": "Brachialis"}
- [Lower Biceps]{"entity": "muscle", "role": "upperarms", "value": "Brachialis"}

## intent:forearms
- [supinators]{"entity": "muscle", "role": "forearms", "value": "Supinators"}
- [brachioradialis]{"entity": "muscle", "role": "forearms", "value": "Brachioradialis"}
- [Upper outer Forearm]{"entity": "muscle", "role": "forearms", "value": "Brachioradialis"}
- [Supinator longus]{"entity": "muscle", "role": "forearms", "value": "Brachioradialis"}
- [Wrist Flexors]{"entity": "muscle", "role": "forearms", "value": "WristFlexors"}
- [Inner Forearm]{"entity": "muscle", "role": "forearms", "value": "WristFlexors"}
- [Hand Flexors]{"entity": "muscle", "role": "forearms", "value": "WristFlexors"}
- [Wrist Extensors]{"entity": "muscle", "role": "forearms", "value": "WristExtensors"}
- [Hand Extensors]{"entity": "muscle", "role": "forearms", "value": "WristExtensors"}
- [outer Forearm]{"entity": "muscle", "role": "forearms", "value": "WristExtensors"}
- [back Forearm]{"entity": "muscle", "role": "forearms", "value": "WristExtensors"}
- [pronators]{"entity": "muscle", "role": "forearms", "value": "Pronators"}

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
- nice, i want to know [upper trapezius]{"entity": "muscle", "role": "back", "value": "TrapeziusUpper"}

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
- wow nice i want to choose [cable](facility)
- This time, i want to know more about [abs]{"entity": "waist", "value": "RectusAbdominis"}

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
- [Abductors]{"entity": "muscle", "role": "hips", "value": "HipAbductor"}

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
- oh, sorry, tell me [rear thigh]{"entity": "muscle", "role": "thighs", "value": "Hamstrings"}
- change minde again! want to know [quadriceps]{"entity": "muscle", "role": "thighs", "value": "Quadriceps"}

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
- any [advice]{"entity": "suggest", "value": "Suggestion"}?
- I need an [example]{"entity": "suggest", "value": "Suggestion"}
- [suggest]{"entity": "suggest", "value": "Suggestion"}
- [Suggest]{"entity": "suggest", "value": "Suggestion"}
- any
- Any good?
- Whatever
- just tell me some
- i have no [idea]{"entity": "suggest", "value": "Suggestion"}
- [advise]{"entity": "suggest", "value": "Suggestion"} me
- [introduce]{"entity": "suggest", "value": "Suggestion"}
- any [suggestion]{"entity": "suggest", "value": "Suggestion"}?

## intent:query
- HELP
- help!!!
- Help please
- Can you help me?
- Can you tell me more?
- What do you have?
- What muscles in chest?
- how do I know what muscle on shoulder?
- tell me more please
- what muscle does hip have?
- Can you tell me what part do you have?
- what do you have
- what do you have?
- cool, what does it have?
- oh what does it have?
- help
- what body exercise do you have?
- what are them?

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
- Anterior Shoulder
- front shoulder
- anterior shoulder

## synonym:DeltoidLateral
- Side Shoulder
- Side Delts
- Lateral Shoulder

## synonym:DeltoidPosterior
- Rear Shoulder
- Rear Delts
- Posterior Shoulder

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
- Abductors

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
- example
- Suggest
- advise
- introduce

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

## synonym:assisted
- Assisted

## synonym:back
- BACK

## synonym:band
- Band

## synonym:barbell
- Barbell

## synonym:bodyweight
- BodyWeight
- Body Weight
- body weight

## synonym:cable
- Cable

## synonym:calves
- calf

## synonym:chest
- Chest

## synonym:dumbbell
- Dumbbell

## synonym:forearms
- fore arms
- Forearm
- fore arm

## synonym:hips
- hip

## synonym:lever
- Lever

## synonym:medicineball
- MedicineBall
- Medicine Ball
- medicine ball

## synonym:neck
- Neck

## synonym:no
- nope
- nah
- uhuh

## synonym:safetybarbell
- SafetyBarbell

## synonym:shoulder
- shoulders
- Shoulder

## synonym:sled
- Sled

## synonym:smith
- smith machine
- Smith

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

## synonym:suspended
- Suspended

## synonym:thighs
- Thigh
- Thighs
- leg
- thigh
- legs

## synonym:trapbar
- TrapBar

## synonym:upperarms
- upper arms
- arm
- arms
- Upper arms
- upper arm

## synonym:waist
- Waist

## synonym:weight
- Weight
