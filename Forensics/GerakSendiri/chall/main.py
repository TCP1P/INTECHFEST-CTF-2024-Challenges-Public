import time

def verify(index ,question, answer):
    while True:
        result = input(f'\n[{index}/6] {question} : ')
        print("Your input : ", result)
        if result != f'{answer}':
            print("Wrong answer😵‍💫, please try again!")
            time.sleep(3)
        else:
            print("Congratulation, you are right!")
            time.sleep(1)
            break

def header():
    head = r"""
  ______                  _                             _ _       _ 
 / _____)                | |                           | (_)     (_)
| /  ___  ____  ____ ____| |  _     ___  ____ ____   _ | |_  ____ _ 
| | (___)/ _  )/ ___) _  | | / )   /___)/ _  )  _ \ / || | |/ ___) |
| \____/( (/ /| |  ( ( | | |< (   |___ ( (/ /| | | ( (_| | | |   | |
 \_____/ \____)_|   \_||_|_| \_)  (___/ \____)_| |_|\____|_|_|   |_|
                                                                                                                  
                                                                                                      
=======================================================================================================
=======================================================================================================
    """
    print(head)

def announcement():
    print("You will need to answer all of the questions to get the flag!")
    input("press enter to continue ...")

def challenge():
    print("""
=======================================================================================================
                                            CHALLENGE
=======================================================================================================    

    I just did an experiment, I challenge you to analyze what is actually happening.
          
    \033[33mNote : All the answers are case sensitive\033[39m

=======================================================================================================
=======================================================================================================""")
    
    verify(1, "What is the device that attacker use to attack victim device? ( answer in lowercase e.g. cpu)", "bluetooth")
    verify(2, "What is the victim bluetooth name? ( answer in lowercase e.g. ujang) ", "asep")
    verify(3, "What is the victim device MAC address ( e.g. 00:11:22:33:44:55 ) ", "10:82:d7:92:50:80")
    verify(4, "What is the first app that attacker use to open victim whatsapp? ( answer in lowercase e.g. twitter ) ", "browser")
    verify(5, "What is the message that attacker send to victim whatsapp?", "l33t1337")
    verify(6, "Attacker trying to open browser again in private mode, there are an attachment that you can see.\nPlease put the value here", "akhirnya aku dapet flag asikkkk")

def flag():
    print("""
=======================================================================================================
                                            FLAG
=======================================================================================================
""")
    while True:
        for i in range(0xf):
            try:
                flag = "INTECHFEST{bluetooth_could_be_dangerous_5dff7d}"
                print(f'\033[32m[{i:x}]  Here is your flag : {flag} [{i:x}]', end='\r')
                time.sleep(0.01)
            except KeyboardInterrupt:
                print('bye')
                exit()
        for i in range(0xf):
            try:
                print(f'[{i:x}]  h3Re 1s y0uR fL4g : {flag} [{i:x}]', end='\r')
                time.sleep(0.01)
            except KeyboardInterrupt:
                print('bye')
                exit()
        for i in range(0xf):
            try:
                print(f'[{i:x}]  hEr3 i5 yOUr Fl4G : {flag} [{i:x}]', end='\r')
                time.sleep(0.01)
            except KeyboardInterrupt:
                print('bye')
                exit()

if __name__ == "__main__":
    import warnings
    warnings.filterwarnings("ignore")
    try:
        header()
        announcement()
        challenge()
        flag()
    except KeyboardInterrupt:
        print("\nbye...")