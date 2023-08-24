import math
from tkinter import *
from tkinter import ttk
from math import sqrt

text_final_result = ''
text_res_calc = ''
text_calc = ''
text_dec = ''
text_bin = ''
text_oct = ''
text_hex = ''

final_result = ''
res_calc = ''

num = ['0']
write_scr = ['0']
write_result = []
calculate = []

sqr_num_1 = ''
sqr_num_2 = ''

sqrt_num_1 = ''
sqrt_num_2 = ''

onedevx_num_1 = ''
onedevx_num_2 = ''

second_num = ''

mark = False
dotted = False
mark_operation = False
zero_devision = False

mark_sqr = False
mark_sqr_1 = False
mark_sqr_2 = False

mark_sqrt = False
mark_sqrt_1 = False
mark_sqrt_2 = False

oper_mark_sqr_1 = False
oper_mark_sqrt_1 = False
oper_mark_onedevx_1 = False

mark_onedevx = False
mark_onedevx_1 = False
mark_onedevx_2 = False

pl = False
mi = False
my = False
dv = False

mark_error = False

percent_num = 0

style_eqv = 0
style_oper = 0
style_sqr = 0

mark_font_oper = False
mark_font_sqr = False

mark_num_sys = False

mark_dec = False
mark_bin = False
mark_oct = False
mark_hex = False


def add_digit(digit):
    global num
    global write_scr
    global mark
    global dotted
    global zero_devision
    global mark_sqr
    global mark_sqr_1
    global mark_sqr_2
    global mark_sqrt
    global mark_sqrt_1
    global mark_sqrt_2
    global mark_onedevx
    global mark_onedevx_1
    global mark_onedevx_2
    global res_calc
    global text_bin
    global text_oct
    global text_hex
    global text_dec
    global mark_num_sys
    global mark_hex
    global mark_oct
    global mark_bin
    global mark_dec

    pl = False
    mi = False
    my = False
    dv = False

    if mark == False and len(num) <= 16:

        if str(digit) in '0123456789ABCDEF.':
            if mark_sqr == True:
                if mark_sqr_1 == True:
                    for i in num:
                        if num == []:
                            break
                        else:
                            num = num[1:]
                            write_scr = write_scr[1:]
                    num.append('0')
                    write_scr.append('0')
                    text_res_calc.set(f"{''.join(num)}")
                    text_calc.set(f"{''.join(num)}")
                    mark_sqr_1 = False
                    dotted = False

                if mark_sqr_2 == True:
                    for i in num:
                        if num[-1] in '+-*/':
                            break
                        else:
                            num = num[:-1]
                            write_scr = write_scr[:-1]
                    num.append('0')
                    write_scr.append('0')
                    text_res_calc.set(f"{''.join(num)}")
                    text_calc.set(f"{''.join(num)}")
                    dotted = False
                    mark_sqr_2 = False

                num = list(num)

                list_digit = []
                for i in str(num):
                    list_digit.append(i)

                if list_digit.count('e') > 0:
                    num = ['0']
                    write_scr = []
                    write_result = []
                    calculate = []
                    text_final_result.set(f'')
                    text_calc.set(f"0")
                    text_res_calc.set(f"0")
                    zero_devision = False
                    mark_sqr = False

            if mark_sqrt == True:
                if mark_sqrt_1 == True:
                    for i in num:
                        if num == []:
                            break
                        else:
                            num = num[1:]
                            write_scr = write_scr[1:]
                    num.append('0')
                    write_scr.append('0')

                    text_res_calc.set(f"{''.join(num)}")
                    text_calc.set(f"{''.join(num)}")
                    mark_sqrt_1 = False
                    dotted = False

                if mark_sqrt_2 == True:
                    for i in num:
                        if num[-1] in '+-*/':
                            break
                        else:
                            num = num[:-1]
                            write_scr = write_scr[:-1]
                    num.append('0')
                    write_scr.append('0')

                    text_res_calc.set(f"{''.join(num)}")
                    text_calc.set(f"{''.join(num)}")
                    dotted = False
                    mark_sqrt_2 = False


            if mark_sqrt == True:
                num = list(num)

                list_digit = []
                for i in str(num):
                    list_digit.append(i)

                if list_digit.count('e') > 0:
                    num = ['0']
                    write_scr = []
                    write_result = []
                    calculate = []
                    text_final_result.set(f'')
                    text_calc.set(f"0")
                    text_res_calc.set(f"0")
                    zero_devision = False
                    mark_sqrt = False

#////////////////////////////////////////////////////////////////////<------- 1/x

            if mark_onedevx == True:
                if mark_onedevx_1 == True:
                    for i in num:
                        if num == []:
                            break
                        else:
                            num = num[1:]
                            write_scr = write_scr[1:]
                    num.append('0')
                    write_scr.append('0')
                    text_res_calc.set(f"{''.join(num)}")
                    text_calc.set(f"{''.join(num)}")
                    mark_onedevx_1 = False
                    dotted = False

                if mark_onedevx_2 == True:
                    for i in num:
                        if num[-1] in '+-*/':
                            break
                        else:
                            num = num[:-1]
                            write_scr = write_scr[:-1]
                    num.append('0')
                    write_scr.append('0')
                    text_res_calc.set(f"{''.join(num)}")
                    text_calc.set(f"{''.join(num)}")
                    dotted = False
                    mark_onedevx_2 = False

                num = list(num)

                list_digit = []
                for i in str(num):
                    list_digit.append(i)

                if list_digit.count('e') > 0:
                    num = ['0']
                    write_scr = []
                    write_result = []
                    calculate = []
                    text_final_result.set(f'')
                    text_calc.set(f"0")
                    text_res_calc.set(f"0")
                    zero_devision = False
                    mark_onedevx = False
