class utility:

    @staticmethod
    def reverseString_iterative(string_object):
        string_object = list(string_object)
        l, r = 0, len(string_object) - 1 #have 2 pointers
        while 1 < r: #till they cross each other in the midddle
            string_object[l], string_object[r] = string_object[r], string_object[l] #switch the characters
            l, r = l + 1, r - 1 #the left would increment and the right would decrement
        string_object = ''.join(string_object) #in driver code (leetcode) joins back at the end
        return string_object


    @staticmethod
    def reverseString_recursive(string_object):
        string_object = list(string_object)

        def reverse(l,r): #put in this recursive function which swaps
            if l < r: 
                string_object[l], string_object[r] = string_object[r], string_object[l] #switch the characters
                reverse(l + 1, r - 1) #move on to the next one

        reverse(0, len(string_object) - 1) #positions
        string_object = ''.join(string_object)
        return string_object

  