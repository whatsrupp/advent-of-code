# The Advent Of Code

I'm about to launch into some data processing at work with pandas and I haven't properly used python in *ages*, so I'm going to use this to get refreshed with the world of python.

I started off writing notes on each task here, pitfalls pros and cons. But I started putting them by the code for context.
Instead, I was struck by just how insane the plot line is of this years calendar.
I'll be writing down what I discover about our protagonist, who I have chosen to call Deboran as we go.

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
Absolutely can't catch a break, what an obtuse baggage handling system. After this, I'm wondering if the airline is actually a front for a fraudulent suitcase upselling scheme.

- points to explore
- How much would all these bags weigh
- How much would they cost
- How long would they take to search and pack
- How much space would they take up


### Day 8:
It's nice to know that the airline can at least get its bread and butter right, ie, flying. Honestly, after all the decisions about boarding, passports and infinite bags I was slightly worried Deboran would never leave. We discover that Deboran is partial to a drink with a bit of *pizazz*. Probably needs it after all these mishaps.
There's a weak plot point in that we're not sure how Deboran is able to get the text file from the Kid's console or how the kid knows that Deboran will fix the boot code of the games console. But we'll gloss over that.


### Day 9
It's here that we begin to see the cracks start to show in sweet benevolent Deboran's morals.
Not content with the small rebellious buzz you get from taking your phone out of airplane mode mid air, Deboran is wiring themselves into the plane mainframe and sniffing away at those sweet sweet festive data packets.
All with two paperclips too. We know at this stage of Deboran's infinite resourcefulness so the paperclips are to be expected. But, until now, Deboran hasn't been autonomous. They've been at the beck and call of others. The first time they have a bit of space for themselves, they hack into a plane. That's a bit suspicious don't you agree?


### Day 10
We all know the international plug adapter scene is a bit chaotic. 
But blimey. Bringing 104 different adapters on one trip. Just for one miscellaneous "device".
Lets hope they have storage space to store all tho...
Wait. 
Lets not forget. THE 9569 BAGS being hauled around inside of the gold shiny bag from task 7. Great no storage issues here.

Assuming plugs of 40x40x20mm weighing in at 50g. That's looking at 5.2L of storage and 5kg of weight.
The best image from this task has got to be the ridiculous 2m tall staff of joltage adaptors that Deboran has to assemble just to charge their gear.  At least we know a Deboran is consistent. Carrying around inane amounts of junk is a mainstay and not just a one off because of airport baggage regulations.






