# Count down from 5.
# - R0: loop index.
# - R1: loop limit.
ldc R0 5
ldc R1 0
loop:
prr R0
dec R0
bne R0 @loop
hlt