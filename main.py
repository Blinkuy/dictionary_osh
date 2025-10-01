
def word_from_line(line: str) -> str:
    ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    
    word = ""
    
    for char in line:
        if char in ALPHABET:
            word += char
        elif char == ",":
            break
    
    return word


def meaning_from_line(line: str) -> str:
    ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    
    above_index = line.find(",") + 1 # удаляю первое слово + зяпятая
    
    line = line[above_index::]
    
    for char in line:
        if char in ALPHABET:
            index = line.find(char)
            line = line[index::]
            break
    
    dot_index = line.find(".") + 1
    
    line = line[0:dot_index]
    
    return line
    
with open(r"new_words\A-D.txt", "r", encoding="utf-8") as file:
    
    lis = []
    for line in file:
        if line.strip() == "":
            continue
        lis.append(line)

    
    for index ,item in enumerate(lis):
        print(word_from_line(item), meaning_from_line(item))
        
        if index == 200:
            break