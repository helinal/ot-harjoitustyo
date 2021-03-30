package com.mycompany.unicafe;

public class Paaohjelma {

    public static void main(String[] args) {
        Kassapaate unicafeExactum = new Kassapaate();
        Maksukortti kortti = new Maksukortti(1000);

        int maksu = 1000;
        System.out.println(unicafeExactum.syoEdullisesti(maksu));
        
        System.out.println(kortti);
    }
}
