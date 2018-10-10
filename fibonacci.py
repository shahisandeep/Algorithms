Input =[1,3,4,6]
#Output: [24,12,8,6]

def doub(Input):
    output = []
    for items in Input:
        mul = 1
        for it in Input:
            if items == it:
                pass
            else:
                mul = mul * it
        output.append(mul)
    return output










def output(input):
   output = [1] * len(input)
   prod = 1
   for i in range(len(input)):
       output[i] = output[i] * prod
       prod = input[i] * prod

   prod = 1
   for i in range(len(input) - 1, -1, -1):
       output[i] = output[i] * prod
       prod = input[i] * prod
   return output

print output(Input)

