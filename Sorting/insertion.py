# Python program for implementation of Insertion Sort

# Function to do insertion sort
class sorting:
    def __init__(self, arr, arr2):
        self.arr = arr
        self.arr2 = arr2
    def insertionSort(self):
        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):

            key = arr[i]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        # Driver code to test above
    def add(self):
        count = 0
        result = 0
        for items in range(len(arr)):
            result = result + arr[count]
            count += 1
        return result

    def recursion(self):
        first = len(arr)/2  #make arr -> first_half
        second = first + 1

        first_half = []
        second_half = []

        first_half.append(arr[:first])
        sorting(first_half).recursion()

    def common(self):

    #Brutal force method, Not good, Can be solved in O(N)

        result = []
        for items in arr2:
            for item in arr:
                if items == item:
                    result.append(items)
                    break
        return len(result) == len(arr2)
    def largest_sum(self):
        #arr = [12, 11, 13, 5, 6, 4, 2, 7]
        initial = 0
        for i in arr:
            count = 1
            for j in range(len(arr)):
                if count != (len(arr)):
                    result = i + arr[count]
                    count += 1
                    if result > initial:
                        initial = result





        return result

    def factorial(self, n):

        if n == 1:
            return 1
        else:
            return n * sorting.factorial(n-1)





if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 4, 2, 7]
    arr2 = [11, 13, 6, 4]
    print sorting(arr, arr2).factorial(2)