#///////////////////////////////////////////////////////////<-------конец 1/x


            if zero_devision == True:
                num = ['0']
                write_scr = []
                write_result = []
                calculate = []
                text_final_result.set(f'')
                text_calc.set(f"0")
                text_res_calc.set(f"0")
                zero_devision = False
                mark_sqr = False

            for i in num:
                if i in '/*-+':

                    if num[-1] == '0' and num[-2] in '+-*/' and mark_num_sys == False:
                        num = num[:-1]
                        write_scr = write_scr[:-1]

            if num[0] == '0':
                if num[-1] in '.123456789ABCDEF':
                    text_calc.set(f'')
                    num.append(str(digit))
                    text_calc.set(f"{''.join(num)}")

                    text_res_calc.set(f'')
                    write_scr.append(str(digit))
                    text_res_calc.set(f"{''.join(write_scr)}")

                elif num.count('0') > 1:
                    text_calc.set(f'')
                    num.append(str(digit))
                    text_calc.set(f"{''.join(num)}")

                    text_res_calc.set(f'')
                    write_scr.append(str(digit))
                    text_res_calc.set(f"{''.join(write_scr)}")

                else:

                    if mark_num_sys == True:
                        if mark_dec == True and mark_bin ==False and mark_oct == False and mark_hex == False:

                            num = num[1:]
                            write_scr = write_scr[1:]
                            text_calc.set(f'')
                            num.append(str(digit))
                            text_calc.set(f"{''.join(num)}")
                            text_res_calc.set(f'')
                            write_scr.append(str(digit))
                            text_res_calc.set(f"{''.join(write_scr)}")

                            text_dec.set(''.join(write_scr))
                            text_bin.set(f"{str(bin(int(''.join(write_scr))))}")
                            text_oct.set(f"{str(oct(int(''.join(write_scr))))}")
                            text_hex.set(f"{str(hex(int(''.join(write_scr)))).upper()}")

                        if mark_bin ==True and mark_dec == False and mark_oct == False and mark_hex == False:

                            num = num[1:]
                            write_scr = write_scr[1:]
                            text_calc.set(f'')
                            num.append(f"0b{str(digit)}")
                            text_calc.set(f"{''.join(num)}")
                            text_res_calc.set(f'')
                            write_scr.append(f"0b{str(digit)}")
                            text_res_calc.set(f"{''.join(write_scr)}")

                            text_dec.set(int(''.join(write_scr), 2))
                            text_bin.set(f"{''.join(write_scr)}")
                            text_oct.set(f"{oct(int(''.join(write_scr),2))}")
                            text_hex.set(f"{hex(int(''.join(write_scr), 2)).upper()}")

                        if mark_oct == True and mark_dec == False and mark_bin == False and mark_hex == False:
                            num = num[1:]
                            write_scr = write_scr[1:]
                            text_calc.set(f'')
                            num.append(f"0o{str(digit)}")
                            text_calc.set(f"{''.join(num)}")
                            text_res_calc.set(f'')
                            write_scr.append(f"0o{str(digit)}")
                            text_res_calc.set(f"{''.join(write_scr)}")

                            text_dec.set(int(''.join(write_scr), 8))
                            text_bin.set(f"{str(bin(int(''.join(write_scr), 8)))}")
                            text_oct.set(f"{''.join(write_scr)}")
                            text_hex.set(f"{str(hex(int(''.join(write_scr), 8))).upper()}")

                        if mark_hex == True and mark_dec == False and mark_bin == False and mark_oct == False:
                            num = num[1:]
                            write_scr = write_scr[1:]
                            text_calc.set(f'')
                            num.append(f"0X{str(digit)}")
                            text_calc.set(f"{''.join(num)}")
                            text_res_calc.set(f'')
                            write_scr.append(f"0X{str(digit)}")
                            text_res_calc.set(f"{''.join(write_scr)}")

                            text_dec.set(int(''.join(write_scr), 16))
                            text_bin.set(f"{str(bin(int(''.join(write_scr), 16)))}")
                            text_oct.set(f"{str(oct(int(''.join(write_scr), 16)))}")
                            text_hex.set(f"{str(''.join(write_scr)).upper()}")
                    else:
                        num = num[1:]
                        write_scr = write_scr[1:]
                        text_calc.set(f'')
                        num.append(str(digit))
                        text_calc.set(f"{''.join(num)}")
                        text_res_calc.set(f'')
                        write_scr.append(str(digit))
                        text_res_calc.set(f"{''.join(write_scr)}")
            else:

                if mark_num_sys == True:
                    if mark_dec == True and mark_bin == False and mark_oct == False and mark_hex == False:

                        text_calc.set(f'')
                        num.append(str(digit))
                        text_calc.set(f"{''.join(num)}")

                        text_res_calc.set(f'')
                        write_scr.append(str(digit))

                        text_res_calc.set(f"{''.join(write_scr)}")

                        text_dec.set(''.join(write_scr))
                        text_bin.set(f"{str(bin(int(''.join(write_scr))))}")
                        text_oct.set(f"{str(oct(int(''.join(write_scr))))}")
                        text_hex.set(f"{str(hex(int(''.join(write_scr)))).upper()}")

                    if mark_bin == True and mark_dec == False and mark_oct == False and mark_hex == False:
                        if num[-1] in '+-*/':
                            text_calc.set(f'')
                            num.append('0b')
                            num.append(str(digit))
                            text_calc.set(f"{''.join(num)}")

                            text_res_calc.set(f'')
                            write_scr.append('0b')
                            write_scr.append(str(digit))

                            text_res_calc.set(f"{''.join(write_scr)}")
                        else:
                            text_calc.set(f'')
                            num.append(str(digit))
                            text_calc.set(f"{''.join(num)}")

                            text_res_calc.set(f'')
                            write_scr.append(str(digit))

                            text_res_calc.set(f"{''.join(write_scr)}")

                        text_dec.set(int(''.join(write_scr), 2))
                        text_bin.set(f"{''.join(write_scr)}")
                        text_oct.set(f"{str(oct(int(''.join(write_scr), 2)))}")
                        text_hex.set(f"{str(hex(int(''.join(write_scr), 2))).upper()}")

                    if mark_oct == True and mark_dec == False and mark_bin == False and mark_hex == False:

                        if num[-1] in '+-*/':
                            text_calc.set(f'')
                            num.append('0o')
                            num.append(str(digit))
                            text_calc.set(f"{''.join(num)}")

                            text_res_calc.set(f'')
                            write_scr.append('0o')
                            write_scr.append(str(digit))

                            text_res_calc.set(f"{''.join(write_scr)}")
                        else:
                            text_calc.set(f'')
                            num.append(str(digit))
                            text_calc.set(f"{''.join(num)}")

                            text_res_calc.set(f'')
                            write_scr.append(str(digit))

                            text_res_calc.set(f"{''.join(write_scr)}")

                        text_dec.set(int(''.join(write_scr), 8))
                        text_bin.set(f"{str(bin(int(''.join(write_scr), 8)))}")
                        text_oct.set(f"{''.join(write_scr)}")
                        text_hex.set(f"{str(hex(int(''.join(write_scr), 8))).upper()}")

                    if mark_hex == True and mark_dec == False and mark_bin == False and mark_oct == False:

                        if num[-1] in '+-*/':
                            text_calc.set(f'')
                            num.append('0X')
                            num.append(str(digit))
                            text_calc.set(f"{''.join(num)}")

                            text_res_calc.set(f'')
                            write_scr.append('0X')
                            write_scr.append(str(digit))

                            text_res_calc.set(f"{''.join(write_scr)}")
                        else:
                            text_calc.set(f'')
                            num.append(str(digit))
                            text_calc.set(f"{''.join(num)}")

                            text_res_calc.set(f'')
                            write_scr.append(str(digit))

                            text_res_calc.set(f"{''.join(write_scr)}")

                        text_dec.set(int(''.join(write_scr), 16))
                        text_bin.set(f"{str(bin(int(''.join(write_scr), 16)))}")
                        text_oct.set(f"{str(oct(int(''.join(write_scr), 16)))}")
                        text_hex.set(f"{''.join(write_scr)}")


                else:
                        text_calc.set(f'')
                        num.append(str(digit))
                        text_calc.set(f"{''.join(num)}")

                        text_res_calc.set(f'')
                        write_scr.append(str(digit))

                        text_res_calc.set(f"{''.join(write_scr)}")


    elif mark == True and num[-1] in '+-*/' and len(num) <= 16:
        if str(digit) in '0123456789.ABCDEF':
            if mark_num_sys == True:
                if mark_dec == True:
                    text_calc.set(f'')
                    num.append(str(digit))
                    text_calc.set(f"{''.join(num)}")

                    text_res_calc.set(f'')
                    write_scr.append(str(digit))
                    text_res_calc.set(f"{''.join(write_scr)}")
                    text_dec.set(''.join(write_scr))
                    text_bin.set(f"{str(bin(int(''.join(write_scr))))}")
                    text_oct.set(f"{str(oct(int(''.join(write_scr))))}")
                    text_hex.set(f"{str(hex(int(''.join(write_scr)))).upper()}")

                if mark_bin == True:
                    text_calc.set(f'')
                    num.append('0b')
                    num.append(str(digit))
                    text_calc.set(f"{''.join(num)}")

                    text_res_calc.set(f'')
                    write_scr.append('0b')
                    write_scr.append(str(digit))

                    text_res_calc.set(f"{''.join(write_scr)}")
                    text_bin.set(f"{''.join(write_scr)}")
                    text_oct.set(f"{str(oct(int(''.join(write_scr), 2)))}")
                    text_hex.set(f"{str(hex(int(''.join(write_scr), 2))).upper()}")

                if mark_oct == True:
                    text_calc.set(f'')
                    num.append('0o')
                    num.append(str(digit))
                    text_calc.set(f"{''.join(num)}")

                    text_res_calc.set(f'')
                    write_scr.append('0o')
                    write_scr.append(str(digit))

                    text_res_calc.set(f"{''.join(write_scr)}")
                    text_bin.set(f"{str(bin(int(''.join(write_scr), 8)))}")
                    text_oct.set(f"{''.join(write_scr)}")
                    text_hex.set(f"{str(hex(int(''.join(write_scr), 8))).upper()}")

                if mark_hex == True:
                    text_calc.set(f'')
                    num.append('0X')
                    num.append(str(digit))
                    text_calc.set(f"{''.join(num)}")

                    text_res_calc.set(f'')
                    write_scr.append('0X')
                    write_scr.append(str(digit))

                    text_res_calc.set(f"{''.join(write_scr)}")
                    text_bin.set(f"{str(bin(int(''.join(write_scr), 16)))}")
                    text_oct.set(f"{str(oct(int(''.join(write_scr), 16)))}")
                    text_hex.set(f"{''.join(write_scr)}")

                mark = False
            else:
                text_calc.set(f'')
                num.append(str(digit))
                text_calc.set(f"{''.join(num)}")

                text_res_calc.set(f'')
                write_scr.append(str(digit))

                text_res_calc.set(f"{''.join(write_scr)}")
                mark = False

    elif mark == True and len(num) <= 16:
        text_final_result.set('')
        num = []
        write_scr = []
        write_result = []
        calculate = []
        if str(digit) in '0123456789.ABCDEF':
            if mark_num_sys == True:
                if mark_dec == True:
                    text_calc.set(f'')
                    num.append(str(digit))
                    text_calc.set(f"{''.join(num)}")

                    text_res_calc.set(f'')
                    write_scr.append(str(digit))
                    text_res_calc.set(f"{''.join(write_scr)}")
                    text_dec.set(''.join(write_scr))
                    text_bin.set(f"{str(bin(int(''.join(write_scr))))}")
                    text_oct.set(f"{str(oct(int(''.join(write_scr))))}")
                    text_hex.set(f"{str(hex(int(''.join(write_scr)))).upper()}")

                if mark_bin == True:
                    text_calc.set(f'')
                    num.append('0b')
                    num.append(str(digit))
                    text_calc.set(f"{''.join(num)}")

                    text_res_calc.set(f'')
                    write_scr.append('0b')
                    write_scr.append(str(digit))

                    text_res_calc.set(f"{''.join(write_scr)}")
                    text_bin.set(f"{''.join(write_scr)}")
                    text_oct.set(f"{str(oct(int(''.join(write_scr), 2)))}")
                    text_hex.set(f"{str(hex(int(''.join(write_scr), 2))).upper()}")

                if mark_oct == True:
                    text_calc.set(f'')
                    num.append('0o')
                    num.append(str(digit))
                    text_calc.set(f"{''.join(num)}")

                    text_res_calc.set(f'')
                    write_scr.append('0o')
                    write_scr.append(str(digit))

                    text_res_calc.set(f"{''.join(write_scr)}")
                    text_bin.set(f"{str(bin(int(''.join(write_scr), 8)))}")
                    text_oct.set(f"{''.join(write_scr)}")
                    text_hex.set(f"{str(hex(int(''.join(write_scr), 8))).upper()}")

                if mark_hex == True:
                    text_calc.set(f'')
                    num.append('0X')
                    num.append(str(digit))
                    text_calc.set(f"{''.join(num)}")

                    text_res_calc.set(f'')
                    write_scr.append('0X')
                    write_scr.append(str(digit))

                    text_res_calc.set(f"{''.join(write_scr)}")
                    text_bin.set(f"{str(bin(int(''.join(write_scr), 16)))}")
                    text_oct.set(f"{str(oct(int(''.join(write_scr), 16)))}")
                    text_hex.set(f"{''.join(write_scr)}")

                mark = False
            else:
                text_calc.set(f'')
                num.append(str(digit))
                text_calc.set(f"{''.join(num)}")

                text_res_calc.set(f'')
                write_scr.append(str(digit))

                text_res_calc.set(f"{''.join(write_scr)}")
                mark = False

    elif mark == True and len(num) > 16:
        text_final_result.set('')
        num = []
        write_scr = []
        write_result = []
        calculate = []
        if str(digit) in '0123456789.':
            text_calc.set(f'')
            num.append(str(digit))
            text_calc.set(f"{''.join(num)}")

            text_res_calc.set(f'')
            write_scr.append(str(digit))

            text_res_calc.set(f"{''.join(write_scr)}")
            mark = False

    font_style()


def dot(dott):
    global dotted
    global num
    global write_scr
    global mark
    global mark_sqr
    global mark_sqr_1
    global mark_sqr_2
    global mark_sqrt
    global mark_sqrt_1
    global mark_sqrt_2


 # ///////////////////////////////////////////////////////////////////////////////////////////<- Здесь точка взаимодействует с квадратом
    if mark_sqr_1 == True and (not num.count('+') > 0 and not num.count('-') > 0 and not num.count('*') > 0 and not num.count('/') > 0):
        for i in num:
            if num == []:
                break
            else:
                num = num[1:]
                write_scr = write_scr[1:]
        num.append('0')
        write_scr.append('0')
        num.append('.')
        write_scr.append('.')
        text_res_calc.set(f"{''.join(num)}")
        text_calc.set(f"{''.join(num)}")
        mark_sqr_1 = False


    if mark_sqr_2 == True and (num.count('+') > 0 or num.count('-') > 0 or num.count('*') > 0 or num.count('/') > 0):
        for i in num:
            if num[-1] in '+-*/':
                break
            else:
                num = num[:-1]
                write_scr = write_scr[:-1]
        num.append('0')
        write_scr.append('0')
        text_res_calc.set(f"{''.join(num)}")
        text_calc.set(f"{''.join(num)}")
        dotted = False
        mark_sqr_2 = False

# ///////////////////////////////////////////////////////////////////////////////////////////^^^^- Здесь точка взаимодействует с квадратом

#///////////////////////////////////////////////////////////////////////////////////////////<- Здесь точка взаимодействует с корнем

    if mark_sqrt_1 == True and (not num.count('+') > 0 and not num.count('-') > 0 and not num.count('*') > 0 and not num.count('/') > 0):
        for i in num:
            if num == []:
                break
            else:
                num = num[1:]
                write_scr = write_scr[1:]
        num.append('0')
        write_scr.append('0')
        num.append('.')
        write_scr.append('.')
        text_res_calc.set(f"{''.join(num)}")
        text_calc.set(f"{''.join(num)}")
        mark_sqrt_1 = False


    if mark_sqrt_2 == True and (num.count('+') > 0 or num.count('-') > 0 or num.count('*') > 0 or num.count('/') > 0):
        for i in num:
            if num[-1] in '+-*/':
                break
            else:
                num = num[:-1]
                write_scr = write_scr[:-1]
        num.append('0')
        write_scr.append('0')
        text_res_calc.set(f"{''.join(num)}")
        text_calc.set(f"{''.join(num)}")
        dotted = False
        mark_sqrt_2 = False


#///////////////////////////////////////////////////////////////////////////////////////////^^^^^- Здесь точка взаимодействует с корнем

    if mark == True:
        num = []
        write_scr =[]
        num.append('0')
        write_scr.append('0')
        num.append(str(dott))
        write_scr.append(str(dott))
        text_res_calc.set(f"{''.join(write_scr)}")
        text_calc.set(f"{''.join(num)}")
        mark = False

    if dotted == False and num[-1] in '+-*/':
        num.append('0')
        write_scr.append('0')
        num.append(str(dott))
        write_scr.append(str(dott))
        text_res_calc.set(f"{''.join(write_scr)}")
        text_calc.set(f"{''.join(num)}")
        dotted = True

    if dotted == False:
        if num[0] == '0':
            num = []
            write_scr = []

            num.append('0')
            write_scr.append('0')

        num.append(str(dott))
        write_scr.append(str(dott))
        text_res_calc.set(f"{''.join(write_scr)}")
        text_calc.set(f"{''.join(num)}")
        dotted = True
    font_style()


