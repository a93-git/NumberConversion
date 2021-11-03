# Binary to Decimal converter
# Process:
# 1. Split on .
# 2. Multiply each bit in the first part (integral part) to a power of 2
#       starting from 2^0 for leftmost bit
# 3. Multiply each bit in the second part (fractional part) to a negative power of 2
#       starting from 2^-1 for rightmost bit
# 4. Add the two numbers


class ConvertToDecimal:
    def __init__(self, i):
        self.i = i

    def bin2decimal(self):
        integer_part = str(self.i).split(".")[0]
        decimal_part = str(self.i).split(".")[1]

        return self._bin2int(integer_part) + self._decimal2int(decimal_part)
        
    def _bin2int(self, i):
        exp = 0
        retval = 0
        for j in i[::-1]:
            retval += int(j) * (2 ** exp)
            exp += 1
        
        return retval

    def _decimal2int(self, i):
        exp = -1
        retval = 0
        for j in i:
            retval += int(j) * (2 ** exp)
            exp -= 1

        return retval


if __name__ == "__main__":
    n = input("Binary to decimal: ")
    print(ConvertToDecimal(n).bin2decimal())
