#!/usr/bin/python

with open('history.csv') as f:
    # dictionary.. vanguard export file stick name : stock ticker
    knownInvestments = {"VANG TOT INTL STK IP" : "VTPSX",  "VANG INST INDEX PLUS":"VIIIX", 
    "VANG TOT INTL STK IS":"VTSNX", "VANG EXT MKT IDX ISP":"VEMPX"}
    # dictionary .. vanguard transaction type : google transaction type
    transactionType = {"CONTRIBUTION": "BUY",  "REVENUE CREDIT":"BUY",  "DIVIDEND":"BUY",  
    "Exchange Out": "SELL",  "Exchange In": "BUY",  "Change In Market Value" : "BUY"}
    newLines = []
    for line in f:
        tokens=line.split(",")
        if  (tokens[1] not in knownInvestments.keys()):
            try:
                amount = float(tokens[3][1:-1])
                numShares = float(tokens[4][1:-2])
                if numShares > 0:
                    pricePerShare = amount/numShares;
            except :
                print("Oops error "+ line)
            
            if tokens[2] != "Change In Marget Value":
                newLines.append(tokens[0]+","+knownInvestments[tokens[1]] +","+tokens[4][1:-2]+","+str(pricePerShare)+","+transactionType[tokens[2]])
    print("")
    for l in newLines:
        print(l)
    
        
