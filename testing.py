def get_name_and_gender():
    last_name = input("What is your last name? ")
    gender = input("Are you male or female (m/f)? ")
    return last_name, gender

def display_name(last_name, gender):
    if gender == "f":
        title = "Ms."
    else:
        title = "Mr."
    print(f"Hello, {title} {last_name}")

def get_birth_year():
    birth_year = input("What year were you born? ")
    return birth_year

def main():
    print(f"You will turn {2026 - int(get_birth_year())} this year.")

main()