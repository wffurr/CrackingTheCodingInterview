public class DecimalToBinary {
    /** Given a decimal number as a string, returns the binary representation as a string or "ERROR" if it can't be converted to binary */
    public static String decimalToBinary(String decimal) {
        int dec = 0;
        try {
            dec = Integer.parseInt(decimal);
        } catch(NumberFormatException ex) {
            return "ERROR";
        }
        if(dec == 0) return "0";
        StringBuilder result = new StringBuilder();
        while(dec != 0) {
            result.insert(0, (dec & 1) == 1 ? "1" : "0");
            dec >>= 1;
        }
        return result.toString();
    }

    public static void runTest(String decimal, String binary) {
        String result = decimalToBinary(decimal);
        if(!binary.equals(result)) {
            System.out.println("For " + decimal + " expected " + binary + " got " + result);
        }
    }

    public static void main(String[] args) {
        runTest("0", "0");
        runTest("1", "1");
        runTest("2", "10");
        runTest("33", "100001");
        runTest("1.1", "ERROR");
        runTest("3000000000000", "ERROR");
    }
}
