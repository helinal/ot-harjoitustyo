package com.mycompany.unicafe;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class MaksukorttiTest {

    Maksukortti kortti;
    Kassapaate unicafeExactum = new Kassapaate();

    @Before
    public void setUp() {
        kortti = new Maksukortti(1000);
        //saldo 10e
    }

    @Test
    public void luotuKorttiOlemassa() {
        assertTrue(kortti!=null);      
    }
    
    @Test
    public void kortinSaldoOnAlussaOikein() {
        assertEquals("saldo: 10.0", kortti.toString());   
    }

    @Test
    public void kortilleLataaminenKasvattaaSaldoaOikein() {
        kortti.lataaRahaa(1000);
        assertEquals("saldo: 20.0", kortti.toString());   
    }
    
    @Test
    public void syoEdullisestiVahentaaSaldoaOikein() {
        unicafeExactum.syoEdullisesti(kortti);
        assertEquals("saldo: 7.60", kortti.toString());
    }
    
    @Test
    public void syoMaukkaastiVahentaaSaldoaOikein() {
        unicafeExactum.syoMaukkaasti(kortti);
        assertEquals("saldo: 6.0", kortti.toString());
    }
    
    @Test
    public void josEiTarpeeksiRahaaSaldoEiMuutu() {
        unicafeExactum.syoMaukkaasti(kortti);
        unicafeExactum.syoMaukkaasti(kortti);
        //saldo 2e
        unicafeExactum.syoMaukkaasti(kortti);
        assertEquals("saldo: 2.0", kortti.toString());
    }
    
    @Test
    public void josRahatRiittävätPalauttaaTrue() {
        assertTrue(unicafeExactum.syoMaukkaasti(kortti));
    }
    
    @Test
    public void josRahatEivätRiitäPalauttaaFalse() {
        unicafeExactum.syoMaukkaasti(kortti);
        unicafeExactum.syoMaukkaasti(kortti);
        //saldo 2e
        assertFalse(unicafeExactum.syoMaukkaasti(kortti));
    }
    
    @Test
    public void josSaldoEiRiitäRahaaOttaessaPalautaFalse() {
        kortti.otaRahaa(1000);
        //Saldo 0e
        assertFalse(kortti.otaRahaa(1000));
    }
}
