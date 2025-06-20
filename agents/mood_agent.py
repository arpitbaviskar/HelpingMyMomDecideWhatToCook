def get_mood_tags(mood_input):
    mood_input = mood_input.lower()
    if "lazy" in mood_input:
        return ["lazy", "light"]
    elif "unwell" in mood_input or "sick" in mood_input:
        return ["unwell", "comfort"]
    elif "happy" in mood_input:
        return ["normal"]
    else:
        return ["normal"]
