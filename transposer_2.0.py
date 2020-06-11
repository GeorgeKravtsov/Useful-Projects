'***************************************************TRANSPOSER 2.0****************************************************'

am_notes = {'A': '1', 'Bb': '2', 'H': '3', 'C': '4', 'C#': '5', 'D': '6', 'Eb': '7', 'E': '8', 'F': '9', 'F#': '10', 'G': '11', 'G#': '12'}
bbm_notes = {'Bb': '1', 'H': '2', 'C': '3', 'Db': '4', 'D': '5', 'Eb': '6', 'E': '7', 'F': '8', 'Gb': '9', 'G': '10', 'Ab': '11', 'A': '12'}
hm_notes = {'H': '1', 'C': '2', 'C#': '3', 'D': '4', 'D#': '5', 'E': '6', 'F': '7', 'F#': '8', 'G': '9', 'G#': '10', 'A': '11', 'A#': '12'}
cm_notes = {'C': '1', 'Db': '2', 'D': '3', 'Eb': '4', 'E': '5', 'F': '6', 'Gb': '7', 'G': '8', 'Ab': '9', 'A': '10', 'Bb': '11', 'H': '12'}
c_sharp_m_notes = {'C#': '1', 'D': '2', 'D#': '3', 'E': '4', 'F': '5', 'F#': '6', 'G': '7', 'G#': '8', 'A': '9', 'A#': '10', 'H': '11', 'C': '12'}
dm_notes = {'D': '1', 'Eb': '2', 'E': '3', 'F': '4', 'F#': '5', 'G': '6', 'Ab': '7', 'A': '8', 'Bb': '9', 'H': '10', 'C': '11', 'C#': '12'}
ebm_notes = {'Eb': '1', 'E': '2', 'F': '3', 'Gb': '4', 'G': '5', 'Ab': '6', 'A': '7', 'Bb': '8', 'H': '9', 'C': '10', 'Db': '11', 'D': '12'}
em_notes = {'E': '1', 'F': '2', 'F#': '3', 'G': '4', 'G#': '5', 'A': '6', 'Bb': '7', 'H': '8', 'C': '9', 'C#': '10', 'D': '11', 'D#': '12'}
fm_notes = {'F': '1', 'Gb': '2', 'G': '3', 'Ab': '4', 'A': '5', 'Bb': '6', 'H': '7', 'C': '8', 'Db': '9', 'D': '10', 'Eb': '11', 'E': '12'}
f_sharp_m_notes = {'F#': '1', 'G': '2', 'G#': '3', 'A': '4', 'A#': '5', 'H': '6', 'C': '7', 'C#': '8', 'D': '9', 'D#': '10', 'E': '11', 'F': '12'}
gm_notes = {'G': '1', 'Ab': '2', 'A': '3', 'Bb': '4', 'H': '5', 'C': '6', 'Db': '7', 'D': '8', 'Eb': '9', 'E': '10', 'F': '11', 'F#': '12'}
g_sharp_m_notes = {'G#': '1', 'A': '2', 'A#': '3', 'H': '4', 'C': '5', 'C#': '6', 'D': '7', 'D#': '8', 'E': '9', 'F': '10', 'F#': '11', 'G': '12'}

