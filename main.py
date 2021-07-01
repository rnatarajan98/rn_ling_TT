import unittest
import numpy as np

def highlight(highlightedPhrases, path):
    f = open(path, 'r')
    input = f.read()
    f.close()

    # IMPLEMENT PHRASE HIGHLIGHTING FUNCTION HERE

    output = 'highlighted phrases with context'
    return output

class Tests(unittest.TestCase):
    def test_preamble_docstart(self):  # test method
        testCasePath = 'TestCase1.txt'

        highlightedPhrases = [[4, 1]]

        expectedOutput = "There once was a <b>farmer</b> from Leeds, who swallowed a ..."

        self.assertEqual(highlight(highlightedPhrases, testCasePath), expectedOutput)

    def test_postamble_sentend(self):  # test method
        testCasePath = 'TestCase2.txt'

        highlightedPhrases = [[12, 2]]

        expectedOutput = "... beard, who said, it is <b>just as</b> I feared ."

        self.assertEqual(highlight(highlightedPhrases, testCasePath), expectedOutput)

    def test_nested_tags(self):  # test method
        testCasePath = 'TestCase3.txt'

        highlightedPhrases = [[8, 5], [9, 1]]

        expectedOutput = "... sit amet, consectetur adipiscing elit, <b>sed do eiusmod tempor incididunt</b> ut labore et dolore magna ..."

        self.assertEqual(highlight(highlightedPhrases, testCasePath), expectedOutput)

if __name__ == '__main__':
    unittest.main()
