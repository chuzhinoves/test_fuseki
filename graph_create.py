class DictionaryGenerator:
    
    NEIB_COUNT = 1000

    def __init__(self):
        self.current_id = 0
        self.dictionary_history = []

    def generate_dictionary(self):
        self.current_id += 1
        new_dict = {'id': self.current_id}
        new_dict['history'] =  self.dictionary_history.copy()
        self.dictionary_history.append(self.current_id)
        if len(self.dictionary_history) > self.NEIB_COUNT:
            self.dictionary_history = self.dictionary_history[-self.NEIB_COUNT:]
        return new_dict


