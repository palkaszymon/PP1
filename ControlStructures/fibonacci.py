pierwsza_liczba=0
druga_liczba=1
for i in range(0,50):
    if i <=1:
        liczba_fibonacci=i
    else:
        liczba_fibonacci=pierwsza_liczba+druga_liczba
        pierwsza_liczba=druga_liczba
        druga_liczba=liczba_fibonacci
    print(liczba_fibonacci)
    