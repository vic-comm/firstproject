"""temp = int(input("what's the temperature "))
if temp <= int(10):
    print("it's a cold day")
elif int(50)>= temp >=int(11):
    print("it's a hot day")
elif temp > 50:
    print("it's dangerously hot")
else :
    print("it's dangerously cold")"""
name = input("what's your name\n").strip()
match name:
    case "victor" | "christiana":
        print("obiezue")
    case 'emmanuel':
        print("sunday")
    case "emmanel":
        print("chukuma")
