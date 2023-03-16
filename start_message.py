class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class StartMessage:
    def __init__(self):
        self.message = f'''{bcolors.OKGREEN}                                       
 _   _  _____ ___________ 
| \ | ||  ___|  ___|  _  \\
|  \| || |__ | |__ | | | |
| . ` ||  __||  __|| | | |
| |\  || |___| |___| |/ / 
\_| \_/\____/\____/|___/   
        {bcolors.ENDC}                        
        '''
    
    def getMessage(self):
        return self.message
        