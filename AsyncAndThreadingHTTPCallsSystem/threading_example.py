import threading

def compute_square(number):
    print(f'Square of {number}: {number ** 2}')

def main():
    numbers = [2, 4, 6, 8]
    threads = []

    for number in numbers:
        thread = threading.Thread(target=compute_square, args=(number,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

main()
