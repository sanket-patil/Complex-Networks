import edge
import connectivity

def analyze(command):
    weighted = False
    directed = False
    
    command.remove('analyze')
    if '-w' in command:
        command.remove('-w')
        weighted = True
    if '-d' in command:
        command.remove('-d')
        directed = True
    if len(command) != 1:
        print "Cannot determine input file name."
        return
    
    ip = open(command.pop(), 'r')
    edgelist = ip.read().split("\n")

    g = graph.graph(directed, weighted)    
    g.createGraph(edgelist)
    print connectivity.isGraphConnected(g)
    
    #basic_properties.displayBasicProperties(g)
    
    return
    

print "Welcome to TopAZ."
print "The program prompt is 'topaz>' at which you can type commands."
print "Type 'help' for help regarding the commands. Type 'info' for information about the program. Type 'quit' to end the program."
print "To analyze a graph, type 'analyze <path/of/input/file> [-d] [-w]"
print "Check the 'readme' for input file format."
print "TopAZ assumes unweighted, undirected graphs by default. Use '-d' if the graph is directed, and '-w' if it is weighted."

while True:
    command = raw_input("topaz> ")
    command = command.split()
    if command[0] == 'help':
        print "To analyze a graph, type 'analyze <path/of/input/file> [-d] [-w]"
        print "Check the 'readme' for input file format. TopAZ takes a list of edges with or without weights as input."
        print "TopAZ assumes unweighted, undirected graphs by default. Use '-d' if the graph is directed, and '-w' if it is weighted."
    elif command[0] == 'info':
        print "TopAZ python version was developed by Sanket Patil."
    elif command[0] == 'analyze':
        analyze(command)    
    elif command[0] == 'quit':
        print "Thanks for using TopAZ. Hope it was of some help."
        break
    else:
        print "Invalid command. Please use 'help' for command syntax."
        break
