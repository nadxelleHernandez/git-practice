def most_common_value(number_list):
    """ returns the most common element of the list
    """
    num_dict = dict()

    for num in number_list:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    
    max = 0
    result = 0
    for num in num_dict:
        if max < num_dict[num]:
            max = num_dict[num]
            result = num
    return result

if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")
