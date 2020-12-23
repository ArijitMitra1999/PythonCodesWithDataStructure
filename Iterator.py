# nums = [3,5,6,7]
#
# print(nums)
#
# for i in nums :
#     print(i)
# #iter convert list into iterator
# it = iter(nums)
# print(next(it))
# # print(it.__next__())

class Topten :
    def __init__(self):
        self.num =  1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10 :
            val = self.num
            self.num += 1
            return val
        #Only way to stop for loop is raise StopIteration
        else :
            raise StopIteration

values = Topten()

for i in values :
    print(i)