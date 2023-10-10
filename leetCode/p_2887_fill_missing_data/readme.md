# LEET CODE
## Problem-2887: Fill Missing Data
Class: Easy

Source: https://leetcode.com/problems/fill_missing_data/

## Description
DataFrame products
| Column Name | Type   |
|-------------|--------|
| name        | object |
| quantity    | int    |
| price       | int    |

## To Do
Write a solution to fill in the missing value as 0 in the quantity column.

The result format is in the following example.

## Example
Input:
| name            | quantity | price |
|-----------------|----------|-------|
| Wristwatch      | 32       | 135   |
| WirelessEarbuds | None     | 821   |
| GolfClubs       | None     | 9319  |
| Printer         | 849      | 3051  |

Output:
| name            | quantity | price |
|-----------------|----------|-------|
| Wristwatch      | 32       | 135   |
| WirelessEarbuds | 0        | 821   |
| GolfClubs       | 0        | 9319  |
| Printer         | 849      | 3051  |

Explanation: 
- The quantity for Toaster and Headphones are filled by 0.
