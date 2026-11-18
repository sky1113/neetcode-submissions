class Solution {
public:
    bool isValid(string s) {
        stack<char> pars;
        char top;
        for (char ch : s) {
            switch(ch) {
                case '[':
                case '{':
                case '(':
                    pars.push(ch);
                    break;
                case ']':
                    if (!pars.empty()) {
                        top = pars.top();
                        if (top != '[') {return false;}
                        pars.pop();
                    } else {return false;}
                    break;
                case '}':
                    if (!pars.empty()) {
                        top = pars.top();
                        if (top != '{') {return false;}
                        pars.pop();
                    } else {return false;}
                    break;
                case ')':
                    if (!pars.empty()) {
                        top = pars.top();
                        if (top != '(') {return false;}
                        pars.pop();
                    } else {return false;}
                    break;
            }
        }

        if (pars.empty()) {
            return true;
        } else {return false;}
    }
};
