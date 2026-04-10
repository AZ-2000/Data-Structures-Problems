class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []
        eq_word = []
        
        
        for word in strs:
            if word in hashmap:
                eq_word.append(word)
            else:
                hashmap[word] = "placeholder"
        for word in strs:
            word_dict = {}
            for c in word:
                if c in word_dict:
                    word_dict[c] += 1
                else:
                    word_dict[c] = 1
            hashmap[word] = word_dict
            
                
        
        keys = list(hashmap.keys())
        complement = {}
        
        for key in keys:
            count = 0
            for k in hashmap:
                if hashmap[key] == hashmap[k] and k not in complement and key!=k:
                    count += 1
                    complement[key] = k
                    res.append([key,k])
                if key in complement.values():
                    count += 1
            if count == 0:
                res.append([key])
                
        merged_res = []
        
        for sublist in res:
            current_set = set(sublist)
            merged = False
            for i, existing_set in enumerate(merged_res):
                if not current_set.isdisjoint(existing_set):
                    merged_res[i] = existing_set.union(current_set)
                    merged = True
                    break 
            if not merged:
                merged_res.append(current_set)
            
        converted_list = [list(s) for s in merged_res]
        for i, sublist in enumerate(converted_list):
            for word in eq_word:
                if word in sublist:
                    sublist.append(word)
        return converted_list