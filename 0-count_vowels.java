public class VowelCounter {
    public static int vowelCounter(char[] letters){
        int count = 0;

        for(char c : letters) {
            switch (c) {
                case 'a':
                    case 'e':
                    case 'i':
                    case 'o':
                    case 'u':
                        count++;
            break;
            default:
            }
        }

        return count;
    }
    
    public static void main(String args[]){
        System.out.println("enter text...");
        Scanner reader = new Scanner(System.in)

        String input = reader.nextLine();
        char[] letters = input.toCharArray();

        int vowelCount = vowelCounter(letters);

        System.out.println("Number of vowels in string [%s] is %d", input, vowelCount);
    }
}