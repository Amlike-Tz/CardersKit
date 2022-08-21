
#calling python from os do not generally means am a kinda

import requests
import random
import time
import os
import sys

#Colours choosen by amlike


YELLOWBG = '\033[103m'
R = '\033[31m' #Red
Y = '\033[93m' #yellow
G = '\033[92m'  #green
clear = '\033[0m'  #clear
B = '\033[1;34m' #Blue
cyan = '\033[96m' #cyan
cy='\033[095m'  #cy
cya='\033[035m' #cya
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy='\033[095m'
cya='\033[035m'


import subprocess



os.system("rm start.py")
os.system("clear")
print ("Amlike says he is checking for any updates../")

#subprocess.call("wget https://raw.githubusercontent.com/Amlike-Tz/CardersKit/main/start.py")

os.system("wget https://raw.githubusercontent.com/Amlike-Tz/CardersKit/main/start.py")

show = "Amlike-Tz"
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
os.system ("clear")
time.sleep (2)
os.system("python .k.py")
print ("")
print (R+"       ➡ "+cyan+"[01] Live || Dead Card Checker")
print ("")

print (R+"       ➡ "+cyan+"[02] Bin Generator")
print ("")
print (R+"       ➡ "+cyan+"[03] Extrofiation")
print ("")
print (R+"       ➡ "+cyan+"[04] Cards Type Detector")
print ("")
print (R+"       ➡ "+cyan+"[05] Fake Bank Cards Generator")
print ("")
print (R+"       ➡ "+cyan+"[06] Chat with developer")
print ("")
print (R+"       ➡ "+cyan+"[x] Exit Script")
print ("")
time.sleep(1)
for i in range (20):
       Main_com = input(R+"Enter your choice: ")
       if Main_com == "01":
                os.system("clear")
                time.sleep(2)
                os.system("python .k.py")
                print ("")
                print ("")
                print (R+"       ➡ "+cyan+"[01] Single Card Check")
                print ("")
                print (R+"       ➡ "+cyan+"[02] Multicard Cheaker")
                print ("")
                print (R+"       ➡ "+cyan+"[03] Back Home")
                print ("")
                for i in range (1):
                    com=input(R+"SELECT: ")
                    if com=="01":
                            os.system("clear")
                            time.sleep(2)
                            os.system("python .k.py")
                            delay_print ("Example: 4100390189222744|04|23|504|")
                            print ("")
                            print (R)
                            os.system("python3 main_api.py")
                            sys.exit(1)
                    elif com=="02":
                            os.system("clear")
                            time.sleep(2)
                            os.system("python .k.py")
                            print ("")
                            delay_print("Opps!! This feature is not available!")
                            sys.exit(1)
                    elif com=="03":
                            os.system("clear")
                            time.sleep(2)
                            os.system("python start.py")
                    else:
                            os.system("clear")
                            time.sleep(2)
                            os.system("python start.py")

       elif Main_com == "02":
                os.system("clear")
                time.sleep(2)
                os.system("python .k.py")
                print ("")
                print ("")
                print (R+"       ➡ "+cyan+"[01] Master Card Bin")
                print ("")
                print (R+"       ➡ "+cyan+"[02] Vissa Bin")
                print ("")
                print (R+"       ➡ "+cyan+"[03] Amex Bin")
                print ("")
                print (R+"       ➡ "+cyan+"[04] Maestro Bin")
                print ("")
                print (R+"       ➡ "+cyan+"[05] Diners Club | American Express")
                print ("")
                print (R+"       ➡ "+cyan+"[x] Back Home")
                print ("")
                for i in range (5):
                    com=input(R+"SELECT: ")
                    if com=="01":
                            os.system("clear")
                            time.sleep(2)
                            #master card first = [51, 52, 53, 54, 55]
                            numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
                            first = [51, 52, 53, 54, 55]
                            n1 = 4
                            n2 = 1
                            os.system("python .k.py")
                            print (R)
                            print ("")
                            amo = int(input("How many MasterCard Bins you want to create? "))
                            check = type(amo)
                            num = int(amo)
                            os.system("clear")
                            os.system("python .k.py")
                            print (R)
                            save = input("Do you want to save into text file? Y=yes / N=no ")
                            for i in range(num):
                                out1 = (random.sample(first, n2))
                                out = (random.sample(numb, n1))
                                out2 = str(out1) + str(out)
                                final = str(out2)
                                final3 = final.replace(','' ', '')
                                final4 = final3.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = green + "MasterCard Bin ➡ {}"
                                fi = final5
                                final7 = final6.format(fi)
                                print (green)
                                if save == ("Y"):
                                         file = open("MasterCard_Bin.txt", "a")
                                         file.write(final7 + "\n")
       	                                 file.close()
                                         time.sleep(0.5)
       	                                 print ("")
                                         print (final7)
                                else:
                                         time.sleep(0.5)
                                         print ("")
                                         print (final7)
                            print (type(final))
                            delay_print (R + "Done√ By Amlike-Tz")
                            print ("")
                            sys.exit(1)
                    elif com=="02":
                            os.system("clear")
                            os.system("python .k.py")
                            time.sleep(2)
                            numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
                            first = "4"
                            n1 = 5
                            print (R)
                            amo = input("How many Vissa Bins you want to create? ")
                            num = int(amo)
                            os.system("clear")
                            os.system("python .k.py")
                            print (R)
                            save = input("Do you want to save into text file? Y=yes / N=no ")
                            print (green)
                            for i in range(num):
                                out = (random.sample(numb, n1))
                                final = str(out)
                                final2 = str(first) + final
                                final3 = final2.replace(',' ' ', '')
                                final4 = final3.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = green + "Vissa Bin ➡ {}"
                                final7 = final6.format(final5)
                                if save == ("Y"):
                                        file = open("Vissa_Bin.txt", "a")
                                        file.write(final7 + "\n")
                                        file.close()
                                        time.sleep(0.5)
                                        print ("")
                                        print (final7)
                                else:
                                        time.sleep(0.5)
                                        print ("")
                                        print (final7)
                            print (type(final))
                            delay_print (R + "Done√ By Amlike-Tz")
                            sys.exit(1)
                    elif com=="03":
                            os.system("clear")
                            os.system("python .k.py")
                            time.sleep(2)
                            numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
                            first = "37"
                            n1 = 4
                            print (R)
                            amo = input("How many Amex Bins you want to create? ")
                            num = int(amo)
                            os.system("clear")
                            print (R)
                            save = input("Do you want to save into text file? Y=yes / N=no ")
                            print (green)
                            for i in range(num):
                                out = (random.sample(numb, n1))
                                final = str(out)
                                final2 = str(first) + final
                                final3 = final2.replace(',' ' ', '')
                                final4 = final3.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = green + "Amex Bin ➡ {}"
                                final7 = final6.format(final5)
                                if save == ("Y"):
                                        file = open("Amex_Bin.txt", "a")
                                        file.write(final7 + "\n")
                                        file.close()
                                        time.sleep(0.5)
                                        print ("")
                                        print (final7)
                                else:
                                        time.sleep(0.5)
                                        print ("")
                                        print (final7)
                            print (type(final7))
                            delay_print (R + "Done√ By Amlike-Tz")
                            sys.exit(1)
                    elif com=="04":
                            os.system("clear")
                            os.system("python .k.py")
                            time.sleep(2)
                            numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
                            first = "67"
                            n1 = 4
                            print (R)
                            amo = input("How many Maestro Bins you want to create? ")
                            num = int(amo)
                            os.system("clear")
                            print (R)
                            save = input("Do you want to save into text file? Y=yes / N=no ")
                            print (green)
                            for i in range(num):
                                out = (random.sample(numb, n1))
                                final = str(out)
                                final2 = str(first) + final
                                final3 = final2.replace(',' ' ', '')
                                final4 = final3.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = green + "Maestro Bin ➡ {}"
                                final7 = final6.format(final5)
                                if save == ("Y"):
                                        file = open("Maestro_Bin.txt", "a")
                                        file.write(final7 + "\n")
                                        file.close()
                                        time.sleep(0.5)
                                        print ("")
                                        print (final7)
                                else:
                                        time.sleep(0.5)
                                        print ("")
                                        print (final7)
                            print (type(final7))
                            delay_print (R + "Done√ By Amlike-Tz")                    
                            sys.exit(1)
                    elif com=="05":
                            os.system("clear")
                            os.system("python .k.py")
                            time.sleep(2)
                            numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
                            first = "3"
                            n1 = 5
                            print (R)
                            amo = input("How many Diners Club/American Express Bin you want to create? ")
                            num = int(amo)
                            os.system("clear")
                            print (R)
                            save = input("Do you want to save into text file? Y=yes / N=no ")
                            print (green)
                            for i in range(num):
                                out = (random.sample(numb, n1))
                                final = str(out)
                                final2 = str(first) + final
                                final3 = final2.replace(',' ' ', '')
                                final4 = final3.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = green + "Diners Club/American Express ➡ {}"
                                final7 = final6.format(final5)
                                if save == ("Y"):
                                         file = open("Diners_Club_American_Express.txt", "a")
                                         file.write(final7 + "\n")
                                         file.close()
                                         time.sleep(0.5)
                                         print ("")
                                         print (final7)
                                else:
                                        time.sleep(0.5)
                                        print ("")
                                        print (final7)
                            print (type(final))
                            delay_print (R + "Done√ By Amlike-Tz")                    
                            sys.exit(1)
                            print ("")
                    elif com=="x":
                            os.system("clear") 
                            time.sleep(2) 
                            print ("") 
                            print (R) 
                            print ("cd $HOME Your going to the home directory") 
                            os.system("python3 start.py")

                    else:
                            os.system("clear")
                            time.sleep(2)
                            print ("")
                            print (R)
                            delay_print ("Opps! Wrong choosen the script is taking you back to the main menu")
                            os.system("python3 start.py")

       elif Main_com == "03":
                os.system("clear")
                os.system("clear")
                time.sleep(3)
                os.system("figlet Updates")
                time.sleep(2)
                print ("")
                print (yellow+"This feature not yet available on this tool---")
                time.sleep(2)
                sys.exit(1)
                print ("")
                #os.system ("cd && rm -rf TellegramSpammer && git clone https://github.com/Amlike-Tz/TellegramSpammer.git  && cd TellegramSpammer && python3 start.py")
       elif Main_com == "04":
                os.system("clear")
                os.system("python .k.py")
                time.sleep(2)
                visa = "40, 41, 42, 43, 44, 45, 46, 47, 48, 49"
                master_card = "51, 52, 53, 54, 55"
                discover =  "60, 61, 62, 63, 64, 65"
                diners_club = "30, 31, 32, 33, 34, 35, 36, 37, 38, 39"
                Amex = "37"
                Maestro = "67, 68"
                print (R)
                amo = input("Enter card which you want to check: ")
                os.system("clear")
                card = amo[0:2]
                print ("")
                print ("")
                amof = amo.lower()
                for i in range(1):
                        print (green)
                        if card in visa:
                                time.sleep(1)
                                os.system("python .k.py")
                                print ("")
                                print ("")
                                print (green)
                                fe = "CC: {}"
                                print (fe.format(amo))
                                print ("")
                                delay_print ("This CC Is Vissa Card!✓")
                                print ("")
                                #sys.exit(1)
                        elif card in master_card:
                                time.sleep(1)
                                os.system("python .k.py")
                                print ("")
                                print ("")
                                print (green)
                                fe = "CC: {}"
                                print (fe.format(amo))
                                print ("")
                                delay_print ("This CC Is Master Card")
                                print ("")
                               # sys.exit(1)
                        elif card in discover:
                                time.sleep(1)
                                os.system("python .k.py")
                                print ("")
                                print ("")
                                print (green)
                                fe = "CC: {}"
                                print (fe.format(amo))
                                print ("")
                                pdelay_print ("This CC Is Discover Card")
                                print ("")
                              #  sys.exit(1)
                        elif card in diners_club:
                                time.sleep(1)
                                os.system("python .k.py")
                                print ("")
                                print ("")
                                print (green)
                                fe = "CC: {}"
                                print (fe.format(amo))
                                print ("")
                                delay_print("This CC  Can be Diners Club Card or American Express Card!✓")
                                print ("")
                             #   sys.exit(1)
                        elif card in Amex:
                                time.sleep(1)
                                os.system("python .k.py")
                                print ("")
                                print ("")
                                print (green)
                                fe = "CC: {}"
                                print (fe.format(amo))
                                print ("")
                                delay_print ("This CC Is Amex Card!✓")
                                print ("")
                            #    sys.exit(1)
                        elif card in Maestro:
                                time.sleep(1)
                                os.system("python .k.py")
                                print ("")
                                print ("")
                                print (green)
                                fe = "CC: {}"
                                print (fe.format(amo))
                                print ("")
                                delay_print ("This CC  Is Maestro Card!✓")
                                print ("")
                           #     sys.exit(1)
                        else:
                                time.sleep(1)
                                print ("")
                                print (green)
                                fe = "CC: {}"
                                print (fe.format(amo))
                                print ("")
                                delay_print ("Opps! Failed To Detect This Type Of Credit Card/Unknown Type OF Card ✍️")
                                time.sleep(1)
                                print ("")
                                print ("")
                delay_print (R + "Done√ By Amlike-Tz")
                print ("")
                sys.exit(1)
                print ("")

       elif Main_com == "05":
                os.system("clear")
                time.sleep(2)
                os.system("python .k.py")

                visa = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
                master_card = [51, 52, 53, 54, 55]
                discover =  [60, 61, 62, 63, 64, 65]
                diners_club = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
                Amex = [37]
                Maestro = [67, 68]

                numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7]
                first = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
                month = ['01', '02', '03', '04']
                # "05", "06", "07", "08", "09", "10", "11", "12"]
                years = [22, 23, 24, 25, 26]
                cvv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
                date = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]

                n1_cc = 14
                n2_date = 1
                n3_month = 1
                n4_year = 1
                n5_cvv = 3

                print ("")
                print ("")
                print (R+"       ➡ "+cyan+"[01] Fake Bank Visa Card")
                print ("")
                print (R+"       ➡ "+cyan+"[02] Fake Bank Master Card")
                print ("")
                print (R+"       ➡ "+cyan+"[03] Fake Bank Amex Card")
                print ("")
                print (R+"       ➡ "+cyan+"[04] Fake Bank Maestro Card")
                print ("")
                print (R+"       ➡ "+cyan+"[05] Fake Bank Diners Club/American Express Card")
                print ("")
                print (R+"       ➡ "+cyan+"[06] Fake Bank Discover Card")
                print ("")
                print (R+"       ➡ "+cyan+"[x] Back Home")
                print ("")
                for i in range (1):
                    com=input(R+"SELECT: ")
                    if com=="01":
                            os.system("clear")
                            time.sleep(2)
                            os.system("python .k.py")
                            print (R)
                            print ("")
                            amo = int(input("How many Fake Vissa Cards you want to create? "))
                            check = type(amo)
                            num = int(amo)
                            os.system("clear")
                            os.system("python .k.py")
                            print (R)
                            save = input("Do you want to save into text file? Y=yes / N=no ")
                            for i in range(num):

                                cc_card_final = str((random.sample(numb, n1_cc)))
                                date_final = str((random.sample(date, n2_date)))
                                month_final = str((random.sample(month, n3_month)))
                                year_final = str((random.sample(years, n4_year)))
                                cvv_final = str((random.sample(cvv, n5_cvv)))

                                final3 = date_final.replace(',', '')
                                final4 = final3.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = final5.replace('"', '')
                                
                                mwanzo  = str((random.sample(visa, n2_date)))
                                full1 = mwanzo.replace(',', '')
                                full2 = full1.replace('[', '')
                                full3 = full2.replace(']', '')

                                actu = "Visa CC ➡ {}{}|{}|{}|{}|"

                                actual_card = actu.format(full3, cc_card_final, month_final, year_final, cvv_final)
                                actual2 = actual_card.replace(',' ' ', '')
                                final4 = actual2.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = final5.replace('\'', '')

                                print (green)
                                if save == ("Y"):
                                         file = open("VisaCard.txt", "a")
                                         file.write(final6 + "\n")
                                         file.close()
                                         time.sleep(0.5)
                                         print ("")
                                         print (final6)
                                else:
                                         time.sleep(0.5)
                                         print ("")
                                         print (final6)
                            print (type(final4))
                            delay_print (R + "Done√ By Amlike-Tz")
                            print ("")
                            sys.exit(1)
                            print ("")

                    elif com=="02":
                            os.system("clear")
                            time.sleep(2)
                            os.system("python .k.py")
                            print (R)
                            print ("")
                            amo = int(input("How many Fake MasterCards  Cards you want to create? "))
                            check = type(amo)
                            num = int(amo)
                            os.system("clear")
                            os.system("python .k.py")
                            print (R)
                            save = input("Do you want to save into text file? Y=yes / N=no ")
                            for i in range(num):

                                cc_card_final = str((random.sample(numb, n1_cc)))
                                date_final = str((random.sample(date, n2_date)))
                                month_final = str((random.sample(month, n3_month)))
                                year_final = str((random.sample(years, n4_year)))
                                cvv_final = str((random.sample(cvv, n5_cvv)))

                                final3 = date_final.replace(',', '')
                                final4 = final3.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = final5.replace('"', '')

                                mwanzo  = str((random.sample(master_card, n2_date)))
                                full1 = mwanzo.replace(',', '')
                                full2 = full1.replace('[', '')
                                full3 = full2.replace(']', '')

                                actu = "MasterCard  CC ➡ {}{}|{}|{}|{}|"

                                actual_card = actu.format(full3, cc_card_final, month_final, year_final, cvv_final)
                                actual2 = actual_card.replace(',' ' ', '')
                                final4 = actual2.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = final5.replace('\'', '')

                                print (green)
                                if save == ("Y"):
                                         file = open("MasterCards.txt", "a")
                                         file.write(final6 + "\n")
                                         file.close()
                                         time.sleep(0.5)
                                         print ("")
                                         print (final6)
                                else:
                                         time.sleep(0.5)
                                         print ("")
                                         print (final6)
                            print (type(final4))
                            delay_print (R + "Done√ By Amlike-Tz")
                            print ("")
                            sys.exit(1)
                            print ("")
                    elif com=="03":
                            os.system("clear")
                            time.sleep(2)
                            os.system("python .k.py")
                            print (R)
                            print ("")
                            amo = int(input("How many Fake Amex Cards  Cards you want to create? "))
                            check = type(amo)
                            num = int(amo)
                            os.system("clear")
                            os.system("python .k.py")
                            print (R)
                            save = input("Do you want to save into text file? Y=yes / N=no ")
                            for i in range(num):

                                cc_card_final = str((random.sample(numb, n1_cc)))
                                date_final = str((random.sample(date, n2_date)))
                                month_final = str((random.sample(month, n3_month)))
                                year_final = str((random.sample(years, n4_year)))
                                cvv_final = str((random.sample(cvv, n5_cvv)))

                                final3 = date_final.replace(',', '')
                                final4 = final3.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = final5.replace('"', '')

                                mwanzo  = str((random.sample(Amex, n2_date)))
                                full1 = mwanzo.replace(',', '')
                                full2 = full1.replace('[', '')
                                full3 = full2.replace(']', '')

                                actu = "Amex CC ➡ {}{}|{}|{}|{}|"

                                actual_card = actu.format(full3, cc_card_final, month_final, year_final, cvv_final)
                                actual2 = actual_card.replace(',' ' ', '')
                                final4 = actual2.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = final5.replace('\'', '')

                                print (green)
                                if save == ("Y"):
                                         file = open("Amex.txt", "a")
                                         file.write(final6 + "\n")
                                         file.close()
                                         time.sleep(0.5)
                                         print ("")
                                         print (final6)
                                else:
                                         time.sleep(0.5)
                                         print ("")
                                         print (final6)
                            print (type(final4))
                            delay_print (R + "Done√ By Amlike-Tz")
                            print ("")
                            sys.exit(1)
                            print ("")

                    elif com=="04":
                            os.system("clear")
                            os.system("clear")
                            time.sleep(2)
                            os.system("python .k.py")
                            print (R)
                            print ("")
                            amo = int(input("How many Fake Maestro  Cards  Cards you want to create? "))
                            check = type(amo)
                            num = int(amo)
                            os.system("clear")
                            os.system("python .k.py")
                            print (R)
                            save = input("Do you want to save into text file? Y=yes / N=no ")
                            for i in range(num):

                                cc_card_final = str((random.sample(numb, n1_cc)))
                                date_final = str((random.sample(date, n2_date)))
                                month_final = str((random.sample(month, n3_month)))
                                year_final = str((random.sample(years, n4_year)))
                                cvv_final = str((random.sample(cvv, n5_cvv)))

                                final3 = date_final.replace(',', '')
                                final4 = final3.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = final5.replace('"', '')

                                mwanzo  = str((random.sample(Maestro, n2_date)))
                                full1 = mwanzo.replace(',', '')
                                full2 = full1.replace('[', '')
                                full3 = full2.replace(']', '')

                                actu = "Maestro CC ➡ {}{}|{}|{}|{}|"

                                actual_card = actu.format(full3, cc_card_final, month_final, year_final, cvv_final)
                                actual2 = actual_card.replace(',' ' ', '')
                                final4 = actual2.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = final5.replace('\'', '')

                                print (green)
                                if save == ("Y"):
                                         file = open("Maestro.txt", "a")
                                         file.write(final6 + "\n")
                                         file.close()
                                         time.sleep(0.5)
                                         print ("")
                                         print (final6)
                                else:
                                         time.sleep(0.5)
                                         print ("")
                                         print (final6)
                            print (type(final4))
                            delay_print (R + "Done√ By Amlike-Tz")
                            print ("")  
                            sys.exit(1)
                            print ("")

                    elif com=="05":
                            os.system("python .k.py")
                            os.system("clear")
                            os.system("clear")
                            time.sleep(2)
                            os.system("python .k.py")
                            print (R)
                            print ("")
                            amo = int(input("How many Fake Diners club/American Express Cards  Cards you want to create? "))
                            check = type(amo)
                            num = int(amo)
                            os.system("clear")
                            os.system("python .k.py")
                            print (R)
                            save = input("Do you want to save into text file? Y=yes / N=no ")
                            for i in range(num):

                                cc_card_final = str((random.sample(numb, n1_cc)))
                                date_final = str((random.sample(date, n2_date)))
                                month_final = str((random.sample(month, n3_month)))
                                year_final = str((random.sample(years, n4_year)))
                                cvv_final = str((random.sample(cvv, n5_cvv)))

                                final3 = date_final.replace(',', '')
                                final4 = final3.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = final5.replace('"', '')

                                mwanzo  = str((random.sample(diners_club, n2_date)))
                                full1 = mwanzo.replace(',', '')
                                full2 = full1.replace('[', '')
                                full3 = full2.replace(']', '')

                                actu = "Diners club/A-Express CC ➡ {}{}|{}|{}|{}|"

                                actual_card = actu.format(full3, cc_card_final, month_final, year_final, cvv_final)
                                actual2 = actual_card.replace(',' ' ', '')
                                final4 = actual2.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = final5.replace('\'', '')

                                print (green)
                                if save == ("Y"):
                                         file = open("Diners_club_American_Express.txt", "a")
                                         file.write(final6 + "\n")
                                         file.close()
                                         time.sleep(0.5)
                                         print ("")
                                         print (final6)
                                else:
                                         time.sleep(0.5)
                                         print ("")
                                         print (final6)
                            print (type(final4))
                            delay_print (R + "Done√ By Amlike-Tz")
                            print ("")
                            sys.exit(1)
                            print ("")
                    elif com=="06":
                            os.system("clear")
                            os.system("clear")
                            time.sleep(2)
                            os.system("python .k.py")
                            print (R)
                            print ("")
                            amo = int(input("How many Fake Discover Cards  Cards you want to create? "))
                            check = type(amo)
                            num = int(amo)
                            os.system("clear")
                            os.system("python .k.py")
                            print (R)
                            save = input("Do you want to save into text file? Y=yes / N=no ") 
                            for i in range(num):

                                cc_card_final = str((random.sample(numb, n1_cc))) 
                                date_final = str((random.sample(date, n2_date)))
                                month_final = str((random.sample(month, n3_month))) 
                                year_final = str((random.sample(years, n4_year)))
                                cvv_final = str((random.sample(cvv, n5_cvv)))

                                final3 = date_final.replace(',', '')
                                final4 = final3.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = final5.replace('"', '')

                                mwanzo  = str((random.sample(diners_club, n2_date)))
                                full1 = mwanzo.replace(',', '')
                                full2 = full1.replace('[', '')
                                full3 = full2.replace(']', '')

                                actu = "Discover CC ➡ {}{}|{}|{}|{}|"

                                actual_card = actu.format(full3, cc_card_final, month_final, year_final, cvv_final)
                                actual2 = actual_card.replace(',' ' ', '')  
                                final4 = actual2.replace('[', '')
                                final5 = final4.replace(']', '')
                                final6 = final5.replace('\'', '')

                                print (green)
                                if save == ("Y"):
                                         file = open("Discover.txt", "a")
                                         file.write(final6 + "\n")
                                         file.close()
                                         time.sleep(0.5)
                                         print ("")
                                         print (final6)
                                else:
                                         time.sleep(0.5)
                                         print ("")
                                         print (final6)
                            print (type(final4))
                            delay_print (R + "Done√ By Amlike-Tz")
                            print ("")
                            sys.exit(1)
                            print ("")

                    elif com=="x":
                            os.system("clear")
                            time.sleep(2)
                            print ("")
                            print (R)
                            delay_print ("cd $HOME Your going to the home directory")
                            os.system("python3 start.py")

                    else:
                            os.system("clear")
                            time.sleep(2)
                            print ("")
                            print (R)
                            print ("Opps! Wrong choosen the script is taking you back to the main menu")
                            os.system("python3 start.py")
       elif Main_com == "06":
                os.system("clear")
                time.sleep(2)
                print ("")
                print ("")
                print (cyan+"  Pleas Wait Is Loading info...." + cyan+"Now going Asap to chat with me! DONT  Exit in your Termux DUDE ")
                print ("")
                time.sleep(3)
                print ("")
                delay_print (show)
                os.system ("bash .chat.sh")
                os.system ("python3 start.py")

       elif Main_com == "x":
                os.system("clear")
                time.sleep(2)
                print ("")
                print ("")
                print (cyan+"  GOING TO EXIT " + cyan+"BYEEEE  AM  Exit in your Termux DUDE")
                print ("")
                time.sleep(3)
                print ("")
                sys.exit(1)
                print ("")
       else:
                os.system("clear")
                time.sleep(2)
                print ("")
                print ("")
                print (cyan+"  WRONG CHOOSEN " + cyan+ "TOOL IS BACK TO MAIN MENU  DUDE")
                print ("")
                time.sleep(3)
                print ("")
                os.system ("python3 start.py")
