# Personal Finance Calculator 💰

A Python-based personal finance calculator built for an AI startup’s
employee benefits portal.  
This project demonstrates clean input validation, financial computation,
Indian currency formatting, and comparison logic.

---

## 📌 Part A – Core Features

### Functionality
- Collects employee financial details:
  - Annual salary
  - Tax bracket
  - Monthly rent
  - Savings goal
- Validates all inputs gracefully
- Computes:
  - Monthly salary
  - Tax deduction
  - Net income
  - Rent ratio
  - Savings amount
  - Disposable income
- Displays a professional financial summary report

---

## 📌 Part B – Stretch Enhancements

### 🇮🇳 Indian Currency Formatting
- Custom formatter for **lakhs/crores**
- Example: `₹12,00,000.00` instead of `₹1,200,000.00`
- Implemented without `locale` for cross-platform reliability

### 👥 Employee Comparison
- Collects data for **two employees**
- Displays a **side-by-side comparison table**:
  - Net salary
  - Rent
  - Savings
  - Disposable income

### 📊 Financial Health Score (0–100)
A transparent scoring system based on:
- **Rent ratio**
- **Savings rate**
- **Disposable income percentage**

Higher scores indicate better overall financial health.

---

## ▶️ How to Run

```bash
python src/finance_calculator.py

assignment_day_7_PM/
├── src/
│   └── finance_calculator.py
├── docs/
├── README.md
└── LICENSE

---

## 📤 Sample Output

```text
Enter details for Employee 1
Enter employee name: himkar vashistha
Enter annual salary (₹): 1000000
Enter tax bracket percentage: 30
Enter monthly rent (₹): 25000
Enter savings goal percentage: 10

Enter details for Employee 2
Enter employee name: ayush tiwari
Enter annual salary (₹): 1500000
Enter tax bracket percentage: 30
Enter monthly rent (₹): 35000
Enter savings goal percentage: 20

--- EMPLOYEE 1 REPORT ---
════════════════════════════════════════════
       EMPLOYEE FINANCIAL SUMMARY
════════════════════════════════════════════
 Employee      : himkar vashistha
 Annual Salary : ₹10,00,000.00
────────────────────────────────────────────
 Monthly Breakdown:
   Gross Salary     : ₹83,333.33
   Tax (30.0%)      : ₹25,000.00
   Net Salary       : ₹58,333.33
   Rent             : ₹25,000.00  (42.9% of net)
   Savings (10.0%)  : ₹5,833.33
   Disposable       : ₹27,500.00
────────────────────────────────────────────
 Annual Projection:
   Total Tax        : ₹3,00,000.00
   Total Savings    : ₹70,000.00
   Total Rent       : ₹3,00,000.00
════════════════════════════════════════════
Financial Health Score: 45/100

--- EMPLOYEE 2 REPORT ---
════════════════════════════════════════════
       EMPLOYEE FINANCIAL SUMMARY
════════════════════════════════════════════
 Employee      : ayush tiwari
 Annual Salary : ₹15,00,000.00
────────────────────────────────────────────
 Monthly Breakdown:
   Gross Salary     : ₹1,25,000.00
   Tax (30.0%)      : ₹37,500.00
   Net Salary       : ₹87,500.00
   Rent             : ₹35,000.00  (40.0% of net)
   Savings (20.0%)  : ₹17,500.00
   Disposable       : ₹35,000.00
────────────────────────────────────────────
 Annual Projection:
   Total Tax        : ₹4,50,000.00
   Total Savings    : ₹2,10,000.00
   Total Rent       : ₹4,20,000.00
════════════════════════════════════════════
Financial Health Score: 80/100

════════════════ EMPLOYEE COMPARISON ════════════════
Metric                    Employee 1      Employee 2
─────────────────────────────────────────────────────
Net Monthly Salary   ₹     58,333.33 ₹     87,500.00
Monthly Rent         ₹     25,000.00 ₹     35,000.00
Monthly Savings      ₹      5,833.33 ₹     17,500.00
Disposable Income    ₹     27,500.00 ₹     35,000.00
═════════════════════════════════════════════════════

