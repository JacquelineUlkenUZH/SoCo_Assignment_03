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
# Exercise 3
# Exercise 4