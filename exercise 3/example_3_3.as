# Reverse first 10 fibbonacci numbers
# First, create the first 10 fibbonacci numbers and store them in the array
# - R0: array start
# - R1: array size
# - R2: first fibbonacci number
# - R3: second fibbonacci number
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
print_array:
ldr R2 R0
prr R2
inc R0
dec R1
bne R1 @print_array
# Now we reverse the array
# - R0: array start
# - R1: array end
# - R2: used both as temporary and to check the difference between R0 and R1
# - R3: temporary
ldc R0 @array
ldc R1 10
add R1 R0
dec R1
ldc R2 0
ldc R3 0
reverse:
dec R2
beq R2 @stop
ldr R2 R0
ldr R3 R1
str R2 R1
str R3 R0
inc R0
dec R1
cpy R2 R0
sub R2 R1
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