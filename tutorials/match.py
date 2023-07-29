while True:
    user_blood_type = input("Enter your blood type: ")

    match user_blood_type.upper():
        case "AB":
            print("you can take from any blood type")
        case "O":
            print("you can just take from O blood type and you can give any other blood type")
        case "A":
            print("you can take from A and O and give AB and A")
        case "B":
            print("you can take from B and O and give AB and B")
        case other:
            print(f"{other} blood type is not defind")