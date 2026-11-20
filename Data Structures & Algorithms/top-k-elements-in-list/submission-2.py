class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        
        for num in nums:
            freq[num]=freq.get(num,0)+1

        dec_freq=dict(sorted(freq.items(),key=lambda item:item[1],reverse=True))

        top_k_list=list(dec_freq.keys())

        top_k=top_k_list[:k]

        return top_k        