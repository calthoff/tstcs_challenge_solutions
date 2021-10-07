import re


def remove_dups(text):
    count = {}
    words = re.compile('\w+').findall(text)
    new_string = ''
    for word in words:
        if word not in count:
            new_string += word + ' '
            count[word] = 1
    return new_string


print(remove_dups("I am a self-taught programmer looking for a job as a programmer."))
