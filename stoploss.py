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
tp = 40

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
    print (' - Input 4 for Take Profit Adjustment (Default +40%)')
    print (' - Input 5 for Stop Loss Adjustment (Default -20%)')
    print (' - Input 6 for Decimals Adjustment (Default 4, for example: 1.0239)')

    print ('\n [info] Current values:\n')

    print ('   - Leverage: x' + str(lv))
    print ('   - Take Profit: +' + str(tp) + '%')
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
        # Multiplied by tp & sl
        target_price_tp = round(float((lv_one_percentage * one_percentage) / 100), dc) * tp
        target_price_sl = round(float((lv_one_percentage * one_percentage) / 100), dc) * sl

        # "entry" + "target_price" (tp & sl)
        target_price_sum_tp = round(float(entry + target_price_tp), dc)
        target_price_sum_sl = round(float(entry - target_price_sl), dc)

        # Risk/Reward Ratio Calculation
        rr = round(float( round(float((entry * tp) / 100), dc) / round(float((entry * sl) / 100), dc) ), 2)
        
        print ('\n [info] Current values:\n')

        print ('   - Leverage: x' + str(lv))
        print ('   - Take Profit: +' + str(tp) + '%')
        print ('   - Stop Loss:   -' + str(sl) + '%')

        print ('\n [+] Take Profit at:', target_price_sum_tp)
        print (' [+] Stop Loss at:  ', target_price_sum_sl)

        print (' [+] Risk/Reward Ratio: ', rr)

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
        # Multiplied by tp & sl
        target_price_tp = round(float((lv_one_percentage * one_percentage) / 100), dc) * tp
        target_price_sl = round(float((lv_one_percentage * one_percentage) / 100), dc) * sl

        # "entry" + "target_price" (tp & sl)
        target_price_sum_tp = round(float(entry - target_price_tp), dc)
        target_price_sum_sl = round(float(entry + target_price_sl), dc)

        # Risk/Reward Ratio Calculation
        rr = round(float( round(float((entry * tp) / 100), dc) / round(float((entry * sl) / 100), dc) ), 2)
        
        print ('\n [info] Current values:\n')

        print ('   - Leverage: x' + str(lv))
        print ('   - Take Profit: +' + str(tp) + '%')
        print ('   - Stop Loss:   -' + str(sl) + '%')

        print ('\n [+] Take Profit at:', target_price_sum_tp)
        print (' [+] Stop Loss at:  ', target_price_sum_sl)

        print (' [+] Risk/Reward Ratio: ', rr)

        input('\n [*] Press any key to continue...')
        os.system('clear')

    # Leverage
    elif option == '3':
        os.system('clear')
        print ('\n    *** Leverage adjustment ***\n')
        print (' [*] Insert new value (Example: 20): ')

        lv = int(input('\n >>> '))

    # Take Profit 
    elif option == '4':
        os.system('clear')
        print ('\n    *** Take Profit adjustment ***\n')
        print (' [*] Insert new value (Example: 9): ')

        tp = float(input('\n >>> '))

    # Stop Loss
    elif option == '5':
        os.system('clear')
        print ('\n    *** Stop Loss adjustment ***\n')
        print (' [*] Insert new value (Example: 3): ')

        sl = float(input('\n >>> '))

    # Decimals
    elif option == '6':
        os.system('clear')
        print ('\n    *** Decimals adjustment ***\n')
        print (' [*] Insert new value (Example: 3): ')

        dc = float(input('\n >>> '))

    # Wrong Option
    else:
        os.system('clear')
        print ('\n[!] Wrong Option! Try Again')
        input('\n   [*] Press any key to continue...')
