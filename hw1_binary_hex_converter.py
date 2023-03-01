#先請使用者輸入一個數
print('請輸入一個十進位整數，幫您轉換為二進位和十六進位:')
#防呆機制，避免亂輸入
while True:
    inputnumber = input()  # 輸入變數
    # 確認變數是不是數字，如果小數點後是0處理成整數，否則重新輸入
    if inputnumber.replace(".", '').isdigit() and inputnumber.count('.') < 2:
        X1 = float(inputnumber)
        X2 = int(float(inputnumber))
        if X2-X1 == 0:
            inputnumber = X2
            break
        else:
            print('請重新輸入一個十進位整數，幫您轉換為二進位和十六進位:')
            continue
    else:
        print('請重新輸入一個十進位整數，幫您轉換為二進位和十六進位:')
        continue
#先找出是小於2的幾次方
N = 0
while 2**N <= inputnumber:
    N = N+1
N=N-1
#從高次向扣回來
Power_num = []
inputnumber_2 = inputnumber
for X3 in range(0, N+1):
    if inputnumber_2 >= 2**(N-X3):
        Power_num.append(1)
        inputnumber_2 = inputnumber_2-2**(N-X3)
    else:
        Power_num.append(0)
answer_2 = "".join([str(_) for _ in Power_num]) #將數字轉為文字

#十六進位轉換開始，先找出是小於16的幾次方
N = 0
while 16**N <= inputnumber:
    N = N+1
N=N-1
#從高次向扣回來
Power_num = []
inputnumber_16 = inputnumber
for X3 in range(0, N+1):
    if inputnumber_16 >= 16**(N-X3):
        Power_num.append(inputnumber_16//(16**(N-X3)))
        inputnumber_16 = inputnumber_16%(16**(N-X3))
    else:
        Power_num.append(0)
#把10~15改成ABCDEF
list_16=['A','B','C','D','E','F']
for X3 in range(0, len(Power_num)):
    if Power_num[X3] >= 10:
        Power_num[X3] = list_16[Power_num[X3]-10]
answer_16 = "".join([str(_) for _ in Power_num])

#考慮輸入數字為0的時候
if inputnumber == 0:
    answer_2 = '0'
    answer_16 = '0'
#顯示答案
print('二進位轉換後為：', answer_2)
print('十六進為轉換後為:', answer_16)