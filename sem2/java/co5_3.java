import java.applet.*;
import java.awt.*;
/*
<applet code="co5_3" width=400 height=400>
</applet>
*/
public class co5_3 extends Applet {
    int[] marks = {65, 30, 16, 60, 40}; 
    int total = 0;
    float percentage = 0;
    public void init() {
        for (int i = 0; i < 5; i++) {
            total += marks[i];
        }
        percentage = (float) total / 5;
    }
    public void paint(Graphics g) {
        g.drawString("Total Marks: " + total, 50, 50);
        g.drawString("Percentage: " + percentage + "%", 50, 70);
        if (percentage > 50) {
            drawHappyFace(g, 150, 100);
            g.drawString("Great! You passed!", 120, 300);
        } else {
            drawSadFace(g,150, 100);
            g.drawString("Sorry, you failed.", 120, 300);
        }
    }
    void drawHappyFace(Graphics g, int x, int y) {
        g.drawOval(x, y, 100, 100); 
        g.fillOval(x + 25, y + 30, 10, 10); 
        g.fillOval(x + 65, y + 30, 10, 10); // Right eye
        g.drawArc(x + 25, y + 40, 50, 30, 0, -180); // Smile
    }
    void drawSadFace(Graphics g, int x, int y) {
        g.drawOval(x, y, 100, 100); // Face outline
        g.fillOval(x + 25, y + 30, 10, 10); // Left eye
        g.fillOval(x + 65, y + 30, 10, 10); // Right eye
        g.drawArc(x + 25, y + 50, 50, 30, 0, 180); // Sad mouth
    }
}


