ldc R0 13
ldc R1 0
# memory[R1] = R0 --> memory[0] = 13:
str R0 R1
prm R1
# R2 = memory[0] = R0 = 13:
ldr R2 R1
sub R2 R0
beq R2 @jump
add R2 R0
jump:
prr R2
hlt