---

## 📌 Part C – (Interview ready 20%)

This section evaluates conceptual understanding, debugging ability, and
type-handling skills in Python.  
All questions are answered in the given order, with explanations and verified outputs.

---

## Q1️⃣ Conceptual — Data Types Deep Dive

**Instruction:**  
Explain the output of each line *without running the code*, then verify by execution.

### Given Code

```python
print(type(True))
print(isinstance(True, int))
print(True + True + False)
print(int(3.99))
print(bool("False"))
print(bool(""))
print(0.1 + 0.2 == 0.3)
print("5" + "3")
print(5 + 3)
Explanation (Without Execution)
Expression	Explanation	Output
type(True)	True is a boolean literal	<class 'bool'>
isinstance(True, int)	bool is a subclass of int	True
True + True + False	True = 1, False = 0	2
int(3.99)	int() truncates decimals	3
bool("False")	Non-empty strings are truthy	True
bool("")	Empty string is falsy	False
0.1 + 0.2 == 0.3	Floating-point precision issue	False
"5" + "3"	String concatenation	53
5 + 3	Integer addition	8
Verified Output (By Execution)
<class 'bool'>
True
2
3
True
False
False
53
8
Q2️⃣ Coding — Build a Type Analyzer
Function Definition
def analyze_value(value):
    """
    Analyze a value and return its characteristics.
    """
    value_type = type(value).__name__
    truthy = bool(value)

    if hasattr(value, "__len__"):
        try:
            length = len(value)
        except TypeError:
            length = "N/A"
    else:
        length = "N/A"

    return (
        f"Value: {value} | "
        f"Type: {value_type} | "
        f"Truthy: {truthy} | "
        f"Length: {length}"
    )
Test Cases (As per Question Order)
print(analyze_value(42))
print(analyze_value(""))
print(analyze_value([1, 2, 3]))
Output
Value: 42 | Type: int | Truthy: True | Length: N/A
Value:  | Type: str | Truthy: False | Length: 0
Value: [1, 2, 3] | Type: list | Truthy: True | Length: 3
Q3️⃣ Debug — Find & Fix 4 Bugs
Given Buggy Code
name = input("Name: ")
age = input("Age: ")

if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(f"name is {age} years old and is a {status}")
print(f"In 5 years: {age + 5}")

score = 85.5
print(f"Score: {score:.0}")
Identified Bugs
Bug #	Issue	Explanation
1	Type mismatch	input() returns string; compared with integer
2	Invalid arithmetic	String + integer operation
3	Wrong variable usage	Literal "name" printed instead of variable
4	Invalid format specifier	.0 is not valid for floats
Corrected Code
name = input("Name: ")
age = int(input("Age: "))

if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(f"{name} is {age} years old and is a {status}")
print(f"In 5 years: {age + 5}")

score = 85.5
print(f"Score: {score:.0f}")

---

# PART D — Type Conversion Reference via AI

This section evaluates the reliability of AI-generated programming knowledge by
testing Python type conversion claims against actual interpreter behavior.

The task involved prompting an AI tool, validating its responses through
execution, and critically evaluating its accuracy and limitations.

---

## 1️⃣ AI Prompt Used

The following **exact prompt** was given to the AI tool:

```text
Generate a Python type conversion matrix showing what happens when you convert
between int, float, str, bool, list, and tuple.

For each conversion:
- Show the result if it succeeds
- Mention the output value
- Highlight edge cases
- Clearly state if the conversion raises an error and why

Cover common and tricky cases such as empty values, zero, and non-numeric strings.
2️⃣ AI-Generated Type Conversion Matrix (Raw Output)

The AI produced the following conversion claims:

int → float     : int(5) → 5.0
int → str       : int("5") → 5
int → bool      : bool(0) → False, bool(5) → True
int → list      : list(5) → Error
int → tuple     : tuple(5) → Error

float → int     : int(3.7) → 3
float → str     : str(3.7) → "3.7"
float → bool    : bool(0.0) → False, bool(2.5) → True
float → list    : list(3.7) → Error
float → tuple   : tuple(3.7) → Error

