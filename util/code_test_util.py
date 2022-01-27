import traceback



class CodeTestUtil:
    def __init__(self) -> None:
        self.solution = None
        self.data_cases = []
        self.pre_processing = self.__pre_processing
        self.multi_args = False
        # self.timeout = 0
    
    def __solution(self, data):
        try:
            if self.multi_args:
                return self.solution(*data)
            else:
                return self.solution(data)
        except Exception:
            print(traceback.format_exc())

    def __pre_processing(self, data_case):
        return data_case

    def __check_solve(self, anwser, correct):
        if type(correct) == list:            
            return (anwser in correct)
        return (anwser == correct)

    # def set_timeout(self, sec):
    #     self.timeout = sec

    def set_multi_args(self, multi):
        self.multi_args = multi

    def add_data_case(self, data, correct):
        self.data_cases.append((data, correct))

    def run(self):
        results = []
        for idx, data_case in enumerate(self.data_cases):
            data = self.pre_processing(data_case[0])
            result = self.__solution(data)
            solve = self.__check_solve(result, data_case[1])
            results.append(solve)
            print(f'[Case {idx + 1}] Answer: {result}, Correct: {data_case[1]}, Solved: {solve}')
        print(f"[Result] Solved: {results.count(True)}, Failed: {results.count(False)}")
