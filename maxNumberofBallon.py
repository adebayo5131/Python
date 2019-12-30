'''
    Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

    You can use each character in text at most once. Return the maximum number of instances that can be formed.
'''

def maxNumberOfBalloons(text):
    """
    :type text: str
    :rtype: int
    """
    if text == " " or len(text) < 7:
        return 0

    string = "balloon"
    memo = {}
    for i in string:
        if i not in memo:
            memo[i] = 0

    for i in text:
        if i in string:
            if i in memo:
                memo[i] += 1

    return min(memo['l'] // 2, memo['o'] // 2)


print(maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopj"))
