def calculate_love_score():
    name1 = input("What is the name of person 1?\n").lower()
    name2 = input("What is the name of person 2?\n").lower()
    
    combined_name = name1 + name2  # combine as string

    word1 = "TRUE"
    word2 = "LOVE"

    # Count total occurrences of letters from "TRUE"
    true_total = 0
    for letter in word1:
        count = combined_name.count(letter.lower())
        print(f"{letter} occurs {count} times.")
        true_total += count
    print(f"Total TRUE score = {true_total}\n")

    # Count total occurrences of letters from "LOVE"
    love_total = 0
    for letter in word2:
        count = combined_name.count(letter.lower())
        print(f"{letter} occurs {count} times.")
        love_total += count
    print(f"Total LOVE score = {love_total}\n")

    # Calculate love score
    love_score = int(str(true_total) + str(love_total))
    print(f"Love Score = {love_score}")

calculate_love_score()