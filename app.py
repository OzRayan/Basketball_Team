import os
import time

import prompt as pt
import constants as con


TEAMS = {}
PLAYERS = [player for player in con.PLAYERS]


def clean():
    """Clean console"""
    os.system('cls' if os.name == 'nt' else 'clear')


def exit_():
    """Exit program and cleaning the console"""
    print(pt.prompt_bye)
    time.sleep(1.3)
    clean()
    exit()


def teams(arg):
    """Extend PANTHER, BANDITS, WARRIORS teams with players
    equally dividing between experienced and inexperienced
    :param: - arg - list of all players
    """
    # Sorting players by experience
    experienced = [i for i in arg if i['experience'] == 'YES']
    inexperienced = [i for i in arg if i['experience'] == 'NO']
    # Add experienced players to teams
    for e in range(1, 4):
        TEAMS[e] = [experienced.pop() for _ in 'len']
        TEAMS[e].extend([inexperienced.pop() for _ in 'len'])


def prepare_data(arg, num):
    """Prepares a list of data for -num- team
    :param: -arg - list of players from a certain team
            -num - team index
    :return: -list_ - list of team data for printout
    """
    guardians, list_ = [], []
    replace_ = ', \n\t, ', ',\n\t'
    team, a, g = '', ' and ', 'guardians'
    if num == 1:
        team = 'Panthers'
    elif num == 2:
        team = 'Bandits'
    else:
        team = 'Warriors'
    # Split up multiple guardians at ' and '
    items = [i[g] if a not in i[g] else i[g].split(a) for i in arg]
    # Make sure names are string, not list
    for item in items:
        if len(guardians) == 6:
            guardians.append('\n\t')
        if type(item) == list:
            guardians.extend([x for x in item])
        if type(item) == str:
            guardians.append(item)

    yes = [i for i in arg if i['experience'] == 'YES']
    no = [i for i in arg if i['experience'] == 'NO']

    # POPULATE list_ AS FOLLOWS:
    # team name {0}, 2 x horizontal lines {1}{2},
    # total players {3}, 2 x in/experienced players {4}{5}
    # average height {6}, guardians name {7}, players name {8}
    list_.extend([
        team, '-' * (12 + len(team)), '-' * 23,
        len(items), len(yes), len(no),
        round(sum(int(i['height'].split()[0]) for i in arg) / len(arg), 2),
        ', '.join(i for i in guardians).replace(*replace_),
        ', '.join(i['name'].strip() for i in arg)
    ])
    return list_


def main():
    """Main menu for stats tool"""
    teams(PLAYERS)
    clean()
    while 1:
        try:
            menu_choice = int(input(pt.prompt_main))
            if menu_choice == 2:
                exit_()
            elif menu_choice == 1:
                clean()
                while 1:
                    try:
                        option_choice = int(input(
                            pt.prompt_options.format(*con.TEAMS)))
                        if option_choice == 4:
                            clean()
                            break
                        elif option_choice in TEAMS.keys():
                            clean()
                            input(pt.prompt_team.format(
                                *prepare_data(TEAMS[option_choice], option_choice)))
                            clean()
                        else:
                            clean()
                            print("Choose from given numbers!")
                    except ValueError:
                        print(pt.prompt_error)
                    except KeyboardInterrupt:
                        exit_()
            else:
                clean()
                print("Choose from given numbers!")
        except ValueError:
            print(pt.prompt_error)
        except KeyboardInterrupt:
            exit_()


if __name__ == "__main__":
    main()

