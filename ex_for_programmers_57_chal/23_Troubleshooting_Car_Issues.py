a = input('Is the car silent when you turn the key?[y/n]: ')[0].lower()
print(a)
match a:
    case 'y':
        b = input ('Are the battery terminals corroded?[y/n]: ')[0].lower()
        match b:
            case 'y':
                print('Clean terminals and try starting again')
            case 'n':
                print('Replace cables and try again')
    case 'n':
        c = input('Does the car make a clicking noise?[y/n]: ')[0].lower()
        match c:
            case 'y':
                print('Replace the battery')
            case 'n':
                d = input('Does the car crank up but fail to start?[y/n]: ')[0].lower()
                match d:
                    case 'y':
                        print('Check spark plug connections')
                    case 'n':
                        e = input('Does the engine start and then die?[y/n]: ')[0].lower()
                        match e:
                            case 'y':
                                f = input('Does your car have fuel injection?[y/n]: ')[0].lower()
                                match f:
                                    case 'y':
                                        print('Get it in for service.')
                                    case 'n':
                                        print('Check to ensure the choke is opening and closing')
                            case 'n':
                                print('Get it in for service.')
                        