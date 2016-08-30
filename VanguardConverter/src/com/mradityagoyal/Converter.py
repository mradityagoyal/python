'''
Created on Jan 8, 2016

@author: aditygoy
'''


with open('D:\pythonWorkspace\python\history.csv') as f:
    # dictionary.. vanguard export file stick name : stock ticker
    knownInvestments = {"VANG TOT INTL STK IP" : "VTPSX", "VANG INST INDEX PLUS":"VIIIX",
    "VANG TOT INTL STK IS":"VTSNX", "VANG EXT MKT IDX ISP":"VEMPX", "FID GROWTH CO POOL" : "MUTF:FGCP", "VANGUARD TARGET 2050":"MUTF:VT2050", "VANGUARD TARGET 2060":"MUTF:VT2060"}
    # dictionary .. vanguard transaction type : google transaction type
    transactionType = {"CONTRIBUTION": "BUY", "REVENUE CREDIT":"BUY", "DIVIDEND":"BUY",
    "Exchange Out": "SELL", "Exchange In": "BUY", "Change In Market Value" : "BUY"}
    newLines = []
    print("Date, Ticker, NumShares, Price, Amount,  Action, Name, Transaction Type")
    for line in f:
        line = line.rstrip()
        if(line.startswith('#')):
#             print(line)
            continue
        tokens = line.split(",")
        if(len(tokens) == 5):
            try:
                amount = float(tokens[3].strip('"'))
                numShares = float(tokens[4].strip('"'))
                if numShares != 0:
                    pricePerShare = amount / numShares;
                else : pricePerShare = "NaN"
                if tokens[2] != "Change In Market Value":
                    newLines.append(tokens[0] + "," + knownInvestments[tokens[1]] + "," + str(numShares) + "," + str(pricePerShare) + "," + str(amount) + "," + transactionType[tokens[2]] + "," + tokens[1] + "," + tokens[2])
            except :
                print("Oops error " + line)
    for l in newLines:
        print(l)
