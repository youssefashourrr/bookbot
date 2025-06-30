def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_counts(text):
    text = text.lower()
    dict = {}
    for char in text:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


def get_report(dict):
    report = []
    for char, count in dict.items():
        if char.isalpha():
            report.append({"char": char, "num": count})

    def sort_key(item):
        return item["num"]
    report.sort(key=sort_key, reverse=True)
    return report