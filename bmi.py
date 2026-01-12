def check_weight_status():
    while True:
        print("\nWelcome! Let's check your weight status based on age and height.")

        try:
            # Get user input
            age = int(input("Enter your age: "))
            height = float(input("Enter your height in cm: "))
            weight = float(input("Enter your weight in kg: "))

            # Convert height to meters
            height_m = height / 100

            # Calculate BMI
            bmi = weight / (height_m ** 2)

            # Age-specific BMI thresholds
            if age < 18:
                low_bmi, high_bmi = 17, 23
            else:
                low_bmi, high_bmi = 18.5, 24.9

            # Convert BMI range to weight range
            min_weight = low_bmi * (height_m ** 2)
            max_weight = high_bmi * (height_m ** 2)

            # Classify and suggest
            if bmi < low_bmi:
                status = "Low (Underweight)"
                suggestion = f"You need to gain at least {min_weight - weight:.1f} kg to reach the healthy range."
            elif low_bmi <= bmi <= high_bmi:
                status = "Perfect (Healthy)"
                suggestion = "Great job! Your weight is within the healthy range."
            else:
                status = "High (Overweight/Obese)"
                suggestion = f"You need to lose at least {weight - max_weight:.1f} kg to reach the healthy range."

            # Output results
            print(f"\nYour BMI is {bmi:.2f}. Based on your age {age}:")
            print(f" Your weight is {status}.")
            print(f" Healthy weight range for your height: {min_weight:.1f} kg – {max_weight:.1f} kg")
            print(f" Suggestion: {suggestion}")

        except ValueError:
            print("Please enter valid numbers for age, height, and weight.")

        # Replay option
        again = input("\nDo you want to check another person? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for using the program! Goodbye ")
            break

# Run the program
check_weight_status()