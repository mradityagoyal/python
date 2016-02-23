'''
Created on Jan 8, 2016

@author: aditygoy
'''


with open('/home/aditygoy/pythonWS/history.csv') as f:
    # dictionary.. vanguard export file stick name : stock ticker
    knownInvestments = {"VANG TOT INTL STK IP" : "VTPSX", "VANG INST INDEX PLUS":"VIIIX",
    "VANG TOT INTL STK IS":"VTSNX", "VANG EXT MKT IDX ISP":"VEMPX"}
    # dictionary .. vanguard transaction type : google transaction type
    transactionType = {"CONTRIBUTION": "BUY", "REVENUE CREDIT":"BUY", "DIVIDEND":"BUY",
    "Exchange Out": "SELL", "Exchange In": "BUY", "Change In Market Value" : "BUY"}
    newLines = []
    for line in f:
        if(line.startswith('#')):
            print(line)
            continue
        tokens = line.split(",")
        if  (tokens[1] in knownInvestments.keys()):
            try:
                amount = float(tokens[3][1:-1])
                numShares = float(tokens[4][1:-3])
                if numShares > 0:
                    pricePerShare = amount / numShares;
                if tokens[2] != "Change In Marget Value":
                    newLines.append(tokens[0] + "," + knownInvestments[tokens[1]] + "," + tokens[4][1:-2] + "," + str(pricePerShare) + "," + transactionType[tokens[2]])
            except :
                print("Oops error " + line)
         
    print("")
    for l in newLines:
        print(l)
