#Question 1
import sys
line = input(": ")

for i in range(len(line)):
    if (line[0] == "0" and line[1] == "x"):
        sys.exit("Hex number does not have the leading '0x'!")
    
    if (line[i] == "A" or line[i] == "B" or line[i] == "C" or line[i] == 
"D" or line[i] == "E" or line[i] == "F"):
        sys.exit("All aplpha characters (a through f) in the input will be 
in lowercase!")
        
        
line = int(line, base = 16)
print(line)
