import os
import glob
import sys
import csv

robos = ["Betterment 72-28", "Betterment 90-10", "BrightPlan 60-40", "BrightPlan 90/10", "Fidelity 90-10", "Fidelity Portfolio", "FirstBridge HodgePodge(Jan 1, 2007)", 
        "FutureAdvisors Portfolio", "Int'l Market", "M-1 60-40", "M-1 90-10", "M-1 International SRI", "M-1 SRI", "New Schwab", "S&P 500", "Schwab 90-10", "Schwab Portfolio", 
        "SigFig 60-40", "SigFig 90-10", "SustainFolio P10", "SustainFolio P5", "TIAA 60-40", "TIAA 60-40 Impact Portfolio", "TIAA 90-10", "TIAA 90-10 Impact", 
        "Three-Asset Portfolio (TAP 90-10)", "Three-Asset Portfolio 2(TAP 60-40)", "Vanguard 90-10", "Vanguard Portfolio", "Wealthfront 90-10", "Wealthfront Portfolio"]

# short list of current robos being analyzed
robos_sl = ["Betterment 90-10", "Fidelity 90-10", "Schwab 90-10", "SigFig 90-10", "Vanguard 90-10", "Wealthfront 90-10", "TIAA 90-10", "M-1 90-10", "Three-Asset Portfolio (TAP 90-10)", "Three-Asset Portfolio 2(TAP 60-40)",
            "Betterment 72-28", "Fidelity Portfolio", "FutureAdvisors Portfolio", "Schwab Portfolio", "SigFig 60-40", "Vanguard Portfolio", "Wealthfront Portfolio", "TIAA 60-40", "M-1 60-40", "BrightPlan 60-40"]

def renameCSV():
    i = 0

    allCSVFiles = glob.glob("csvs/" + "*.csv")
    allCSVFiles.sort()

    for filename in allCSVFiles: 
        new_filename = "csvs/" + robos[i] + ".csv"
        # rename() function will rename all the files 
        os.rename(filename, new_filename)
        i += 1
    

    # for filename in directory: 
    #     src = os.path.join('csvs/'+ filename)
    #     new_filename = robos_sl_60_40[i] + ".csv"
    #     dst = os.path.join('csvs/'+ new_filename)

def main():
    print(len(robos))
    renameCSV()

if __name__ == "__main__":
    main()


######################################## Scratch
# open and store the csv file
# IDs = {}
# with open('.csv','rb') as csvfile:
#     timeReader = csv.reader(csvfile, delimiter = ',')
    
#     # build dictionary with associated IDs
#     for row in timeReader:
#         IDs[row[0]] = row[1]
#         os.rename(src, dst)
# path = 'txt_orig'
# tmp_path = 'txt_tmp'

# with open('..csv','rb') as csvfile:
#     reader = csv.reader(csvfile, delimiter = ',')
#     for row in reader:
#        oldname = os.path.join(path, row[0])
#        if os.path.exists(oldname):
#            newname = os.path.join(tmp_path, row[1])
#            os.rename(oldname, newname)
#            print >> os.stderr, "renamed '%s' to '%s'" % (oldname, newname)
#        else:
#            print >> os.stderr, "file '%s' not found" % oldname