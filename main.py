import ticket_control
from enums import Areas


def generate_ticket():
    continue_program = True
    tickets_control = []
    for area in Areas:
        tickets_control.append(ticket_control.get_ticket_number(area))
    while continue_program:
        area_selected = get_area_selected()
        if area_selected == 0:
            continue
        print('================================================================')
        print(f'Tienes el turno: {next(tickets_control[area_selected])}')
        print('================================================================')
        ask_next = input('Press N to finish, or any key to continue ')
        continue_program = False if ask_next.lower() == 'n' else True


def get_area_selected():
    print('Store available areas: ')
    for area in Areas:
        print(f'{area.value} {area.name.title()}')
    area_selected = input('Enter area do you want to visit: ')
    try:
        if not 0 < int(area_selected) <= len(list(Areas)):
            print('Area entered doesn\'t exist')
            return 0
    except ValueError:
        print('Invalid area!')
        return 0

    return int(area_selected)


generate_ticket()
