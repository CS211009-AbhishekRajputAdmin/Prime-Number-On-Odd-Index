# Title: Find the Maximum Prime Number at Odd Index Positions

# Description:
You are given an array of numbers, and your task is to write a program or function that finds and returns the index of the largest prime number occurring at odd index positions within the array. The prime number should be selected from all the prime numbers present in the array. If the prime number is not found the print -1.

Here are the specific requirements for your solution:

## 1. Input:
   - You will be given an array of integers, the array can be empty if the it is empty then print -1 .

## 2. Prime Number:
   - A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.

## 3. Odd Index Positions:
   - Consider the array indices starting from 0.
   - Only consider prime numbers that are present at odd index positions (1, 3, 5, etc.).

## 4. Maximum Prime Number:
   - Identify the largest prime number among those found at odd index positions.

## 5. Output:
   - Return the index of the maximum prime number within the odd-indexed elements of the array.

## Example:
```python
Input: [4, 6, 11, 7, 9, 13, 10, 17]
Output: 5
Explanation: 
   - The prime numbers at odd index positions are [11, 7, 13, 17].
   - The largest prime number is 17, which is at index 5.
   - Therefore, the function should return 5 as the result.
```

Please implement a solution that adheres to these requirements and efficiently finds the desired result.

  



