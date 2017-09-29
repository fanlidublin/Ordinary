package cc;

public class Cc {
    public int LastRem(int n, int m, int i) {
        if (i == 1)
            return (n + m - 1) % n;
        else
            return (LastRem(n - 1, m, i - 1) + m) % n;
    }

    public static void main(String[] args) {
        Cc c = new Cc();
        for (int i = 1; i <= 100; i++)
            System.out.println(c.LastRem(100, 7, i) + 1);
    }
}
