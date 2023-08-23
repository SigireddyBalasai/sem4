import java.util.*;

class prelab
{
    public static void main(String args[])
    {
        Stack<Character> stack = new Stack<Character>();
        Scanner input = new Scanner(System.in);
        System.out.println("Please enter the no of commands");
        int number_of_commands = input.nextInt();
        for(int i=0;i < number_of_commands;i++)
        {
            String line = input.next();
            if(line.charAt(0) == '1')
            {
                stack.push(line.charAt(1));
            }
            else if(line.charAt(0) == '2')
            {
                System.out.println("The elemnent that is popped is "+stack.pop());
                
            }
            else if(line.charAt(0) == '3')
            {
                System.out.println("The largest element is "+max_element(stack));
            }
        }
        input.close();
        
    }
    static char max_element(Stack<Character> stack_g)
    {
        char max_number = 0;
        char ok = 0;
        Stack<Character> stack = (Stack<Character>) stack_g.clone();
        try
        {
            ok = stack.pop();
            while(ok != 0)
            {
                if(ok > max_number)
                {
                    max_number = ok;
                }
                ok = stack.pop();
            }
        }
        catch(Exception e)
        {
            return ok;
        }
        return ok;
    }

}