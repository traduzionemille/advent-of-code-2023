f = open("input-2.txt", "r")
games_list = (f.readlines())

red_cubes = 12
green_cubes = 13
blue_cubes = 14

game_IDs = []
IDs_possible_games = []


for game in games_list:
    game = game + '$'
    game_IDs = game.split()[1].replace(":", '')
    game_split = game.split(': ')
    game_split.pop(0)
    all_games = game_split[0]
    individual_games = all_games.split('; ')

    for reveal in individual_games:

        blue_total = 0
        red_total = 0
        green_total = 0
        individual_games_split = reveal.split()
        numbers = []
        colours = []

        for i in individual_games_split:

            if i.isdigit():
                numbers.append(int(i))
            else:
                colours.append(i)

        for colour in range(len(colours)):
            if 'blue' in colours[colour]:
                blue_total = blue_total + numbers[colour]
            if 'red' in colours[colour]:
                red_total = red_total + numbers[colour]
            if 'green' in colours[colour]:
                green_total = green_total + numbers[colour]
    
        if blue_total > blue_cubes or red_total > red_cubes or green_total > green_cubes:
            break
        elif '$' in i:
            IDs_possible_games.append(int(game_IDs))          

print("The sum of all game IDs is: ", sum(IDs_possible_games))
