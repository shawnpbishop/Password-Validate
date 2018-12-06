#This program is written by Shawn Bishop.


def get_digits(password):
    count=0
    for i in password:
        if i.isdigit():
            count += 1
    return count

def isValid(password):
    return len(password)>=8 and password.isalnum() and not password.isdigit() and not password.isalpha()

       
    
        
def main():
    password = input("Enter a password: ").strip()
    if isValid(password) and get_digits(password)>=2:
        print("Valid password")
    else:
        print("Invalid password")
    
      
main()
