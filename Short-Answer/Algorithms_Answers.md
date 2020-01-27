#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear O(n) time. Since the input of 'a' isn't changing, as you increase the input 'n', the time complexity & loops required for this program will increase at the same rate as 'n'.


b) Linearithmic O(n log n) time. This one's tricky b/c it looks like it might be O(n) time- b/c the program still runs through every number in range(n). But for each iteration of n it still has to run the while loop, doubling j each time, so there's a log element to add to the time complexity here.


c) Linear O(n) time. As the input 'bunnies' grows, the # of times we run bunnyEars grows at the same rate (since 'bunnies' only decreases by 1 each time).

## Exercise II

I mean thinking about this from the smallest # of broken eggs...0....the best case is where floor f = the top floor of the building. 

So I'm not sure if this is allowed but it's simplest to just write a program where f = len(building) (assuming the 'building' is a list of floors, last entry being the top floor). That way, an egg dropped from any floor will not break no matter what, by definition, unless it's thrown from the very top floor.

In which case, runtime complexity would be constant time O(1) because f = len(building) is just a variable assignment. If the program throws eggs off the building, I'd loop through list(eggs) to throw from a random floor, in which case the program complexity would change to O(n) for every entry in list(eggs).