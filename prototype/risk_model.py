# Simple prototype for TryggAI risk scoring

def risk_score(lighting, incidents, activity_level):
    """
    Calculates a simple risk score based on:
    - lighting: 0 = dark, 1 = good lighting
    - incidents: number of incidents in area
    - activity_level: 0 = empty streets, 1 = active area
    """

    score = 0

    if lighting == 0:
        score += 2
    if incidents > 0:
        score += incidents * 0.5
    if activity_level == 0:
        score += 1

    return score


# Example usage
if __name__ == "__main__":
    print("Low lighting, 3 incidents, empty street → risk score:",
          risk_score(0, 3, 0))
