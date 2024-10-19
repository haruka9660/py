def count_words(text):
    """统计单词数量"""
    words = text.split()
    word_count = len(words)
    return word_count

def count_unique_words(text):
    """统计唯一单词数量"""
    words = text.split()
    unique_words = set(words)
    unique_word_count = len(unique_words)
    return unique_word_count

def count_characters(text):
    """统计字符数量（包括空格）"""
    char_count = len(text)
    return char_count

def count_characters_no_spaces(text):
    """统计字符数量（不包括空格）"""
    char_count = len(text.replace(" ", ""))
    return char_count

input_text = input("请输入一段文本：")

print("统计结果：")
print("单词数量：", count_words(input_text))
print("唯一单词数量：", count_unique_words(input_text))
print("字符数量（包括空格）：", count_characters(input_text))
print("字符数量（不包括空格）：", count_characters_no_spaces(input_text))

"""
定义了四个函数，分别用于统计单词数量、唯一单词数量、字符数量（包括空格）和字符数量（不包括空格）。
count_words()函数接收一个文本字符串作为参数，使用split()方法将文本字符串拆分为单词列表，并使用len()函数获取单词数量。
count_unique_words()函数接收一个文本字符串作为参数，使用split()方法将文本字符串拆分为单词列表，并使用set()函数将列表转换为集合，从而获取唯一单词的集合，最后使用len()函数获取唯一单词数量。
count_characters()函数接收一个文本字符串作为参数，使用len()函数获取文本字符串的字符数量（包括空格）。
count_characters_no_spaces()函数接收一个文本字符串作为参数，使用replace()方法将空格替换为空字符串，然后使用len()函数获取文本字符串的字符数量（不包括空格）。
使用input()函数获取用户输入的一段文本，并将其存储在input_text变量中。
打印统计结果，分别调用上述四个函数，并传入input_text作为参数，将统计结果打印输出。
"""