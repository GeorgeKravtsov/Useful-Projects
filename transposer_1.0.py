'***************************************************TRANSPOSER 1.0****************************************************'
# The program transposes user-entered chords into the key specified by the user.
# Transposition is possible in each of the 12 major and minor keys.
# Only diatonic chord progressions are currently supported.
# The principle of the program is as follows: at the invitation of "Original key:" the user enters the original key,
# for example, Am, then at the prompt "New key:" enters the required key, for example, Hm, then at the invitation
# "Enter chord:" sequentially enters chord symbols, for example Am7, Dm9, E13, etc., pressing Enter key after each
# chord character. Each time after pressing Enter, the chord entered by the user is displayed a progression in the
# original key in the form of a list placed in sims [], for example:
# 'Chords in original key: [' Am7 ',' G11 ',' C6 ',' Dm7 ',' E13 ',' Am9 ']; chord symbols and keys can be entered in
# lower case (the first letter of the chord symbol and key is converted to upper case automatically).
# User-entered chord symbols become values ​​in the dictionary entered_user_chords, whose keys are numbers from 0, added
# automatically and increasing by 1 after each press of the Enter key when any chord symbol entered. To display a chord
# sequence in a new key you must press Enter at the prompt "Enter chord:" without entering anything before.
# When you press Enter after an empty line at the "Enter chord:" prompt, the last entered element whose value is an
# empty string, that occurs after pressing Enter without anything to display a chord sequence in a new key, becomes
# deleted from the entered_user_chords dictionary.
# If the chord symbol does NOT end with '6/9', '6', '7', '9', '11', '13', 'maj', 'aug', 'add2', 'add9', 'sus ','b5 # 5',
# that is, it looks like 'Am', 'Dm', 'C', etc., this character is added to the end of the chords_no_digits list.
# Otherwise, any of the “endings” presented above is cut off from the chord symbol which is entered in the chords_digits
# dictionary, whose keys are the keys of the entered_user_chords dictionary to serve sequence numbers of the "endings"
# for the subsequent correct concatenation with the corresponding chord symbol in the new key.
# Next, each chord symbol from the chords_no_digits list is mapped to a value in the x_notes dictionary (ordinal step
# number), where x is the original key entered by the user. As a result of matching, ordinal the number of the step of
# each of the chords entered by the user is entered in the steps list (chord steps).
# After that, each element of the steps list is mapped to a value in the y_steps dictionary (the letter designation of
# the step chord in a new key), where y is the new key entered by the user.
# Chord lettering in the new key concatenates with the "endings" of chords from the chords_digits dictionary only if the
# index (NOT SCALE STEP NUMBER) of the step in the steps list corresponds to the "end" number in dictionary
# chords_digits. Otherwise, the chord symbol in the new key is displayed without a "ending".
# The result of the program execution is a string of chord characters entered by the user in the user specified key,
# for example: 'Chords in a new key:
#                         Hm7   A11   D6   Em7   F#13   Hm9'.

am_notes = {'Am': '1', 'H dim': '2', 'C': '3', 'Dm': '4', 'E': '5', 'F': '6', 'G': '7'}
bbm_notes = {'Bbm': '1', 'C dim': '2', 'Db': '3', 'Ebm': '4', 'F': '5', 'Gb': '6', 'Ab': '7'}
hm_notes = {'Hm': '1', 'C# dim': '2', 'D': '3', 'Em': '4', 'F#': '5', 'G': '6', 'A': '7'}
cm_notes = {'Cm': '1', 'D dim': '2', 'Eb': '3', 'Fm': '4', 'G': '5', 'Ab': '6', 'Bb': '7'}
c_sharp_m_notes = {'C#m': '1', 'D# dim': '2', 'E': '3', 'F#m': '4', 'G#': '5', 'A': '6', 'H': '7'}
dm_notes = {'Dm': '1', 'E dim': '2', 'F': '3', 'Gm': '4', 'A': '5', 'Bb': '6', 'C': '7'}
ebm_notes = {'Ebm': '1', 'F dim': '2', 'Gb': '3', 'Abm': '4', 'Bb': '5', 'Cb': '6', 'Db': '7'}
em_notes = {'Em': '1', 'F# dim': '2', 'G': '3', 'Am': '4', 'H': '5', 'C': '6', 'D': '7'}
fm_notes = {'Fm': '1', 'G dim': '2', 'Ab': '3', 'Bbm': '4', 'C': '5', 'Db': '6', 'Eb': '7'}
f_sharp_m_notes = {'F#m': '1', 'G# dim': '2', 'A': '3', 'Hm': '4', 'C#': '5', 'D': '6', 'E': '7'}
gm_notes = {'Gm': '1', 'A dim': '2', 'Bb': '3', 'Cm': '4', 'D': '5', 'Eb': '6', 'F': '7'}
g_sharp_m_notes = {'G#m': '1', 'A# dim': '2', 'H': '3', 'C#m': '4', 'D#': '5', 'E': '6', 'F#': '7'}

