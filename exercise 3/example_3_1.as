# Count down from 3 then count back up.
# - R0: loop index.
# - R1: loop limit.
ldc R0 3
loop1:
prr R0
dec R0
bne R0 @loop1
ldc R1 3
loop2:
prr R0
inc R0
dec R1
bne R1 @loop2
prr R0
hlt