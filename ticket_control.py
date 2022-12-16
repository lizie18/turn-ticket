from enums import Areas


# def format_ticket(f):
#     def add_title_footer(area_selected):
#         print('Hello, yor turn is:')
#         return get_ticket_number(area_selected)
#         print('Thanks for your visit!')
#     return add_title_footer
#
#
# @format_ticket
def get_ticket_number(area_enum):
    areas_control = {}
    area_selected = area_enum.name.lower()
    for area_item in Areas:
        areas_control[area_item.name.lower()] = 1
    while True:
        yield areas_control[area_selected]
        areas_control[area_selected] += 1

# pharmacy_turn = get_ticket_number(Areas.PHARMACY)
# perfumery_turn = get_ticket_number(Areas.PERFUMERY)
# cosmetics_turn = get_ticket_number(Areas.COSMETICS)
#
# print(next(pharmacy_turn))
# print(next(perfumery_turn))
# print(next(pharmacy_turn))
# print(next(pharmacy_turn))
# print(next(pharmacy_turn))
# print(next(perfumery_turn))
# print(next(cosmetics_turn))
