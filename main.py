from helper_function import Automate_function


object = Automate_function()

arr = [1,2,3,4,5,6,7,8,9,10,12]
if object.search_the_number_existance_using_BS(arr,11):
    print("Number is present")
else:
    print("Number is not present")
