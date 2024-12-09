public class Participant {
    private static int counter;
    private String registrationId;
    private String name;
    private long contactNumber;
    private String branch;
    
    static {
        counter = 1000;
    }
    
    public Participant(String name, long contactNumber, String branch) {
        this.name = name;
        this.contactNumber = contactNumber;
        this.branch = branch;
        counter++;
        registrationId = "D" + counter;
    }
    
    public String getRegistrationId() {
        return registrationId;
    }
        
    public String getName() {
        return name;
    }

     public long getContactNumber() {
        return contactNumber;
    }

    public String getBranch() {
        return branch;
    }
    
    public static void main(String[] args) {
        Participant P1 = new Participant("Rohit",1234567889, "Computer");
        Participant P2 = new Participant("Sayli", 1988612300, "Mechanical");
        System.out.println("Hi " + P1.getName() + "! Your registration id is " + P1.getRegistrationId() + " and branch is " + P1.getBranch());
        System.out.println("Hi " + P2.getName() + "! Your registration id is " + P2.getRegistrationId() + " and branch is " + P2.getBranch());
    }
}