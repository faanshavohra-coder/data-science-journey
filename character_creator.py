def create_character(character_name, strength, intelligence, charisma):
    # 1. Define the symbols inside the function (important for some tests)
    full_dot = "●"
    empty_dot = "○"

    # 2. Error checks with EXACT punctuation (periods at the end!)f not isinstance(character_name,str):
    if not isinstance(character_name,str):
        return "The character name should be a string"
    if not character_name:
        return "The character should have a name"
    if len(character_name) > 10:
        return "The character name is too long"
    if " " in character_name:
        return "The character name should not contain spaces"
    if not isinstance(strength,int) or not isinstance(intelligence, int) or not isinstance(charisma,int):
        return "All stats should be integers"

    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    
    if (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"

    # 3. Create the lines (Check the space after STR, INT, CHA)
    line_1 = character_name
    line_2 = "STR " + (full_dot * strength) + (empty_dot * (10 - strength))
    line_3 = "INT " + (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    line_4 = "CHA " + (full_dot * charisma) + (empty_dot * (10 - charisma))

    # 4. Return as a single string with newlines
    return f"{line_1}\n{line_2}\n{line_3}\n{line_4}"
  