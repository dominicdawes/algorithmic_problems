# Hops
#### Level 2
A family of frogs in a pond are traveling towards dry land to hibernate. They hope to do so by hopping across a trail of 
N lily pads, numbered from 
1
1 to N in order.
There are F frogs, numbered from 
1
1 to F. Frog i is currently perched atop lily pad P_i. No two frogs are currently on the same lily pad. Lily pad 
N is right next to the shore, and none of the frogs are initially on lily pad N.
Each second, one frog may hop along the trail towards lily pad N. When a frog hops, it moves to the nearest lily pad 
after its current lily pad which is not currently occupied by another frog (hopping over any other frogs on intermediate 
lily pads along the way). If this causes it to reach lily pad N, it will immediately exit onto the shore. Multiple 
frogs may not simultaneously hop during the same second.
Assuming the frogs work together optimally when deciding which frog should hop during each second, determine the minimum number 
of seconds required for all F of them to reach the shore.

### Constraints
2≤N≤10 
1≤F≤500,000
1≤P_i ≤N−1

## Sample test case #1
N = 3
F = 1
P = [1]
Expected Return Value = 2
## Sample test case #2
N = 6
F = 3
P = [5, 2, 4]
Expected Return Value = 4

## Sample Explanation
In the first case, there are 
3
3 lily pads and 
1
1 frog. The frog is initially atop lily pad 
1
1 and will take 
2
2 hops to reach lily pad 
3
3.
In the second case, there are 
6
6 lily pads, with frogs on lily pads 
5
5, 
2
2, and 
4
4. Initially the lily pads and frog numbers can be represented as .2.31.
One optimal sequence of hops is:
Frog 
2
2 hops forward to lily pad 
3
3: 
..231.
Frog 
2
2 hops over frogs 
1
1 and 
3
3, onto lily pad 
6
6 and exiting onto the shore: 
...31.
Frog 
3
3 hops over frog 
1
1, onto lily pad 
6
6 and exiting onto the shore: 
....1.
Frog 
1
1 hops onto lily pad 
6
6, exiting onto the shore.

# Answer
Turns out you can solve this with a simple one-liner (though it takes a little while to explain why). Ultimately the formula is deceptively simple: N - min(P). Working backwards from that, though, the original verbose formula is: F + (N - F - 1) - (min(P) - 1).

The first part - F + - is because once you get all the frogs lined up at the end, each one takes one second to hop off.

The second part - N - F - 1 - answers the question of "how many empty lily pads are there?" The best solution is that every second, a frog is hopping to an empty pad, so we need to find out how many empty pads will be hopped to at the end. That works out to the total number of pads (N), less the number of frogs occupying pads (F), less 1 (the final pad which is never really occupied anyway).

The final part - min(P) - 1 makes more sense if you look at this in terms of an array. For example, you might have N = 7, F = 2, and P = [3, 5]. If you were to draw it out, your pond would look like this:
[ . . A . B . . ]
N-F-1 in this case is 4, telling us that there are four empty lily pads (excluding the final): [1, 2, 4, 6]. But no one's hopping backwards, so we can drop the first two empty pads by finding the minimum of P and subtracting 1 (in this example, 3 - 1 = 2 so we drop the first two pads, and our list of empty and eligible pads drops to [4, 6]).

Putting it all together, it'll take two seconds to collapse the frogs to the right of the list (frog A moves from 3 to 4 in the 1st second, and then hops over frog B in the 2nd second, leaving you with [. . . . B A .], and then it takes two more seconds for both to jump to shore (frog B jumps over A, then frog A goes to shore). But don't get bogged down in which frog moves where because ultimately (and weirdly) it doesn't really matter how many frogs there are, only how many pads there are and where the farthest frog from shore is located. The actual math factors out the number of frogs from the equation, which feels odd to me...but on further reflection, if you don't think of which specific frog is on which specific pad and how the frog can jump, and look at it in terms of how long it takes to make the leftmost occupied lily pad to be the last one, it makes more sense (ie. don't think of it in terms of [. . A . B . ] but in terms of [. . x . x .] => [. . . x x .] => [. . . . x x] => [. . . . . x] => [. . . . . .]). Anyway, to the code...
