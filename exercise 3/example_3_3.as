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
# - R1: difference between end and start of array
# - R2: takes value from R0 and stores it at R0 + R1
# - R3: takes value from R0 + R1 and stores it at R0
ldc R0 @array
ldc R1 9
reverse:
# If R1 = - 1, then stop
inc R1
beq R1 @stop
dec R1
add R1 R0  # R1 is now end of array
# Swap the first and last elements
ldr R2 R0
ldr R3 R1
str R2 R1
str R3 R0
# Increment the array start and decrement the array end
inc R0
dec R1
sub R1 R0  # R1 is now difference between end and start of array
bne R1 @reverse  # If R1 is not 0, continue
stop:
# Finally print the reversed array
ldc R0 @array
ldc R1 10
print_reversed:
ldr R2 R0
prr R2
inc R0
dec R1
bne R1 @print_reversed
hlt
.data
array: 10