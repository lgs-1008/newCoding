test = 'include <stdio.h>int main(){int i;for(i=1; i<=10; i++)printf ("%d\n",i);}'
check = []
test = list(test)
a = ['[',']','(',')','{','}']
b = ['[]','()','{}']
for i in test:
    if i in a:
        check.append(i)
        if len(check)>1:
            v = check[-2]+check[-1]
            if v in b:
                check.pop()
                check.pop()
if not check:
    print("코드가 유효합니다.")
else:
    print("코드가 유효하지 않습니다.")
    print(check)

