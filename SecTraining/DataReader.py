
START_IDX=0
END_IDX = 10
CAPTURES_DIR = '../resources/captures/TEST1_'
TEXT_DIR = '../resources/text/TEST1_'

def getMapping() -> {str, set} :
    result = {}
    filePairs = [('%s%s.png'% (CAPTURES_DIR, i),('%s%s.txt'% (TEXT_DIR, i) )) for i in range(START_IDX, END_IDX)]
    for img_path, txt_path in filePairs:
        f = open(txt_path, "r")
        result[img_path] = frozenset(f.read().split())
    return  result

def filter_by_word(word : str, mapping: {str, set}) -> {str, set} :
    d =  {img:text for img, text in mapping.items() if word in text}
    # print(d)
    return d

def filter_by_words(words: [str], mapping: {str, set}) -> {str, set}:
    if not words:
        return mapping
    if not mapping:
        return  mapping
    # print(words)
    top = words.pop()
    mapping = filter_by_word(top, mapping)
    return filter_by_words(words, mapping)

def files_with_words(words: [str], mappings: {str, set}) -> [str] :
    return filter_by_words(words, mappings).keys()


mappings = getMapping()
#
# print(filter_by_word("Firewall-based", mappings).keys())

print(files_with_words(["Firewall-based"], mappings))