am_steps = {'1': 'A', '2': 'Bb', '3': 'H', '4': 'C', '5': 'C#', '6': 'D', '7': 'Eb', '8': 'E', '9': 'F', '10': 'F#', '11': 'G', '12': 'G#'}
bbm_steps = {'1': 'Bb', '2': 'H', '3': 'C', '4': 'Db', '5': 'D', '6': 'Eb', '7': 'E', '8': 'F', '9': 'Gb', '10': 'G', '11': 'Ab', '12': 'A'}
hm_steps = {'1': 'H', '2': 'C', '3': 'C#', '4': 'D', '5': 'D#', '6': 'E', '7': 'F', '8': 'F#', '9': 'G', '10': 'G#', '11': 'A', '12': 'A#'}
cm_steps = {'1': 'C', '2': 'Db', '3': 'D', '4': 'Eb', '5': 'E', '6': 'F', '7': 'Gb', '8': 'G', '9': 'Ab', '10': 'A', '11': 'Bb', '12': 'H'}
c_sharp_m_steps = {'1': 'C#', '2': 'D', '3': 'D#', '4': 'E', '5': 'F', '6': 'F#', '7': 'G', '8': 'G#', '9': 'A', '10': 'A#', '11': 'H', '12': 'C'}
dm_steps = {'1': 'D', '2': 'Eb', '3': 'E', '4': 'F', '5': 'F#', '6': 'G', '7': 'Ab', '8': 'A', '9': 'Bb', '10': 'H', '11': 'C', '12': 'C#'}
ebm_steps = {'1': 'Eb', '2': 'E', '3': 'F', '4': 'Gb', '5': 'G', '6': 'Ab', '7': 'A', '8': 'Bb', '9': 'H', '10': 'C', '11': 'Db', '12': 'D'}
em_steps = {'1': 'E', '2': 'F', '3': 'F#', '4': 'G', '5': 'G#', '6': 'A', '7': 'Bb', '8': 'H', '9': 'C', '10': 'C#', '11': 'D', '12': 'D#'}
fm_steps = {'1': 'F', '2': 'Gb', '3': 'G', '4': 'Ab', '5': 'A', '6': 'Bb', '7': 'H', '8': 'C', '9': 'Db', '10': 'D', '11': 'Eb', '12': 'E'}
f_sharp_m_steps = {'1': 'F#', '2': 'G', '3': 'G#', '4': 'A', '5': 'A#', '6': 'H', '7': 'C', '8': 'C#', '9': 'D', '10': 'D#', '11': 'E', '12': 'F'}
gm_steps = {'1': 'G', '2': 'Ab', '3': 'A', '4': 'Bb', '5': 'H', '6': 'C', '7': 'Db', '8': 'D', '9': 'Eb', '10': 'E', '11': 'F', '12': 'F#'}
g_sharp_m_steps = {'1': 'G#', '2': 'A', '3': 'A#', '4': 'H', '5': 'C', '6': 'C#', '7': 'D', '8': 'D#', '9': 'E', '10': 'F', '11': 'F#', '12': 'G'}

c_notes = {'C': '1', 'Db': '2', 'D': '3', 'Eb': '4', 'E': '5', 'F': '6', 'Gb': '7', 'G': '8', 'Ab': '9', 'A': '10', 'Bb': '11', 'H': '12'}
db_notes = {'Db': '1', 'D': '2', 'Eb': '3', 'E': '4', 'F': '5', 'Gb': '6', 'G': '7', 'Ab': '8', 'A': '9', 'Bb': '10', 'H': '11', 'C': '12'}
d_notes = {'D': '1', 'Eb': '2', 'E': '3', 'F': '4', 'F#': '5', 'G': '6', 'Ab': '7', 'A': '8', 'Bb': '9', 'H': '10', 'C': '11', 'C#': '12'}
eb_notes = {'Eb': '1', 'E': '2', 'F': '3', 'Gb': '4', 'G': '5', 'Ab': '6', 'a': '7', 'Bb': '8', 'H': '9', 'C': '10', 'Db': '11', 'D': '12'}
e_notes = {'E': '1', 'F': '2', 'F#': '3', 'G': '4', 'G#': '5', 'A': '6', 'Bb': '7', 'H': '8', 'C': '9', 'C#': '10', 'D': '11', 'D#': '12'}
f_notes = {'F': '1', 'Gb': '2', 'G': '3', 'Ab': '4', 'A': '5', 'Bb': '6', 'H': '7', 'C': '8', 'Db': '9', 'D': '10', 'Eb': '11', 'E': '12'}
f_sharp_notes = {'F#': '1', 'G': '2', 'G#': '3', 'A': '4', 'A#': '5', 'H': '6', 'C': '7', 'C#': '8', 'D': '9', 'D#': '10', 'E': '11', 'F': '12'}
g_notes = {'G': '1', 'Ab': '2', 'A': '3', 'Bb': '4', 'H': '5', 'C': '6', 'Db': '7', 'D': '8', 'Eb': '9', 'E': '10', 'F': '11', 'F#': '12'}
ab_notes = {'Ab': '1', 'A': '2', 'Bb': '3', 'H': '4', 'C': '5', 'Db': '6', 'D': '7', 'Eb': '8', 'E': '9', 'F': '10', 'Gb': '11', 'G': '12'}
a_notes = {'A': '1', 'Bb': '2', 'H': '3', 'C': '4', 'C#': '5', 'D': '6', 'Eb': '7', 'E': '8', 'F': '9', 'F#': '10', 'G': '11', 'G#': '12'}
bb_notes = {'Bb': '1', 'H': '2', 'C': '3', 'Db': '4', 'D': '5', 'eb': '6', 'E': '7', 'F': '8', 'Gb': '9', 'G': '10', 'Ab': '11', 'A': '12'}
h_notes = {'H': '1', 'C': '2', 'C#': '3', 'D': '4', 'D#': '5', 'E': '6', 'F': '7', 'F#': '8', 'G':'9', 'G#': '10', 'A': '11', 'A#': '12'}