am_steps = {'1': 'Am', '2': 'H dim', '3': 'C', '4': 'Dm', '5': 'E', '6': 'F', '7': 'G'}
bbm_steps = {'1': 'Bbm', '2': 'C dim', '3': 'Db', '4': 'Ebm', '5': 'F', '6': 'Gb', '7': 'Ab'}
hm_steps = {'1': 'Hm', '2': 'C# dim', '3': 'D', '4': 'Em', '5': 'F#', '6': 'G', '7': 'A'}
cm_steps = {'1': 'Cm', '2': 'D dim', '3': 'Eb', '4': 'Fm', '5': 'G', '6': 'Ab', '7': 'Bb'}
c_sharp_m_steps = {'1': 'C#m', '2': 'D# dim', '3': 'E', '4': 'F#m', '5': 'G#', '6': 'A', '7': 'H'}
dm_steps = {'1': 'Dm', '2': 'E dim', '3': 'F', '4': 'Gm', '5': 'A', '6': 'Bb', '7': 'C'}
ebm_steps = {'1': 'Ebm', '2': 'F dim', '3': 'Gb', '4': 'Abm', '5': 'Bb', '6': 'Cb', '7': 'Db'}
em_steps = {'1': 'Em', '2': 'F# dim', '3': 'G', '4': 'Am', '5': 'H', '6': 'C', '7': 'D'}
fm_steps = {'1': 'Fm', '2': 'G', '3': 'Ab', '4': 'Bbm', '5': 'C', '6': 'Db', '7': 'Eb'}
f_sharp_m_steps = {'1': 'F#m', '2': 'G#', '3': 'A', '4': 'Hm', '5': 'C#', '6': 'D', '7': 'E'}
gm_steps = {'1': 'Gm', '2': 'A dim', '3': 'Bb', '4': 'Cm', '5': 'D', '6': 'Eb', '7': 'F'}
g_sharp_m_steps = {'1': 'G#m', '2': 'A# dim', '3': 'H', '4': 'C#m', '5': 'D#', '6': 'E', '7': 'F#'}

c_notes = {'C': '1', 'Dm': '2', 'Em': '3', 'F': '4', 'G': '5', 'Am': '6', 'H dim': '7'}
db_notes = {'Db': '1', 'Ebm': '2', 'Fm': '3', 'Gb': '4', 'Ab': '5', 'Bbm': '6', 'C dim': '7'}
d_notes = {'D': '1', 'Em': '2', 'F#': '3', 'G': '4', 'A': '5', 'Hm': '6', 'C# dim': '7'}
eb_notes = {'Eb': '1', 'Fm': '2', 'Gm': '3', 'Ab': '4', 'Bb': '5', 'Cm': '6', 'D dim': '7'}
e_notes = {'E': '1', 'F#m': '2', 'G#m': '3', 'A': '4', 'H': '5', 'C#m': '6', 'D# dim': '7'}
f_notes = {'F': '1', 'Gm': '2', 'Am': '3', 'Bb': '4', 'C': '5', 'Dm': '6', 'E dim': '7'}
gb_notes = {'Gb': '1', 'Abm': '2', 'Bbm': '3', 'Cb': '4', 'Db': '5', 'Ebm': '6', 'F dim': '7'}
g_notes = {'G': '1', 'Am': '2', 'Hm': '3', 'C': '4', 'D': '5', 'Em': '6', 'F# dim': '7'}
ab_notes = {'Ab': '1', 'Bbm': '2', 'Cm': '3', 'Db': '4', 'Eb': '5', 'F': '6', 'G dim': '7'}
a_notes = {'A': '1', 'Hm': '2', 'C#m': '3', 'D': '4', 'E': '5', 'F#m': '6', 'G# dim': '7'}
bb_notes = {'Bb': '1', 'Cm': '2', 'Dm': '3', 'Eb': '4', 'F': '5', 'Gm': '6', 'A dim': '7'}
h_notes = {'H': '1', 'C#m': '2', 'D#m': '3', 'E': '4', 'F#': '5', 'G#m': '6', 'A# dim': '7'}

