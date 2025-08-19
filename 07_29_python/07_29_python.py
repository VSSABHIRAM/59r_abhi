# Taking inputs
num1 = int(input("Enter the num1 (integer): "))
num2 = float(input("Enter the num2 (float): "))

# Conversions
int_to_float = float(num1)
int_to_complex = complex(num1)
float_to_int = int(num2)

# Print table header
print(f"\n{'Original Type':<15}{'Original Value':<20}{'Converted Type':<20}{'Converted Value'}")
print("-" * 75)

# Table rows
print(f"{'int':<15}{num1:<20}{'float':<20}{int_to_float}")
print(f"{'int':<15}{num1:<20}{'complex':<20}{int_to_complex}")
print(f"{'float':<15}{num2:<20}{'int':<20}{float_to_int}")
