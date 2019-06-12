import os
import glob
import sys
import csv

robos = ["Betterment 72-28", "Betterment 90-10", "BrightPlan 60-40", "BrightPlan 90/10", "Fidelity 90-10", "Fidelity Portfolio", "FirstBridge HodgePodge(Jan 1, 2007)", 
        "FutureAdvisors Portfolio", "Int'l Market", "M-1 60-40", "M-1 90-10", "M-1 International SRI", "M-1 SRI", "New Schwab", "S&P 500", "Schwab 90-10", "Schwab Portfolio", 
        "SigFig 60-40", "SigFig 90-10", "SustainFolio P10", "SustainFolio P5", "TIAA 60-40", "TIAA 60-40 Impact Portfolio", "TIAA 90-10", "TIAA 90-10 Impact", 
        "TAP 90-10", "TAP 60-40", "Vanguard 90-10", "Vanguard Portfolio", "Wealthfront 90-10", "Wealthfront Portfolio"]

# short list of current robos being analyzed
robos_sl = ["Betterment 90-10", "Fidelity 90-10", "Schwab 90-10", "SigFig 90-10", "Vanguard 90-10", "Wealthfront 90-10", "TIAA 90-10", "M-1 90-10", "TAP 90-10", "TAP 60-40",
            "Betterment 72-28", "Fidelity Portfolio", "FutureAdvisors Portfolio", "Schwab Portfolio", "SigFig 60-40", "Vanguard Portfolio", "Wealthfront Portfolio", "TIAA 60-40", "M-1 60-40", "BrightPlan 60-40"]

robos_90_10 = ["Betterment 90-10", "Fidelity 90-10", "Schwab 90-10", "SigFig 90-10", "Vanguard 90-10", "Wealthfront 90-10", "TIAA 90-10", "M-1 90-10", "TAP 90-10"]

def renameCSV():
    i = 0

    allCSVFiles = glob.glob("csvs/" + "*.csv")
    allCSVFiles.sort()

    for filename in allCSVFiles: 
        # new_filename = "csvs/" + robos_sl[i] + ".csv"
        new_filename = "csvs/" + robos_90_10[i] + ".csv"

        # rename() function will rename all the files 
        os.rename(filename, new_filename)
        i += 1
    

    # for filename in directory: 
    #     src = os.path.join('csvs/'+ filename)
    #     new_filename = robos_sl_60_40[i] + ".csv"
    #     dst = os.path.join('csvs/'+ new_filename)

def main():
    print(len(robos_sl))
    renameCSV()
    print (len([name for name in os.listdir("csvs/") if os.path.isfile(name)]))


if __name__ == "__main__":
    main()
