# DP Line Breaking
Finding the optimal way to break a paragraph into lines to minimize the amount of "slack" on each line using dynamic programming.

## Algorithm Design:
The line breaking algorithm follows these steps:
- **Base Case:**
  - If the index exceeds the number of words, return 0.
- **Recursive Case:**
  - Iterate over possible line breaks.
  - Compute the total length of the current line.
  - If the length exceeds the limit, break out of the loop.
  - Compute the slack squared for the current line.
  - If this is the last line, set slack to 0.
  - Otherwise, recursively compute the minimum slack for the remaining lines.
  - Store the optimal break point.

## Data Structures/Variables Used:
- **w (list of integers):** Represents the widths of words.
- **b (integer):** Represents the space between words.
- **l (integer):** Maximum allowed length of a line.
- **n (integer):** Total number of words.
- **min_slack (list):** Stores the minimum slack for each index to prevent unnecessary recomputation.
- **break_at (list):** Keeps track of optimal line breaks.

## Time Complexity Analysis:
The algorithm recursively explores possible line breaks while using memoization to avoid redundant calculations. The recurrence relation can be described as:
- T(n) = O(n^2) due to the nested loop that iterates over the remaining words.
- Memoization reduces redundant calls, leading to an overall time complexity of **O(n^2)**, which is efficient for this type of problem.

## Usage:
1. Provide an input file `input.txt` with the following format:
   ```
   w1 w2 w3 ... wn  # Space-separated word lengths
   b                 # Minimum blank width
   l                 # Maximum line length
   ```
2. Run the script, and it will output:
   - The minimum slack value.
   - The optimal positions for line breaks.
