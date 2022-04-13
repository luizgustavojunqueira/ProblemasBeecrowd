hInicio, mInicio, hFim, mFim = map(int, input().split())

duracaoH = 0
duracaoM = 0

if hFim > hInicio:
    duracaoH = hFim - hInicio
elif hFim < hInicio:
    duracaoH = hFim + 24 - hInicio

if mInicio < mFim:
    duracaoM = mFim - mInicio
elif mInicio > mFim:
    duracaoH -= 1
    duracaoM = 60 - mInicio + mFim
elif mInicio == mFim:
    duracaoM = 0

if hInicio == hFim:
    if mInicio < mFim:
        duracaoM = mFim - mInicio
        duracaoH = 0
    elif mInicio > mFim:
        duracaoH = 23
        duracaoM = 60 - mInicio + mFim
    elif mInicio == mFim:
        duracaoH = 24
        duracaoM = 0

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(duracaoH, duracaoM))