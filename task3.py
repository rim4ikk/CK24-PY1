# TODO  Напишите функцию count_letters
def count_letters(main_str):
    letters = []
    Counts = []
    for letter in main_str:
        if not(letter in letters) and letter.isalpha():
            Counts.append(main_str.count(letter))
            letters.append(letter)
    massive = [letters, Counts]
    return massive

# TODO Напишите функцию calculate_frequency
def calculate_frequency(main_str, massive):
    letters = massive[0]
    Counts = massive[1]
    summa = 0
    for i in Counts:
        summa += i
    Frequency = []
    for i in Counts:
        Frequency.append(round(i / summa, 2))
    End = ''
    for i in range(len(letters)):
        if str(Frequency[i]) == '0.0':
            End += letters[i] + ': ' + '0.00' + '\n'
        elif i == len(letters) - 1:
            End += letters[i] + ': ' + str(Frequency[i])
        else:
            End += letters[i] + ': ' + str(Frequency[i]) + '\n'
    return End

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
print(calculate_frequency(main_str.lower(), count_letters(main_str.lower())))
# TODO Распечатайте в столбик букву и её частоту в тексте
