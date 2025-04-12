def main():
    while True:
        try:
            curr_value = int(input("Enter a number: "))  
            break  
        except ValueError:
            print("That's not a valid number. Please enter a valid integer.")
    
    while curr_value < 100:
        if curr_value * 2 >= 100:
            break  
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == '__main__':
    main()
