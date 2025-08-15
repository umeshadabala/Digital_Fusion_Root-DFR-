# Function to calculate the sum of digits of a number
def digit_sum(n):
    return sum(int(d) for d in str(n))  # Adds all digits in the number

# Function to calculate the product of digits of a number
def digit_product(n):
    product = 1
    for d in str(n):
        product *= int(d)  # Multiplies all digits together
    return product

# Function to check if a number is a Digital Fusion Root (DFR)
def is_dfr(n):
    return n == int(str(digit_sum(n)) + str(digit_product(n)))  # True if n equals sum||product

# Function to find all DFRs up to a given limit
def find_dfrs(limit=2147483647):
    return [n for n in range(10, limit) if is_dfr(n)]  # Find all valid DFRs from 10 to limit

# Function to print details of found DFRs
def analyze_dfrs(dfrs):
    print("Found DFRs:", dfrs)  # Print all found DFRs
    print("Total:", len(dfrs))  # Print count of DFRs
    for n in dfrs:
        print(f"{n}: Digits={len(str(n))}, Sum={digit_sum(n)}, Product={digit_product(n)}, Concatenation={n}")  # Detailed info

# Run the DFR search and analysis
dfr_list = find_dfrs(2147483647)       # Get DFRs up to 100
analyze_dfrs(dfr_list)          # Show results
