# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separ = ','):
    all_participants = []
    for a in participants_first_group:
        for b in participants_second_group:
            if a == b:
                if all_participants == []:
                    all_participants.append(a)
                else:
                    for c in all_participants:
                        if a != c:
                            all_participants.append(a)
    return sorted(all_participants)



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
for i in participants_first_group:
    if ord(i) < ord('А') or ord(i) > ord('я'):
        separator = i
        break
participants_first_group = participants_first_group.split(separator)
participants_second_group = participants_second_group.split(separator)
print(find_common_participants(participants_first_group, participants_second_group, separ = ','))
# TODO Провеьте работу функции с разделителем отличным от запятой