import cv2


RESIZEKOEF = 2
path = './numbers_n/symbols/'
all_symb = 'yvotkacnxpme'
regions = [188,206,224]
alph = {
    'y': [14,42,67,92,118,144], 'k': [14,42,67,92,117,143], 'x': [14,42,67,92,118,144],
    'v': [14,42,67,92,118,144], 'a': [13,42,67,92,116,144], 'p': [17,42,67,92,120,145],
    'o': [13,42,67,92,118,144], 'c': [13,42,67,92,118,144], 'm': [14,42,67,92,118,145],
    't': [13,42,67,92,118,144], 'n': [14,42,67,92,118,144], 'e': [14,42,67,92,118,144],
    '1':[13,42,67,92,116,144], '2':[13,42,67,92,116,144], '3':[13,42,67,92,116,144],
    '4':[13,42,67,92,116,144], '5':[13,42,67,92,116,144], '6':[13,42,67,92,116,144],
    '7':[13,42,67,92,116,144], '8':[13,42,67,92,116,144], '9':[13,42,67,92,116,144],
    '0':[13,42,67,92,116,144]
       }


def view(temp):
    cv2.imshow('tmplate', cv2.resize(temp, (0, 0), fx=RESIZEKOEF, fy=RESIZEKOEF))
    cv2.waitKey(300)
    cv2.destroyAllWindows()


def past_in_template(symb, i_sym, temp):
    symbol = cv2.imread(path + symb+'.jpeg')
    h, w, _ = symbol.shape
    if 4 > i_sym > 0:
        st = 5
    else:
        st = 12
    temp[st:st + h, alph[symb][i_sym]:alph[symb][i_sym] + w] = symbol
    view(temp)

    return temp


def change_region(temp, region):
    if len(region) == 2:
        for idx, r in enumerate(region):
            reg = cv2.imread(path + 'r' + r + '.jpeg')
            rh,rw,_ = reg.shape
            temp[4:(4 + rh), regions[idx]:regions[idx] + rw] = reg
            view(temp)
    if len(region) == 3:
        for idx, r in enumerate(region):
            reg = cv2.imread(path + 'r' + r + '.jpeg')
            rh,rw,_ = reg.shape
            temp[4:(4 + rh), regions[idx] - 4:regions[idx] + rw-4] = reg
            view(temp)

    return temp




if __name__ == '__main__':
    arr = ['o476xt', 'k324mr']
    region = '31'

    for number in arr:
        out = None
        temp = cv2.imread(path+'clear_template_2.jpeg')
        for idx, s in enumerate(number):
            if s == 's':
                s = 'c'
            if s == 'r':
                s = 'p'
            if s == 'b':
                s = 'v'

            out = past_in_template(s, idx, temp)

        out = change_region(out, region)

        if not None:
            print(out.shape)
            cv2.imwrite('./numbers_n/created/'+number+region+'.jpg', out)
            print('[SUCCESS WRITE]: {}'.format(number+region))
            # view(out)
