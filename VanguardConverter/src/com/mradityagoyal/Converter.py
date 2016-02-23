'''
Created on Jan 8, 2016

@author: aditygoy
'''


with open('/home/aditygoy/pythonWS/python/history.csv') as f:
    # dictionary.. vanguard export file stick name : stock ticker
    knownInvestments = {"VANG TOT INTL STK IP" : "VTPSX", "VANG INST INDEX PLUS":"VIIIX",
    "VANG TOT INTL STK IS":"VTSNX", "VANG EXT MKT IDX ISP":"VEMPX"}
    # dictionary .. vanguard transaction type : google transaction type
    transactionType = {"CONTRIBUTION": "BUY", "REVENUE CREDIT":"BUY", "DIVIDEND":"BUY",
    "Exchange Out": "SELL", "Exchange In": "BUY", "Change In Market Value" : "BUY"}
    newLines = []
    print("Date, Ticker, Quantity, Price, Action, Name, Transaction Type")
    for line in f:
        line = line.rstrip()
        if(line.startswith('#')):
#             print(line)
            continue
        tokens = line.split(",")
        if(len(tokens)!= 5):
            continue
        if  (tokens[1] in knownInvestments.keys()):
            try:
                amount = float(tokens[3].strip('"'))
                numShares = float(tokens[4].strip('"'))
                if numShares > 0:
                    pricePerShare = amount / numShares;
                if tokens[2] != "Change In Marget Value":
                    newLines.append(tokens[0] + "," + knownInvestments[tokens[1]] + "," + tokens[4][1:-2] + "," + str(pricePerShare) + "," + transactionType[tokens[2]]+ ","+ tokens[1] +","+ tokens[2])
            except :
                print("Oops error " + line)
    for l in newLines:
        print(l)
