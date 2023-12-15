def validate_cnp(cnp):

    cnp = str(cnp)
    gender = int(cnp[0])
    year = int(cnp[1:3])
    month = int(cnp[3:5])
    day = int(cnp[5:7])
    place = int(cnp[7:9])
    
    if not (1 <= gender <= 8):
    # if gender not in [1, 2, 3, 4, 5, 6, 7, 8]:
        return False
    
    if not (0 <= year <= 99):
        return False
    
    if not (1 <= month <= 12):
        return False

    if not (1 <= day <= 31):
        return False

    #verificare zile pentru luni specifice cu 30 zile + februarie
    if (month in [4, 6, 9, 11] and day > 30) or (month == 2 and day > 29):
        return False
    
    #regula an bisect : 
    # daca anul ESTE divizibil cu 4 si NU este divizibil si cu 100 este an bisect. 
    # daca este totusi divizibil SI cu 4 SI cu 100 atunci TREBUIE sa fie divizibil SI cu 400 ca sa fie an bisect
    # verificare data: 29.09.anbisect --> daca e 29 februarie si not <an bisect> --> return False
    if month == 2 and day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return False

    if not (1 <= place <= 48):
        return False

    control_cnp = cnp[:-1]
    const = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    total = [int(dig) * const[i] for i, dig in enumerate(control_cnp)] 
    total = sum(total) % 11
    if total == 10:
        total = 1

    if total != int(cnp[12]):
        return False

    return True

def validate_input(input_function):
    def input_wrap():
        while True:
            cnp_input = input("Enter a 13-digit CNP (or type 'exit' to quit): ")

            if cnp_input.lower() == "exit":
                break

            if not cnp_input.isdigit() or len(cnp_input) != 13:
                print("Invalid input. Please enter a 13-digit CNP.")
                continue 
            input_function(cnp_input)
            
    return input_wrap

@validate_input
def process_cnp(cnp):
    result = {
        "gender": cnp[0],
        "year": cnp[1:3],
        "month": cnp[3:5],
        "day": cnp[5:7],
        "place": cnp[7:9],
        "numbers": cnp[9:12],
        "control": cnp[-1]
    }
    if int(result["gender"]) % 2 == 0:
        result["gender"] = "F"
    else:
        result["gender"] = "M"
    #same method for every key that has to represent "place" or "month"
    
    if validate_cnp(cnp):
        print("\n===CNP RESULT===\n")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print("Invalid CNP!")

process_cnp()
