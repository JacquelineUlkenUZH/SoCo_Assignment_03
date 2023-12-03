# SoCo_Assignment_03

# Exercise 1
In folder `exercise 1`, run: `pytest`
### General
To import the vm classes, we resorted to appending the path with `sys.path.append()`. (So as not to alter the directory structure by adding `__init__.py`.)

We wrote three assembly programs that cover all 11 instructions of the vm at least once.
- `count_up.as` counts to 3 using a loop.
- `memory.as` @Anna can you explain it in one sentence? ==TODO==
- `simple_arithmetic.as` Tests simple add, subtract and copy operations

### A solved in `test_1a_assembler.py`
We created **manual "expected" solutions as .mx-files** named `TESTNAME_expected.mx`. This way they could easily be reused in task (B), which is arguably a better testing strategy. They contain comments (for our understanding) which are stripped when they're loaded.

The tests use the provided assembler to generate the "actual" programs. The tests then save these programs as .mx-files named `TESTNAME.mx`. The programs are then compared to the "expected" solutions.

We'd prefer to delete the .mx-files the tests generate, or not generate these files at all, but (A)(iii) explicitly requires us to generate and not delete these files.

### B solved in `test_1b_vm.py`
As required, by default we use the `TESTNAME.mx`-files generated by the tests in A. But our implementation can also use the more robust `TESTNAME_expected.mx` files, which we prefer (just change the filenames).

We capture the output with `StringIO()` and then compare it to our expected outputs that are stored in files named `TESTNAME_expected_out.log`.

### C solved in `test_1c_devmistakes.py`
Using too much memory we test in three ways:
- The assembler should throw an AssertionError if an array of length 1000 is created.
- The assembler should throw an AssertionError if two arrays both of length 200 are created
- The VM itself should run an IndexError if a memory position with a position above 255 is used. (We use `add` to store a value above 255 in a register and then use it as a memory address.)

Using an unknown instruction, we test in one way:
- A small hex-program contains an operation of value `0101AA`, so the operation is `AA`, which isn't registered. 

Interestingly, with these tests we realised the registers can hold values above 255, but the assembler code and our hex-format cannot. 

### D solved using `pytest.ini`
One can report the test coverage using the python package `pytest-conv` and the command-line arguments `pytest --cov-report term-missing --cov=.. .`

We were also required to make sure all tests print their output in the terminal, which is the `-s` argument.

We realised we can set these options as default by adding them to a `pytest.ini` file in the folder. The default command we enshrine this way is:
```
pytest -s --cov-report term-missing --cov=.. .
```

Our test coverage is `87%`.

# Exercise 2
In folder `exercise 2`, run: `pytest`

### `disassembly.py`
We created a disassembler using the provided assembler class as a blueprint. ==The disassembler can't restore labels.== (Check if true before handing it in)

### Tests in `test_disassembler.py`
The tests successfully restore our programs from Exercise 1 (stripped of labels).
# Exercise 3
You can run the commands as per requirement or, for your convenience, in folder `exercise 3`, just run: `pytest`

### 3.1 solved in `example_3_1.as`
We created two loops that print values on each iteration. The first showcases `dec` to count back from 3 to 0, the second then uses `inc` to count up from 0 to 3 (whilst using `dec` to control the loop in `R1`).
### 3.2 solved in `example_3_2.as`
We load `R0` and `R1` with two 3 and 7, respectively. We then print both registers, swap them, and print them again.
### 3.3 solved in `example_3_2.as`
We decided to be fancy and generate an array with the first ten Fibonacci numbers. We then reverse the array.

# Exercise 4
### 4.1 Show Memory Range
In folder `exercise 4`, run: `python ./vm_4_solved.py ./count_up.mx` which counts 0, 1, 2 using a loop.

Showcase:
1. Print entire memory: `m`
2. Verify memory position `4` is `020006`
3. Print memory position 4 alone: `m 4`
4. Verify you see `000004: 020006`
5. Print memory positions 4 to 11: `m 4 11`
6. Verify with previous printout.
7. Verify input validation: `m a`, `m 280`, `m 11 4`
8. Print entire memory range: `m 0 255`

### 4.2 Breakpoint Addresses
In folder `exercise 4`, run: `python ./vm_4_solved.py ./count_up.mx` which counts 0, 1, 2 using a loop.

Showcase:
1. Add breakpoint to position 5: `b 5`
2. Run: `r`
3. Note the program printed `0` and breakpoint hit on position 5.
4. Run: `r`
3. Note the program printed `1` and breakpoint hit on position 5.
6. Step to be on different address: `s`
7. Clear breakpoint on position 5: `c 5`
8. Run: `r`
9. Note the program printed `2` without hitting any breakpoint.

### 4.3 Command Completion
In folder `exercise 4`, run: `python ./vm_4_solved.py ./count_up.mx` which counts 0, 1, 2 using a loop.

Showcase:
1. Verify these commands produce the same output:
	1. `m 4 7`
	2. `me 4 7`
	3. `memor 4 7`
2. Verify `step`:
	1. `s`
	2. `st`
	3. `ste`
	4. `step`

### 4.4 Watchpoints
Note: We decided to break on watchpoints every time a value is written, no matter if the old value is the same. Also beware we use the custom program `count_up_store.mx` to showcase.

In folder `exercise 4`, run: `python ./vm_4_solved.py ./count_up_store.mx` which counts 0, 1, 2 using a loop and stores the counter in memory position 240.

We called the debugger commands `watch` and `unwatch`.

Showcase:
1. Add watchpoint to memory address 240: `w 240`
2. Run: `r`
3. Verify output: `Watchpoint 0000f0 (240): Overriding 0 with 0`
4. Run: `r`
5. Verify output: `Watchpoint 0000f0 (240): Overriding 0 with 1`
6. Run: `r`
7. Verify output: `Watchpoint 0000f0 (240): Overriding 1 with 2`
8. Run: `r`
9. The program finishes, prints the memory, verify memory address `0000f0 (240)` is 2.
