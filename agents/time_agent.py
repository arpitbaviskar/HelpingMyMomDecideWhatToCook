def get_time_based_filter(time_of_day):
    if time_of_day == "morning":
        return ["quick", "light", "morning"]
    elif time_of_day == "afternoon":
        return ["normal", "balanced", "afternoon"]
    elif time_of_day == "evening":
        return ["light", "snack", "evening"]
    else:
        return []
