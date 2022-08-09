#  Invalid Transactions
# https://leetcode.com/problems/invalid-transactions/
class Solution(object):
    def __init__(self):
        self.invalidTransactionsList = []
    
    def giveTransactionUniqueId(self, transactions):
        transactionsWithId = []
        for i in range(len(transactions)):
            transactionsWithId.append(transactions[i]+","+str(i))
        return transactionsWithId
    
    def amountGreater1000(self, transactions):
        for t in transactions:
            name, time, amount, city, tid = t.split(",")
            if (int(amount) > 1000):
                if (t not in self.invalidTransactionsList):
                    self.invalidTransactionsList.append(t)
    
    def sameNameDifferentCity(self, transactions):
        for i in range(len(transactions)):
            for j in range(i+1, len(transactions)):
                name_i, time_i, amount_i, city_i, id_i = transactions[i].split(",")
                name_j, time_j, amount_j, city_j, id_j = transactions[j].split(",")
                # if not same name then skip
                if(name_i != name_j):
                    continue
                # if same city then also skip
                if (city_i == city_j):
                    continue
                # if time difference is within 60 minutes
                if (abs(int(time_i) - int(time_j)) <= 60):
                    if not (transactions[i] in self.invalidTransactionsList):
                        self.invalidTransactionsList.append(transactions[i])
                    if not (transactions[j] in self.invalidTransactionsList):
                        self.invalidTransactionsList.append(transactions[j])
    
    def removeId(self):
        for i in range(len(self.invalidTransactionsList)):
            name, time, amount, city, tid = self.invalidTransactionsList.pop(0).split(",")
            self.invalidTransactionsList.append(",".join([name, time, amount, city]))
            
                                
    def invalidTransactions(self, transactions):
        transactionsWithId = self.giveTransactionUniqueId(transactions)
        self.amountGreater1000(transactionsWithId)
        self.sameNameDifferentCity(transactionsWithId)
        self.removeId()
        return self.invalidTransactionsList
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        
