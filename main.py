"""
For Florian
"""
import math
import os

WORD = "ABRACADABRA"
OUTPUT = "abracadabra.txt"


def perm(l, choices, reporter):
    if len(choices) == 1:
        return reporter.report(l + choices)
    for i in xrange(len(choices)):
        l.append(choices[i])
        if not perm(l, choices[0:i] + choices[i+1:], reporter):
            return False
        l.pop(-1)
    return True


class Reporter(object):
    def __init__(self, max_count, stream):
        self.stream = stream
        self.max_count = max_count
        self.count = 0
    
    def report(self, permutation):
        self.count += 1
        word = "".join(permutation)
        self.stream.write(word)
        self.stream.write(" ")
        if self.count >= self.max_count:
            return False
        return True


def main():
    n = math.factorial(len(WORD))
    print "Total number of permutations: {0}".format(n)
    print "Will write out to {0} in the current directory".format(OUTPUT)
    count = raw_input("How many permutations do you want? [all]")
    if not count:
        count = n
    else:
        count = int(count)
    file = open(OUTPUT, "w")
    reporter = Reporter(count, file)
    try:
        perm([], list(WORD), reporter)
        print "Done."
    finally:
        file.close()
        
if __name__ == "__main__":
    main()
