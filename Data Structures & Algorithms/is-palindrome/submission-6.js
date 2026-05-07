class Solution {
    isPalindrome(s) {
        let f = 0
        let b = s.length -1

        const isAlphanum = (s) =>/^[a-z0-9]+$/i.test(s);
        while (f < b)
        {
            while (f < b && !isAlphanum(s[f]))
            {
                f+=1; 
            }
            while (f < b && !isAlphanum(s[b]))
            {
                b-=1; 
            }
            if(s[f].toLowerCase() != s[b].toLowerCase())
            {
                return false 
            }
            f+=1
            b-=1
        }
        return true 
    }
    
}
