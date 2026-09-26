"""
Module 2 — Lesson 3: Loops & Lists
Student: Calayag, Edward P.
Date: 09/26/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]
In programming, a loop is way to repeat and make the code more efficient. 
Like a literal loop, that goes around and around, as long as the condition is always True, 
it will keep repeating the code inside the loop.
However, Lists is a group of data that been stored (weather it's the user or the programmer), 
in simple words, it's like a container that can hold multiple data types.

============================================
KEY VOCABULARY
============================================
- list: a collection of data that can hold multiple data types. 
- for loop: a loop that keeps repeating the code inside the loop until the condition is False or didn't met the right condition. 
            But it can be possible that the loop will not stop, if the logic or condition is not properly set, so it end up eating up
            your computer's memory and will eventually crash your computer.
- while loop: is also a loop that also repeats the code inside the block until the condition is False. 
              However, it is different from the "for loop" because it doesn't have a specific number of loop, 
              it depends on the condition that you set. But it can also be possible that the would not stop, 
              so it will eat up your computer's memory.
- index: is a method where you can specify the data that you want to be print out. 
         But always remember that when you type the number position of a value inside the list; it's always starts from 0 
         and it counts from left to right.
- iteration: is a process of repeatedly accessing the elements of a itterable value; like the numbers, string one at a time.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
list = ["Apple", "Banana", "Orange"]
print(list[0]) # Output: Apple

for i in list:
    print(list) # Loop 3 times (3 Iterations)

count = 0
while count < 3: # Counts from 0 - 2
    print(count)
    count +=1
# --- your code example goes here ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]
In my experience, I always forgot the difference between those 2 loops (for/while), 
and use them not knowing what's their functions and purpose.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""