class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        word_positions = {}
        for word in words:
            word_num = int(word[-1])
            word_positions[word_num] = word[:-1]
        
       
        sorted_words = [word_positions[i+1] for i in range(len(word_positions))]
        
        
        original_sentence = ' '.join(sorted_words)
        
        return original_sentence
