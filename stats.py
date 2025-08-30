def count_words(text):
    return len(text.split())


def count_chars(text):
    dict = {}
    for char in text.lower():
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


def sort_on(items):
    return items["num"]


def sort_chars(dict):
    output = []
    for k, v in dict.items():
        output.append({"char": k, "num": v})
    output.sort(reverse=True, key=sort_on)
    return output
