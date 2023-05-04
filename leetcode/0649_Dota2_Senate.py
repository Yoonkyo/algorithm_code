class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        r_count = 0
        d_count = 0
        length = len(senate)
        vote = [False]*length

        while r_count < length and d_count < length:
            for i in range(length):
                if vote[i]:
                    continue
                if r_count == length or d_count == length:
                    break
                if senate[i] == 'R':
                    if r_count < d_count:
                        vote[i] = True
                    r_count += 1
                else:
                    if d_count < r_count:
                        vote[i] = True
                    d_count += 1
        if r_count == length:
            return "Radiant"
        else:
            return "Dire"
