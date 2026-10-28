# SE Lab 6 – Code Coverage and Branch Coverage

## Aim
To understand and implement code coverage and branch coverage using Python, pytest, and Coverage.py.

## Objectives
- To write unit tests for a Python calculator program.
- To measure statement coverage using Coverage.py.
- To measure branch coverage using Coverage.py.
- To analyze test results and identify uncovered statements or branches.

## Technologies Used
- Python 3.13
- pytest
- Coverage.py
- Git and GitHub

## Project Structure

```text
SE-Lab6-Code-Branch-Coverage/
├── calculator.py
├── test_calculator.py
├── BranchCoverageTest_calculator.py
├── README.md
└── .gitignore
```

Coverage screenshots:
- `CodeCoverageTest_Screenshot.png`
- `BranchCoverageTest_Screenshot.png`

## Installation

Install the required Python packages:

```bash
python -m pip install pytest coverage
```

## Code Coverage

Run the unit tests and measure statement coverage:

```bash
python -m coverage erase
python -m coverage run -m pytest test_calculator.py
python -m coverage report -m
```

### Result
- Tests passed: 1
- Statement coverage: 100%

## Branch Coverage

Run the branch coverage tests:

```bash
python -m coverage erase
python -m coverage run --branch -m pytest BranchCoverageTest_calculator.py
python -m coverage report -m
```

### Result
- Tests passed: 4
- Statement coverage: 100%
- Branches: 4
- Partial branches: 0
- Total coverage: 100%

## Screenshots

The execution screenshots are included in the repository:

1. `CodeCoverageTest_Screenshot.png` – Code coverage results.
2. `BranchCoverageTest_Screenshot.png` – Branch coverage results.

## Conclusion

Code coverage and branch coverage were successfully implemented using pytest and Coverage.py. The code coverage tests achieved 100% statement coverage. The branch coverage tests also achieved 100% total coverage, with all four branches covered and no partial branches. This demonstrates that the implemented test cases exercised all measured statements and branches in the calculator program.

## Repository

GitHub: https://github.com/Poojakanakappanavara/SE-Lab6-Code-Branch-Coverage