c_steps = {'1': 'C', '2': 'Dm', '3': 'Em', '4': 'F', '5': 'G', '6': 'Am', '7': 'H dim'}
db_steps = {'1': 'Db', '2': 'Ebm', '3': 'Fm', '4': 'Gb', '5': 'Ab', '6': 'Bbm', '7': 'C dim'}
d_steps = {'1': 'D', '2': 'Em', '3': 'F#', '4': 'G', '5': 'A', '6': 'Hm', '7': 'C# dim'}
eb_steps = {'1': 'Eb', '2': 'Fm', '3': 'Gm', '4': 'Ab', '5': 'Bb', '6': 'Cm', '7': 'D dim'}
e_steps = {'1': 'E', '2': 'F#m', '3': 'G#m', '4': 'A', '5': 'H', '6': 'C#m', '7': 'D# dim'}
f_steps = {'1': 'F', '2': 'Gm', '3': 'Am', '4': 'Bb', '5': 'C', '6': 'Dm', '7': 'E dim'}
gb_steps = {'1': 'Gb', '2': 'Abm', '3': 'Bbm', '4': 'Cb', '5': 'Db', '6': 'Ebm', '7': 'F dim'}
g_steps = {'1': 'G', '2': 'Am', '3': 'Hm', '4': 'C', '5': 'D', '6': 'Em', '7': 'F# dim'}
ab_steps = {'1': 'Ab', '2': 'Bbm', '3': 'Cm', '4': 'Db', '5': 'Eb', '6': 'F', '7': 'G dim'}
a_steps = {'1': 'A', '2': 'Hm', '3': 'C#m', '4': 'D', '5': 'E', '6': 'F#m', '7': 'G# dim'}
bb_steps = {'1': 'Bb', '2': 'Cm', '3': 'Dm', '4': 'Eb', '5': 'F', '6': 'Gm', '7': 'A dim'}
h_steps = {'1': 'H', '2': 'C#m', '3': 'D#m', '4': 'E', '5': 'F#', '6': 'G#m', '7': 'A# dim'}

