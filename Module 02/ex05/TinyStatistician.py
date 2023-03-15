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
        return count

    def get_rows(self, mat):
        count = 0
        if isinstance(mat[0], list):
            for row in mat:
                count += 1
        else:
            count =1
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
            return float(lst[math.ceil((len(lst) - 1) / 2)])
        return (lst[math.floor((len(lst) - 1) / 2)] + lst[math.ceil((len(lst) - 1) / 2)]) / 2.0 # Mean function could be used

    def quartile(self, x):
        lst = x
        if isinstance(x[0], list):
            lst = [j for row in x for j in row]
        lst.sort()
        q1_index = (len(lst) - 1) / 4.0
        if len(lst) % 2 != 0:
            return [float(lst[math.floor(q1_index)]), float(lst[math.ceil(q1_index * 2)])]
        return [self.mean([lst[math.floor(q1_index)], lst[math.ceil(q1_index)]]),
                self.mean([lst[math.floor(q1_index * 3)], lst[math.ceil(q1_index * 3)]])]

    def var(self, x):
        lst = x
        if isinstance(x[0], list):
            lst = [j for row in x for j in row]
        lst.sort()
        mean = self.mean(lst)
        result = 0
        for value in lst:
            result += math.pow(value - mean, 2)
        return result / len(lst)

    def std(self, x):
        lst = x
        if isinstance(x[0], list):
            lst = [j for row in x for j in row]
        lst.sort()
        mean = self.mean(lst)
        result = 0
        for value in lst:
            result += abs(math.pow(value - mean, 2))
        return math.pow(result / len(lst), (1/2))


## TEST
tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
b = [1, 42, 300, 10, 59, 5, 26, 78]
print("A> ", a)
print("Mean: 82.4 - ", tstat.mean(a))
print("Median: 42.0 - ", tstat.median(a))
print("Quartile: [10.0, 59.0] - ", tstat.quartile(a))
print("Var: 12279.439999999999 - ", tstat.var(a))
print("STD: 110.81263465868862", tstat.std(a))

print("--------------------------------------------")
print("B> ", b)
print("Mean: 65.125 - ", tstat.mean(b))
print("Median: 34.0 - ", tstat.median(b))
print("Quartile: [7.5, 68.5] - ", tstat.quartile(b))