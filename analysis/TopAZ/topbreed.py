import topbreed.breeder
import graph.graph
import fitness.fitness_functions
import efficiency.efficiency_measures
import sys

def main(argv):
    if len(sys.argv) < 2:
        print "Error: Missing parameters!"
        return
    topbreed.breeder.breed(argv[0], argv[1])

if __name__ == "__main__":
    main(sys.argv[1:])