c_steps = {'1': 'C', '2': 'Db', '3': 'D', '4': 'Eb', '5': 'E', '6': 'F', '7': 'Gb', '8': 'G', '9': 'Ab', '10': 'A', '11': 'Bb', '12': 'H'}
db_steps = {'1': 'Db', '2': 'D', '3': 'Eb', '4': 'E', '5': 'F', '6': 'Gb', '7': 'G', '8': 'Ab', '9': 'A', '10': 'Bb', '11': 'H', '12': 'C'}
d_steps = {'1': 'D', '2': 'Eb', '3': 'E', '4': 'F', '5': 'F#', '6': 'G', '7': 'Ab', '8': 'A', '9': 'Bb', '10': 'H', '11': 'C', '12': 'C#'}
eb_steps = {'1': 'Eb', '2': 'E', '3': 'F', '4': 'Gb', '5': 'G', '6': 'Ab', '7': 'a', '8': 'Bb', '9': 'H', '10': 'C', '11': 'Db', '12': 'D'}
e_steps = {'1': 'E', '2': 'F', '3': 'F#', '4': 'G', '5': 'G#', '6': 'A', '7': 'Bb', '8': 'H', '9': 'C', '10': 'C#', '11': 'D', '12': 'D#'}
f_steps = {'1': 'F', '2': 'Gb', '3': 'G', '4': 'Ab', '5': 'A', '6': 'Bb', '7': 'H', '8': 'C', '9': 'Db', '10': 'D', '11': 'Eb', '12': 'E'}
f_sharp_steps = {'1': 'F#', '2': 'G', '3': 'G#', '4': 'A', '5': 'A#', '6': 'H', '7': 'C', '8': 'C#', '9': 'D', '10': 'D#', '11': 'E', '12': 'F'}
g_steps = {'1': 'G', '2': 'Ab', '3': 'A', '4': 'Bb', '5': 'H', '6': 'C', '7': 'Db', '8': 'D', '9': 'Eb', '10': 'E', '11': 'F', '12': 'F#'}
ab_steps = {'1': 'Ab', '2': 'A', '3': 'Bb', '4': 'H', '5': 'C', '6': 'Db', '7': 'D', '8': 'Eb', '9': 'E', '10': 'F', '11': 'Gb', '12': 'G'}
a_steps = {'1': 'A', '2': 'Bb', '3': 'H', '4': 'C', '5': 'C#', '6': 'D', '7': 'Eb', '8': 'E', '9': 'F', '10': 'F#', '11': 'G', '12': 'G#'}
bb_steps = {'1': 'Bb', '2': 'H', '3': 'C', '4': 'Db', '5': 'D', '6': 'eb', '7': 'E', '8': 'F', '9': 'Gb', '10': 'G', '11': 'Ab', '12': 'A'}
h_steps = {'1': 'H', '2': 'C', '3': 'C#', '4': 'D', '5': 'D#', '6': 'E', '7': 'F', '8': 'F#', '9': 'G', '10': 'G#', '11': 'A', '12': 'A#'}

print("""\t\t\tWelcome to TRANSPOSER 2.0!
* Type chords in lowercase.
* Press Enter after empty string in invitation 'Enter chord: ' to get progression in a new key.""")

