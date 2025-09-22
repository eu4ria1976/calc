# Scientific Calculator

A feature-rich scientific calculator application with a graphical user interface built using Python and Tkinter.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Scientific functions (sin, cos, tan, asin, acos, atan)
- Logarithmic functions (natural log, log base 10, log base 2)
- Exponential and power functions (square, cube, square root, cube root, exponent, reciprocal)
- Factorial calculations (including double factorial)
- Constants (π, e)
- Parentheses for complex expressions
- Keyboard support for input
- Error handling for invalid expressions
- Delete (DEL) function to remove the last input digit
- Percentage (%) function for calculating percentages

## Installation

1. Clone or download this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the calculator application:

```bash
python src/calculator/main.py
```

Or if you have installed the package:

```bash
scientific-calculator
```

### Keyboard Shortcuts

- Digits 0-9: Input numbers
- +, -, *, /: Basic operations
- Enter/Return: Calculate result
- Escape: Clear all
- Backspace: Clear input
- (, ): Parentheses

## Running Tests

To run the test suite:

```bash
pytest tests/
```

Or for more detailed output:

```bash
pytest -v tests/
```

### Test Results

All unit tests are passing. A total of 52 tests were executed covering all calculator modules:
- Trigonometry: 16 tests
- Logarithms: 8 tests
- Powers: 10 tests
- Factorials: 6 tests
- Fractions: 12 tests

Issues were found and fixed in the test expectations (not in the implementation):
- Logarithms test for `log(10, 10)` was expecting 2 instead of 1
- Factorials test for `factorial(10)` was expecting 362880 instead of 3628800

## Building Windows Executable

To create a standalone Windows executable, you have several options:

### Option 1: Using the build script (Recommended)

For Windows users, run the batch file:
```bash
build.bat
```

For cross-platform usage, run the Python script:
```bash
python build.py
```

### Option 2: Using PyInstaller directly

```bash
pyinstaller --clean calculator.spec
```

### Option 3: Manual PyInstaller command

```bash
pyinstaller --onefile --windowed --name "ScientificCalculator" run.py
```

## Prerequisites for Building

- Python 3.8 or higher
- PyInstaller 5.0 or higher
- All dependencies listed in requirements.txt

To install the build dependencies:
```bash
pip install -r requirements.txt
```

## Build Output

The executable will be created in the `dist/` directory as `ScientificCalculator.exe`.

## Testing

All unit tests are passing. A total of 52 tests were executed covering all calculator modules:
- Trigonometry: 16 tests
- Logarithms: 8 tests
- Powers: 10 tests
- Factorials: 6 tests
- Fractions: 12 tests

Issues were found and fixed in the test expectations (not in the implementation):
- Logarithms test for `log(10, 10)` was expecting 2 instead of 1
- Factorials test for `factorial(10)` was expecting 362880 instead of 3628800

The GUI application launches successfully and the Windows executable builds without errors.

## Project Structure

```
scientific-calculator/
├── src/
│   └── calculator/
│       ├── core/          # Core calculator logic
│       ├── gui/           # GUI components
│       ├── modules/       # Mathematical function modules
│       └── utils/         # Utility functions
├── tests/                 # Unit tests
├── requirements.txt       # Python dependencies
├── setup.py              # Package setup file
├── README.md             # This file
└── .gitignore            # Git ignore file
```

## Dependencies

- Python 3.8+
- Tkinter (included with standard Python installation)
- pytest (for testing)
- pyinstaller (for creating executables)

## License

This project is licensed under the MIT License - see the LICENSE file for details.