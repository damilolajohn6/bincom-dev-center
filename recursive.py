def recursive_search(number, number_list, start_index=0):
    if start_index >= len(number_list):
        return False
    if number_list[start_index] == number:
        return True
    return recursive_search(number, number_list, start_index + 1)
