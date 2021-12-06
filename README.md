# Python based solutions for the [AOC 2021](https://adventofcode.com/2021/)

Trying hard to do it with built-in packages 🤞

## Code structure
> This excludes the common files like `.gitignore`, `README`, etc.

> The `common_<n>.py` may not be present in all folders, only where the code needs to structured separately.

> On my local machine, I also have a file called `input_<n>_my.txt` which is basically the input given to me.
> You will need to have your own input file and execute the code (as mentioned [below](#run-code-for-each-day)) to get the answer to your puzzle.
```
.
├── day<n>
│   ├── code_<n>_1.py
│   ├── code_<n>_2.py
│   ├── common_<n>.py
│   ├── __init__.py
│   └── input_<n>.txt
└── tests
    ├── conftest.py
    ├── __init__.py
    └── tests_days.py
```

## Run tests
`pytest tests/tests_days.py -vvv`

## Run code for each day
`python -m day5.code_5_1 day5/input_5.txt`
