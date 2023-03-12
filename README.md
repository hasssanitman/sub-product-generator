# Usage

First, clone the project with the following command:
```bash
git clone https://github.com/hasssanitman/sub-product-generator.git
```
Then enter the project directory. and enter the following command:

```bash
python main.py
```

# Challenge

Imagine that you have an unspecified number of arrays in set (A), each of which has an unspecified number of items. And you want to have a new collection (B) of arrays that are a combination of the items of the arrays of collection (A).

There are 2 rules here:

1. Each of the resulting arrays must be unique.
2. The difference in the order of the items of two similar arrays cannot make them unique.


### Example

In one of the projects called [Carbon](https://www.hasssanitman.ir/casestudy/carbon.html "Carbon") (an online store builder), we mostly focused on clothing stores. A product might have different features, based on the price, the number of stock in stock, and different discounts.

For example, a blouse may have different features, each of which has its own conditions for sale.

| Model           | Features(color,size,sleeve) | Price | In-Stock    |
|-----------------|-----------------------------|-------|-------------|
| Blouse-Model X  | Red - Small - Long          | 50$   | 10          |
| Blouse-Model X  | Red - Small - Short         | 49$   | Out of Stock|   
| Blouse-Model X  | Green - Large - Short       | 55$   | 20          |   
| Blouse-Model X  | Red - X-large - Long        | 69$   | 8           |   

If the number of arrays of set A and their items are always known, it will be much easier to solve the problem. But here we are talking about a situation where we do not know how much data the user enters each time!

It is possible that a certain model t-shirt has only two characteristics, color, and size, and it is also monochromatic!

If the store manager tries to manually enter a large number of values every time, there will definitely be a mistake in entering the information. And it may have very bad consequences.

# Solution

I coded in JavaScript in the [Carbon](https://www.hasssanitman.ir/casestudy/carbon.html "Carbon") project, but here I rewrote it in Python.
You have a set as follows:

The first array is the color, the second array is the size, and the third array is the sleeve type.

with the following format:

```
[
    {
        property: 'Color',
        values: ['Red', 'Green', 'Blue']
    },
    {
        property: 'Size',
        values: ['Small', 'Medium', 'Large', 'X-large']
    },
    {
        property: 'Sleeve',
        values: ['Short-Sleeve', 'Long-Sleeve']
    },
]
```
And you expect to get a result similar to the array below:

```
{
    ['Red', 'Small', 'Short-Sleeve'],
    ['Red', 'Small', 'Long-Sleeve'],
    ['Red', 'Medium', 'Short-Sleeve'],
    ['Red', 'Medium', 'Long-Sleeve'],
    ['Red', 'Large', 'Short-Sleeve'],
    ['Red', 'Large', 'Long-Sleeve'],
    ['Red', 'X-large', 'Short-Sleeve'],
    ['Red', 'X-large', 'Long-Sleeve'],
    ['Green', 'Small', 'Short-Sleeve'],
    ['Green', 'Small', 'Long-Sleeve'],
    ['Green', 'Medium', 'Short-Sleeve'],
    ['Green', 'Medium', 'Long-Sleeve'],
    ['Green', 'Large', 'Short-Sleeve'],
    ['Green', 'Large', 'Long-Sleeve'],
    ['Green', 'X-large', 'Short-Sleeve'],
    ['Green', 'X-large', 'Long-Sleeve'],
    ['Blue', 'Small', 'Short-Sleeve'],
    ['Blue', 'Small', 'Long-Sleeve'],
    ['Blue', 'Medium', 'Short-Sleeve'],
    ['Blue', 'Medium', 'Long-Sleeve'],
    ['Blue', 'Large', 'Short-Sleeve'],
    ['Blue', 'Large', 'Long-Sleeve'],
    ['Blue', 'X-large', 'Short-Sleeve'],
    ['Blue', 'X-large', 'Long-Sleeve'],
}
```

I found a solution to this problem, and I was able to implement it in two ways. **Column** and **Row**


Column implementation is really a disaster!
But Row has a much better algorithm.

Here I put the main solution. Then you can read the codes of both methods.
Pay attention to the image below:

![image](https://raw.githubusercontent.com/hasssanitman/sub-product-generator/master/sub_products.png)

As you can see, the most important point of this algorithm is the correct calculation of `counter` and `round` values.

We have a variable called `last_counter` whose initial value is equal to the value of the `total_sub_products`.

But after the execution of the first loop, its value is equal to the `counter` value of the previous array!
And based on this value, the `round` value is calculated correctly.


