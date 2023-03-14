class Evaluator():
    
    def zip_evaluate(coefs: list, words: list):
        if len(words) != len(coefs):
            return -1
        result = 0
        for value in zip(words, coefs):
            result += len(value[0]) * value[1]
        return result

    def enumerate_evaluate(coefs: list, words: list):
        if len(words) != len(coefs):
            return -1
        result = 0
        for index, value in enumerate(words):
            result += len(value) * coefs[index]
        return result

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))

words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))