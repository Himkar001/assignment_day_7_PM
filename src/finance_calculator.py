"""
Personal Finance Calculator
---------------------------
Collects employee salary details and generates a financial summary report.
"""


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

    annual_salary = get_valid_float(
        "Enter annual salary (₹): ", min_value=0
    )
    tax_percentage = get_valid_float(
        "Enter tax bracket percentage: ", min_value=0, max_value=50
    )
    monthly_rent = get_valid_float(
        "Enter monthly rent (₹): ", min_value=0
    )
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

    Args:
        data (dict): Employee input data.
        results (dict): Calculated financial results.
    """
    print("════════════════════════════════════════════")
    print("       EMPLOYEE FINANCIAL SUMMARY")
    print("════════════════════════════════════════════")
    print(f" Employee      : {data['name']}")
    print(f" Annual Salary : ₹{data['annual_salary']:,.2f}")
    print("────────────────────────────────────────────")
    print(" Monthly Breakdown:")
    print(f"   Gross Salary     : ₹{results['monthly_salary']:>11,.2f}")
    print(
        f"   Tax ({data['tax_percentage']}%)      : "
        f"₹{results['monthly_tax']:>11,.2f}"
    )
    print(f"   Net Salary       : ₹{results['net_salary']:>11,.2f}")
    print(
        f"   Rent             : ₹{data['monthly_rent']:>11,.2f}  "
        f"({results['rent_ratio']:.1f}% of net)"
    )
    print(
        f"   Savings ({data['savings_percentage']}%)  : "
        f"₹{results['monthly_savings']:>11,.2f}"
    )
    print(
        f"   Disposable       : ₹{results['disposable_income']:>11,.2f}"
    )
    print("────────────────────────────────────────────")
    print(" Annual Projection:")
    print(f"   Total Tax        : ₹{results['annual_tax']:>11,.2f}")
    print(f"   Total Savings    : ₹{results['annual_savings']:>11,.2f}")
    print(f"   Total Rent       : ₹{results['annual_rent']:>11,.2f}")
    print("════════════════════════════════════════════")


def main():
    """
    Main execution function.
    """
    employee_data = collect_employee_data()
    finance_results = calculate_finances(employee_data)
    print_financial_report(employee_data, finance_results)


if __name__ == "__main__":
    main()