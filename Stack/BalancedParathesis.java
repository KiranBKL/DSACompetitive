import java.util.*;
class BalancedParanthesis
{
    public static void main(String args[])
    {
        Scanner scan=new Scanner(System.in);
        String str=scan.nextLine();
        Stack<Character> stack= new Stack<Character>();
        //char[] ch={'(','[','{'};
        Set<Character> l= new HashSet<Character>(Arrays.asList('(','[','{'));
        
       //l.add('a');
        //System.out.println(l.contains('a'));
        int n=str.length();
        for(int i=0;i<n;i++)
        {
            if(l.contains(str.charAt(i)))
            {
                stack.push(str.charAt(i));
            }
            else
            {
                System.out.println(str.charAt(i) +" "+stack.peek()+" "+check(stack.peek(),str.charAt(i)));
                if(!check(stack.peek(),str.charAt(i)))
                {
                    System.out.println("Not Blanacedd");
                    break;
                   
                }
                else
                {
                     stack.pop();
                }
            }
        }
        if(stack.empty())
        System.out.println("Blanced");
        else
        System.out.println("Not Balanced");
    }
    private static boolean check(char a,char b)
    {
        return((a=='('&& b==')') || (a=='[' && b==']') || (a=='{' && b=='}'));
    }
}