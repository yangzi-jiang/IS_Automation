# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import os

# A list of robo portofolios to be analyzed
robos = ["Betterment 72-28", "Betterment 90-10", "BrightPlan 60-40", "BrightPlan 90/10", "Fidelity 90-10", "Fidelity Portfolio", "FirstBridge HodgePodge(Jan 1, 2007)", 
        "FutureAdvisors Portfolio", "Int'l Market", "M-1 60-40", "M-1 90-10", "M-1 International SRI", "M-1 SRI", "New Schwab", "S&P 500", "Schwab 90-10", "Schwab Portfolio", 
        "SigFig 60-40", "SigFig 90-10", "SustainFolio P10", "SustainFolio P5", "TIAA 60-40", "TIAA 60-40 Impact Portfolio", "TIAA 90-10", "TIAA 90-10 Impact", 
        "Three-Asset Portfolio (TAP 90-10)", "Three-Asset Portfolio 2(TAP 60-40)", "Vanguard 90-10", "Vanguard Portfolio", "Wealthfront 90-10", "Wealthfront Portfolio"]

# short list of current robos being analyzed
robos_sl = ["Betterment 90-10", "Fidelity 90-10", "Schwab 90-10", "SigFig 90-10", "Vanguard 90-10", "Wealthfront 90-10", "TIAA 90-10", "M-1 90-10", "Three-Asset Portfolio (TAP 90-10)", "Three-Asset Portfolio 2(TAP 60-40)",
            "Betterment 72-28", "Fidelity Portfolio", "FutureAdvisors Portfolio", "Schwab Portfolio", "SigFig 60-40", "Vanguard Portfolio", "Wealthfront Portfolio", "TIAA 60-40", "M-1 60-40", "BrightPlan 60-40"]

def csvDownload():
    """ 
    Download the csv files each containing the data of the robo portfolio
    """

    # Use Firefox
    browser = webdriver.Firefox()

    #Go to the portofolio visualizer
    browser.get('https://www.portfoliovisualizer.com/login')

    #Login to finSightful team account
    username = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")
    username.send_keys("treyharris5@gmail.com")
    password.send_keys("mathmodeling2018")
    browser.find_element_by_id("submitButton").click()

    #Click Backtest Portfolio
    #browser.wait(browser, 3)
    backtest = browser.find_element_by_partial_link_text("Backtest Portfolio")
    backtest.click()
    
    # Pick the robo list to run
    for roboAdvisor in robos_sl:
        if(roboAdvisor == "SustainFolio P10" or roboAdvisor == "SustainFolio P5"):
            pass
            # browser.find_element_by_id("timePeriod_chosen").click()
            # browser.implicitly_wait(1)
            # browser.find_element_by_partial_link_text("Month-to-Month").click() # There is a new bug
            # browser.implicitly_wait(1)

        browser.find_element_by_id("allocationOptionsButton1").click()
        roboPortfolio = browser.find_element_by_partial_link_text(roboAdvisor)
        roboPortfolio.click()
        browser.find_element_by_id("submitButton").click()
        browser.find_element_by_link_text("Excel").click()

        if(roboAdvisor == "SustainFolio P10" or roboAdvisor == "SustainFolio P5"):
            pass
            # browser.find_element_by_id("timePeriod_chosen").click()
            # browser.implicitly_wait(1)
            # browser.find_element_by_partial_link_text("Year-to-Year").click()
            # browser.implicitly_wait(1)

    # Logout
    browser.find_element_by_link_text("Davidson").click()
    browser.find_element_by_link_text("Logout").click()

def main():
    print (len(robos))
    print (len(robos_sl))
    csvDownload()

if __name__ == "__main__":
    print("Auto Downloading CSVs from Portfolio Visualizer...")
    main()
    print("Finished Download CSVs")

#################
# useful functions
# executable_path=r'users/yangzijiang/Downloads/geckodriver'
# browser.findElement(By.iD('loginForm'))
# username = browser.findElement(By.ID('loginForm'))
# browser.wait(browser, 3)
# browser.findElement(By.XPATH("href='backtest-portfolio")).click()

#Login Info
#treyharris5@gmail.com
#mathmodeling2018
