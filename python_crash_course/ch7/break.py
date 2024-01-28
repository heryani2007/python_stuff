for i in range(3):  # Outer loop
    for j in range(3):  # Inner loop
        if j == 2:
            break  # Breaks out of the inner loop
        print(f"i = {i}, j = {j}")
    print(f"End of iteration {i} for the outer loop.")
