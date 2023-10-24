def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Determine the range of input values
    min_val, max_val = min(arr), max(arr)
    
    # Create empty buckets
    num_buckets = max_val - min_val + 1
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute elements into buckets
    for num in arr:
        index = num - min_val
        buckets[index].append(num)
    
    # Sort each bucket (using insertion sort in this example)
    for i in range(num_buckets):
        insertion_sort(buckets[i])
    
    # Concatenate the sorted buckets to get the final sorted array
    sorted_arr = [num for bucket in buckets for num in bucket]
    
    return sorted_arr

def main():
    # Input a list of numbers
    try:
        input_str = input("Enter a list of numbers separated by spaces: ")
        unsorted_list = [int(num) for num in input_str.split()]
    except ValueError:
        print("Invalid input. Please enter a list of numbers.")
        return

    # Call the bucket_sort function to sort the list
    sorted_list = bucket_sort(unsorted_list)

    # Display the sorted list
    print("Sorted List:", sorted_list)

if __name__ == "__main__":
    main()