print("""\t\tWelcome to TRANSPOSER 1.0!
* Type chords in lowercase. 
* For '6/9', 'add2' and 'add9' use (), for example: (6/9), (add2) and (add9).
* Type 'aug', 'sus', (add2), (add9) without whitespaces between chord character.
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
chords_digits = {}                   # {number(counter): tail} ({счётчик: "хвост("окончание")" аккорда})
chords_no_digits = []                # аккорды без "окончаний"

for number, chord in entered_user_chords.items():
    if not chord.endswith('6') and not chord.endswith('7') \
            and not chord.endswith('9') and not chord.endswith('11') \
            and not chord.endswith('13') and not chord.endswith('aug') \
            and not chord.endswith('(add2)') and not chord.endswith('(add9)') \
            and not chord.endswith('sus') and not chord.endswith('maj') \
            and not chord.endswith('(6/9)') and not chord.endswith('b5#5'):  # если введённый аккордовый символ не имеет
        chords_no_digits.append(chord)  # "окончания" (имеет вид Am, C и т. д.), он вносится в список в неизменном виде
    elif chord.endswith('6') or chord.endswith('7') or chord.endswith('9'):  # в случае наличия "окончания" оно отделя-
        chords_digits[number] = chord[-1]  # ется от начала аккорда и помещается в словарь, где ключом является порядко-
        chords_no_digits.append(chord[:-1])  # вый номер аккорда в момент его ввода, необходимый для сохранения порядка
    elif chord.endswith('11') or chord.endswith('13'):  # следования аккордовых символов и их "окончаний" при их после-
        chords_digits[number] = chord[-2:]  # дующем соединении; аккордовый символ, отделённый от "окончания", помеща-
        chords_no_digits.append(chord[:-2])  # ется в список аккордов без окончаний
    elif chord.endswith('aug') or chord.endswith('sus') or chord.endswith('maj'):
        chords_digits[number] = chord[-3:]
        chords_no_digits.append(chord[:-3])
    elif chord.endswith('b5#5'):
        chords_digits[number] = chord[-4:]
        chords_no_digits.append(chord[:-4])
    elif chord.endswith('(6/9)'):
        chords_digits[number] = chord[-5:]
        chords_no_digits.append(chord[:-5])
    elif chord.endswith('(add2)') or chord.endswith('(add9)'):
        chords_digits[number] = chord[-6:]
        chords_no_digits.append(chord[:-6])

for symbol in chords_no_digits:         # словари, имена которых заканчиваются на _notes, состоят из элементов, ключами
    if original_key == 'am':            # которых являются аккордовые символы, значениями-номера ступеней лада, соответ-
        steps.append(am_notes[symbol])  # ствующих этим символам
    elif original_key == 'hm':
        steps.append(hm_notes[symbol])  # каждый аккордовый символ из списка сопоставляется со ступенью, которой он со-
    elif original_key == 'cm':          # ответствует в тональности, указанной пользователем как 'Original key'
        steps.append(cm_notes[symbol])
    elif original_key == 'dm':          # в результате получаются ступени введённых пользователем аккордовых символов,
        steps.append(dm_notes[symbol])  # которые вносятся в список ступеней для последующего сопоставления их с аккор-
    elif original_key == 'em':          # довыми символами в тональности, указанной пользователем как 'New key'
        steps.append(em_notes[symbol])
    elif original_key == 'fm':
        steps.append(fm_notes[symbol])
    elif original_key == 'gm':
        steps.append(gm_notes[symbol])
    elif original_key == 'bbm':
        steps.append(bbm_notes[symbol])
    elif original_key == 'c#m':
        steps.append(c_sharp_m_notes[symbol])
    elif original_key == 'ebm':
        steps.append(ebm_notes[symbol])
    elif original_key == 'f#m':
        steps.append(f_sharp_m_notes[symbol])
    elif original_key == 'g#m':
        steps.append(g_sharp_m_notes[symbol])
    elif original_key == 'c':
        steps.append(c_notes[symbol])
    elif original_key == 'd':
        steps.append(d_notes[symbol])
    elif original_key == 'e':
        steps.append(e_notes[symbol])
    elif original_key == 'f':
        steps.append(f_notes[symbol])
    elif original_key == 'g':
        steps.append(g_notes[symbol])
    elif original_key == 'a':
        steps.append(a_notes[symbol])
    elif original_key == 'h':
        steps.append(h_notes[symbol])
    elif original_key == 'db':
        steps.append(db_notes[symbol])
    elif original_key == 'eb':
        steps.append(eb_notes[symbol])
    elif original_key == 'bb':
        steps.append(bb_notes[symbol])
    elif original_key == 'ab':
        steps.append(ab_notes[symbol])
    elif original_key == 'gb':
        steps.append(gb_notes[symbol])

print('\nChords in a new key: ')  # словари c именами на _steps: key: номер ступени лада; value: аккорд на этой ступени
# сопоставление ступени c соответствующим ей аккордовым символом в новой тональности и конкатенацией полученного аккор-
for step_number, step in enumerate(steps):  # дового символа с "окончанием" при условии, что оно для данного аккорда
    if new_key == 'am':  # имеется в словаре и вывод результата; иначе-вывод аккорда в новой тональности без "окончания"
        print(am_steps[step] + chords_digits[step_number] if step_number in chords_digits else am_steps[step], ' ', end=' ')
    elif new_key == 'hm':
        print(hm_steps[step] + chords_digits[step_number] if step_number in chords_digits else hm_steps[step], ' ', end=' ')
    elif new_key == 'cm':
        print(cm_steps[step] + chords_digits[step_number] if step_number in chords_digits else cm_steps[step], ' ', end=' ')
    elif new_key == 'dm':
        print(dm_steps[step] + chords_digits[step_number] if step_number in chords_digits else dm_steps[step], ' ', end=' ')
    elif new_key == 'em':
        print(em_steps[step] + chords_digits[step_number] if step_number in chords_digits else em_steps[step], ' ', end=' ')
    elif new_key == 'fm':
        print(fm_steps[step] + chords_digits[step_number] if step_number in chords_digits else fm_steps[step], ' ', end=' ')
    elif new_key == 'gm':
        print(gm_steps[step] + chords_digits[step_number] if step_number in chords_digits else gm_steps[step], ' ', end=' ')
    elif new_key == 'bbm':
        print(bbm_steps[step] + chords_digits[step_number] if step_number in chords_digits else bbm_steps[step], ' ', end=' ')
    elif new_key == 'c#m':
        print(c_sharp_m_steps[step] + chords_digits[step_number] if step_number in chords_digits else c_sharp_m_steps[step], ' ', end=' ')
    elif new_key == 'ebm':
        print(ebm_steps[step] + chords_digits[step_number] if step_number in chords_digits else ebm_steps[step], ' ', end=' ')
    elif new_key == 'f#m':
        print(f_sharp_m_steps[step] + chords_digits[step_number] if step_number in chords_digits else f_sharp_m_steps[step], ' ', end=' ')
    elif new_key == 'g#m':
        print(g_sharp_m_steps[step] + chords_digits[step_number] if step_number in chords_digits else g_sharp_m_steps[step], ' ', end=' ')
    elif new_key == 'c':
        print(c_steps[step] + chords_digits[step_number] if step_number in chords_digits else c_steps[step], ' ', end=' ')
    elif new_key == 'd':
        print(d_steps[step] + chords_digits[step_number] if step_number in chords_digits else d_steps[step], ' ', end=' ')
    elif new_key == 'e':
        print(e_steps[step] + chords_digits[step_number] if step_number in chords_digits else e_steps[step], ' ', end=' ')
    elif new_key == 'f':
        print(f_steps[step] + chords_digits[step_number] if step_number in chords_digits else f_steps[step], ' ', end=' ')
    elif new_key == 'g':
        print(g_steps[step] + chords_digits[step_number] if step_number in chords_digits else g_steps[step], ' ', end=' ')
    elif new_key == 'a':
        print(a_steps[step] + chords_digits[step_number] if step_number in chords_digits else a_steps[step], ' ', end=' ')
    elif new_key == 'h':
        print(h_steps[step] + chords_digits[step_number] if step_number in chords_digits else h_steps[step], ' ', end=' ')
    elif new_key == 'db':
        print(db_steps[step] + chords_digits[step_number] if step_number in chords_digits else db_steps[step], ' ', end=' ')
    elif new_key == 'eb':
        print(eb_steps[step] + chords_digits[step_number] if step_number in chords_digits else eb_steps[step], ' ', end=' ')
    elif new_key == 'bb':
        print(bb_steps[step] + chords_digits[step_number] if step_number in chords_digits else bb_steps[step], ' ', end=' ')
    elif new_key == 'ab':
        print(ab_steps[step] + chords_digits[step_number] if step_number in chords_digits else ab_steps[step], ' ', end=' ')
    elif new_key == 'gb':
        print(gb_steps[step] + chords_digits[step_number] if step_number in chords_digits else gb_steps[step], ' ', end=' ')
