# Load value 5 into register 0
ldc R0 5

# Load value 3 into register 1
ldc R1 3

# Add value in register 1 to register 0
add R0 R1

# Copy value from register 0 to register 2
cpy R0 R2

# Subtract value 2 from register 2
ldc R3 2
sub R2 R3

# Store value from register 2 into memory location 0
str R2 R0

# Print all registers
prr R0
prr R1
prr R3

# Halt the program
hlt