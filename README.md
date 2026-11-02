# Udemy Python Course Projects

A collection of hands-on Python projects built while following a Udemy Python course.
Each file corresponds to a day/challenge from the course, progressing from beginner scripts to deeper concepts like OOP and type-checked modules.

## Project Structure

```
├── non_virtual/        # Exercises from the non-virtual environment
│   ├── d1_miles_to_km.py
│   ├── d2_income_tax_calculator.py
│   ├── ...
│   └── d8_guess_that_number.py
├── virtual/            # Exercises from the virtual environment
│   ├── d9_website_status.py
│   ├── d10_currency_converter.py
│   ├── ...
│   └── d24_notes.py
├── formatter.py        # Code formatting utility
├── main.py             # Scratch/test file (list slicing)
└── oop.py              # Object-oriented programming practice
```

## What's Inside

| Day | Project |
|-----|---------|
| d1 | Miles to Kilometers converter |
| d2 | Income Tax Calculator |
| d3 | Mad Libs game |
| d4 | Rock–Paper–Scissors game |
| d5 | Expense Splitter |
| d6–d8 | Chatbot v1, Print Clone, Guess That Number |
| d9–d10 | Website Status Checker, Currency Converter |
| d11–d13 | Grocery List, Car Factory, Car Theft Identifier |
| d14–d15 | Password Checker (with common-password list), Chatbot v2 |
| d16–d17 | Activity Generator, Finance Bar Chart |
| d18–d19 | Email Finder, Text Analyzer |
| d20–d21 | Lucky Lemons, Folder Analyser |
| d22–d24 | Chatbot v3, Website Status, Notes |

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
2. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   ```

## How to Run

Run any exercise directly with Python:

```bash
python non_virtual/d4_rock-paper-scissor.py
python virtual/d14_password_checker.py
```

## Tools Used

- **Python 3.14**
- **mypy** — for static type checking
- **VS Code** — as the development environment

## Notes

This repository is for learning purposes while following the course. Some exercises use `type hints` (`list[str]`, etc.) as I practice writing type-annotated Python.
