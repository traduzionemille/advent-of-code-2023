f = open("input-2.txt", "r")
games_list = (f.readlines())

power_list = []

for game in games_list:
    game_IDs = game.split()[1].replace("", '')
    game_split = game.split(': ')
    game_split.pop(0)
    game_string = game.split()
    game_string.pop(0)
    game_string.pop(0)
    new_numbers = []
    new_colours = []
    
    for item in game_string:
            
        blue_list = []
        red_list = []
        green_list = []

        if item.isdigit():
            new_numbers.append(int(item))
        else:
            new_colours.append(item)
        
    for colour in range(len(new_colours)):

        if 'blue' in new_colours[colour]:
            blue_list.append(new_numbers[colour])
        if 'red' in new_colours[colour]:
            red_list.append(new_numbers[colour])
        if 'green' in new_colours[colour]:
            green_list.append(new_numbers[colour])

    a = max(blue_list)
    b = max(green_list)
    c = max(red_list)

    power = a * b * c
    power_list.append(power)

sum_power = sum(power_list)
print('The sum of the powers is: ', sum_power)
