s = input()
nxt = 0 
digit = ''
alpha = ''
while True:
    while nxt < len(s) and s[nxt].isdigit():
        digit += s[nxt] 
        nxt += 1

    while nxt < len(s) and s[nxt].isalpha():
        alpha += s[nxt] 
        nxt += 1

    digit = int(digit)
    print(end = digit * alpha)
    digit = ''
    alpha = ''
