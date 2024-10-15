def calculate_bmi(weight, height):
    """Calculate BMI using the formula: BMI = weight / (height ** 2)"""
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """Classify BMI into categories with emojis."""
    if bmi < 18.5:
        return "Underweight 🥗"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight 🏋️‍♂️"
    elif 25 <= bmi < 29.9:
        return "Overweight 🍔"
    else:
        return "Obesity 🏥"

def get_health_tips(category):
    """Provide health tips based on BMI category."""
    tips = {
        "Underweight 🥗": "You might want to eat more nutritious meals and consult a healthcare provider.",
        "Normal weight 🏋️‍♂️": "Great job! Keep maintaining a balanced diet and regular exercise.",
        "Overweight 🍔": "Consider incorporating more physical activity and a balanced diet into your routine.",
        "Obesity 🏥": "It's advisable to consult with a healthcare provider for personalized advice."
    }
    return tips.get(category, "Invalid category")

def get_valid_input(prompt, input_type=float):
    """Ensure valid numerical input from the user."""
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def convert_units(weight, height):
    """Convert feet to meters for height."""
    height = height * 0.3048  # Convert feet to meters
    return weight, height

def main():
    while True:
        print("\n--- BMI Calculator ---")
        
        # Get weight in kilograms
        weight = get_valid_input("Enter your weight in kilograms: ")
        
        # Get height in feet
        height = get_valid_input("Enter your height in feet: ")
        
        # Convert units (feet to meters)
        weight, height = convert_units(weight, height)
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Classify BMI result
        category = classify_bmi(bmi)
        
        # Display the result
        print(f"\nYour BMI is: {bmi:.2f} 😊")
        print(f"Your BMI places you in the {category} category.")
        
        # Provide health tips based on BMI category
        tips = get_health_tips(category)
        print(f"Health Tips: {tips}")
        
        # Ask if the user wants to calculate another BMI
        repeat = input("\nDo you want to calculate another BMI? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Thank you for using the BMI calculator! 👋")
            break

if __name__ == "__main__":
    main()                