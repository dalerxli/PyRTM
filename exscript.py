from pyrtm import rtm, utils

"""
print utils.underline("Test 1: a single run of SBdart", strong=True)
sbdart = rtm.SBdart()
myresult = sbdart()
print myresult

print utils.underline("Test 2: single run of SMARTS", strong=True)
smarts = rtm.SMARTS()
smarts_results = smarts()
print smarts_results

print utils.underline("Test 3: ALL THE rtms", strong=True)
every_rtm = rtm.All()
all_results = every_rtm()
print all_results
"""


def donecallback(results):
    print results


print utils.underline("Test 1: a single run of SBdart", strong=True)
sbdart = rtm.SBdart()
sbdart(donecallback)

print utils.underline("Test 2: single run of SMARTS", strong=True)
smarts = rtm.SMARTS()
smarts(donecallback)

print utils.underline("Test 3: ALL THE rtms", strong=True)
every_rtm = rtm.All()
every_rtm(donecallback)








"""
before

precip water (temp(database) and rel humidity(database))
ozone (database)
nitrogen tropospheric [database]
surface pressure [where available]
later -- stratsopheric (smog) [???; not much effect on spectrum -- maybe based on proximity to city]
later -- cloud cover from cloud photos?

iterating on TAERST or DBAER

SMARTS for clear days
SBdart for cloudy days

"""
