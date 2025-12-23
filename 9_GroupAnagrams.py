from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    
    for word in words:
        # Sort word to use as a key: "eat" becomes "aet"
        sorted_key = "".join(sorted(word))
        groups[sorted_key].append(word)
        
    return list(groups.values())

# Test
input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"Grouped Words: {group_anagrams(input_words)}")
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]