entered_user_chords = {}
steps = []                                      # список ступеней аккордовых символов, введённых пользователем
original_key = input('Original key: ').lower()
new_key = input('New key: ').lower()
counter = 0                  # автоинкрементный счётчик порядковых номеров аккордовых символов, введённых пользователем

while True:
    user_chord_in_process = input('Enter chord: ')
    entered_user_chords[counter] = (user_chord_in_process[0].upper() + user_chord_in_process[1:] if len(
        user_chord_in_process) > 1 else user_chord_in_process.upper())  # запись аккордов в словарь {счётчик:аккорд}
    counter += 1                                                        # с переводом первого символа в верхний регистр
    print('Chords in original key: ', [i for i in list(entered_user_chords.values()) if i])  # удаление пустой строки
    if user_chord_in_process == '':  # (полученной в результате нажатия Enter для вывода аккордов в новой тональности)
        break                        # из списка введённых аккордов, отображаемых в процессе ввода

entered_user_chords.popitem()        # удаление элемента {counter: ''}
chord_tails = {}                     # {number(counter): tail} ({счётчик: "хвост("окончание")" аккорда})
chords_no_tails = []                 # аккорды без "окончаний"

for number, chord in entered_user_chords.items():
    if len(chord) == 1:
        chords_no_tails.append(chord)
    elif len(chord) == 2 and (chord[1] == 'b' or chord[1] == '#'):
        chords_no_tails.append(chord)
    elif len(chord) >= 2 and (chord[1] != 'b' or chord[1] != '#'):
        chord_tails[number] = chord[1:]
        chords_no_tails.append(chord[0])
    elif len(chord) > 2 and (chord[1] == 'b' or chord[1] == '#'):
        chord_tails[number] = chord[2:]
        chords_no_tails.append(chord[:2])

for symbol in chords_no_tails:          # словари, имена которых заканчиваются на _notes, состоят из элементов, ключами
    if original_key == 'am':            # которых являются аккордовые символы, значениями-номера ступеней лада, соответ-
        steps.append(am_notes[symbol])  # ствующих этим символам
    elif original_key == 'bbm':
        steps.append(bbm_notes[symbol])
    elif original_key == 'hm':
        steps.append(hm_notes[symbol])  # каждый аккордовый символ из списка сопоставляется со ступенью, которой он со-
    elif original_key == 'cm':          # ответствует в тональности, указанной пользователем как 'Original key'
        steps.append(cm_notes[symbol])
    elif original_key == 'c#m':
        steps.append(c_sharp_m_notes[symbol])
    elif original_key == 'dm':          # в результате получаются ступени введённых пользователем аккордовых символов,
        steps.append(dm_notes[symbol])  # которые вносятся в список ступеней для последующего сопоставления их с аккор-
    elif original_key == 'ebm':         # довыми символами в тональности, указанной пользователем как 'New key'
        steps.append(ebm_notes[symbol])
    elif original_key == 'em':
        steps.append(em_notes[symbol])
    elif original_key == 'fm':
        steps.append(fm_notes[symbol])
    elif original_key == 'f#m':
        steps.append(f_sharp_m_notes[symbol])
    elif original_key == 'gm':
        steps.append(gm_notes[symbol])
    elif original_key == 'g#m':
        steps.append(g_sharp_m_notes[symbol])
    elif original_key == 'c':
        steps.append(c_notes[symbol])
    elif original_key == 'db':
        steps.append(db_notes[symbol])
    elif original_key == 'd':
        steps.append(d_notes[symbol])
    elif original_key == 'eb':
        steps.append(eb_notes[symbol])
    elif original_key == 'e':
        steps.append(e_notes[symbol])
    elif original_key == 'f':
        steps.append(f_notes[symbol])
    elif original_key == 'f#':
        steps.append(f_sharp_steps[symbol])
    elif original_key == 'g':
        steps.append(g_notes[symbol])
    elif original_key == 'ab':
        steps.append(ab_notes[symbol])
    elif original_key == 'a':
        steps.append(a_notes[symbol])
    elif original_key == 'bb':
        steps.append(bb_notes[symbol])
    elif original_key == 'h':
        steps.append(h_notes[symbol])

