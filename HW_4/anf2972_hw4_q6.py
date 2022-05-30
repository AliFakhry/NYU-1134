def appearances(s,low,high):
    if low == high:
        return {s[low]: 1}
    else:
        dict = appearances(s,low+1, high)
        if s[low] in dict:
            dict.update({s[low]: dict[s[low]] + 1})
        else:
            dict.update({s[low]: 1})
        return dict