#problem 1
fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
print(len(fruit_list))
fruit_list.append("mango")
print(fruit_list)

#problem 2
num_lst = [10,20,30,40,50]

def access_element(num_lst, index):
    if index >= 0 and index < len(num_lst):
        return num_lst[index]
    else:
        return "Index out of range"

def modify_element(my_list, index, new_value):
    if index >= 0 and index < len(my_list):
        my_list[index] = new_value
        return my_list
    else:
        return "Invalid index"
    
def slice_list(num_lst, start, end):
    return num_lst[start:end]

def main():
    num_lst = [10, 20, 30, 40, 50]
    
    operation = input("What do you want to do? (access / modify / slice): ").lower()

    if operation == "access":
        index = int(input("Enter index to access: "))
        print("Element:", access_element(num_lst, index))

    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print("Updated list:", modify_element(num_lst, index, new_value))

    elif operation == "slice":
        start = int(input("Start index: "))
        end = int(input("End index: "))
        print("Sliced list:", slice_list(num_lst, start, end))

    else:
        print("Invalid operation!")

# Run game
main()
