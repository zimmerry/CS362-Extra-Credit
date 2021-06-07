def rev(sentence):
    sent = sentence.split()
    sent.reverse()
    r_sent = ""
    for i in range(0, len(sent) - 1):
        r_sent += sent[i] + " "
    r_sent += sent[len(sent) - 1]

    return r_sent
