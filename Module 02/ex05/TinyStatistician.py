import math

class TinyStatistician():
    def __init__(self):
        pass

    def get_cols(self, mat):
        count = 0
        if isinstance(mat[0], list):
            for num in mat[0]:
                count += 1
        else:
            for num in mat:
                count +=1
        print("TR cols: ", count)
        return count

    def get_rows(self, mat):
        count = 0
        if isinstance(mat[0], list):
            for row in mat:
                count += 1
        else:
            count =1
        print("TR rows: ", count)
        return count
    
    def sum_mat(self, mat):
        result = 0
        for item in mat:
            if isinstance(item, list):
                for num in item:
                    result += num
            else:
                result += item
        return result

    def mean(self, x):
        if x is None or len(x) == 0:
            return None
        sum = self.sum_mat(x)
        total_items = self.get_cols(x) * self.get_rows(x)
        return sum / float(total_items)

    def median(self, x):
        lst = x
        if isinstance(x[0], list):
            lst = [j for row in x for j in row]
        lst.sort()
        if len(lst) % 2 != 0:
            return float(lst[int(len(lst) / 2)])
        return (lst[math.floor(int(len(lst) / 2))] + lst[math.ceil(int(len(lst) / 2))]) / 2.0 # Mean function could be used

    def quartile(self, x):
        lst = x
        if isinstance(x[0], list):
            lst = [j for row in x for j in row]
        lst.sort()
        q1_index = len(lst) / 4.0
        print("TR: ", q1_index)
        print("TR2: ", len(lst) % 2)
        if len(lst) % 2 != 0:
            return [float(lst[math.floor(q1_index)]), float(lst[math.ceil(q1_index * 2)])]
        print("TR: PAR")
        return [(lst[math.floor(q1_index)] + lst[math.ceil(q1_index)]) / 2.0,
                (lst[math.floor(q1_index * 2)] + lst[math.ceil(q1_index * 2)]) / 2.0]


    def var(x):
        pass

    def std(x):
        pass

## TEST
tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
b = [1, 42, 300, 10, 59, 5]
print("A> ", a)
print("Mean: 82.4 - ", tstat.mean(a))
print("Median: 42.0 - ", tstat.median(a))
print("Quartile: [10.0, 59.0] - ", tstat.quartile(a))
#tstat.var(a)
# Expected result: 12279.439999999999
#tstat.std(a)
# Expected result: 110.81263465868862
print("--------------------------------------------")
print("B> ", b)
print("Mean: 69.5 - ", tstat.mean(a))
print("Median: 26.0 - ", tstat.median(a))
print("Quartile: [4.0, 119.25] - ", tstat.quartile(a))