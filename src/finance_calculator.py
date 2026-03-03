"""
Personal Finance Calculator
---------------------------
Collects employee salary details and generates a financial summary report
using Indian number formatting (lakhs/crores).
"""


def format_inr(amount):
    """
    Format a number using Indian currency (lakhs/crores) style.

    Args:
        amount (float): Numeric amount.

    Returns:
        str: Amount formatted in Indian numbering format.
    """
    amount_str = f"{amount:.2f}"
    integer_part, decimal_part = amount_str.split(".")

    if len(integer_part) <= 3:
        return f"{integer_part}.{decimal_part}"

    last_three = integer_part[-3:]
    remaining = integer_part[:-3]

    parts = []
    while len(remaining) > 2:
        parts.insert(0, remaining[-2:])
        remaining = remaining[:-2]

    if remaining:
        parts.insert(0, remaining)

    formatted_integer = ",".join(parts) + "," + last_three
    return f"{formatted_integer}.{decimal_part}"


def get_valid_float(prompt, min_value=None, max_value=None):
    """
    Prompt the user for a float input and validate it against optional bounds.

    Args:
        prompt (str): Input prompt message.
        min_value (float, optional): Minimum allowed value.
        max_value (float, optional): Maximum allowed value.

    Returns:
        float: Validated numeric input.
    """
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value <= min_value:
                print(f"Value must be greater than {min_value}. Please try again.")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must not exceed {max_value}. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def collect_employee_data():
    """
    Collect validated employee financial inputs.

    Returns:
        dict: Dictionary containing employee data.
    """
    name = input("Enter employee name: ").strip()

    annual_salary = get_valid_float("Enter annual salary (₹): ", min_value=0)
    tax_percentage = get_valid_float(
        "Enter tax bracket percentage: ", min_value=0, max_value=50
    )
    monthly_rent = get_valid_float("Enter monthly rent (₹): ", min_value=0)
    savings_percentage = get_valid_float(
        "Enter savings goal percentage: ", min_value=0, max_value=100
    )

    return {
        "name": name,
        "annual_salary": annual_salary,
        "tax_percentage": tax_percentage,
        "monthly_rent": monthly_rent,
        "savings_percentage": savings_percentage,
    }


def calculate_finances(data):
    """
    Perform financial calculations.

    Args:
        data (dict): Employee financial data.

    Returns:
        dict: Calculated financial metrics.
    """
    monthly_salary = data["annual_salary"] / 12
    monthly_tax = monthly_salary * (data["tax_percentage"] / 100)
    net_salary = monthly_salary - monthly_tax
    rent_ratio = (data["monthly_rent"] / net_salary) * 100
    monthly_savings = net_salary * (data["savings_percentage"] / 100)
    disposable_income = net_salary - data["monthly_rent"] - monthly_savings

    return {
        "monthly_salary": monthly_salary,
        "monthly_tax": monthly_tax,
        "net_salary": net_salary,
        "rent_ratio": rent_ratio,
        "monthly_savings": monthly_savings,
        "disposable_income": disposable_income,
        "annual_tax": monthly_tax * 12,
        "annual_savings": monthly_savings * 12,
        "annual_rent": data["monthly_rent"] * 12,
    }


def print_financial_report(data, results):
    """
    Print formatted financial summary report.
    """
    print("════════════════════════════════════════════")
    print("       EMPLOYEE FINANCIAL SUMMARY")
    print("════════════════════════════════════════════")
    print(f" Employee      : {data['name']}")
    print(f" Annual Salary : ₹{format_inr(data['annual_salary'])}")
    print("────────────────────────────────────────────")
    print(" Monthly Breakdown:")
    print(f"   Gross Salary     : ₹{format_inr(results['monthly_salary'])}")
    print(
        f"   Tax ({data['tax_percentage']}%)      : "
        f"₹{format_inr(results['monthly_tax'])}"
    )
    print(f"   Net Salary       : ₹{format_inr(results['net_salary'])}")
    print(
        f"   Rent             : ₹{format_inr(data['monthly_rent'])}  "
        f"({results['rent_ratio']:.1f}% of net)"
    )
    print(
        f"   Savings ({data['savings_percentage']}%)  : "
        f"₹{format_inr(results['monthly_savings'])}"
    )
    print(
        f"   Disposable       : ₹{format_inr(results['disposable_income'])}"
    )
    print("────────────────────────────────────────────")
    print(" Annual Projection:")
    print(f"   Total Tax        : ₹{format_inr(results['annual_tax'])}")
    print(f"   Total Savings    : ₹{format_inr(results['annual_savings'])}")
    print(f"   Total Rent       : ₹{format_inr(results['annual_rent'])}")
    print("════════════════════════════════════════════")

def print_comparison_table(emp1, res1, emp2, res2):
    """
    Print side-by-side financial comparison for two employees.
    """
    print("\n════════════════ EMPLOYEE COMPARISON ════════════════")
    print(f"{'Metric':<20} {'Employee 1':>15} {'Employee 2':>15}")
    print("─────────────────────────────────────────────────────")

    print(
        f"{'Net Monthly Salary':<20} "
        f"₹{format_inr(res1['net_salary']):>14} "
        f"₹{format_inr(res2['net_salary']):>14}"
    )
    print(
        f"{'Monthly Rent':<20} "
        f"₹{format_inr(emp1['monthly_rent']):>14} "
        f"₹{format_inr(emp2['monthly_rent']):>14}"
    )
    print(
        f"{'Monthly Savings':<20} "
        f"₹{format_inr(res1['monthly_savings']):>14} "
        f"₹{format_inr(res2['monthly_savings']):>14}"
    )
    print(
        f"{'Disposable Income':<20} "
        f"₹{format_inr(res1['disposable_income']):>14} "
        f"₹{format_inr(res2['disposable_income']):>14}"
    )

    print("═════════════════════════════════════════════════════\n")

def calculate_health_score(results):
    """
    Calculate financial health score (0–100).

    Scoring logic:
    - Rent ratio < 30%  → 40 points
      30–40%            → 20 points
      > 40%             → 0 points
    - Savings rate:
      ≥ 20%             → 30 points
      10–19%            → 15 points
      < 10%             → 0 points
    - Disposable income ≥ 20% of net → 30 points
      else                           → 0 points
    """
    score = 0

    # Rent ratio score
    rent_ratio = results["rent_ratio"]
    if rent_ratio < 30:
        score += 40
    elif rent_ratio <= 40:
        score += 20

    # Savings score
    savings_rate = (
        results["monthly_savings"] / results["net_salary"]
    ) * 100
    if savings_rate >= 20:
        score += 30
    elif savings_rate >= 10:
        score += 15

    # Disposable income score
    disposable_ratio = (
        results["disposable_income"] / results["net_salary"]
    ) * 100
    if disposable_ratio >= 20:
        score += 30

    return score

def main():
    """
    Main execution function.
    """
    print("\nEnter details for Employee 1")
    employee_1 = collect_employee_data()
    results_1 = calculate_finances(employee_1)

    print("\nEnter details for Employee 2")
    employee_2 = collect_employee_data()
    results_2 = calculate_finances(employee_2)

    print("\n--- EMPLOYEE 1 REPORT ---")
    print_financial_report(employee_1, results_1)
    print(f"Financial Health Score: {calculate_health_score(results_1)}/100")

    print("\n--- EMPLOYEE 2 REPORT ---")
    print_financial_report(employee_2, results_2)
    print(f"Financial Health Score: {calculate_health_score(results_2)}/100")

    print_comparison_table(employee_1, results_1, employee_2, results_2)

if __name__ == "__main__":
    main()