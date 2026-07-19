class Reporter:

    def report(self, result):

        print(result.severity.value, result.message)
