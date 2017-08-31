def reverse(sentence):
    new_array = []
    sentence_array = sentence.split(' ')
    for sentence in sentence_array:
        new_array.append(sentence[::-1])
    return ' '.join(new_array)


