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

