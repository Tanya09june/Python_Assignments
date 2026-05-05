def remove_uneven(numbers):
    even_numbers = [n for n in numbers if n % 2 == 0]
    return even_numbers

def main():
   original_list = [3, 8, 1, 12, 5, 20, 7, 4]
   cut_down_list = remove_uneven(original_list)
   print(f"Original list: {original_list}")
   print(f"Cut-down list: {cut_down_list}")

if __name__ == "__main__":
    main()