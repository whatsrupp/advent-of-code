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

