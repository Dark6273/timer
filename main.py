# Import required libraries
from os import system,name
from colorama import Fore
from time import sleep
from pyfiglet import Figlet

# figlet variables for print beautiful text
figlet = Figlet(font='big')

# Main menu
def menu():
    system('cls' if name == 'nt' else 'clear')
    print(Fore.RED + """
        ████████╗██╗███╗   ███╗███████╗██████╗ 
        ╚══██╔══╝██║████╗ ████║██╔════╝██╔══██╗
           ██║   ██║██╔████╔██║█████╗  ██████╔╝
           ██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗
           ██║   ██║██║ ╚═╝ ██║███████╗██║  ██║
           ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ 
          """)
    print(Fore.WHITE + "         --------------------------------------")
    sleep(0.05)
    print(Fore.RED + ' [' + Fore.WHITE + '#' + Fore.RED + ']' + Fore.BLUE + " Choose one of the options below\n\n")
    sleep(0.05)
    print(Fore.YELLOW + ' [1] Cooking the timer')
    sleep(0.05)
    print(Fore.RED + ' [0] Exit...' + Fore.RESET)
    
# Select user   
def select(text, title):
    sleep(0.03) # 0.03s sleep
    try:
        # Print input text and turn it into number and return base
        return input(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "TIMER "+ Fore.GREEN + "~ " + Fore.BLUE + title + Fore.GREEN +" <<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "#" + Fore.RED +"] "+ Fore.YELLOW + text + Fore.RESET + " ")
    except:
        # In the event of incoming number
        return -1
    
    
# Print Good Bye :)
def bye():
    print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "TIMER "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "!" + Fore.RED +"] " + Fore.YELLOW + 'We hope you enjoy the app')


# Wrong Input
def wrong():
    print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "TIMER "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.YELLOW + 'The input structure has not been observed !!')

# Count down timer
def count_down(data):
    time = 0
    try:
        data = data.split(":") # Cutting data based on :
        time = int(data[0]) * 3600 + int(data[1]) * 60 + int(data[2]) # Convert time to seconds
    except:
        # Wrong input
        wrong()
        sleep(1)
        exit()
        
    while time > 0: # The loop was greater whit a higher condition of zero
        system('cls' if name == 'nt' else 'clear') # Clear screen
        
        hour = time // 3600 # Find the hours
        min = (time - (hour * 3600)) // 60 # Find the minute
        sec = (time - (hour * 3600) - (min * 60)) # Find the second
        
        text = "{:02d} : {:02d} : {:02d}".format(hour, min, sec) # Build text
        
        if hour == 0 and min == 0 and sec <= 10:
            if sec % 2 == 0:
                print(Fore.RED + figlet.renderText(text))
            else:
                print(Fore.WHITE + figlet.renderText(text))
        else:
            print(Fore.CYAN + figlet.renderText(text))
        
        sleep(1) # Stop a second
        time -= 1
         
    system('cls' if name == 'nt' else 'clear') # Clear screen
    
    print('\a') # Sound creation
    print(Fore.YELLOW + figlet.renderText('FINISH TIMER')) # Print end time
    sleep(2) # Stop two second

    
def main():
    while True:
        menu()
        try:
            status = int(select('', 'HOME'))
        except:
            status = int(select('', 'HOME'))
            
        if status == 0:
            bye()
            sleep(0.1)
            exit()
        elif status == 1:
            count = select('Set the timer as follows (hh:mm:ss | 01:22:10) ', 'SET TIMER')
            count_down(count)

main() # Call base function