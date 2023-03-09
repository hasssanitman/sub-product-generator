<h2>The Challenge</h2>

Imagine that you have an indefinite number of arrays in a colletion, each of which has an indefinite length.
Now you want to get a new collection of arrays, each value of which is a combination of the values of the original collection so that none of the items are duplicates.

Depending on the platform of your application, these collection may be obtained in different ways.
For example, in the web environment, you may receive this data from the user through HTML forms and you want to perform the combination operation with Javascript.

Imagine you have an collection as follows:
The first item is color, the second array is size and the third array is sleeve type.

This is the format:

[

    {
        property: 'color',
        values: ['red', 'green', 'blue']
    },

    {
        property: 'size',
        values: ['small', 'medium', 'large', 'x-large']
    },

    {
        property: 'sleeve',
        values: ['short-sleeve', 'long-sleeve']
    },

]

And you expect to get a result similar to the array below:

{

    ['red', 'small', 'short-sleeve'],

    ['red', 'small', 'long-sleeve'],

    ['red', 'medium', 'short-sleeve'],

    ['red', 'medium', 'long-sleeve'],

    .
    .
    .

    ['blue', 'large', 'short-sleeve'],

    ['blue', 'large', 'long-sleeve'],

    ['blue', 'x-large', 'short-sleeve'],

    ['blue', 'x-large', 'long-sleeve'],

}

<h2>The Old Solution</h2>

First you have to count the number of different modes.
The formola is this:

array1.lenght _ array2.lenght _ ...... arrayN.lenght

In our case it's 24

color.length _ size.length _ sleeve.length

      3      *      4      *       2      = 24

total_number_of_quality = 24

Then you must create an array that has the number of empty array items obtained. In this example, 24 empty arrays in one array.

After that, you have to make a loop from the main array.

Note: You need three counters:

"where" to count the result array.

"round_of_game" To count the number of repetitions of each item.

"counter" To count the number of repetitions of the item in each round of "round_of_game".

In each execution of the loop, you have a property that contains values.

Check if the values exist then calculate the value of the other 2 counters (counter and round_of_game).

The counter indicates how many times a value should be printed in each round. It's amount is obtained according to this formula:

counter = last_qulity_counter / [length of vals]

round_of_game indicates how many rounds each value should be printed. And its amount is obtained according to this formula:

round_of_game = total_number_of_quality / (counter \* [length of vals])

Now you need to create a loop that runs as long as the round_of_game and prints the values as many counters in each run.

After that the last_qulity_counter must be cahnge to the counter value, and the where value reset to 0.

NOTE: The value of the "counter" and "round-of-game" depends on the value of the previous counter round, and each time the main loop (color, size, sleeve) is executed their value changes.

<h2>The New Solution</h2>
