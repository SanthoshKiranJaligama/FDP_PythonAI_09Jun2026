import os
import sys

def calculate_risk(attendance, internal_score, assignment_score, threshold):
    """
    Calculates a weighted normalized performance score (0 to 1) and classifies
    the student as either 'safe' or 'at_risk'.
    
    Weights:
      - Attendance: 30%
      - Internal score: 40%
      - Assignment score: 30%
    """
    score = (attendance * 0.3 + internal_score * 0.4 + assignment_score * 0.3) / 100.0
    label = "safe" if score >= threshold else "at_risk"
    return {
        "environment": os.environ.get("APP_ENV", "dev"),
        "score": round(score, 3),
        "threshold": threshold,
        "label": label
    }

def get_input(prompt_text, default_val, min_val=0.0, max_val=100.0):
    while True:
        try:
            val = input(f"{prompt_text} [{default_val}]: ").strip()
            if not val:
                return default_val
            num = float(val)
            if min_val <= num <= max_val:
                return num
            else:
                print(f"Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Please enter a valid numeric value.")

def main():
    app_env = os.environ.get("APP_ENV", "dev")
    app_env_lower = app_env.lower()
    
    # Pick default threshold based on selected environment
    if app_env_lower == "test":
        default_threshold = 0.7
    elif app_env_lower == "dev":
        default_threshold = 0.5
    else:
        default_threshold = 0.6

    threshold_str = os.environ.get("MODEL_THRESHOLD")
    if threshold_str is not None:
        try:
            threshold = float(threshold_str)
        except ValueError:
            threshold = default_threshold
    else:
        threshold = default_threshold

    print(f"Environment: {app_env}")
    print(f"Model Threshold: {threshold}")

    # Check for CLI arguments or interactive prompting
    attendance = 62.0
    internal_score = 58.0
    assignment_score = 70.0

    # Non-interactive check (standard input is not a TTY or running in CI)
    is_interactive = sys.stdin.isatty() and not os.environ.get("CI")

    if is_interactive:
        print("\n--- Student Risk Predictor Input Configuration ---")
        choice = input("Do you want to use the default demo values (Attendance=62, Internal=58, Assignment=70)? [Y/n]: ").strip().lower()
        if choice in ["n", "no"]:
            print("Please enter custom values (0 to 100):")
            attendance = get_input("  Attendance", 62.0)
            internal_score = get_input("  Internal assessment score", 58.0)
            assignment_score = get_input("  Assignment score", 70.0)
        else:
            print("Using default demo values.")
    else:
        # Check CLI arguments if any
        if len(sys.argv) >= 4:
            try:
                attendance = float(sys.argv[1])
                internal_score = float(sys.argv[2])
                assignment_score = float(sys.argv[3])
                print(f"Using values from command-line arguments: Attendance={attendance}, Internal={internal_score}, Assignment={assignment_score}")
            except ValueError:
                print("Invalid command line arguments. Using default demo values.")
        else:
            print("Non-interactive mode or arguments missing. Using default demo values: Attendance=62, Internal=58, Assignment=70")

    result = calculate_risk(attendance, internal_score, assignment_score, threshold)

    print("\n--- Prediction Results ---")
    print(f"Attendance Score  : {attendance}%")
    print(f"Internal Score    : {internal_score}%")
    print(f"Assignment Score  : {assignment_score}%")
    print(f"Weighted Score    : {result['score']:.3f}")
    print(f"Threshold Applied : {result['threshold']}")
    print(f"Result Label      : {result['label'].upper()}")
    print("--------------------------")
    print(f"Output Dictionary : {result}\n")
    
    return result

if __name__ == "__main__":
    main()
