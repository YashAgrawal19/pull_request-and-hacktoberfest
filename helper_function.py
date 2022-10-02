from collections import defaultdict


class Automate_function:

    def __init__(self):
        pass

    def search_the_number_existance_using_BS(self, arr, number):
        arr = sorted(arr)

        start = 0
        end = len(arr)
        while start<=end:
            mid = (start+end)//2
            if arr[mid]==number:
                return True
            if arr[mid]<number:
                start = mid+1
            else:
                end = mid-1

        return False