str → int       : int("123") → 123
str → float     : float("3.14") → 3.14
str → bool      : bool("False") → False
str → list      : list("abc") → ['a', 'b', 'c']
str → tuple     : tuple("abc") → ('a', 'b', 'c')

bool → int      : int(True) → 1
bool → float    : float(True) → 1.0
bool → str      : str(True) → "True"
bool → list     : list(True) → Error
bool → tuple    : tuple(False) → Error

list → tuple    : tuple([1, 2]) → (1, 2)
list → str      : str([1,2]) → "[1, 2]"
list → int      : int([1,2]) → Error
list → float    : float([1,2]) → Error
list → bool     : bool([]) → False

tuple → list    : list((1,2)) → [1,2]
tuple → str     : str((1,2)) → "(1, 2)"
tuple → int     : int((1,2)) → Error
tuple → float   : float((1,2)) → Error
tuple → bool    : bool(()) → False
3️⃣ Python Verification Process

All conversions were tested directly in Python using a scripted test file.
Each conversion was executed inside a try/except block to capture both
successful results and raised exceptions.

4️⃣ AI Accuracy Check
Verified Conversion Results
Conversion	AI Claim	Actual Result	Verdict
int → float	5 → 5.0	5.0	✅ Correct
int → str	int("5")	str(5)	❌ Incorrect
int → bool	True if non-zero	True	✅ Correct
int → list	Error	TypeError	✅ Correct
int → tuple	Error	TypeError	✅ Correct

| float → int | 3 | 3 | ✅ Correct |
| float → str | "3.7" | "3.7" | ✅ Correct |
| float → bool | True if non-zero | True | ✅ Correct |
| float → list | Error | TypeError | ✅ Correct |
| float → tuple | Error | TypeError | ✅ Correct |

| str → int | "123" → 123 | 123 | ✅ Correct |
| str → float | "3.14" → 3.14 | 3.14 | ✅ Correct |
| str → bool | False | True | ❌ Incorrect |
| str → list | ['a','b','c'] | ['a','b','c'] | ✅ Correct |
| str → tuple | ('a','b','c') | ('a','b','c') | ✅ Correct |

| bool → int | 1 / 0 | 1 / 0 | ✅ Correct |
| bool → float | 1.0 | 1.0 | ✅ Correct |
| bool → str | "True" | "True" | ✅ Correct |
| bool → list | Error | TypeError | ✅ Correct |
| bool → tuple | Error | TypeError | ✅ Correct |

| list → tuple | (1,2) | (1,2) | ✅ Correct |
| list → str | "[1, 2]" | "[1, 2]" | ✅ Correct |
| list → int | Error | TypeError | ✅ Correct |
| list → float | Error | TypeError | ✅ Correct |
| list → bool | False if empty | False | ✅ Correct |

| tuple → list | [1,2] | [1,2] | ✅ Correct |
| tuple → str | "(1, 2)" | "(1, 2)" | ✅ Correct |
| tuple → int | Error | TypeError | ✅ Correct |
| tuple → float | Error | TypeError | ✅ Correct |
| tuple → bool | False if empty | False | ✅ Correct |

5️⃣ Critical Evaluation (≈170 words)

The AI-generated type conversion matrix was largely accurate for common and
well-known Python behaviors, particularly for numeric conversions, iterable
transformations, and error cases involving non-iterable types. Most failures
were raised correctly as TypeError, and standard truthiness rules for lists,
tuples, and numbers were accurately described.

However, the AI made notable conceptual mistakes. It incorrectly represented
int → str conversion by using int("5") instead of str(5), demonstrating
confusion between parsing and casting. More critically, it claimed
bool("False") evaluates to False, which is incorrect — Python treats all
non-empty strings as truthy regardless of their textual meaning. This reveals a
tendency of AI systems to apply human semantics rather than language rules.

Additionally, the AI omitted edge cases such as empty lists vs non-empty lists
in truthiness explanations and did not mention ValueError cases like
int("abc"). While AI is useful for quick references, this exercise shows that
developer validation is essential, especially for language fundamentals.