def add_operation(operation):
    global num
    global write_scr
    global write_result
    global calculate
    global dotted
    global mark_operation
    global zero_devision
    global mark_sqr_1
    global mark_sqr_2
    global mark_sqrt_1
    global mark_sqrt_2
    global mark_onedevx_1
    global mark_onedevx_2
    global oper_mark_sqr_1
    global oper_mark_sqrt_1
    global oper_mark_onedevx_1
    global mark_error
    global style_oper
    global mark_font_oper

    oper_mark_sqr_1 = mark_sqr_1
    oper_mark_sqrt_1 = mark_sqrt_1
    oper_mark_onedevx_1 = mark_onedevx_1

    try:
        if num[-1] in '-+/*':
            num.pop(-1)

        if num[0] in '+-*/':
            num.pop(0)

        if mark_num_sys == True:
            if mark_dec == True:
                calculate = eval(''.join(num))
            if mark_bin == True:
                calculate = eval(''.join(num))
                calculate = bin(calculate)
            if mark_oct == True:
                calculate = eval(''.join(num))
                calculate = oct(calculate)
            if mark_hex == True:
                calculate = eval(''.join(num))
                calculate = hex(calculate).upper()
        else:
            calculate = eval(''.join(num))

        text_calc.set(f"{calculate}")

        if len(str(calculate)) <= 17:
            style_oper = len(str(calculate))
        else:
            calculate = '{:g}'.format(calculate)
            style_oper = len(str(calculate))

        num = [str(calculate)]
        if mark_sqr_1 == True and mark_sqrt_1 == False and mark_onedevx_1 == False:
            text_final_result.set(f'({sqr_num_1})²{operation}')
        if mark_sqrt_1 == True and mark_sqr_1 == False and mark_onedevx_1 == False:
            text_final_result.set(f'√({sqrt_num_1}){operation}')
        if mark_onedevx_1 == True and mark_sqrt_1 == False and mark_sqr_1 == False:
            text_final_result.set(f'1/({onedevx_num_1}){operation}')
        if mark_sqr_1 == False and mark_sqrt_1 == False and mark_onedevx_1 == False:
            if mark_num_sys == True:
                if mark_dec == True:
                    text_final_result.set(f'{calculate}{operation}')
                if mark_bin == True:
                    text_final_result.set(f'{calculate}{operation}')
                if mark_oct == True:
                    text_final_result.set(f'{calculate}{operation}')
                if mark_hex == True:
                    text_final_result.set(f'{calculate.upper()}{operation}')
            else:
                text_res_calc.set(f"{calculate}")
                text_final_result.set(f'{calculate}{operation}')

        num.append(str(operation))
        text_calc.set(f"{''.join(num)}")
        write_scr = []

        dotted = False
        mark_operation = True
        mark_sqr_1 = False
        mark_sqr_2 = False
        mark_sqrt_1 = False
        mark_sqrt_2 = False
        mark_onedevx_1 = False
        mark_onedevx_2 = False
        mark_font_oper = mark_operation

    except ZeroDivisionError:
        text_res_calc.set(f"Деление на ноль невозможно")
        text_calc.set(f"")
        zero_devision = True
        mark_sqr_1 = False
        mark_sqr_2 = False
        mark_sqrt_1 = False
        mark_sqrt_2 = False
        mark_error = True

    font_style()


def rawno():
    global num
    global calculate
    global mark
    global dotted
    global mark_operation
    global zero_devision
    global mark_sqr_1
    global mark_sqr_2

    global mark_sqrt_1
    global mark_sqrt_2

    global oper_mark_sqr_1
    global oper_mark_sqrt_1

    global mark_onedevx_1
    global mark_onedevx_2

    global style_eqv
    global mark_error

    global text_bin
    global text_oct
    global text_hex
    global text_dec

    try:
        if num[-1] in '-+/*':
            num.pop(-1)

        calculate = eval(''.join(num))

        if len(str(calculate)) >= 16:
            calculate = round(calculate, 15)


#Вывод квадратов////////////////////////////////////////////////////////////////////////////////<--------!!!
        if (mark_sqr_1 == True or oper_mark_sqr_1 == True) and mark_sqr_2 == False and mark_sqrt_1 == False and mark_sqrt_2 == False and mark_onedevx_2 == False and mark_onedevx_1 == False:
            not_sqr_num_1 = ''
            for i in num:
                if i not in '+-*/':
                    num = num[1:]
                else:
                    break
            num = num[::-1]
            for i in num:
                if i not in '+-*/':
                    not_sqr_num_1 = i + not_sqr_num_1

            if num.count('+') > 0:
                text_final_result.set(f"({sqr_num_1})² + {not_sqr_num_1} =")
            if num.count('-') > 0:
                text_final_result.set(f"({sqr_num_1})² - {not_sqr_num_1} =")
            if num.count('*') > 0:
                text_final_result.set(f"({sqr_num_1})² * {not_sqr_num_1} =")
            if num.count('/') > 0:
                text_final_result.set(f"({sqr_num_1})² / {not_sqr_num_1} =")

            num = str(calculate)

        if mark_sqr_2 == True and mark_sqr_1 == False and mark_sqrt_1 == False and mark_sqrt_2 == False and oper_mark_sqr_1 == False and oper_mark_sqrt_1 == False and mark_onedevx_2 == False and mark_onedevx_1 == False and oper_mark_onedevx_1 == False:
            not_sqr_num_2 = ''
            for i in num:
                if i not in '+-*/':
                    num = num[:-1]
                else:
                    break
            for i in num:
                if i not in '+-*/':
                    not_sqr_num_2 = i + not_sqr_num_2

            if num.count('+') > 0:
                text_final_result.set(f"{not_sqr_num_2} + ({sqr_num_2})² =")
            if num.count('-') > 0:
                text_final_result.set(f"{not_sqr_num_2} - ({sqr_num_2})² =")
            if num.count('*') > 0:
                text_final_result.set(f"{not_sqr_num_2} * ({sqr_num_2})² =")
            if num.count('/') > 0:
                text_final_result.set(f"{not_sqr_num_2} / ({sqr_num_2})² =")

            num = str(calculate)

        if mark_sqr_2 == True and (mark_sqr_1 == True or oper_mark_sqr_1 == True) and mark_sqrt_1 == False and mark_sqrt_2 == False and mark_onedevx_2 == False and mark_onedevx_1 == False:

            if num.count('+') > 0:
                text_final_result.set(f"({sqr_num_1})² + ({sqr_num_2})² =")
            if num.count('-') > 0:
                text_final_result.set(f"({sqr_num_1})² - ({sqr_num_2})² =")
            if num.count('*') > 0:
                text_final_result.set(f"({sqr_num_1})² * ({sqr_num_2})² =")
            if num.count('/') > 0:
                text_final_result.set(f"({sqr_num_1})² / ({sqr_num_2})² =")
            num = str(calculate)


        if mark_sqr_1 == False and mark_sqr_2 == False and mark_sqrt_1 == False and mark_sqrt_2 == False and oper_mark_sqr_1 == False and oper_mark_sqrt_1 == False and mark_onedevx_2 == False and mark_onedevx_1 == False and oper_mark_sqrt_1 == False:
            text_final_result.set(f"{''.join(num)} =")


#Вывод корней/////////////////////////////////////////////////////////////////////////////////<--------!!!
        if (mark_sqrt_1 == True or oper_mark_sqrt_1 == True) and mark_sqrt_2 == False and mark_sqr_1 == False and mark_sqr_2 == False and mark_onedevx_2 == False and mark_onedevx_1 == False:
            not_sqrt_num_1 = ''
            for i in num:
                if i not in '+-*/':
                    num = num[1:]
                else:
                    break
            num = num[::-1]

            for i in num:
                if i not in '+-*/':
                    not_sqrt_num_1 = i + not_sqrt_num_1

            if num.count('+') > 0:
                text_final_result.set(f"√({sqrt_num_1}) + {not_sqrt_num_1} =")
            if num.count('-') > 0:
                text_final_result.set(f"√({sqrt_num_1}) - {not_sqrt_num_1} =")
            if num.count('*') > 0:
                text_final_result.set(f"√({sqrt_num_1}) * {not_sqrt_num_1} =")
            if num.count('/') > 0:
                text_final_result.set(f"√({sqrt_num_1}) / {not_sqrt_num_1} =")

            num = str(calculate)


        if mark_sqrt_2 == True and mark_sqrt_1 == False and mark_sqr_1 == False and mark_sqr_2 == False and oper_mark_sqrt_1 == False and oper_mark_sqr_1 == False and mark_onedevx_2 == False and mark_onedevx_1 == False and oper_mark_onedevx_1 == False:
            not_sqrt_num_2 = ''
            for i in num:
                if i not in '+-*/':
                    num = num[:-1]
                else:
                    break
            for i in num:
                if i not in '+-*/':
                    not_sqrt_num_2 = i + not_sqrt_num_2

            if num.count('+') > 0:
                text_final_result.set(f"{not_sqrt_num_2} + √({sqrt_num_2}) =")
            if num.count('-') > 0:
                text_final_result.set(f"{not_sqrt_num_2} - √({sqrt_num_2}) =")
            if num.count('*') > 0:
                text_final_result.set(f"{not_sqrt_num_2} * √({sqrt_num_2}) =")
            if num.count('/') > 0:
                text_final_result.set(f"{not_sqrt_num_2} / √({sqrt_num_2}) =")

            num = str(calculate)


        if mark_sqrt_2 == True and (mark_sqrt_1 == True or oper_mark_sqrt_1 == True) and mark_sqr_1 == False and mark_sqr_2 == False and mark_onedevx_2 == False and mark_onedevx_1 == False:

            if num.count('+') > 0:
                text_final_result.set(f"√({sqrt_num_1}) + √({sqrt_num_2}) =")
            if num.count('-') > 0:
                text_final_result.set(f"√({sqrt_num_1}) - √({sqrt_num_2}) =")
            if num.count('*') > 0:
                text_final_result.set(f"√({sqrt_num_1}) * √({sqrt_num_2}) =")
            if num.count('/') > 0:
                text_final_result.set(f"√({sqrt_num_1}) / √({sqrt_num_2}) =")
            num = str(calculate)


        if mark_sqrt_1 == False and mark_sqrt_2 == False and mark_sqr_1 == False and mark_sqr_2 == False and oper_mark_sqr_1 == False and oper_mark_sqrt_1 == False and mark_onedevx_2 == False and mark_onedevx_1 == False and oper_mark_sqrt_1 == False:
            text_final_result.set(f"{''.join(num)} =")


# Вывод 1/x <------/////////////////////////////////////////////////////////////////////////////////<--------!!!

        if (mark_onedevx_1 == True or oper_mark_onedevx_1 == True) and mark_sqr_1 == False and mark_sqr_2 == False and mark_sqrt_1 == False and mark_sqrt_2 == False and mark_onedevx_2 == False:
            not_onedevx_num_1 = ''
            for i in num:
                if i not in '+-*/':
                    num = num[1:]
                else:
                    break
            num = num[::-1]
            for i in num:
                if i not in '+-*/':
                    not_onedevx_num_1 = i + not_onedevx_num_1

            if num.count('+') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) + {not_onedevx_num_1} =")
            if num.count('-') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) - {not_onedevx_num_1} =")
            if num.count('*') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) * {not_onedevx_num_1} =")
            if num.count('/') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) / {not_onedevx_num_1} =")

            num = str(calculate)


        if mark_onedevx_2 == True and mark_sqr_1 == False and mark_sqr_2 == False and mark_sqrt_1 == False and mark_sqrt_2 == False and oper_mark_sqr_1 == False and oper_mark_sqrt_1 == False and mark_onedevx_1 == False and oper_mark_onedevx_1 == False:
            not_onedevx_num_2 = ''
            for i in num:
                if i not in '+-*/':
                    num = num[:-1]
                else:
                    break

            for i in num:
                if i not in '+-*/':
                    not_onedevx_num_2 = i + not_onedevx_num_2

            if num.count('+') > 0:
                text_final_result.set(f"{not_onedevx_num_2} + 1/({onedevx_num_2}) =")
            if num.count('-') > 0:
                text_final_result.set(f"{not_onedevx_num_2} - 1/({onedevx_num_2}) =")
            if num.count('*') > 0:
                text_final_result.set(f"{not_onedevx_num_2} * 1/({onedevx_num_2}) =")
            if num.count('/') > 0:
                text_final_result.set(f"{not_onedevx_num_2} / 1/({onedevx_num_2}) =")

            num = str(calculate)


        if mark_onedevx_2 == True and (mark_onedevx_1 == True or oper_mark_onedevx_1 == True) and mark_sqrt_1 == False and mark_sqrt_2 == False and mark_sqr_1 == False and mark_sqr_2 == False:

            if num.count('+') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) + 1/({onedevx_num_2}) =")
            if num.count('-') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) - 1/({onedevx_num_2}) =")
            if num.count('*') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) * 1/({onedevx_num_2}) =")
            if num.count('/') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) / 1/({onedevx_num_2}) =")
            num = str(calculate)


        if mark_sqr_1 == False and mark_sqr_2 == False and mark_sqrt_1 == False and mark_sqrt_2 == False and oper_mark_sqr_1 == False and oper_mark_sqrt_1 == False and mark_onedevx_1 == False and mark_onedevx_2 == False and oper_mark_onedevx_1 == False:
            text_final_result.set(f"{''.join(num)} =")

