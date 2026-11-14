import math
import string


def analyze_password(password):
    score = 0
    feedback = []

    checks = {
        "At least 8 characters": len(password) >= 8,
        "At least 12 characters": len(password) >= 12,
        "Lowercase letters": any(c.islower() for c in password),
        "Uppercase letters": any(c.isupper() for c in password),
        "Numbers": any(c.isdigit() for c in password),
        "Special characters": any(c in string.punctuation for c in password)
    }

    for check, passed in checks.items():
        if passed:
            score += 1
        else:
            if check == "At least 8 characters":
                feedback.append("Use at least 8 characters.")
            elif check == "At least 12 characters":
                feedback.append("Use 12 or more characters.")
            else:
                feedback.append(f"Add {check.lower()}.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback,
        "checks": checks
    }
