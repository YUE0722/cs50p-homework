x = input("What is the Anwser to the Great Question of Life, the Universe and Everything? ")
match x:
    case "42" | "forty-two" | "forty two":
        print("yes")
    case _ :
        print("No")


