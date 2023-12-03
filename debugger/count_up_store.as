ldc R0 0
ldc R1 3
ldc R3 240
loop:
prr R0
str R0 R3
ldc R2 1
add R0 R2
cpy R2 R1
sub R2 R0
bne R2 @loop
hlt
