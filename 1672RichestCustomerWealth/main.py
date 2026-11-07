class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max = 0
        total = 0
        # for i in range(len(accounts)):
        #     sum = 0
        #     for j in range(len(accounts[i])):
        #         sum += accounts[i][j]
        #     if sum > max:
        #         max = sum

        for customer in accounts:
            total = sum(customer)
            if total > max:
                max = total
        return max