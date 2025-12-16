class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
                
        maxFrequency = 0

        for frequency in frequencies.values():
            maxFrequency = max(maxFrequency, frequency)

        frequencyOfMaxFrequency = 0
        for frequency in frequencies.values():
            if frequency == maxFrequency:
                 frequencyOfMaxFrequency += 1

        return  frequencyOfMaxFrequency * maxFrequency

