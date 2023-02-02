class linearQueue:
    def __init__(self):  # constructor
        self.maxSize = 3
        self.items = ["" for i in range(self.maxSize)] # list comprehension
        self.frontPointer = -1  # used to dequeue the front item
        self.rearPointer = -1  # used to enqueue

    def enqueue(self, item):  # enqueue an item
        if self.isEmpty():
            # set the pointers to 0
            self.rearPointer += 1
            self.frontPointer += 1
            # insert the item into the queue
            self.items[self.rearPointer] = item
        elif not self.isFull():
            self.rearPointer += 1
            self.items[self.rearPointer] = item
        else:
            print("Error: Cannot enqueue as the queue is full")

    def dequeue(self):
        if not(self.isEmpty()):
            # replace the item
            self.items[self.frontPointer] = ""
            self.frontPointer +=1
            if self.frontPointer > self.rearPointer:
                self.frontPointer = -1
                self.rearPointer = -1
        else:
            print("Error: There are no items to dequeue")


    def peek(self):
        if not (self.isEmpty()):
            print(self.items[self.frontPointer])
        else:
            print("Error: There are no items to peek")


    def isEmpty(self):
        if self.rearPointer == -1:
            return True
        return False


    def isFull(self):  # identify whether the queue is full
        if self.rearPointer == self.maxSize - 1:
            return True
        return False


q1 = linearQueue()

instructions = """ Choose one of the following: \noption 1 - enqueue\noption 2 - dequeue\noption 3 - peek
        >> """
while True:
    print(f"Queue:{q1.items}")
    print(f"FP:{q1.frontPointer}")
    print(f"RP:{q1.rearPointer}")

    option = input(instructions)
    match option:
        case "1":
            value = input("enter a value>> ")
            q1.enqueue(value)
        case "2":
            q1.dequeue()
        case "3":
            q1.peek()
        case _:
            print("Invalid option. Try again")