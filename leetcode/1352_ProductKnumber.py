class ProductOfNumbers:
    def __init__(self):
        self.numbers = [1]

    def add(self, num: int) -> None:
        numbers = self.numbers
        if num == 0:
            self.numbers = [1]
        else:
            numbers.append(numbers[-1]*num)

    def getProduct(self, k: int) -> int:
        numbers = self.numbers
        if k+1 > len(numbers):
            result = 0
        else:
            result = numbers[-1]//numbers[-1-k]
        return result


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
