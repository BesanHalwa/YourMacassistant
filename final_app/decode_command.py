def decode(command):
    command.lower()
    operation1 = command.find('read')
    operation2 = command.find('send mail')
    operation3 = command.find('looking at')
    operation4 = command.find('where')
    operation5 = max(command.find('wikipedia'), command.find('wiki'), command.find('search'))
    operation6 = max(command.find('in frame'), command.find('in the frame'))
    operation7 = max(command.find('music'), command.find('play'), command.find('songs'), )
    operation8 = command.find('news')

    if (operation1 > -1):
        return 1
    elif (operation2 > -1):
        return 2
    elif (operation3 > -1):
        return 3
    elif (operation4 > -1):
        return 4
    elif (operation5 > -1):
        return 5
    elif (operation6 > -1):
        return 6
    elif (operation7 > -1):
        return 7
    elif (operation8 > -1):
        return 8
    else:
        return -1
