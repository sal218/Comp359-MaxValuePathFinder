# Comp359-MaxValuePathFinder
This program finds the optimal path from (0,0) to (n-1,n-1) on an n × n chessboard, maximizing the total value collected. It allows movement in all four directions without revisiting positions.


# Members:
- Sal Mourad 
- Simar Padda

# Running The Program:
## Option 1: With UI Output
1. To run the program open the terminal and run
```bash
python src/gui_main.py
```
2. The UI will appear and prompt the user to enter in their desired n value to create the board <br> 
> Note: Since the time complexity grows exponentially with larger n, we reccommend you limit the size of n to 5 or less to view the programs functionality without having to wait too long. 

3. Enter your desired n value and click <code>Okay</code> to run the program. The UI should now show the optimal maximum path taken from start to finish as well as the maximum value accumulated along the way.

## Option 2: Strictly Confined To The Terminal
1. To run the program open the terminal and run
```bash
python src/main.py
```
2. This should prompt you to enter in a value for n. Enter your desired value and click enter. The board will be printed out, as well as the path taken to achieve the maximum sum, and the maximum value collected. 
> Note: Since the time complexity grows exponentially with larger n, we reccommend you limit the size of n to 5 or less to view the programs functionality without having to wait too long. 


# Running The Test Cases:
1. Open the terminal and run either of the following commands
```bash
python tests/test_3X3.py
python tests/test_4x4.py
python tests/test_5x5.py
python tests/test_6x6.py
```
2. The UI will appear and prompt the user to enter in their desired n value to create the board
> Note: Since this is a test case, the n value has been pre-defined.
3. The UI should now show the optimal maximum path taken from start to finish as well as the maximum value accumulated along the way.

