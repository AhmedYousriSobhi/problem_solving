# HACKER RANK
## PRoblem: Employee Salaries
Class: Easy

Source: https://www.hackerrank.com/challenges/salary-of-employees/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

## Description
Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than $2000 per month who have been employees for less than 10 months. Sort your result by ascending employee_id.

Input Format

The Employee table containing employee data for a company is described as follows: 

![image](https://s3.amazonaws.com/hr-challenge-images/19629/1458557872-4396838885-ScreenShot2016-03-21at4.27.13PM.png)

where employee_id is an employee's ID number, name is their name, months is the total number of months they've been working for the company, and salary is their monthly salary.

## Example
![example](https://s3.amazonaws.com/hr-challenge-images/19630/1458558612-af3da3ceb7-ScreenShot2016-03-21at4.32.59PM.png)

Sample Output
```
Angela
Michael
Todd
Joe
```
Explanation
- Angela has been an employee for 1 month and earns $3443 per month.
- Michael has been an employee for 6 months and earns $2017 per month.
- Todd has been an employee for 6 months and earns $3396 per month.
- Joe has been an employee for 9 months and earns $3573 per month.
- We order our output by ascending employee_id.
