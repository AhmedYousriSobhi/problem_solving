# HACKER RANK
## Problem: The Blunder
Class: Easy

Source: https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true

## Description
Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's

key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

## To Do
Write a query calculating the amount of error (i.e.:

average monthly salaries), and round it up to the next integer.

Input Format

The EMPLOYEES table is described as follows:

![image](https://s3.amazonaws.com/hr-challenge-images/12893/1443817108-adc2235c81-1.png)

Note: Salary is per month.

Constrains:
- 1000 < Salary < 10^5

## Example
Input

![image](https://s3.amazonaws.com/hr-challenge-images/12893/1443817161-299cc6eb7f-2.png)

Output
- 2061

Explanation
- The table below shows the salaries without zeros as they were entered by Samantha:

![Image](https://s3.amazonaws.com/hr-challenge-images/12893/1443817229-eb00d44a3b-3.png)

Samantha computes an average salary of . The actual average salary is 2159.00.

The resulting error between the two calculations is 2159.00 - 98.00 = 2061.00. Since it is equal to the integer , it does not get rounded up. 
