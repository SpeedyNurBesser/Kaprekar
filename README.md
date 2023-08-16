# KaprekarGraphView
 A little script designed to show the Kaprekar's constant in a graph view

This python code creates 10.000 markdown files with a link to the number you get, if you follow Kaprekar's routine (see beneath). I create markdown files to look at them in [Obsidian](obsidian.md)'s graph view that is really fancy and links files that reference each other.


Explanation:
---
 Do you know about Kaprekar's constant? If you don't, it's 6174.

 6174? Yes, 6174 is Kaprekar's constant.

 Kaprekar's constant is a special number, because...

 

If you take any 4 digit number, other than numbers which only have the same digit like 3333, and with it follow Kaprekar's routine you will after a few cycles definitely get 6174.

If you wonder what Kaprekar's routine is, it's the following:


Kaprekar's routine goes as following:

1. Take a number, any number, and sort the single digits by value.

So if you have 5832 for example, you get 2358, if you sort small to big, or 8532, if you sort big to small.

2. Then subtract the small number from the big number (e.g. 8532 - 2358).

(3. If the initial number was a 4 digit number and you haven't instanteneously got 6174, repeat.)
