class Solution:
    def sortSentence(self, s: str) -> str:
        sent_list = s.split()
        for i in range(len(sent_list)):
            for j in range(len(sent_list) - 1):
                if (sent_list[j][-1] > sent_list[j + 1][-1]):
                    sent_list[j], sent_list[j +
                                            1] = sent_list[j + 1], sent_list[j]
        ret_string = ""
        for i in range(len(sent_list)):
            if i != len(sent_list) - 1:
                ret_string = ret_string + sent_list[i][:-1] + " "
            else:
                ret_string = ret_string + sent_list[i][:-1]
        return ret_string
