# Simple Stop Loss Calculator
# HGP 05-Mar-2021

###########
# Imports #
###########

import os

#############
# Variables #
#############

# Decimals
dc = 4

# Leverage xN
lv = 20

# Stop Loss Percentage
sl = 20

# Take Profit Percentage
tp1 = 20
tp2 = 40
tp3 = 60

########
# Main #
########

while True:
    os.system('clear')
    print ('\n    *** Stop Loss Calculator ***')
    print ('\n - Input 0 to exit.')
    print (' - Input 1 for Long Position')
    print (' - Input 2 for Short Position')
    print (' - Input 3 for Leverage Adjustment (Default x20)')
    print (' - Input 4 for Stop Loss Adjustment (Default -20%)')
    print (' - Input 5 for Take Profit 1 Adjustment (Default +20%)')
    print (' - Input 6 for Take Profit 2 Adjustment (Default +40%)')
    print (' - Input 7 for Take Profit 3 Adjustment (Default +60%)')
    print (' - Input 8 for Decimals Adjustment (Default 4, for example: 1.0239)')

    print ('\n [info] Current values:\n')

    print ('   - Leverage: x' + str(lv))
    print ('   - Take Profit 1: +' + str(tp1) + '%')
    print ('   - Take Profit 2: +' + str(tp2) + '%')
    print ('   - Take Profit 3: +' + str(tp3) + '%')
    print ('   - Stop Loss:   -' + str(sl) + '%')

    option = input('\n >> ')

    # Exit Menu
    if option == '0':
        os.system('clear')
        print ('\n [!] Closing...')
        exit()

    # Long Position
    elif option == '1':
        os.system('clear')
        print ('\n    *** Long Position ***\n')
        print (' [*] Insert Entry Price: ')
        
        entry = float(input('\n >>> '))

        # How much % is "lv" of "entry"
        # Example: 
        # entry = 5000 
        # lv = 10
        # How much is 10% of 5000?
        # result = 500
        lv_percentage = round(float((entry * lv) / 100), dc)

        # How much is 1% of "entry"
        # Example: 
        # entry = 5000 
        # How much is 1% of 5000?
        # result = 50
        one_percentage = round(float((entry * 1) / 100), dc)

        # "lv_percentage" is what percent of 1%?
        # Example: 
        # 500 is what percent of 50?
        # result = 10%
        lv_one_percentage = round(float((one_percentage * 100) / lv_percentage), dc)

        # How much % is "lv_one_percentage" of 1%?
        # Example: 
        # How much is 10% of 50?
        # result = 5
        # Multiplied by tp1 & sl
        target_price_tp1 = round(float((lv_one_percentage * one_percentage) / 100), dc) * tp1
        target_price_tp2 = round(float((lv_one_percentage * one_percentage) / 100), dc) * tp2
        target_price_tp3 = round(float((lv_one_percentage * one_percentage) / 100), dc) * tp3
        target_price_sl = round(float((lv_one_percentage * one_percentage) / 100), dc) * sl

        # "entry" + "target_price" (tp & sl)
        target_price_sum_tp1 = round(float(entry + target_price_tp1), dc)
        target_price_sum_tp2 = round(float(entry + target_price_tp2), dc)
        target_price_sum_tp3 = round(float(entry + target_price_tp3), dc)
        target_price_sum_sl = round(float(entry - target_price_sl), dc)

        # Risk/Reward Ratio Calculation
        rr1 = round(float( round(float((entry * tp1) / 100), dc) / round(float((entry * sl) / 100), dc) ), 1)
        rr2 = round(float( round(float((entry * tp2) / 100), dc) / round(float((entry * sl) / 100), dc) ), 1)
        rr3 = round(float( round(float((entry * tp3) / 100), dc) / round(float((entry * sl) / 100), dc) ), 1)

        # Price Difference Calculation
        pd1 = round(float( round(float(target_price_sum_tp1 - entry), dc) * 100 ), 2)
        pd2 = round(float( round(float(target_price_sum_tp2 - entry), dc) * 100 ), 2)
        pd3 = round(float( round(float(target_price_sum_tp3 - entry), dc) * 100 ), 2)
        pd4 = round(float( round(float(entry - target_price_sum_sl), dc) * 100 ), 2)

        # Price Change Calculation
        pc1 = round(float( pd1 / entry ), 2)
        pc2 = round(float( pd2 / entry ), 2)
        pc3 = round(float( pd3 / entry ), 2)
        pc4 = round(float( pd4 / entry ), 2)

        # STDOUT
        print ('\n [info] Current values:\n')

        print ('   - Leverage: x' + str(lv))
        print ('   - Take Profit 1: +' + str(tp1) + '%')
        print ('   - Take Profit 2: +' + str(tp2) + '%')
        print ('   - Take Profit 3: +' + str(tp3) + '%')
        print ('   - Stop Loss:   -' + str(sl) + '%')

        print ('\n [+] Take Profit 1 at:', target_price_sum_tp1)
        print (' [+] Take Profit 2 at:', target_price_sum_tp2)
        print (' [+] Take Profit 3 at:', target_price_sum_tp3)
        print (' [+] Stop Loss at:  ', target_price_sum_sl)

        print ('\n [+] Risk/Reward Ratio 1: ', rr1)
        print (' [+] Risk/Reward Ratio 2: ', rr2)
        print (' [+] Risk/Reward Ratio 3: ', rr3)

        print ('\n [+] Real Price Change for Take Profit 1: ', str(pc1) + '%')
        print (' [+] Real Price Change for Take Profit 2: ', str(pc2) + '%')
        print (' [+] Real Price Change for Take Profit 3: ', str(pc3) + '%')
        print (' [+] Real Price Change for Stop Loss: ', str(pc4) + '%')

        input('\n [*] Press any key to continue...')
        os.system('clear')

    # Short Position
    elif option == '2':
        os.system('clear')
        print ('\n    *** Short Position ***\n')
        print (' [*] Insert Entry Price: ')
        
        entry = float(input('\n >>> '))

        # How much % is "lv" of "entry"
        # Example: 
        # entry = 5000 
        # lv = 10
        # How much is 10% of 5000?
        # result = 500
        lv_percentage = round(float((entry * lv) / 100), dc)

        # How much is 1% of "entry"
        # Example: 
        # entry = 5000 
        # How much is 1% of 5000?
        # result = 50
        one_percentage = round(float((entry * 1) / 100), dc)

        # "lv_percentage" is what percent of 1%?
        # Example: 
        # 500 is what percent of 50?
        # result = 10%
        lv_one_percentage = round(float((one_percentage * 100) / lv_percentage), dc)

        # How much % is "lv_one_percentage" of 1%?
        # Example: 
        # How much is 10% of 50?
        # result = 5
        # Multiplied by tp1 & sl
        target_price_tp1 = round(float((lv_one_percentage * one_percentage) / 100), dc) * tp1
        target_price_tp2 = round(float((lv_one_percentage * one_percentage) / 100), dc) * tp2
        target_price_tp3 = round(float((lv_one_percentage * one_percentage) / 100), dc) * tp3
        target_price_sl = round(float((lv_one_percentage * one_percentage) / 100), dc) * sl

        # "entry" + "target_price" (tp1 & sl)
        target_price_sum_tp1 = round(float(entry - target_price_tp1), dc)
        target_price_sum_tp2 = round(float(entry - target_price_tp2), dc)
        target_price_sum_tp3 = round(float(entry - target_price_tp3), dc)
        target_price_sum_sl = round(float(entry + target_price_sl), dc)

        # Risk/Reward Ratio Calculation
        rr1 = round(float( round(float((entry * tp1) / 100), dc) / round(float((entry * sl) / 100), dc) ), 1)
        rr2 = round(float( round(float((entry * tp2) / 100), dc) / round(float((entry * sl) / 100), dc) ), 1)
        rr3 = round(float( round(float((entry * tp3) / 100), dc) / round(float((entry * sl) / 100), dc) ), 1)
        
        # Price Difference Calculation
        pd1 = round(float( round(float(entry - target_price_sum_tp1), dc) * 100 ), 2)
        pd2 = round(float( round(float(entry - target_price_sum_tp2), dc) * 100 ), 2)
        pd3 = round(float( round(float(entry - target_price_sum_tp3), dc) * 100 ), 2)
        pd4 = round(float( round(float(target_price_sum_sl - entry), dc) * 100 ), 2)

        # Price Change Calculation
        pc1 = round(float( pd1 / entry ), 2)
        pc2 = round(float( pd2 / entry ), 2)
        pc3 = round(float( pd3 / entry ), 2)
        pc4 = round(float( pd4 / entry ), 2)

        # STDOUT
        print ('\n [info] Current values:\n')

        print ('   - Leverage: x' + str(lv))
        print ('   - Take Profit: +' + str(tp1) + '%')
        print ('   - Stop Loss:   -' + str(sl) + '%')

        print ('\n [+] Take Profit 1 at:', target_price_sum_tp1)
        print (' [+] Take Profit 2 at:', target_price_sum_tp2)
        print (' [+] Take Profit 3 at:', target_price_sum_tp3)
        print (' [+] Stop Loss at:  ', target_price_sum_sl)

        print ('\n [+] Risk/Reward Ratio 1: ', rr1)
        print (' [+] Risk/Reward Ratio 2: ', rr2)
        print (' [+] Risk/Reward Ratio 3: ', rr3)

        print ('\n [+] Real Price Change for Take Profit 1: ', str(pc1) + '%')
        print (' [+] Real Price Change for Take Profit 2: ', str(pc2) + '%')
        print (' [+] Real Price Change for Take Profit 3: ', str(pc3) + '%')
        print (' [+] Real Price Change for Stop Loss: ', str(pc4) + '%')

        input('\n [*] Press any key to continue...')
        os.system('clear')

    # Leverage
    elif option == '3':
        os.system('clear')
        print ('\n    *** Leverage adjustment ***\n')
        print (' [*] Insert new value (Example: 10): ')

        lv = int(input('\n >>> '))

    # Stop Loss
    elif option == '4':
        os.system('clear')
        print ('\n    *** Stop Loss adjustment ***\n')
        print (' [*] Insert new value (Example: 10): ')

        sl = float(input('\n >>> '))

    # Take Profit 1
    elif option == '5':
        os.system('clear')
        print ('\n    *** Take Profit 1 adjustment ***\n')
        print (' [*] Insert new value (Example: 10): ')

        tp1 = float(input('\n >>> '))

    # Take Profit 2
    elif option == '6':
        os.system('clear')
        print ('\n    *** Take Profit 2 adjustment ***\n')
        print (' [*] Insert new value (Example: 20): ')

        tp2 = float(input('\n >>> '))

    # Take Profit 3
    elif option == '7':
        os.system('clear')
        print ('\n    *** Take Profit 3 adjustment ***\n')
        print (' [*] Insert new value (Example: 30): ')

        tp3 = float(input('\n >>> '))

    # Decimals
    elif option == '8':
        os.system('clear')
        print ('\n    *** Decimals adjustment ***\n')
        print (' [*] Insert new value (Example: 3): ')

        dc = float(input('\n >>> '))

    # Wrong Option
    else:
        os.system('clear')
        print ('\n[!] Wrong Option! Try Again')
        input('\n   [*] Press any key to continue...')
