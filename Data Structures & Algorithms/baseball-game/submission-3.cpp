class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<string> board;
        for (string op : operations) {
            if (op == "+") {
                string top1 = board.top();
                board.pop();
                string top2 = board.top();
                board.push(top1);

                board.push(to_string(stoi(top1) + stoi(top2)));
            } else if (op == "D") {
                string top = board.top();
                board.push(to_string(stoi(top) * 2));
            } else if (op == "C") {
                board.pop();
            } else {
                board.push(op);
            }
        }

        int res = 0;
        while (!board.empty()) {
            res += stoi(board.top());
            board.pop();
        }
        return res;;
    }
};