#смешанный вывод корней и квадратов и 1/x <-------/////////////////////////////////////////////////////////////////////////<--------!!!

        if (mark_sqr_1 == True or oper_mark_sqr_1 == True) and mark_sqrt_2 == True and mark_sqrt_1 == False and mark_onedevx_1 == False and mark_onedevx_2 == False and oper_mark_onedevx_1 == False and oper_mark_sqrt_1 == False:
            if num.count('+') > 0:
                text_final_result.set(f"({sqr_num_1})² + √({sqrt_num_2}) =")
            if num.count('-') > 0:
                text_final_result.set(f"({sqr_num_1})² - √({sqrt_num_2}) =")
            if num.count('*') > 0:
                text_final_result.set(f"({sqr_num_1})² * √({sqrt_num_2}) =")
            if num.count('/') > 0:
                text_final_result.set(f"({sqr_num_1})² / √({sqrt_num_2}) =")
            num = str(calculate)

        if (mark_sqrt_1 == True or oper_mark_sqrt_1 == True) and mark_sqr_2 == True and mark_sqr_1 == False and mark_onedevx_1 == False and mark_onedevx_2 == False and oper_mark_onedevx_1 == False and oper_mark_sqr_1 == False:

            if num.count('+') > 0:
                text_final_result.set(f"√({sqrt_num_1}) + ({sqr_num_2})² =")
            if num.count('-') > 0:
                text_final_result.set(f"√({sqrt_num_1}) - ({sqr_num_2})² =")
            if num.count('*') > 0:
                text_final_result.set(f"√({sqrt_num_1}) * ({sqr_num_2})² =")
            if num.count('/') > 0:
                text_final_result.set(f"√({sqrt_num_1}) / ({sqr_num_2})² =")
            num = str(calculate)

        if (mark_onedevx_1 == True or oper_mark_onedevx_1 == True) and mark_sqr_2 == True and mark_sqr_1 == False and mark_sqrt_1 == False and mark_sqrt_2 == False and oper_mark_sqr_1 == False and oper_mark_sqrt_1 == False:

            if num.count('+') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) + ({sqr_num_2})² =")
            if num.count('-') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) - ({sqr_num_2})² =")
            if num.count('*') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) * ({sqr_num_2})² =")
            if num.count('/') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) / ({sqr_num_2})² =")
            num = str(calculate)

        if (mark_onedevx_1 == True or oper_mark_onedevx_1 == True) and mark_sqrt_2 == True and mark_sqrt_1 == False and mark_sqr_1 == False and mark_sqr_2 == False and oper_mark_sqr_1 == False and oper_mark_sqrt_1 == False:

            if num.count('+') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) + √({sqrt_num_2}) =")
            if num.count('-') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) - √({sqrt_num_2}) =")
            if num.count('*') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) * √({sqrt_num_2}) =")
            if num.count('/') > 0:
                text_final_result.set(f"1/({onedevx_num_1}) / √({sqrt_num_2}) =")
            num = str(calculate)

        if (mark_sqr_1 == True or oper_mark_sqr_1 == True) and mark_onedevx_2 == True and mark_onedevx_1 == False and mark_sqr_2 == False and mark_sqrt_1 == False and mark_sqrt_2 == False and oper_mark_sqrt_1 == False and oper_mark_onedevx_1 == False:

            if num.count('+') > 0:
                text_final_result.set(f"({sqr_num_1})² + 1/({onedevx_num_2}) =")
            if num.count('-') > 0:
                text_final_result.set(f"({sqr_num_1})² - 1/({onedevx_num_2}) =")
            if num.count('*') > 0:
                text_final_result.set(f"({sqr_num_1})² * 1/({onedevx_num_2}) =")
            if num.count('/') > 0:
                text_final_result.set(f"({sqr_num_1})² / 1/({onedevx_num_2}) =")
            num = str(calculate)

        if (mark_sqrt_1 == True or oper_mark_sqrt_1 == True) and mark_onedevx_2 == True and mark_onedevx_1 == False and mark_sqrt_2 == False and mark_sqr_1 == False and mark_sqr_2 == False and oper_mark_sqr_1 == False and oper_mark_onedevx_1 == False:

            if num.count('+') > 0:
                text_final_result.set(f"√({sqrt_num_1}) + 1/({onedevx_num_2}) =")
            if num.count('-') > 0:
                text_final_result.set(f"√({sqrt_num_1}) - 1/({onedevx_num_2}) =")
            if num.count('*') > 0:
                text_final_result.set(f"√({sqrt_num_1}) * 1/({onedevx_num_2}) =")
            if num.count('/') > 0:
                text_final_result.set(f"√({sqrt_num_1}) / 1/({onedevx_num_2}) =")
            num = str(calculate)


        #общий вывод//////////////////////////////////////////////////////////////
        if mark_num_sys == True:
            if mark_dec == True:
                text_res_calc.set(f"{'{:,}'.format(calculate)}")
            if mark_bin == True:
                text_res_calc.set(f"{bin(calculate)}")
            if mark_oct == True:
                text_res_calc.set(f"{oct(calculate)}")
            if mark_hex == True:
                text_res_calc.set(f"{hex(calculate).upper()}")

            text_dec.set(int(calculate))
            text_bin.set(bin(calculate))
            text_oct.set(oct(calculate))
            text_hex.set(hex(calculate).upper())

        else:
            style_eqv = len(str('{:,}'.format(calculate)))

            text_calc.set(f"{'{:,}'.format(calculate)}")
            text_res_calc.set(f"{'{:,}'.format(calculate)}")

        mark = True
        dotted = False
        mark_operation = False
        mark_sqr_1 = False
        mark_sqr_2 = False
        mark_sqrt_1 = False
        mark_sqrt_2 = False
        mark_onedevx_1 = False
        mark_onedevx_2 = False

    except ZeroDivisionError:
        text_res_calc.set(f"Деление на ноль невозможно")
        text_calc.set(f"")
        zero_devision = True
        mark_error = True
    font_style()



def clear():
    global num
    global write_scr
    global write_result
    global calculate
    global dotted
    global mark_operation
    global mark_sqr
    global mark_sqr_1
    global mark_sqr_2
    global mark_sqrt
    global mark_sqrt_1
    global mark_sqrt_2
    global mark_onedevx
    global mark_onedevx_1
    global mark_onedevx_2

    if mark_num_sys == True:
        text_dec.set(f"0")
        text_bin.set(f"0")
        text_oct.set(f"0")
        text_hex.set(f"0")

    num = ['0']
    write_scr = []
    write_result = []
    calculate = []
    text_final_result.set(f'')
    text_calc.set(f"0")
    text_res_calc.set(f"0")

    mark = False
    dotted = False
    mark_operation = False
    mark_sqr = False
    mark_sqrt = False
    mark_sqr_1 = False
    mark_sqr_2 = False
    mark_sqrt_1 = False
    mark_sqrt_2 = False
    mark_onedevx = False
    mark_onedevx_1 = False
    mark_onedevx_2 = False
    pl = False
    mi = False
    my = False
    dv = False
    res_calc.config(font=("Arial", 36))


def CE():
    global num
    global write_scr
    global mark_operation
    global mark
    global dotted
    global mark_sqr
    global mark_sqrt
    global mark_sqr_1
    global mark_sqr_2
    global mark_sqrt_1
    global mark_sqrt_2
    global not_sqr_num_1
    global not_sqr_num_2
    global mark_onedevx_1
    global mark_onedevx_2
    global mark_onedevx

    if mark == True:
        num = ['0']
        write_scr = ['0']
        write_result = []
        calculate = []
        text_final_result.set(f'')
        text_calc.set(f"0")
        text_res_calc.set(f"0")
        not_sqr_num_1 = ''
        not_sqr_num_2 = ''


    if mark_operation == True:
        try:
            if num[-1] in '+-*/':
                try:
                    while num[0] not in '+-*/':
                        num.pop(0)
                        write_scr.pop(0)
                        text_res_calc.set(f"{''.join(write_scr)}")
                        text_calc.set(f"{''.join(num)}")

                except IndexError:
                    num.append('0')
                    write_scr.append('0')

                    text_res_calc.set(f"{''.join(write_scr)}")
                    text_calc.set(f"{''.join(num)}")
                    text_final_result.set(f"")

                    mark_operation == False

            while num[-1] not in '+-*/':
                num.pop(-1)
                write_scr.pop(-1)

            num.append('0')
            write_scr.append('0')
            text_res_calc.set(f"{''.join(write_scr)}")
            text_calc.set(f"{''.join(num)}")
            mark_operation == False
            not_sqr_num_2 = ''

        except IndexError:
            num.append('0')
            write_scr.append('0')
            text_res_calc.set(f"{''.join(write_scr)}")
            text_calc.set(f"{''.join(num)}")
            mark_operation == False
            not_sqr_num_2 = ''

    else:
        try:
            while num[0] not in '':
                num.pop(0)
                write_scr.pop(0)
                text_res_calc.set(f"{''.join(write_scr)}")
                text_calc.set(f"{''.join(num)}")
            not_sqr_num_1 = ''

        except IndexError:
            num.append('0')
            write_scr.append('0')
            text_res_calc.set(f"{''.join(write_scr)}")
            text_calc.set(f"{''.join(num)}")
            mark_operation == False
            not_sqr_num_2 = ''

    dotted = False
    mark_sqr = False
    mark_sqrt = False
    mark_onedevx = False
    res_calc.config(font=("Arial", 36))



def znak():
    try:
        dg = ''
        global num
        global write_scr
        zn = False

        if num.count('+') > 0 or num.count('-') > 0 or num.count('*') > 0 or num.count('/') > 0:
            invdg = ''
            while num[-1] not in '+-*/':
                invdg = num[-1] + invdg
                num.pop(-1)
                write_scr.pop(-1)

            num.append(invdg)
            write_scr.append(invdg)

            num = num[::-1]
            for i in num:
                if i in '+-*/':
                    break
                else:
                    dg = dg + i
            if dg[-1] in '-' and zn == True:
                dg = list(dg).pop(-1)
                zn = False

            if dg.count('.') > 0:
                dg = str(float(dg) * -1)
                zn = True

            else:
                dg = str(int(dg) * -1)
                zn = True

            num = num[::-1]

            while num[-1] not in '+-*/':
                num.pop(-1)
                write_scr.pop(-1)

        else:
            for i in num:
                if i in '+-*/':
                    pass
                else:
                    dg = dg + i
            if dg.count('.') > 0:
                dg = str(float(dg) * -1)

            else:
                dg = str(int(dg) * -1)

            num = []
            write_scr = []

        num.append(dg)
        write_scr.append(dg)
        text_res_calc.set(f"{''.join(write_scr)}")
        text_calc.set(f"{''.join(num)}")

    except IndexError:
        num = num.pop(-1)
        for i in num:
            if i in '+-*/':
                pass
            else:
                dg = dg + i

        if dg.count('.') > 0:
            dg = str(float(dg) * -1)


        else:
            dg = str(int(dg) * -1)

        num = []
        write_scr = []
        num.append(dg)
        write_scr.append(dg)
        text_res_calc.set(f"{''.join(write_scr)}")
        text_calc.set(f"{''.join(num)}")
        text_final_result.set(f'')


