def selection_sort(collection):
        """
                Implement selection_sort Algorithm
                Ý tưởng chính: duyệt từ phần tử đầu đến cuối danh sách, duyệt tìm phần tử nhỏ nhất từ vị trí kế phần tử đang duyệt đến hết, sau đó
                        hoán đổi vị trí của phần tử nhỏ nhất với phần tử đang duyệt và cứ tiếp tục như vậy.
                        Cũng sử dụng 2 vòng lặp
        """
        len_collection = len(collection)
        min = 0

        for i in range(len_collection - 1):
                for j in range(i+1, len_collection):
                        if collection[j] < collection[min]:
                                collection[j], collection[min] = collection[min], collection[j]
                        
                min += 1
        
        return collection

if __name__ == '__main__':
        import time

        start = time.process_time()

        user_input = input("Enter numbers separated by comma: \n").strip()

        unsorted = [int(num) for num in user_input.split(',')]

        print(selection_sort(unsorted))

        print(f"Time to process is: ", time.process_time() - start)
                