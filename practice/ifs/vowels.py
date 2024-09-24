def vowels(lett):
    i = lett.lower()
    v = ['a', 'e', 'i', 'o', 'u']
    if i in v:
        print(f"{i} is a vowel")
    else:
        print(f"{i} isn't a vowel")

vowels('A')