def backspase():
    global num
    global write_scr
    global mark
    global dotted
    if mark ==True:
        num = ['0']
        write_scr = []
        write_result = []
        calculate = []
        text_final_result.set(f'')
        text_calc.set(f"0")
        text_res_calc.set(f"0")
        mark = False

    if num[-1] in '+-*/':
        pass
    else:
        try:
            if num[-1] in '.':
                dotted = False
            num.pop(-1)
            write_scr.pop(-1)
            text_res_calc.set(f"{''.join(write_scr)}")
            text_calc.set(f"{''.join(num)}")

            if num[-1] in '+-*/':
                num.append('0')
                write_scr.append('0')
                text_res_calc.set(f"{''.join(write_scr)}")
                text_calc.set(f"{''.join(num)}")
        except IndexError:
            num.append('0')
            write_scr.append('0')
            text_res_calc.set(f"{''.join(write_scr)}")
            text_calc.set(f"{''.join(num)}")
    font_style()


def square():
    global num
    global write_scr
    global calculate
    global mark
    global dotted
    global mark_operation
    global zero_devision
    global mark_sqr
    global mark_sqr_1
    global mark_sqr_2
    global sqr_num_1
    global sqr_num_2
    global mark_error
    global mark_font_sqr
    global style_sqr


    mark_sqr = False

    if mark == False:

        if (num.count('+') > 0 or num.count('-') > 0 or num.count('*') > 0 or num.count('/') > 0) and num[-1] not in '+-*/':

            first_num = ''
            num = num[::-1]
            for i in num:
                if i not in '+-*/':
                    first_num = i + first_num
                else:
                    break

            for i in num:
                if i not in '+-*/':
                    num = num[1:]
                    write_scr = write_scr[1:]
                else:
                    break

            num = num[::-1]
            mark_sqr_2 = True

            sqr_num_2 = first_num


        else:


            first_num = ''
            for i in num:
                first_num = first_num + i

            if first_num[-1] in '+-*/':
                first_num = first_num[:-1]

            sqr_num_1 = first_num
            num = []
            write_scr = []
            mark_sqr_1 = True


        try:
            if ''.join(first_num).count('.') > 0:
                output = float(first_num)
            else:
                output = int(first_num)
            sqr_output = output * output
            sqr = sqr_output

            if len(str(sqr)) <= 17:
                style_sqr = len(str(sqr))
            else:
                sqr = '{:g}'.format(sqr)
                style_sqr = len(str(sqr))

            num.append(str(sqr))
            write_scr.append(str(sqr))

            if str(sqr).count('i') == 0:
                text_res_calc.set(f"{''.join(write_scr)}")
                text_calc.set(f"{''.join(num)}")
                text_final_result.set(f'({output})² =')

            else:
                num = ['0']
                write_scr = ['0']
                calculate = []
                text_res_calc.set(f"Переполнено")
                text_calc.set(f"")
                text_final_result.set(f'({output})² =')
                mark_sqr_1 = False
                mark_sqr_2 = False
                mark_error = True
                mark_sqr = False
        except ValueError:
            clear()
            text_res_calc.set(f"Переполнено")
            mark_error = True



    else:

        if num[-1] in '-+/*':
            num.pop(-1)

        calculate = eval(''.join(num))

        text_final_result.set(f"{''.join(num)} =")
        text_calc.set(f"{calculate}")
        text_res_calc.set(f"{calculate}")

        dotted = False
        mark_operation == False

        if ''.join(num).count('.') > 0:
            output = float(calculate)
        else:
            output = int(calculate)
        num = []
        write_scr = []
        sqr = output * output

        if len(str(sqr)) >= 16:
            sqr = round(sqr, 15)

        num.append(str(sqr))
        write_scr.append(str(sqr))

        if len(str(sqr)) <= 16:
            text_res_calc.set(f"{''.join(write_scr)}")
            text_calc.set(f"{''.join(num)}")
            text_final_result.set(f'({output})² =')


        else:
            num = ['0']
            write_scr = ['0']
            calculate = []
            text_res_calc.set(f"Переполнено")
            text_calc.set(f"")
            text_final_result.set(f'({output})² =')
            mark_error = True

        sqr_num_1 = calculate
        mark_sqr_1 = True

    mark_sqr = True
    mark = False
    mark_font_sqr = mark_sqr
    font_style()

def btsqrt():
    global num
    global write_scr
    global calculate
    global mark
    global dotted
    global mark_operation
    global zero_devision
    global mark_sqrt
    global mark_sqrt_1
    global mark_sqrt_2
    global sqrt_num_1
    global sqrt_num_2
    global mark_error

    try:
        mark_sqrt = False

        if mark == False:

            if (num.count('+') > 0 or num.count('-') > 0 or num.count('*') > 0 or num.count('/') > 0) and num[-1] not in '+-*/':

                first_num = ''
                num = num[::-1]
                for i in num:
                    if i not in '+-*/':
                        first_num = i + first_num
                    else:
                        break

                for i in num:
                    if i not in '+-*/':
                        num = num[1:]
                        write_scr = write_scr[1:]
                    else:
                        break

                num = num[::-1]
                mark_sqrt_2 = True
                sqrt_num_2 = first_num

            else:

                first_num = ''
                for i in num:
                    first_num = first_num + i

                if first_num[-1] in '+-*/':
                    first_num = first_num[:-1]

                sqrt_num_1 = first_num
                num = []
                write_scr = []
                mark_sqrt_1 = True

            if ''.join(first_num).count('.') > 0:
                output = float(first_num)
            else:
                output = int(first_num)

            sqrt_output = math.sqrt(output)
            sqrt = '{:g}'.format(sqrt_output)
            if len(str(sqrt)) >= 16:
                sqrt = round(sqrt, 15)

            num.append(str(sqrt))
            write_scr.append(str(sqrt))

            if len(str(sqrt)) <= 16:
                text_res_calc.set(f"{''.join(write_scr)}")
                text_calc.set(f"{''.join(num)}")
                text_final_result.set(f'√({output}) =')

            else:
                num = ['0']
                write_scr = ['0']
                calculate = []
                text_res_calc.set(f"Переполнено")
                text_calc.set(f"")
                text_final_result.set(f'√({output}) =')
                mark_error = True

        else:

            if num[-1] in '-+/*':
                num.pop(-1)

            calculate = eval(''.join(num))

            text_final_result.set(f"{''.join(num)} =")

            text_calc.set(f"{calculate}")

            text_res_calc.set(f"{calculate}")

            dotted = False
            mark_operation = False

            if ''.join(num).count('.') > 0:
                output = float(calculate)
            else:
                output = int(calculate)
            num = []
            write_scr = []
            sqrt = output**0.5

            if len(str(sqrt)) >= 16:
                sqrt = round(sqrt, 15)

            num.append(str(sqrt))
            write_scr.append(str(sqrt))

            if len(str(sqrt)) <= 16:
                text_res_calc.set(f"{''.join(write_scr)}")
                text_calc.set(f"{''.join(num)}")
                text_final_result.set(f'√({output}) =')


            else:
                num = ['0']
                write_scr = ['0']
                calculate = []
                text_res_calc.set(f"Переполнено")
                text_calc.set(f"")
                text_final_result.set(f'√({output}) =')
                mark_error = True

            sqrt_num_1 = calculate
            mark_sqrt_1 = True

        mark_sqrt = True
        mark = False

    except ValueError:
        text_final_result.set(f'√({output}) =')
        text_res_calc.set(f"Неверный ввод")
        text_calc.set(f"")
        num = ['0']
        write_scr = ['0']
        calculate = []
        mark_error = True
    font_style()


def onedevx():
    global num
    global write_scr
    global calculate
    global mark
    global dotted
    global mark_operation
    global zero_devision
    global mark_sqr
    global mark_sqr_1
    global mark_sqr_2
    global sqr_num_1
    global sqr_num_2
    global mark_onedevx
    global mark_onedevx_1
    global mark_onedevx_2
    global onedevx_num_1
    global onedevx_num_2
    global mark_error

    mark_onedevx = False

    if mark_onedevx == False:

        if (num.count('+') > 0 or num.count('-') > 0 or num.count('*') > 0 or num.count('/') > 0) and num[-1] not in '+-*/':

            first_num = ''
            num = num[::-1]
            for i in num:
                if i not in '+-*/':
                    first_num = i + first_num
                else:
                    break

            for i in num:
                if i not in '+-*/':
                    num = num[1:]
                    write_scr = write_scr[1:]
                else:
                    break

            num = num[::-1]
            mark_onedevx_2 = True
            onedevx_num_2 = first_num

        else:

            first_num = ''
            for i in num:
                first_num = first_num + i

            if first_num[-1] in '+-*/':
                first_num = first_num[:-1]

            onedevx_num_1 = first_num
            num = []
            write_scr = []
            mark_onedevx_1 = True

        try:
            if ''.join(first_num).count('.') > 0:
                output = float(first_num)
            else:
                output = int(first_num)
            onedevx_output = 1 / output
            onedevx = '{:g}'.format(onedevx_output)

            if len(str(onedevx)) >= 16:
                onedevx = round(onedevx, 15)

            num.append(str(onedevx))
            write_scr.append(str(onedevx))

            if onedevx.count('i') == 0:
                text_res_calc.set(f"{''.join(write_scr)}")
                text_calc.set(f"{''.join(num)}")
                text_final_result.set(f'1/({output}) =')

            else:
                num = ['0']
                write_scr = ['0']
                calculate = []
                text_res_calc.set(f"Переполнено")
                text_calc.set(f"")
                text_final_result.set(f'1/({output}) =')
                mark_onedevx_1 = False
                mark_onedevx_2 = False
                mark_error = True
                mark_onedevx = False
        except ZeroDivisionError:
            text_res_calc.set(f"Деление на ноль невозможно")
            text_calc.set(f"")
            num = ['0']
            write_scr = ['0']
            calculate = []
            zero_devision = True
            mark_error = True

    else:

        if num[-1] in '-+/*':
            num.pop(-1)

        calculate = eval(''.join(num))

        text_final_result.set(f"{''.join(num)} =")

        text_calc.set(f"{calculate}")

        text_res_calc.set(f"{calculate}")

        dotted = False
        mark_operation = False

        if ''.join(num).count('.') > 0:
            output = float(calculate)
        else:
            output = int(calculate)
        num = []
        write_scr = []
        onedevx = 1 / output

        if len(str(onedevx)) >= 16:
            sqr = round(onedevx, 15)

        num.append(str(onedevx))
        write_scr.append(str(onedevx))

        if len(str(onedevx)) <= 16:
            text_res_calc.set(f"{''.join(write_scr)}")
            text_calc.set(f"{''.join(num)}")
            text_final_result.set(f'1/({output}) =')


        else:
            num = ['0']
            write_scr = ['0']
            calculate = []
            text_res_calc.set(f"Переполнено")
            text_calc.set(f"")
            text_final_result.set(f'1/({output}) =')
            mark_error = True
        onedevx_num_1 = calculate
        mark_onedevx_1 = True

    mark_onedevx = True
    mark = False
    font_style()


