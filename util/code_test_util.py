import traceback

class CodeTestUtil:
    def __init__(self) -> None:
        self.solution = None
        self.data_cases = []
        self.pre_processing = self.__pre_processing
        self.multi_args = False
    
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

    def set_multi_args(self, multi):
        self.multi_args = multi

    def add_data_case(self, data, correct):
        self.data_cases.append((data, correct))

    def run(self):
        results = []
        for idx, data_case in enumerate(self.data_cases):
            data = self.pre_processing(data_case[0])
            result = self.__solution(data)
            solve = (result == data_case[1])
            results.append(solve)
            print(f'[Case {idx + 1}] Answer: {result}, Correct: {data_case[1]}, Solved: {solve}')
        print(f"[Result] Solved: {results.count(True)}, Failed: {results.count(False)}")
