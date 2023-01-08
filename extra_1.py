types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

result = {}


def remove_duplicates(my_dict):
    tmp_list = []
    for key in my_dict:
        tmp_tickets = []
        for ticket in my_dict[key]:
            if ticket not in tmp_list:
                tmp_list.append(ticket)
                tmp_tickets.append(ticket)
        my_dict[key] = tmp_tickets
    return my_dict


def link_tickets_to_types(my_dict):
    result_dict = {}
    for key in my_dict:
        for key_type in types:
            if key == key_type:
                result_dict[types[key_type]] = my_dict[key]
    return result_dict

print(link_tickets_to_types(remove_duplicates(tickets)))