def percent():
    global num
    global write_scr
    global calculate
    global mark
    global dotted
    global mark_operation
    global zero_devision
    global second_num
    global mark_sqr_1
    global mark_sqr_2
    global mark_sqrt_1
    global mark_sqrt_2
    global mark_onedevx_1
    global mark_onedevx_2
    global pl
    global mi
    global my
    global dv
    global percent_num

    opening_num = ''

    if mark == False:

        if (num.count('+') > 0 or num.count('-') > 0 or num.count('*') > 0 or num.count('/') > 0) and num[-1] not in '+-*/':
            pl = False
            mi = False
            my = False
            dv = False

            second_num = ''
            num = num[::-1]

            for i in num:
                if i not in '+-*/':
                    second_num = i + second_num
                else:
                    break

            for i in num:
                if i not in '+-*/':
                    num = num[1:]
                    write_scr = write_scr[1:]
                else:
                    break

            num = num[::-1]

            for i in num:
                opening_num = opening_num + i

            if opening_num[-1] in '+-*/':
                opening_num = opening_num[:-1]

            try:

                if ''.join(second_num).count('.') > 0 or ''.join(opening_num).count('.') > 0:
                        opening_num = float(opening_num)
                        second_num = float(second_num)
                else:
                        opening_num = int(opening_num)
                        second_num = int(second_num)

                if num.count('+') > 0:
                    percent_num = (opening_num * second_num) / 100
                    percent_num = '{:g}'.format(percent_num)
                    num.append(str(percent_num))
                    write_scr.append(str(percent_num))
                    text_calc.set(f"{''.join(num)}")
                    text_res_calc.set(f"{''.join(write_scr)}")
                    text_final_result.set(f'{opening_num} + {percent_num}')
                    pl = True

                if num.count('-') > 0:
                    percent_num = (opening_num * second_num) / 100
                    percent_num = '{:g}'.format(percent_num)
                    num.append(str(percent_num))
                    write_scr.append(str(percent_num))
                    text_calc.set(f"{''.join(num)}")
                    text_res_calc.set(f"{''.join(write_scr)}")
                    text_final_result.set(f'{opening_num} - {percent_num}')
                    mi = True

                if num.count('*') > 0:

                    percent_num = second_num * 0.01
                    percent_num = '{:g}'.format(percent_num)
                    num.append(str(percent_num))
                    write_scr.append(str(percent_num))
                    text_calc.set(f"{''.join(num)}")
                    text_res_calc.set(f"{''.join(write_scr)}")
                    text_final_result.set(f'{opening_num} * {percent_num}')
                    my = True

                if num.count('/') > 0:
                    percent_num = second_num * 0.01
                    percent_num = '{:g}'.format(percent_num)
                    num.append(str(percent_num))
                    write_scr.append(str(percent_num))
                    text_calc.set(f"{''.join(num)}")
                    text_res_calc.set(f"{''.join(write_scr)}")
                    text_final_result.set(f'{opening_num} / {percent_num}')
                    dv = True
            except ValueError:
                clear()
                text_res_calc.set(f"Более не поддерживается")

        else:
            num = ['0']
            write_scr = ['0']
            calculate = []
            text_res_calc.set(f"0")
            text_calc.set(f"0")
            text_final_result.set(f'0')

    else:
        if pl == True:
            percent_num = (float(calculate) * float(second_num)) / 100
            rez_calculate = float(calculate) + float(percent_num)
            rez_calculate = '{:g}'.format(rez_calculate)
            num = []
            write_scr = []
            num.append(str(rez_calculate))
            write_scr.append(str(rez_calculate))
            text_calc.set(f"{''.join(num)}")
            text_res_calc.set(f"{''.join(write_scr)}")
            text_final_result.set(f"{calculate} + {second_num}% =")
            calculate = '{:g}'.format(float(rez_calculate))

        if mi == True:
            percent_num = (float(calculate) * float(second_num)) / 100
            rez_calculate = float(calculate) - float(percent_num)
            rez_calculate = '{:g}'.format(rez_calculate)
            num = []
            write_scr = []
            num.append(str(rez_calculate))
            write_scr.append(str(rez_calculate))
            text_calc.set(f"{''.join(num)}")
            text_res_calc.set(f"{''.join(write_scr)}")
            text_final_result.set(f"{calculate} - {second_num}% =")
            calculate = '{:g}'.format(float(rez_calculate))

        if my == True:
            calculate = float(calculate) * float(percent_num)
            calculate = '{:g}'.format(calculate)
            num = []
            write_scr = []
            num.append(str(calculate))
            write_scr.append(str(calculate))
            text_calc.set(f"{''.join(num)}")
            text_res_calc.set(f"{''.join(write_scr)}")
            text_final_result.set(f"{calculate} * {second_num}% =")

        if dv == True:
            calculate = float(calculate) / float(percent_num)
            calculate = '{:g}'.format(calculate)
            num = []
            write_scr = []
            num.append(str(calculate))
            write_scr.append(str(calculate))
            text_calc.set(f"{''.join(num)}")
            text_res_calc.set(f"{''.join(write_scr)}")
            text_final_result.set(f"{calculate} / {second_num}% =")

    mark_sqr_1 = False
    mark_sqr_2 = False
    mark_sqrt_1 = False
    mark_sqrt_2 = False
    mark_onedevx_1 = False
    mark_onedevx_2 = False


#Новый дизайн--------------------------------------------------------------------------------
def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char in '\r':
        rawno()
    elif event.char in '\x08':
        backspase()
    elif event.char in '.':
        dot('.')
    elif event.char in '\x1b':
        clear()



root = Tk()
root.title("Калькулятор")
w, h = 328, 460
root.geometry(f'{w}x{h}+{(root.winfo_screenwidth()-w)//2}+{(root.winfo_screenheight()-h) // 2}')
root.iconbitmap('icon.ico')
root.resizable(width=False, height=False)
root.bind('<Key>', press_key)

rad_but = IntVar()
rad_but.set(0)

main_menu = Menu(root)
root.config(menu=main_menu)

working_mode = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Режим', menu=working_mode)
working_mode.add_command(label="Стандартный", command=lambda :start_mode())
working_mode.add_command(label="Системы счисления", command=lambda :second_mode())

def font_style():
    global mark_error
    global mark_font_oper
    global mark_font_sqr
    if len(write_scr) <= 11:
        res_calc.config(font=("Arial", 36))
    if len(write_scr) > 11:
        res_calc.config(font=("Arial", 34))
    if len(write_scr) > 12:
        res_calc.config(font=("Arial", 32))
    if len(write_scr) > 13:
        res_calc.config(font=("Arial", 30))
    if len(write_scr) > 14:
        res_calc.config(font=("Arial", 28))
    if len(write_scr) > 15:
        res_calc.config(font=("Arial", 26))
    if len(write_scr) > 16:
        res_calc.config(font=("Arial", 25))

    if mark == True:
        if style_eqv <= 11:
            res_calc.config(font=("Arial", 36))
        if style_eqv > 11:
            res_calc.config(font=("Arial", 34))
        if style_eqv > 12:
            res_calc.config(font=("Arial", 32))
        if style_eqv > 13:
            res_calc.config(font=("Arial", 30))
        if style_eqv > 14:
            res_calc.config(font=("Arial", 28))
        if style_eqv > 15:
            res_calc.config(font=("Arial", 26))
        if style_eqv > 16:
            res_calc.config(font=("Arial", 25))
        if style_eqv > 17:
            res_calc.config(font=("Arial", 20))

    if mark_font_oper == True:
        if style_oper <= 11:
            res_calc.config(font=("Arial", 36))
        if style_oper > 11:
            res_calc.config(font=("Arial", 34))
        if style_oper > 12:
            res_calc.config(font=("Arial", 32))
        if style_oper > 13:
            res_calc.config(font=("Arial", 30))
        if style_oper > 14:
            res_calc.config(font=("Arial", 28))
        if style_oper > 15:
            res_calc.config(font=("Arial", 26))
        if style_oper > 16:
            res_calc.config(font=("Arial", 25))
        if style_oper > 17:
            res_calc.config(font=("Arial", 20))
        mark_font_oper = False

    if mark_font_sqr == True:
        if style_sqr <= 11:
            res_calc.config(font=("Arial", 36))
        if style_sqr > 11:
            res_calc.config(font=("Arial", 34))
        if style_sqr > 12:
            res_calc.config(font=("Arial", 32))
        if style_sqr > 13:
            res_calc.config(font=("Arial", 30))
        if style_sqr > 14:
            res_calc.config(font=("Arial", 28))
        if style_sqr > 15:
            res_calc.config(font=("Arial", 26))
        if style_sqr > 16:
            res_calc.config(font=("Arial", 25))
        if style_sqr > 17:
            res_calc.config(font=("Arial", 20))
        mark_font_sqr = False

    if mark_error == True:
        res_calc.config(font=("Arial", 15))
        mark_error = False

def clear_screen():
    for i in root.winfo_children():
        if str(i) == '.!menu':
            pass
        else:
            i.destroy()

def start_mode():
    clear_screen()
    global final_result
    global res_calc
    global text_final_result
    global text_res_calc
    global text_calc
    global rad_but
    global num
    global write_scr
    global write_result
    global calculate

    num = ['0']
    write_scr = []
    write_result = []
    calculate = []

    rad_but.set(0)

    text_final_result = StringVar()
    text_res_calc = StringVar()
    text_calc = StringVar()

    text_final_result.set(f'')
    text_calc.set(f"0")
    text_res_calc.set(f"0")

    frame_finnaly = Frame(root)
    frame_finnaly.place(x=0, y=0, width=328, height=40)
    frame_num = Frame(root)
    frame_num.place(x=0, y=40, width=328, height=80)
    frame_button = Frame(root)
    frame_button.place(x=0, y=120, width=328, height=320)


    final_result = ttk.Label(frame_finnaly, text='0', style="Nine.TButton", textvariable=text_final_result, font=("Arial", 13), anchor=SE)
    final_result.place(x=1, y=0, width=326, height=38)
    res_calc = ttk.Label(frame_num, text="0", style="Eight.TButton", textvariable=text_res_calc, font=("Arial", 36), anchor=SE)
    res_calc.place(x=1, y=0, width=326, height=78)

    # <------------!!!!!Это общая строка для отладки! Не удалять!!!!!!!!!-------------------------------|
    # calc = Label(textvariable=text_calc, font=("Arial", 22)).grid(column=0, columnspan=4, row=2, ipady=5, sticky=E)
    # <^^^^^^^^^^^^!!!!!Это общая строка для отладки! Не удалять!!!!!!!!!^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|

    oper_btn_style = ttk.Style()
    oper_btn_style.configure("One.TButton", font = 'Arial 19', foreground = '#454545' )
    oper_btn_style.configure("Two.TButton", font = 'Arial 16 bold', foreground = '#e61919' )
    oper_btn_style.configure("Three.TButton", font = 'Arial 30', foreground = '#009aff' )
    oper_btn_style.configure("Four.TButton", font = 'Arial 11', foreground = '#358d24' )
    oper_btn_style.configure("Six.TButton", font = 'Arial 30', foreground = '#e61919' )
    oper_btn_style.configure("Seven.TButton", font = 'Arial 14', foreground = '#721294' )
    oper_btn_style.configure("Eight.TButton", font = 'Arial 14', foreground = '#004bcf' )
    oper_btn_style.configure("Nine.TButton", font = 'Arial 14', foreground = '#116062' )
    oper_btn_style.configure("Ten.TButton", font = 'Arial 14 bold', foreground = '#721294' )

    ttk.Button(frame_button, text="+", style = "Six.TButton", command=lambda: add_operation('+')).place(x=245, y=212, width=81, height=53)
    ttk.Button(frame_button, text="—", style = "Two.TButton",command=lambda: add_operation('-')).place(x=245, y=159, width=81, height=53)
    ttk.Button(frame_button, text="✕", style = "Two.TButton",command=lambda: add_operation('*')).place(x=245, y=106, width=81, height=53)
    ttk.Button(frame_button, text="÷", style = "Six.TButton",command=lambda: add_operation('/')).place(x=245, y=53, width=81, height=53)
    ttk.Button(frame_button, text="√x", style = "Four.TButton", command=lambda: btsqrt()).place(x=164, y=53, width=81, height=53)
    ttk.Button(frame_button, text="x²", style = "Four.TButton", command=lambda: square()).place(x=83, y=53, width=81, height=53)
    ttk.Button(frame_button, text="1/x", style = "Four.TButton", command=lambda: onedevx()).place(x=2, y=53, width=81, height=53)
    ttk.Button(frame_button, text="=", style = "Three.TButton",command=lambda: rawno()).place(x=245, y=265, width=81, height=53)
    ttk.Button(frame_button, text=".", style = "One.TButton", command=lambda: dot('.')).place(x=164, y=265, width=81, height=53)
    ttk.Button(frame_button, text="+/-", style = "One.TButton", command=lambda: znak()).place(x=2, y=265, width=81, height=53)
    ttk.Button(frame_button, text="⌫", style = "Ten.TButton", command=lambda: backspase()).place(x=245, y=0, width=81, height=53)
    ttk.Button(frame_button, text="C", style = "Seven.TButton", command=lambda: clear()).place(x=164, y=0, width=81, height=53)
    ttk.Button(frame_button, text="CE", style = "Seven.TButton", command=lambda: CE()).place(x=83, y=0, width=81, height=53)
    ttk.Button(frame_button, text="%", style = "Four.TButton", command=lambda: percent()).place(x=2, y=0, width=81, height=53)

    ttk.Button(frame_button, text="0", style = "One.TButton", command=lambda: add_digit(0)).place(x=83, y=265, width=81, height=53)
    ttk.Button(frame_button, text="1", style = "One.TButton", command=lambda: add_digit(1)).place(x=2, y=212, width=81, height=53)
    ttk.Button(frame_button, text="2", style = "One.TButton", command=lambda: add_digit(2)).place(x=83, y=212, width=81, height=53)
    ttk.Button(frame_button, text="3", style = "One.TButton", command=lambda: add_digit(3)).place(x=164, y=212, width=81, height=53)
    ttk.Button(frame_button, text="4", style = "One.TButton", command=lambda: add_digit(4)).place(x=2, y=159, width=81, height=53)
    ttk.Button(frame_button, text="5", style = "One.TButton", command=lambda: add_digit(5)).place(x=83, y=159, width=81, height=53)
    ttk.Button(frame_button, text="6", style = "One.TButton", command=lambda: add_digit(6)).place(x=164, y=159, width=81, height=53)
    ttk.Button(frame_button, text="7", style = "One.TButton", command=lambda: add_digit(7)).place(x=2, y=106, width=81, height=53)
    ttk.Button(frame_button, text="8", style = "One.TButton", command=lambda: add_digit(8)).place(x=83, y=106, width=81, height=53)
    ttk.Button(frame_button, text="9", style = "One.TButton", command=lambda: add_digit(9)).place(x=164, y=106, width=81, height=53)
    mark_num_sys = False


