DefaultEnvironment(tools=[])
env = Environment(tools=[])

exp=GetOption('experimental')
print("Experimental=%s"%exp)
print("All=%s"%('all' in exp))