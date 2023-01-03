from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:

        def stripComments(line):
            n = len(line)

            lineCommentIdx = float("inf")
            for i in range(1, n):
                if line[i] == line[i - 1] == '/':
                    lineCommentIdx = i - 1
                    break

            blockCommentIdx = float("inf")
            for i in range(1, n):
                if line[i] == '*' and line[i - 1] == '/':
                    blockCommentIdx = i
                    break

            if lineCommentIdx < blockCommentIdx:
                return line[:lineCommentIdx], False
            if blockCommentIdx < lineCommentIdx and blockCommentIdx < float("inf"):
                after = closeBlockComment(line[blockCommentIdx + 1:])

                return line[:blockCommentIdx - 1] + after[0], after[1]

            return line, False

        def closeBlockComment(line):
            n = len(line)
            blockCommentIdx = float("inf")
            for i in range(1, n):
                if line[i] == '/' and line[i - 1] == '*':
                    blockCommentIdx = i
                    break
            if blockCommentIdx == float("inf"):
                return '', True
            return stripComments(line[blockCommentIdx + 1:])

        N = len(source)
        i = 0
        doFun = stripComments
        acc = []
        while i < N:
            a, b = doFun(source[i])
            acc.append(a)
            if not b:
                ret = ''.join(acc)
                if ret:
                    yield ret
                acc.clear()
            doFun = closeBlockComment if b else stripComments
            i += 1

        pass