print('\nChords in new key: ')  # словари c именами на _steps: key: номер ступени лада; value: аккорд на этой ступени
# сопоставление ступени c соответствующим ей аккордовым символом в новой тональности и конкатенацией полученного аккор-
for step_number, step in enumerate(steps):  # дового символа с "окончанием" при условии, что оно для данного аккорда
    if new_key == 'am':  # имеется в словаре и вывод результата; иначе-вывод аккорда в новой тональности без "окончания"
        print(am_steps[step] + chord_tails[step_number] if step_number in chord_tails else am_steps[step], ' ', end=' ')
    elif new_key == 'hm':
        print(hm_steps[step] + chord_tails[step_number] if step_number in chord_tails else hm_steps[step], ' ', end=' ')
    elif new_key == 'cm':
        print(cm_steps[step] + chord_tails[step_number] if step_number in chord_tails else cm_steps[step], ' ', end=' ')
    elif new_key == 'dm':
        print(dm_steps[step] + chord_tails[step_number] if step_number in chord_tails else dm_steps[step], ' ', end=' ')
    elif new_key == 'em':
        print(em_steps[step] + chord_tails[step_number] if step_number in chord_tails else em_steps[step], ' ', end=' ')
    elif new_key == 'fm':
        print(fm_steps[step] + chord_tails[step_number] if step_number in chord_tails else fm_steps[step], ' ', end=' ')
    elif new_key == 'gm':
        print(gm_steps[step] + chord_tails[step_number] if step_number in chord_tails else gm_steps[step], ' ', end=' ')
    elif new_key == 'bbm':
        print(bbm_steps[step] + chord_tails[step_number] if step_number in chord_tails else bbm_steps[step], ' ',
              end=' ')
    elif new_key == 'c#m':
        print(c_sharp_m_steps[step] + chord_tails[step_number] if step_number in chord_tails else c_sharp_m_steps[step],
              ' ', end=' ')
    elif new_key == 'ebm':
        print(ebm_steps[step] + chord_tails[step_number] if step_number in chord_tails else ebm_steps[step], ' ',
              end=' ')
    elif new_key == 'f#m':
        print(f_sharp_m_steps[step] + chord_tails[step_number] if step_number in chord_tails else f_sharp_m_steps[step],
              ' ', end=' ')
    elif new_key == 'g#m':
        print(g_sharp_m_steps[step] + chord_tails[step_number] if step_number in chord_tails else g_sharp_m_steps[step],
              ' ', end=' ')
    elif new_key == 'c':
        print(c_steps[step] + chord_tails[step_number] if step_number in chord_tails else c_steps[step], ' ', end=' ')
    elif new_key == 'd':
        print(d_steps[step] + chord_tails[step_number] if step_number in chord_tails else d_steps[step], ' ', end=' ')
    elif new_key == 'e':
        print(e_steps[step] + chord_tails[step_number] if step_number in chord_tails else e_steps[step], ' ', end=' ')
    elif new_key == 'f':
        print(f_steps[step] + chord_tails[step_number] if step_number in chord_tails else f_steps[step], ' ', end=' ')
    elif new_key == 'g':
        print(g_steps[step] + chord_tails[step_number] if step_number in chord_tails else g_steps[step], ' ', end=' ')
    elif new_key == 'a':
        print(a_steps[step] + chord_tails[step_number] if step_number in chord_tails else a_steps[step], ' ', end=' ')
    elif new_key == 'h':
        print(h_steps[step] + chord_tails[step_number] if step_number in chord_tails else h_steps[step], ' ', end=' ')
    elif new_key == 'db':
        print(db_steps[step] + chord_tails[step_number] if step_number in chord_tails else db_steps[step], ' ', end=' ')
    elif new_key == 'eb':
        print(eb_steps[step] + chord_tails[step_number] if step_number in chord_tails else eb_steps[step], ' ', end=' ')
    elif new_key == 'bb':
        print(bb_steps[step] + chord_tails[step_number] if step_number in chord_tails else bb_steps[step], ' ', end=' ')
    elif new_key == 'ab':
        print(ab_steps[step] + chord_tails[step_number] if step_number in chord_tails else ab_steps[step], ' ', end=' ')
    elif new_key == 'f#':
        print(f_sharp_steps[step] + chord_tails[step_number] if step_number in chord_tails else f_sharp_steps[step], ' ', end=' ')




