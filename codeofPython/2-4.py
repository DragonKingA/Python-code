#第一题

def rankHurricane(velocity):
    #请在下面编写代码
    # ********** Begin ********** #
    velocity = int(input())
    rank = "None"
    if velocity >= 74 and velocity <= 95:
        rank=1;
    elif velocity >= 96 and velocity <= 110:
        rank=2;
    elif velocity >= 111 and velocity <= 130:
        rank=3;
    elif velocity >= 131 and velocity <= 154:
        rank=4;
    elif velocity >= 155:
        rank=5;
    print(rank);
    # ********** End ********** #
    #请不要修改下面的代码
    return rank


#第二题

def validCreditCard(num):
    #请在下面编写代码
    # ********** Begin ********** #
    eachnum=[];
    sum1=0;
    sum2=0;
    valid="False";
    for i in range(0,8,1):
        eachnum[i] = (num % (10**(i+1)))/(10**i);
        if i==0 or i%2==0:
            sum1+=eachnum[i];
    for i in range(1,8,2):
            sum2+=(eachnum[i]*2)/10 + (eachnum[i]*2)%10;
    if (sum1+sum2)%10 == 0:
        valid="True";
    # ********** End ********** #    
    #请不要修改下面的代码
    return valid

#第三题

def ISBN(n):
    # 请在下面编写代码
    # ********** Begin ********** #
    eachnum0=[];
    sumofcheck=0;
    for i in range(0,9,1):
        eachnum0[i] = (n % (10**(i+1)))/(10**i);
    for i in range(0,11,1):
        sum=i;
        for j in range(0,9,1):
            sum += (j+2)*eachnum0[j];
        if(sum % 11 == 0):
            sumofcheck=i;
            break;
    if(sumofcheck == 10):
        trueISBN=str(n) + "X";
    else:
        trueISBN=str(n) + str(sumofcheck);
    # ********** End ********** #    
    # 请不要修改下面的代码
    return (trueISBN)

#第四题

def day(y, m, d):#计算y年m月d日是星期几
    # 请在下面编写代码
    # ********** Begin ********** #
    y0 = y - (14-m)//12;
    x = y0 + y0//4 - y0//100 + y0//400;
    m0 = m + 12*((14-m)//12) - 2;
    d0 = (d+x+(31*m0)//12)%7;
    # ********** End ********** #    
    # 请不要修改下面的代码
    return d0

def isLeapYear(year): #判断year年是否闰年
    # 请在下面编写代码
    # ********** Begin ********** #
    isLeapYear = 0;
    if (year % 4 == 0 and year % 100 != 0) or year%400==0:
        isLeapYear = 1;
    else:
        isLeapYear = 0;
    # ********** End ********** #    
    # 请不要修改下面的代码
    return isLeapYear

def calendar(y, m): #打印y年m月日历
    print('       {}年{}月'.format(y,m))
    print('Su\tM\tTu\tW\tTh\tF\tSa')
    # 请在下面编写代码
    # ********** Begin ********** #
    
    datemax=0;
    datemaxofFeb=0;
    if isLeapYear==1:
        datemaxofFeb=29;
    else:
        datemaxofFeb=28;
    mons = [1,3,5,7,8,10,12,2,4,6,9,11];
    if m==2:
        datemax=datemaxofFeb;
    elif mons.index(m) <= 6:
        datemax=31;
    else:
        datemax=30;

    dateofday=1;
    i=1
    while (dateofday<=datemax):
        for j in range(1,8,1):
            if dateofday>datemax:
                break;

            if day(y, m, 1)!=6 and i==1:
                for k in range(1,day(y, m, 1)+1,1):
                    print("\t");

            print("{:<d}".format(dateofday));
            dateofday+=1;

            if j<7:
                print("\t");
            elif j==7:
                print("\n");
    
        i+=1;
    
    # ********** End ********** #
    # 请不要修改下面的代码

#第五题

def ramanujan(n):
    results = []

    #请在下面编写代码
    # ********** Begin ********** #
    for a in range(1,n+1,1):
        for b in range(1,n+1,1):
            for c in range(1,n+1,1):
                for d in range(1,n+1,1):
                    if a**3+b**3 == c**3+d**3:
                        results[a-1]=str(a**3+b**3)+" = "+str(a)+"^3 + "+str(b)+"^3 = "+str(c)+"^3 + "+str(d)+"^3";
    # ********** End ********** #    
    # 请不要修改下面的代码
    return results


#第六题

def unit_to_word(u): #将0～9的数字转换成英文，并返回转换后的英文
    # 请在下面编写代码
    # ********** Begin ********** #
    convert_table = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    return convert_table[u]
    
    # ********** End ********** #
    # 请不要修改下面的代码


def tens_to_word(t): #利用unit_to_word，将10～19、以及20～99的十位部分数字转换成英文，并返回转换后的英文
    # 请在下面编写代码
    # ********** Begin ********** #
    convert_table = {
        0: "",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }
    if 9 < t < 20:
        return convert_table[t]
    else:
        tens = convert_table[t/10] + " " + unit_to_word(t%10)
        return tens
    # ********** End ********** #
    # 请不要修改下面的代码

def hundreds_to_word(h): #利用unit_to_word、tens_to_word进行转换，并返回转换后结果的函数
    # 请在下面编写代码
    # ********** Begin ********** #
    if h > 99:
        word = unit_to_word(h/100) + " hundred"
        tens = h % 100
        if tens == 0:
            return word
        else:
            return word + " and " + tens_to_word(tens)
    else:
        return tens_to_word(h)
    for test in [0, 5, 19, 23, 100, 700, 711, 729]:
        print (test, "=>", hundreds_to_word(test))
    # ********** End ********** #    
    # 请不要修改下面的代码

if __name__ == '__main__':
    for v in [60, 74, 95, 96, 110, 111, 130, 131, 154, 170]:
        rank = rankHurricane(v)
        print(rank)
    print('\n***********************\n')

    for num in [1234567, 43589795, 87539319, 123456789]:
        valid = validCreditCard(num)
        print(valid)
    print('\n***********************\n')

    for num in [201314525, 488888913, 977889994, 753231846, 701134069]:
        trueISBN = ISBN(num)
        print(trueISBN)
    print('\n***********************\n')

    for (y,m) in [(2017,8), (2017,10),(2015,8), (2017,2), (2016,2)]:
        calendar(y, m)
        print('---------------------------')

    print('\n***********************\n')

    for num in [2000, 10000, 100000]:
        st = ramanujan(num)
        for item in st:
            print(item)

    print('\n***********************\n')

    for test in [0, 5, 19, 23, 100, 700, 711, 729]:
        print(test, "=>", hundreds_to_word(test))

