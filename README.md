The Challenge

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


The Solution

First you have to count the number of different modes.
The formola is this: array1.lenght * array2.lenght * ...... arrayN.lenght

In our case it's 24
color.length * size.length * sleeve.length
      3      *      4      *       2      = 24