def second_mode():
    clear_screen()
    global final_result
    global res_calc
    global text_final_result
    global text_res_calc
    global text_calc
    global text_bin
    global rad_but
    global text_dec
    global text_hex
    global text_oct
    global mark_num_sys
    global mark_hex
    global mark_oct
    global mark_bin
    global mark_dec
    global num
    global write_scr
    global write_result
    global calculate

    num = ['0']
    write_scr = []
    write_result = []
    calculate = []

    text_final_result = StringVar()
    text_res_calc = StringVar()
    text_calc = StringVar()
    text_dec = StringVar()
    text_bin = StringVar()
    text_oct = StringVar()
    text_hex = StringVar()

    text_final_result.set(f'')
    text_calc.set(f"0")
    text_res_calc.set(f"0")
    text_dec.set(f"0")
    text_bin.set(f"0")
    text_oct.set(f"0")
    text_hex.set(f"0")

    def clb():
        for i in frame_button.winfo_children():
            i.destroy()


    def dec_numb():
        global mark_hex
        global mark_oct
        global mark_bin
        global mark_dec
        clear()
        clb()
        text_res_calc.set(text_dec.get())
        oper_btn_style = ttk.Style()
        oper_btn_style.configure("Dec1.TButton", font = 'Arial 19')
        oper_btn_style.configure("Dec2.TButton", font = 'Arial 13 bold')
        oper_btn_style.configure("Dec3.TButton", font = 'Arial 23')
        oper_btn_style.configure("Dec4.TButton", font = 'Arial 11')
        oper_btn_style.configure("Dec6.TButton", font = 'Arial 23')
        oper_btn_style.configure("Dec7.TButton", font = 'Arial 14')
        oper_btn_style.configure("Dec8.TButton", font = 'Arial 14')
        oper_btn_style.configure("Dec9.TButton", font = 'Arial 14')
        oper_btn_style.configure("Dec10.TButton", font = 'Arial 14 bold')
        oper_btn_style.configure("Dec11.TButton", font = 'Arial 12 bold',foreground = '#c1c1c1' )

        ttk.Button(frame_button, text="+", style = "Dec6.TButton", command=lambda: add_operation('+')).place(x=262, y=135, width=65, height=45)
        ttk.Button(frame_button, text="—", style = "Dec2.TButton",command=lambda: add_operation('-')).place(x=262, y=90, width=65, height=45)
        ttk.Button(frame_button, text="✕", style = "Dec2.TButton",command=lambda: add_operation('*')).place(x=262, y=45, width=65, height=45)
        ttk.Button(frame_button, text="÷", style = "Dec6.TButton",command=lambda: add_operation('/')).place(x=262, y=0, width=65, height=45)
        ttk.Button(frame_button, text="=", style = "Dec3.TButton",command=lambda: rawno()).place(x=262, y=180, width=65, height=45)
        ttk.Button(frame_button, text=".", style = "Dec11.TButton").place(x=197, y=180, width=65, height=45)
        ttk.Button(frame_button, text="+/-", style = "Dec11.TButton").place(x=67, y=180, width=65, height=45)
        ttk.Button(frame_button, text="⌫", style = "Dec10.TButton", command=lambda: backspase()).place(x=197, y=0, width=65, height=45)
        ttk.Button(frame_button, text="C", style = "Dec7.TButton", command=lambda: clear()).place(x=132, y=0, width=65, height=45)
        ttk.Button(frame_button, text="CE", style = "Dec7.TButton", command=lambda: CE()).place(x=67, y=0, width=65, height=45)

        ttk.Button(frame_button, text="0", style = "Dec1.TButton", command=lambda: add_digit(0)).place(x=132, y=180, width=65, height=45)
        ttk.Button(frame_button, text="1", style = "Dec1.TButton", command=lambda: add_digit(1)).place(x=67, y=135, width=65, height=45)
        ttk.Button(frame_button, text="2", style = "Dec1.TButton", command=lambda: add_digit(2)).place(x=132, y=135, width=65, height=45)
        ttk.Button(frame_button, text="3", style = "Dec1.TButton", command=lambda: add_digit(3)).place(x=197, y=135, width=65, height=45)
        ttk.Button(frame_button, text="4", style = "Dec1.TButton", command=lambda: add_digit(4)).place(x=67, y=90, width=65, height=45)
        ttk.Button(frame_button, text="5", style = "Dec1.TButton", command=lambda: add_digit(5)).place(x=132, y=90, width=65, height=45)
        ttk.Button(frame_button, text="6", style = "Dec1.TButton", command=lambda: add_digit(6)).place(x=197, y=90, width=65, height=45)
        ttk.Button(frame_button, text="7", style = "Dec1.TButton", command=lambda: add_digit(7)).place(x=67, y=45, width=65, height=45)
        ttk.Button(frame_button, text="8", style = "Dec1.TButton", command=lambda: add_digit(8)).place(x=132, y=45, width=65, height=45)
        ttk.Button(frame_button, text="9", style = "Dec1.TButton", command=lambda: add_digit(9)).place(x=197, y=45, width=65, height=45)
        ttk.Button(frame_button, text="A", style = "Dec11.TButton").place(x=2, y=0, width=65, height=38)
        ttk.Button(frame_button, text="B", style = "Dec11.TButton").place(x=2, y=38, width=65, height=38)
        ttk.Button(frame_button, text="C", style = "Dec11.TButton").place(x=2, y=76, width=65, height=38)
        ttk.Button(frame_button, text="D", style = "Dec11.TButton").place(x=2, y=113, width=65, height=38)
        ttk.Button(frame_button, text="E", style = "Dec11.TButton").place(x=2, y=150, width=65, height=38)
        ttk.Button(frame_button, text="F", style = "Dec11.TButton").place(x=2, y=187, width=65, height=38)
        mark_dec = True
        mark_bin = False
        mark_oct = False
        mark_hex = False

    def bin_numb():
        global mark_hex
        global mark_oct
        global mark_bin
        global mark_dec
        clear()
        clb()
        text_res_calc.set(text_bin.get())
        oper_btn_style = ttk.Style()
        oper_btn_style.configure("Dec1.TButton", font = 'Arial 19')
        oper_btn_style.configure("Dec2.TButton", font = 'Arial 13 bold')
        oper_btn_style.configure("Dec3.TButton", font = 'Arial 23')
        oper_btn_style.configure("Dec4.TButton", font = 'Arial 11')
        oper_btn_style.configure("Dec6.TButton", font = 'Arial 23')
        oper_btn_style.configure("Dec7.TButton", font = 'Arial 14')
        oper_btn_style.configure("Dec8.TButton", font = 'Arial 14')
        oper_btn_style.configure("Dec9.TButton", font = 'Arial 14')
        oper_btn_style.configure("Dec10.TButton", font = 'Arial 14 bold')
        oper_btn_style.configure("Dec11.TButton", font = 'Arial 12 bold',foreground = '#c1c1c1' )

        ttk.Button(frame_button, text="+", style = "Dec6.TButton", command=lambda: add_operation('+')).place(x=262, y=135, width=65, height=45)
        ttk.Button(frame_button, text="—", style = "Dec2.TButton",command=lambda: add_operation('-')).place(x=262, y=90, width=65, height=45)
        ttk.Button(frame_button, text="✕", style = "Dec2.TButton",command=lambda: add_operation('*')).place(x=262, y=45, width=65, height=45)
        ttk.Button(frame_button, text="÷", style = "Dec6.TButton",command=lambda: add_operation('/')).place(x=262, y=0, width=65, height=45)
        ttk.Button(frame_button, text="=", style = "Dec3.TButton",command=lambda: rawno()).place(x=262, y=180, width=65, height=45)
        ttk.Button(frame_button, text=".", style = "Dec11.TButton").place(x=197, y=180, width=65, height=45)
        ttk.Button(frame_button, text="+/-", style = "Dec11.TButton").place(x=67, y=180, width=65, height=45)
        ttk.Button(frame_button, text="⌫", style = "Dec10.TButton", command=lambda: backspase()).place(x=197, y=0, width=65, height=45)
        ttk.Button(frame_button, text="C", style = "Dec7.TButton", command=lambda: clear()).place(x=132, y=0, width=65, height=45)
        ttk.Button(frame_button, text="CE", style = "Dec7.TButton", command=lambda: CE()).place(x=67, y=0, width=65, height=45)

        ttk.Button(frame_button, text="0", style = "Dec1.TButton", command=lambda: add_digit(0)).place(x=132, y=180, width=65, height=45)
        ttk.Button(frame_button, text="1", style = "Dec1.TButton", command=lambda: add_digit(1)).place(x=67, y=135, width=65, height=45)
        ttk.Button(frame_button, text="2", style = "Dec11.TButton").place(x=132, y=135, width=65, height=45)
        ttk.Button(frame_button, text="3", style = "Dec11.TButton").place(x=197, y=135, width=65, height=45)
        ttk.Button(frame_button, text="4", style = "Dec11.TButton").place(x=67, y=90, width=65, height=45)
        ttk.Button(frame_button, text="5", style = "Dec11.TButton").place(x=132, y=90, width=65, height=45)
        ttk.Button(frame_button, text="6", style = "Dec11.TButton").place(x=197, y=90, width=65, height=45)
        ttk.Button(frame_button, text="7", style = "Dec11.TButton").place(x=67, y=45, width=65, height=45)
        ttk.Button(frame_button, text="8", style = "Dec11.TButton").place(x=132, y=45, width=65, height=45)
        ttk.Button(frame_button, text="9", style = "Dec11.TButton").place(x=197, y=45, width=65, height=45)
        ttk.Button(frame_button, text="A", style = "Dec11.TButton").place(x=2, y=0, width=65, height=38)
        ttk.Button(frame_button, text="B", style = "Dec11.TButton").place(x=2, y=38, width=65, height=38)
        ttk.Button(frame_button, text="C", style = "Dec11.TButton").place(x=2, y=76, width=65, height=38)
        ttk.Button(frame_button, text="D", style = "Dec11.TButton").place(x=2, y=113, width=65, height=38)
        ttk.Button(frame_button, text="E", style = "Dec11.TButton").place(x=2, y=150, width=65, height=38)
        ttk.Button(frame_button, text="F", style = "Dec11.TButton").place(x=2, y=187, width=65, height=38)
        mark_bin = True
        mark_oct = False
        mark_hex = False
        mark_dec = False


    def oct_numb():
        global mark_hex
        global mark_oct
        global mark_bin
        global mark_dec
        clear()
        clb()
        text_res_calc.set(text_oct.get())
        oper_btn_style = ttk.Style()
        oper_btn_style.configure("Dec1.TButton", font = 'Arial 19')
        oper_btn_style.configure("Dec2.TButton", font = 'Arial 13 bold')
        oper_btn_style.configure("Dec3.TButton", font = 'Arial 23')
        oper_btn_style.configure("Dec4.TButton", font = 'Arial 11')
        oper_btn_style.configure("Dec6.TButton", font = 'Arial 23')
        oper_btn_style.configure("Dec7.TButton", font = 'Arial 14')
        oper_btn_style.configure("Dec8.TButton", font = 'Arial 14')
        oper_btn_style.configure("Dec9.TButton", font = 'Arial 14')
        oper_btn_style.configure("Dec10.TButton", font = 'Arial 14 bold')
        oper_btn_style.configure("Dec11.TButton", font = 'Arial 12 bold',foreground = '#c1c1c1' )

        ttk.Button(frame_button, text="+", style = "Dec6.TButton", command=lambda: add_operation('+')).place(x=262, y=135, width=65, height=45)
        ttk.Button(frame_button, text="—", style = "Dec2.TButton",command=lambda: add_operation('-')).place(x=262, y=90, width=65, height=45)
        ttk.Button(frame_button, text="✕", style = "Dec2.TButton",command=lambda: add_operation('*')).place(x=262, y=45, width=65, height=45)
        ttk.Button(frame_button, text="÷", style = "Dec6.TButton",command=lambda: add_operation('/')).place(x=262, y=0, width=65, height=45)
        ttk.Button(frame_button, text="=", style = "Dec3.TButton",command=lambda: rawno()).place(x=262, y=180, width=65, height=45)
        ttk.Button(frame_button, text=".", style = "Dec11.TButton").place(x=197, y=180, width=65, height=45)
        ttk.Button(frame_button, text="+/-", style = "Dec11.TButton").place(x=67, y=180, width=65, height=45)
        ttk.Button(frame_button, text="⌫", style = "Dec10.TButton", command=lambda: backspase()).place(x=197, y=0, width=65, height=45)
        ttk.Button(frame_button, text="C", style = "Dec7.TButton", command=lambda: clear()).place(x=132, y=0, width=65, height=45)
        ttk.Button(frame_button, text="CE", style = "Dec7.TButton", command=lambda: CE()).place(x=67, y=0, width=65, height=45)

        ttk.Button(frame_button, text="0", style = "Dec1.TButton", command=lambda: add_digit(0)).place(x=132, y=180, width=65, height=45)
        ttk.Button(frame_button, text="1", style = "Dec1.TButton", command=lambda: add_digit(1)).place(x=67, y=135, width=65, height=45)
        ttk.Button(frame_button, text="2", style = "Dec1.TButton", command=lambda: add_digit(2)).place(x=132, y=135, width=65, height=45)
        ttk.Button(frame_button, text="3", style = "Dec1.TButton", command=lambda: add_digit(3)).place(x=197, y=135, width=65, height=45)
        ttk.Button(frame_button, text="4", style = "Dec1.TButton", command=lambda: add_digit(4)).place(x=67, y=90, width=65, height=45)
        ttk.Button(frame_button, text="5", style = "Dec1.TButton", command=lambda: add_digit(5)).place(x=132, y=90, width=65, height=45)
        ttk.Button(frame_button, text="6", style = "Dec1.TButton", command=lambda: add_digit(6)).place(x=197, y=90, width=65, height=45)
        ttk.Button(frame_button, text="7", style = "Dec1.TButton", command=lambda: add_digit(7)).place(x=67, y=45, width=65, height=45)
        ttk.Button(frame_button, text="8", style = "Dec11.TButton").place(x=132, y=45, width=65, height=45)
        ttk.Button(frame_button, text="9", style = "Dec11.TButton").place(x=197, y=45, width=65, height=45)
        ttk.Button(frame_button, text="A", style = "Dec11.TButton").place(x=2, y=0, width=65, height=38)
        ttk.Button(frame_button, text="B", style = "Dec11.TButton").place(x=2, y=38, width=65, height=38)
        ttk.Button(frame_button, text="C", style = "Dec11.TButton").place(x=2, y=76, width=65, height=38)
        ttk.Button(frame_button, text="D", style = "Dec11.TButton").place(x=2, y=113, width=65, height=38)
        ttk.Button(frame_button, text="E", style = "Dec11.TButton").place(x=2, y=150, width=65, height=38)
        ttk.Button(frame_button, text="F", style = "Dec11.TButton").place(x=2, y=187, width=65, height=38)
        mark_oct = True
        mark_hex = False
        mark_dec = False
        mark_bin = False


    def hex_numb():
        global mark_hex
        global mark_oct
        global mark_bin
        global mark_dec
        clear()
        clb()
        text_res_calc.set(text_hex.get())
        oper_btn_style = ttk.Style()
        oper_btn_style.configure("Dec1.TButton", font = 'Arial 19')
        oper_btn_style.configure("Dec2.TButton", font = 'Arial 13 bold')
        oper_btn_style.configure("Dec3.TButton", font = 'Arial 23')
        oper_btn_style.configure("Dec4.TButton", font = 'Arial 11')
        oper_btn_style.configure("Dec6.TButton", font = 'Arial 23')
        oper_btn_style.configure("Dec7.TButton", font = 'Arial 14')
        oper_btn_style.configure("Dec8.TButton", font = 'Arial 14')
        oper_btn_style.configure("Dec9.TButton", font = 'Arial 14')
        oper_btn_style.configure("Dec10.TButton", font = 'Arial 14 bold')
        oper_btn_style.configure("Dec11.TButton", font = 'Arial 12 bold',foreground = '#c1c1c1' )

        ttk.Button(frame_button, text="+", style = "Dec6.TButton", command=lambda: add_operation('+')).place(x=262, y=135, width=65, height=45)
        ttk.Button(frame_button, text="—", style = "Dec2.TButton",command=lambda: add_operation('-')).place(x=262, y=90, width=65, height=45)
        ttk.Button(frame_button, text="✕", style = "Dec2.TButton",command=lambda: add_operation('*')).place(x=262, y=45, width=65, height=45)
        ttk.Button(frame_button, text="÷", style = "Dec6.TButton",command=lambda: add_operation('/')).place(x=262, y=0, width=65, height=45)
        ttk.Button(frame_button, text="=", style = "Dec3.TButton",command=lambda: rawno()).place(x=262, y=180, width=65, height=45)
        ttk.Button(frame_button, text=".", style = "Dec11.TButton").place(x=197, y=180, width=65, height=45)
        ttk.Button(frame_button, text="+/-", style = "Dec11.TButton").place(x=67, y=180, width=65, height=45)
        ttk.Button(frame_button, text="⌫", style = "Dec10.TButton", command=lambda: backspase()).place(x=197, y=0, width=65, height=45)
        ttk.Button(frame_button, text="C", style = "Dec7.TButton", command=lambda: clear()).place(x=132, y=0, width=65, height=45)
        ttk.Button(frame_button, text="CE", style = "Dec7.TButton", command=lambda: CE()).place(x=67, y=0, width=65, height=45)

        ttk.Button(frame_button, text="0", style = "Dec1.TButton", command=lambda: add_digit(0)).place(x=132, y=180, width=65, height=45)
        ttk.Button(frame_button, text="1", style = "Dec1.TButton", command=lambda: add_digit(1)).place(x=67, y=135, width=65, height=45)
        ttk.Button(frame_button, text="2", style = "Dec1.TButton", command=lambda: add_digit(2)).place(x=132, y=135, width=65, height=45)
        ttk.Button(frame_button, text="3", style = "Dec1.TButton", command=lambda: add_digit(3)).place(x=197, y=135, width=65, height=45)
        ttk.Button(frame_button, text="4", style = "Dec1.TButton", command=lambda: add_digit(4)).place(x=67, y=90, width=65, height=45)
        ttk.Button(frame_button, text="5", style = "Dec1.TButton", command=lambda: add_digit(5)).place(x=132, y=90, width=65, height=45)
        ttk.Button(frame_button, text="6", style = "Dec1.TButton", command=lambda: add_digit(6)).place(x=197, y=90, width=65, height=45)
        ttk.Button(frame_button, text="7", style = "Dec1.TButton", command=lambda: add_digit(7)).place(x=67, y=45, width=65, height=45)
        ttk.Button(frame_button, text="8", style = "Dec1.TButton", command=lambda: add_digit(8)).place(x=132, y=45, width=65, height=45)
        ttk.Button(frame_button, text="9", style = "Dec1.TButton", command=lambda: add_digit(9)).place(x=197, y=45, width=65, height=45)
        ttk.Button(frame_button, text="A", style = "Dec1.TButton", command=lambda: add_digit('A')).place(x=2, y=0, width=65, height=38)
        ttk.Button(frame_button, text="B", style = "Dec1.TButton", command=lambda: add_digit('B')).place(x=2, y=38, width=65, height=38)
        ttk.Button(frame_button, text="C", style = "Dec1.TButton", command=lambda: add_digit('C')).place(x=2, y=76, width=65, height=38)
        ttk.Button(frame_button, text="D", style = "Dec1.TButton", command=lambda: add_digit('D')).place(x=2, y=113, width=65, height=38)
        ttk.Button(frame_button, text="E", style = "Dec1.TButton", command=lambda: add_digit('E')).place(x=2, y=150, width=65, height=38)
        ttk.Button(frame_button, text="F", style = "Dec1.TButton", command=lambda: add_digit('F')).place(x=2, y=187, width=65, height=38)
        mark_hex = True
        mark_dec = False
        mark_bin = False
        mark_oct = False


    frame_finnaly = Frame(root)
    frame_finnaly.place(x=0, y=0, width=328, height=38)
    frame_num = Frame(root)
    frame_num.place(x=0, y=40, width=328, height=170)
    frame_button = Frame(root)
    frame_button.place(x=0, y=210, width=328, height=500) #height=230

    #print(frame_button.winfo_children())

    final_result = ttk.Label(frame_finnaly, text='0', style="Nine.TButton", textvariable=text_final_result, font=("Arial", 13), anchor=SE)
    final_result.place(x=1, y=0, width=326, height=38)
    res_calc = ttk.Label(frame_num, text="0", style="Eight.TButton", textvariable=text_res_calc, font=("Arial", 36), anchor=SE)
    res_calc.place(x=1, y=0, width=326, height=58)

    # <------------!!!!!Это общая строка для отладки! Не удалять!!!!!!!!!-------------------------------|
    # calc = ttk.Label(frame_num,textvariable=text_calc, font=("Arial", 10), anchor=SE)
    # calc.place(x=1, y=58, width=326, height=17)
    # <^^^^^^^^^^^^!!!!!Это общая строка для отладки! Не удалять!!!!!!!!!^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|

    dec_calc = ttk.Label(frame_num,textvariable=text_dec, font=("Arial", 10), anchor=SE)
    dec_calc.place(x=1, y=75, width=280, height=17)
    bin_calc = ttk.Label(frame_num,textvariable=text_bin, font=("Arial", 10), anchor=SE)
    bin_calc.place(x=1, y=92, width=280, height=17)
    oct_calc = ttk.Label(frame_num,textvariable=text_oct, font=("Arial", 10), anchor=SE)
    oct_calc.place(x=1, y=109, width=280, height=17)
    hex_calc = ttk.Label(frame_num,textvariable=text_hex, font=("Arial", 10), anchor=SE)
    hex_calc.place(x=1, y=126, width=280, height=17)
    dec_rad = ttk.Radiobutton(frame_num, text='DEC', variable=rad_but, value=0, command=lambda :dec_numb())
    dec_rad.place(x=280, y=75, width=47, height=17)
    bin_rad = ttk.Radiobutton(frame_num, text='BIN', variable=rad_but, value=1, command=lambda :bin_numb())
    bin_rad.place(x=280, y=92, width=47, height=17)
    oct_rad = ttk.Radiobutton(frame_num, text='OCT', variable=rad_but, value=2, command=lambda :oct_numb())
    oct_rad.place(x=280, y=109, width=47, height=17)
    hex_rad = ttk.Radiobutton(frame_num, text='HEX', variable=rad_but, value=3, command=lambda :hex_numb())
    hex_rad.place(x=280, y=126, width=47, height=17)

    dec_numb()
    mark_num_sys = True

start_mode()
#Это новый коментарий!
#это новый коментарий в новой ветке number-systems
root.mainloop()


