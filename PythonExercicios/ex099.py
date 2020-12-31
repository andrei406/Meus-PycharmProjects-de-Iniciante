from time import sleep


def maior(* num):
    maival = 0
    for c in num:
        if c > maival:
            maival = c
    print(f'Analizando os valores: {num}')
    sleep(1)
    print(f'O maior número foi {maival}')
    print('~' * 40 )


maior(1, 5, 9)
maior(3, 6, 0 ,1, 12)
maior(9, 15, 6, 1)