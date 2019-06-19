array = [8,-1231]
def input_integer(array):
    sum = 0
    for i in array: #looping proses sum 1
        sum += i
    print(sum)
    str_sum = str(sum)
    sum = 0
    if str_sum[0]!='-':
        for ix, i in enumerate(str_sum): #looping proses sum 2
            i = int(i)
            sum+=i
    elif str_sum[0]=='-' and len(str_sum)==2:
        return int(str_sum)
    else:
        for i in range(len((str_sum))): #looping proses sum 3
            if i==0:
                pass
            elif i == 1:
                x = int(str_sum[i])
#                 print(x)
                sum+=(-x)
            else:
                x = int(str_sum[i])
                sum+=x
    return (sum)
input_integer(array)