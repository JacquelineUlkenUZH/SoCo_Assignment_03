# Reverse first 10 fibbonacci numbers
# - R0: array index
# - R1: array size
# - R2: first fibbonacci number
# - R3: second fibbonacci number
# First, create the first 10 fibbonacci numbers and store them in the array
ldc R0 @array
ldc R1 10
ldc R2 0
ldc R3 1
fibb:
str R3 R0
swp R3 R2
add R3 R2
inc R0
dec R1
bne R1 @fibb
# Then print the array
ldc R0 @array
ldc R1 10
printar:
ldr R2 R0
prr R2
inc R0
dec R1
bne R1 @printar
# Now we reverse the array
# R0 - start of the array
# R1 - end of the array
# R2 - used both as temporary and to check the difference between R0 and R1
# R3 - temporary
ldc R0 @array
ldc R1 10
add R1 R0
dec R1
# Setting it to 255 instead of 0 so it doesn't get negative
ldc R2 0
reverse:
ldr R2 R0
ldr R3 R1
str R2 R1
str R3 R0
inc R0
# Subtracting old end - new start, leaves possibility there is one single element left in the middle
cpy R2 R1
sub R2 R0
# If 0, this means they were neighbours
beq R2 @stop
# Now covering possibility of one single element left
dec R1
dec R2
bne R2 @reverse
stop:
# Finally print the reversed array
ldc R0 @array
ldc R1 10
printre:
ldr R2 R0
prr R2
inc R0
dec R1
bne R1 @printre
hlt
.data
array: 10