"""
For Florian
"""
import math

WORD = "ABRACADABRA"
OUTPUT_NAME = "abracadabra"
OUTPUT_EXT = "txt"
# Number of permutations before we go on to the next file
OUTPUT_ROTATE = 1000000

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
    def __init__(self, max_count):
        self.rotation_index = 0
        self.stream = open(self._log_path(1), "w")
        self.max_count = max_count
        self.count = 0
    
    def _log_path(self, index):
        return "{0}.{1}.{2}".format(OUTPUT_NAME, index, OUTPUT_EXT)
    
    def report(self, permutation):
        self.count += 1
        word = "".join(permutation)
        self.stream.write(word)
        self.stream.write(" ")
        rotation = self.count // OUTPUT_ROTATE
        if rotation > self.rotation_index:
            self.stream.close()
            self.rotation_index += 1
            path = self._log_path(self.rotation_index + 1)
            print "Rotating to " + path
            self.stream = open(path, "w")
        if self.count >= self.max_count:
            self.stream.close()
            return False
        return True


def main():
    n = math.factorial(len(WORD))
    print "Total number of permutations: {0}".format(n)
    print "Will write out to {0} in the current directory".format(OUTPUT_NAME + ".*." + OUTPUT_EXT)
    count = raw_input("How many permutations do you want? [all]")
    if not count:
        count = n
    else:
        count = int(count)
    reporter = Reporter(count)
    perm([], list(WORD), reporter)
    print "Done."
        
if __name__ == "__main__":
    main()
