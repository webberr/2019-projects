list = ['apples', 'bananas', 'tofu', 'cats']

def stringify(array):
    out = ''
    for i in list:
        if(i == array[0]):
            out = out + i
        else:
            out = out + ', ' + i
    print(out) 

stringify(list)