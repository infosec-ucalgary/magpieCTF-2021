#MagpieSays
### Category: Misc
### Author: Ejaaz Lakhani 

##Description
1) standard game of Simon Says 
2) run java SimonTest on cmd line
3) mimic the game output using keyboard
	0 - green
	1 - red
	2 - blue
	3 - yellow
	4 - pink
	5 - lightgray
	6 - cyan
	7 - gray
	8 - orange
	9 - magenta  


##Solution
1) The game works as a normal game of Simon Says where the CPU gives a string of arguments equal to the level then the user has to mimic those arguments to move on to the next level. 

2) User can input the pattern using number keys from 0-9 going counter clockwise starting from green. 

3) There are a total of 57 levels in the game. The final order of all buttons is 
1,0,9,0,9,7,1,0,3,1,2,1,0,5,1,0,1,1,1,2,3,0,6,5,0,8,3,0,6,7,0,7,3,0,7,3,0,9,5,1,0,5,1,1,5,0,9,5,1,0,2,1,1,7,1,1,0,1,2,5

4) One must think how can we represent data with a set of numbers. 

5) The solution here is ASCII where every 3 numbers correspond to an ASCII character 

6) 

109 - m
097 - a
103 - g	
112 - p
105 - i
101 - e

123 - {

065 - A
083 - S
067 - C
073 - I
073 - I

095 - _

105 - i
115 - s

095 - _

102 - f
117 - u
110 - n

125 - }

(could also use a simple decimal to ASCII conversion site) 

## Flag

magpie{ASCII_is_fun}
