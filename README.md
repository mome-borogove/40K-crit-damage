# How Criticals Work in 40K: Inquisitor

Critical damage in Warhammer 40K: Inquisitor - Martyr is a bit different than most systems.
Instead of a straight multiplier, there's an extra level of indirection.
While this has advantages (crits have a much wider range which can "feel" more exciting, and it smoothly caps the crit multiplier), it also confuses new players often.

Let's start with making sure we're all on the same page. Here's how criticals work in 40K: Inquisitor:

![How Crits Work](how-crits-work.svg)

When an attack crits, the game internally rolls a random value from 1 to 100, adds your **critical strength** score, then looks up the value in a table.
It takes the result as your initial critical multiplier, then adds any **critical damage** from your gear and skills, and uses that as the final multiplier for your normal attack damage.

## Critical strength versus critical damage

This simple script visualizes what "critical strength" means in terms of critical damage.
In other words, it derives the average multiplier over all possible random numbers the game could roll (1&ndash;100) and then translates that into the equivalent amount of critical damage you would need to get the same outcome.
Note: as described above, critical strength and critical damage work together to increase your damage, so this experiment is really about choosing between the two when there is a direct conflict.
For instance, an artifact-rarity (purple) signum can have a critical strength or critical damage primary enchant, *but not both*.
You have to choose one or the other.
These plots help to visualize that tradeoff.
To reiterate, though, it is always good to get both critical strength and critical damage when possible.

The first plot shows the average critical damage you can expect with a given amount of critical strength on your gear.

![Equivalent critical damage](Equivalent_crit_damage.png)

The second plot shows how much a single additional point of critical strength is assuming you already have a given amount.

Note: As of v2.3.0, the critical damage per point of critical strength plot is a bit wonky. This isn't a bug, it's a result of inconsistently-sized intervals in the critical strength table. The good news is that you can basically ignore the hiccup in the middle: there's essentially no scenario in which it makes sense to change your gear for that little window.

![Critical damage per strength point](Critical_damage_per_strength.png)

## Parting note

Remember that in any ARPG, stats can be strong or weak, but their availability also impacts choices on what to wear.
In the case of 40K: Inquisitor, primary enchants for critical strength generally have less points than primary enchants for critical damage.
This means that while an item might be able to roll 15% critical damage, it can only roll only 10 points of critical strength.
So even if 1 point of critical strength is worth 1.5% critical damage, the value of the *available* enchants on the items might be the same or even reversed.
This also means that if you can get critical strength or critical damage in a place where you cannot get the other, it's generally worthwhile to do so, because that means you can choose the more valuable one in places where you are forced to make that call.
