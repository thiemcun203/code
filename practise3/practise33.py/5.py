def remove_duplicates(your_list):
    return [v for i, v in enumerate(your_list) if i == 0 or v != your_list[i-1]]