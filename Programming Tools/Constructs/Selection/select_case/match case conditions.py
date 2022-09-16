examScore = 90

match examScore:
    case examScore if examScore > 90:
        print("Grade A")
    case examScore if examScore > 80:
        print("Grade B")