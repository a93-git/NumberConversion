# Base of the number - count of digits used un that number system
# Smallest entity of data in computing is a bit - either 0 or 1
# bit = BInary digiT
# Bit to the extreme left is the MSB (Most Significant Bit)
# Bit to the extreme right is the LSB (Least Significant Bit)

class ConvertToBinary:
    def __init__(self, i):
        self.i = i

    def dec2bin(self):
        # Check if number is float or not
        if isinstance(self.i, int):
            return self.int2bin()
        elif isinstance(self.i, float):
            return self.float2bin()
        else:
            raise ValueError("Given value is neither integer nor float")

    def int2bin(self):
        result = []
        j = int(str(self.i).split(".")[0])
        
        while (j != 0):
            _t = j % 2
            result.append(_t)
            j = j // 2
        result.reverse()
        result = [str(i) for i in result]
        return "".join(result)

    def float2bin(self):
        # Convert the integer part to binary
        int_result = self.int2bin()
        # Extract the float part
        float_part = "0.{0}".format(str(self.i).split(".")[1])
        result = []
        count = 0
        while True:
            count = count + 1
            if count > 24:
                break
            float_part = float(float_part) * 2
            if self.check_if_1(str(float_part)):
                result.append(self.first_bit(str(float_part)))
                break
            result.append(self.first_bit(str(float_part)))
            float_part = "0.{0}".format(str(float_part).split(".")[1])
        result = "".join([str(i) for i in result])
        return "{0}.{1}".format(int_result, result)

    def check_if_1(self, i):
        return i == "1.0"

    def first_bit(self, float_part):
        return float_part.split(".")[0]

if __name__ == "__main__":
    number = input("Integer or float to convert to binary:") 
    try:
        if ("." in number):
            number = float(number)
        else:
            number = int(number)
    except Exception as e:
        print("Invalid input")
        exit(0) 

    a = ConvertToBinary(number)
    print(a.dec2bin())