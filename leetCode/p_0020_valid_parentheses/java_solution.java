class Solution {
    public boolean isValid(String s) {
        Stack stack = new Stack();
        ArrayList<Character> charsClose = new ArrayList<Character>();
        charsClose.add(')');
        charsClose.add(']');
        charsClose.add('}');
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(charsClose.contains(c)){
                StringBuilder sc = new StringBuilder();
                if(!stack.empty()){
                    sc.append(stack.peek());
                    sc.append(c);
                    System.out.println(sc.toString());
                    if(sc.toString().equals("()") || sc.toString().equals("[]") || sc.toString().equals("{}")){
                        stack.pop();
                        continue;
                    }
                }
                return false;             
            }
            stack.push(c);
        }
        return stack.empty();
    }
}

// Another Solution
class Solution {
    public boolean isValid(String s) {
        Stack stack = new Stack();
        ArrayList<Character> charsClose = new ArrayList<Character>();
        charsClose.add(')');
        charsClose.add(']');
        charsClose.add('}');
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(charsClose.contains(c)){
                if(!stack.empty()){
                    String sc = ""+ stack.peek()+c;
                    System.out.println(sc.toString());
                    if(sc.toString().equals("()") || sc.toString().equals("[]") || sc.toString().equals("{}")){
                        stack.pop();
                        continue;
                    }
                }
                return false;             
            }
            stack.push(c);
        }
        return stack.empty();
    }
}