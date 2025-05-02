# TEXT FILE PRACTISE

shake = open("shakespeare.txt")
shake_words = shake.read().split()

## length of text
#print(len(shake_words))

## show first 25 words
#print(shake_words[:25])

## how many times "thou" appears
#print(shake_words.count("thou"))

## what percentage "thou" appears
#thou_percentage = (shake_words.count("thou") / len(shake_words)) * 100
#print(f"{'{0:.2f}'.format(thou_percentage)} %")

## how many unique words
#unique = set(shake_words)
#print(len(unique))

## is "thou" in unique words
#unique = set(shake_words)
#print("thou" in unique)

## reverse of "thou"
#print("thou"[::-1])

## how many palindromes of length 5
#print(len({w for w in shake_words if w == w[::-1] and len(w) == 5}))

## WARNING this might take a long time for the computer to complete:
## how many reversed words of length 5 are actually in text
#print(len({w for w in shake_words if w[::-1] in shake_words and len(w) == 5}))
