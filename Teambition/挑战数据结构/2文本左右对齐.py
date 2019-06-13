class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        tmp = []
        lst = maxWidth
        wdl = 0
        wdn = 0
        res = []
        while words:
            a = words.pop(0)
            if lst>=len(a):
                if not words:
                    tmp += [a]
                    temp=' '.join(tmp)
                    lem = len(temp)
                    for i in range(maxWidth-lem):
                        temp+=' '
                    res.append(temp)
                    return res
                tmp.append(a)
                wdl += len(a)
                wdn += 1
                lst = maxWidth-wdl-wdn
                print tmp
            else:
                words =[a]+words
                snu = maxWidth - wdl
                if wdn ==1:
                    n = 0
                    v = snu
                else:
                    n = snu%(wdn-1)
                    v = snu/(wdn-1)
                temp = ''
                for i in range(wdn):
                    if i ==0:
                        temp=tmp[i]+' '*v
                        if n!=0:
                            temp+=' '
                            n-=1
                    if i==wdn-1:
                        if i!=0:
                            temp+=tmp[i]
                        res.append(temp)
                        tmp = []
                        lst = maxWidth
                        wdl = 0
                        wdn = 0
                    elif i!=0 and i!=wdn-1:
                        temp+=tmp[i]+' '*v
                        if n!=0:
                            temp+=' '
                            n-=1
