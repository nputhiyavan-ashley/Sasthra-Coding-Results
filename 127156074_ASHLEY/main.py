def get_median(arr):
    n = len(arr)
    mid = n // 2
    if n % 2 == 0:
        return (arr[mid - 1] + arr[mid]) / 2.0
    return float(arr[mid])

def main():
    try:
        n = int(input("Enter the array size: "))
        str_values = input("Enter the numbers separated by spaces: ").split()
    except EOFError:
        return
        
    float_values = [float(x) for x in str_values]
    
    sorted_floats = sorted(float_values)
    mid = n // 2
    
    if n % 2 == 0:
        lower_half = sorted_floats[:mid]
        upper_half = sorted_floats[mid:]
    else:
        lower_half = sorted_floats[:mid]
        upper_half = sorted_floats[mid+1:]
        
    q1 = get_median(lower_half)
    q3 = get_median(upper_half)
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = []
    for s, v in zip(str_values, float_values):
        if v < lower_bound or v > upper_bound:
            outliers.append(s)
            
    if outliers:
        print(" ".join(outliers))
    else:
        print("NONE")

if __name__ == "__main__":
    main()