#wachtwoord generator
import random
import math
keuze = raw_input("1. Number generator \n2. Letter generator \n3. Letter/getallen generator\n4. Letter+Hoofdletter/getallen generator\n5. Letter+Hoofdletter/getallen/symbol generator\n>")
if (keuze == '1'):
    numbers = input("Lengte van je wachtwoord\n>")
    nums = ['1','2','3','4','5','6','7','8','9','0']
    c = int(10)**int(numbers)
    print("Zoveel combinaties zijn er met dit wachtwoord:")
    if (c > 60):
        c1 = (int(c)/ 60 / 100000)
        c2 = 'seconde over'
    if (c > 60*60*100000):
        c1 = (int(c)/ 60 / 60 / 100000)
        c2 = 'uren over'
    if (c > 60*60*24*100000):
        c1 = (int(c)/24/60/ 60 / 100000)
        c2 = 'dagen over'
    if (c > 60*60*24*365*100000):
        c1 = (int(c)/365/24/60/ 60 / 100000)
        c2 = 'jaren over'

    print("Hier doet men ongeveer", round(c1,4),c2)
    print("\n")
    print("Wachtwoord:")
    for x in range(10):
        ww = []
        for x in range(int(numbers)):
            ww.append(random.choice(nums))
        ww = ''.join(ww)
        print(ww)
    end = input("")
        
if (keuze == '2'):
    length = input('Lengte van je wachtwoord\n>')
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    c = int(26)**int(length)
    print("Zoveel combinaties zijn er met dit wachtwoord:")
    if (c > 60):
        c1 = (int(c)/ 60 / 100000)
        c2 = 'seconde over'
    if (c > 60*60*100000):
        c1 = (int(c)/ 60 / 60 / 100000)
        c2 = 'uren over'
    if (c > 60*60*24*100000):
        c1 = (int(c)/24/60/ 60 / 100000)
        c2 = 'dagen over'
    if (c > 60*60*24*365*100000):
        c1 = (int(c)/365/24/60/ 60 / 100000)
        c2 = 'jaren over'
    print(c1,c2)

    print(c)
    print("Hier doet men ongeveer", round(c1,4),c2)
    print("\n")
    print("Wachtwoord:")
    for x in range(10):
        ww = []
        for x in range(int(length)):
            ww.append(random.choice(abc))
        ww = ''.join(ww)
        print(ww)
    end = input("")
    
if (keuze == '3'):
    length = input('Lengte van je wachtwoord\n>')
    abc123 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    c = int(len(abc123))**int(length)
    print("Zoveel combinaties zijn er met dit wachtwoord:")
    if (c > 60):
        c1 = (int(c)/ 60 / 100000)
        c2 = 'seconde over'
    if (c > 60*60*100000):
        c1 = (int(c)/ 60 / 60 / 100000)
        c2 = 'uren over'
    if (c > 60*60*24*100000):
        c1 = (int(c)/24/60/ 60 / 100000)
        c2 = 'dagen over'
    if (c > 60*60*24*365*100000):
        c1 = (int(c)/365/24/60/ 60 / 100000)
        c2 = 'jaren over'
    print(c1,c2)

    print(c)
    print("Hier doet men ongeveer", round(c1,4),c2)
    print("\n")
    print("Wachtwoord:")
    for x in range(10):
        ww = []
        for x in range(int(length)):
            ww.append(random.choice(abc123))
        ww = ''.join(ww)
        print(ww)
    end = input("")
    
if (keuze == '4'):
    length = input('Lengte van je wachtwoord\n>')
    abc123ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    c = int(len(abc123ABC))**int(length)
    print("Zoveel combinaties zijn er met dit wachtwoord:")
    if (c > 60):
        c1 = (int(c)/ 60 / 100000)
        c2 = 'seconde over'
    if (c > 60*60*100000):
        c1 = (int(c)/ 60 / 60 / 100000)
        c2 = 'uren over'
    if (c > 60*60*24*100000):
        c1 = (int(c)/24/60/ 60 / 100000)
        c2 = 'dagen over'
    if (c > 60*60*24*365*100000):
        c1 = (int(c)/365/24/60/ 60 / 100000)
        c2 = 'jaren over'
    print(c1,c2)

    print(c)
    print("Hier doet men ongeveer", round(c1,4),c2)
    print("\n")
    print("Wachtwoord:")
    for x in range(10):
        ww = []
        for x in range(int(length)):
            ww.append(random.choice(abc123ABC))
        ww = ''.join(ww)
        print(ww)
    end = input("")
    
if (keuze == '5'):
    length = input('Lengte van je wachtwoord\n>')
    abc123ABCtoken = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','^','&','*','(',')']
    c = int(len(abc123ABCtoken))**int(length)
    print("Zoveel combinaties zijn er met dit wachtwoord:")
    if (c > 60):
        c1 = (int(c)/ 60 / 100000)
        c2 = 'seconde over'
    if (c > 60*60*100000):
        c1 = (int(c)/ 60 / 60 / 100000)
        c2 = 'uren over'
    if (c > 60*60*24*100000):
        c1 = (int(c)/24/60/ 60 / 100000)
        c2 = 'dagen over'
    if (c > 60*60*24*365*100000):
        c1 = (int(c)/365/24/60/ 60 / 100000)
        c2 = 'jaren over'
    print(c1,c2)

    print(c)
    print("Hier doet men ongeveer", round(c1,4),c2)
    print("\n")
    print("Wachtwoord:")
    for x in range(10):
        ww = []
        for x in range(int(length)):
            ww.append(random.choice(abc123ABCtoken))
        ww = ''.join(ww)
        print(ww)
    end = input("")
