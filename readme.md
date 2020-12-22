# The Advent Of Code

I'm about to launch into some data processing at work with pandas and I haven't properly used python in *ages*, so I'm going to use this to get refreshed with the world of python.

### Day 1:
Ok after enthusiastically setting off on this one, I regret the pandas decision - would have been much better with recursion. Blimey. Although, it seems to be a common theme online that people pick inappropriate tech and force themselves to solve it with that. Eg. Excel. 

### Day 2:
Reflection - regex on string splitting is too complicated 
Didn't know about line.partition - could have been useful here, regex was probably too complex
Hacky outer scope array manipulation, this is very javascripty, but not possible in python
Maybe just read whole file in as a list, not really concerned about stream

### Day 3:
Really enjoyed this one, who doesn't love the concept of a lil' toboggan smashing into trees at high speed?
I felt this required just understanding the problem and nothing too challenging on the python side which was nice.

### Day 4:
I'm glad I did this one infront of the TV with Die Hard on in the background and with a lil' bit of mulled wine (festive right?). If I hadn't, I would have been focusing too much on how thoroughly tedious it is to be given a festive task that is essentially "Write a form validator". 
Viva La Regex.

### Day 5:
Honestly, day 4 put me off a bit, so took a break. Fingers crossed they stay a bit funner like 1-3. 
I was quite happy with the approach to part 1: break down into Binary and find the highest id. 
I also decided to try out a bit of pytest! TDD bébé.
Scanning online, looks like you could condense what I wrote into 2 lines of chained function calls. Who needs readability? It's like codewars all over again.

### Day 6:
It's at this point I begin to feel a bit concerned for our protagonist, lets call them Deboran.
Deboran spends *yet another day* in an airpot obsessing over another airport related logistical nightmare. 
I'm beginning to worry Deboran is a bit of a hyper altruistic walkover, drifting through life, loved by many but subject to exploitation. Are the airport staff crossing lines here? Are they asking too much? How long is it until Deboran overstreches and emotionally implodes into a maelstrom of resentment and bitterness? 
Additionally, after working through such a long task, to not read the original instructions properly would be crippling. Step it up Deboran

Concerns about the storylines aside, I enjoyed this one.
I took the opportunity to look into pytest and work out:
- mocking of file inputs so I can have the test cases inline rather than in a separate file
- parameterisation of tests so I can try out a variety of cases with less boiler plate.

Haven't used sets in python before, thought they worked quite well for part 1

### Day 7:
Absolutely can't catch a break, what an obtuse baggage handling system. After this, I'm wondering if the airline is actually a front for the biggest.
We're in the poles,
And impractical

I'm going to d
I'd like to take this a bit seriously and properly consider the implications of such an obtuse baggage handling policy. 

Lets say a bag search takes about 30s per bag, for a thorough search

Going to drop some spoilers here. To take a shiny gold bag on you need 9569 other bags inside the 

```
Apparently, nobody responsible for these regulations considered how long they would take to enforce!
```



A regular suitcase 

### Day 8:
It's nice to know that the airline can at least get its bread and butter right, ie, flying. Honestly, after all the decisions about boarding, passports and infinite bags I was slightly worried Deboran would never leave. We discover that Deboran is partial to a drink with a bit of *pizazz*. Probably needs it after all these mishaps.
There's a weak plot point in that we're not sure how Deboran is able to get the text file from the Kid's console but we'll gloss over that.
Today, Deboran fixes a kid's handhold console by looking at some boot code.

This was a good one. 
I stumbled a bit with part 2 because I tried to do it all within one loop. But really there's two loop concepts.
1) The outer loop which is running through the broken program.
2) When you hit a nop or a jmp and then loop through the program using a potential fix

It's possible to do it with one loop but you add if statements and need to be aware if you're exploring a potential fix or just iterating through the broken program.
It was much more sensible (and leant on the code you'd written in part one) to simply step through the original program and then explore if fixing a line makes the program exit, if it doesn't then keep stepping through.

Other mistakes I made were to mutate the the operations data structure to store the visited state as you might in a large tree. But because there's lots of potential pathways if you mutate state you have to reset state. Using a new empty set when exploring if a fix works was more effective. 
