# Mathematical Foundations for AI

This repository organizes the assignment PDFs and Python scripts by topic to
make review and progress tracking easier.

## Repository structure

| Folder | Contents |
| --- | --- |
| [`assignment-1-lagrange-interpolation/`](./assignment-1-lagrange-interpolation/) | Assignment 1 PDF and the Lagrange interpolation script (`assignment1_lagrange_interpolation.py`). |
| [`assignment-2-numerical-interpolation/`](./assignment-2-numerical-interpolation/) | Assignment 2 PDF and a comparison of Lagrange, Newton, and Hermite interpolation (`assignment2_interpolation_methods.py`). |
| [`assignment-3-numerical-integration/`](./assignment-3-numerical-integration/) | Assignment 3 PDF and numerical integration using the trapezoidal and Simpson's rules (`assignment3_numerical_integration.py`). |

Each folder contains the corresponding assignment PDF and, when available,
the related Python script.

## Running the scripts

From the repository root, run a script with Python:

```powershell
python .\assignment-1-lagrange-interpolation\assignment1_lagrange_interpolation.py
python .\assignment-2-numerical-interpolation\assignment2_interpolation_methods.py
python .\assignment-3-numerical-integration\assignment3_numerical_integration.py
```

The first two scripts use NumPy. The second assignment script also uses
Matplotlib to display plots. Install these dependencies if needed:

```powershell
python -m pip install numpy matplotlib
```
