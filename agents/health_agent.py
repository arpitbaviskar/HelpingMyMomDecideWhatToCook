def get_health_tags(health_preference):
    health_preference = health_preference.lower()
    if "low calorie" in health_preference or "weight loss" in health_preference:
        return ["light", "healthy"]
    elif "balanced" in health_preference:
        return ["balanced"]
    elif "high protein" in health_preference:
        return ["protein"]
    else:
        return []
