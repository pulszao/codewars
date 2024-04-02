def strip_comments(strng, markers):
    words = strng.split('\n')

    comments = []
    for word in words:
        for mark in markers:
            if mark in word:
                i = 0
                for letter in word:
                    if letter == mark:
                        word = word[:i]  # update the word with the removed comment
                        break
                    i += 1
        comments.append(word.rstrip())

    return '\n'.join(comments)
