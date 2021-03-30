
package com.mycompany.unicafe;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class KassapaateTest {
    
    Maksukortti kortti;
    Kassapaate kassapaate;
    Integer kateisosto;

    @Before
    public void setUp() {
        kassapaate = new Kassapaate();
        kortti = new Maksukortti(1000);
        //kortin saldo 10e
        kateisosto = 1000;
        //käteisen määrä 10e
    }
    
    @Test
    public void rahamaaraAlussaOikein() {
        assertEquals(100000, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void lounaidenMaaraAlussaOikein() {
        assertEquals(0, kassapaate.edullisiaLounaitaMyyty());
        assertEquals(0, kassapaate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void kateisOstoKasvattaaLounaidenMaaraOikein() {
        kassapaate.syoEdullisesti(kateisosto);
        kassapaate.syoMaukkaasti(kateisosto);
        assertEquals(1, kassapaate.edullisiaLounaitaMyyty());
        assertEquals(1, kassapaate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void kateisellaOstettuEdullinenNostaaRahamaaraaOikein() {
        kassapaate.syoEdullisesti(kateisosto);
        assertEquals(100240, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void kateisellaOstettuMaukasNostaaRahamaaraaOikein() {
        kassapaate.syoMaukkaasti(kateisosto);
        assertEquals(100400, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void vaihtorahanSuuruusOikeinKunEdullinenLounas() {
        assertEquals(760, kassapaate.syoEdullisesti(kateisosto));
    }
    
    @Test
    public void vaihtorahanSuuruusOikeinKunMaukasLounas() {
        assertEquals(600, kassapaate.syoMaukkaasti(kateisosto));
    }
    
    @Test
    public void lounaidenMaaraEiMuutuJosMaksuEiRiittäväKateisostossa() {
        kateisosto = 0;
        kassapaate.syoEdullisesti(kateisosto);
        kassapaate.syoMaukkaasti(kateisosto);
        
        assertEquals(0, kassapaate.edullisiaLounaitaMyyty());
        assertEquals(0, kassapaate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void kassanRahamaaraEiMuutuJosMaksuEiRiittäväKateisostossa() {
        kateisosto = 0;
        kassapaate.syoEdullisesti(kateisosto);
        kassapaate.syoMaukkaasti(kateisosto);
        
        assertEquals(100000, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void rahatPalautetaanOikeinJosMaksuEiRiittäväKateisostossaEdullinen() {
        kateisosto = 100;
        assertEquals(100, kassapaate.syoEdullisesti(kateisosto));
    }
    
    @Test
    public void rahatPalautetaanOikeinJosMaksuEiRiittäväKateisostossaMaukas() {
        kateisosto = 100;
        assertEquals(100, kassapaate.syoMaukkaasti(kateisosto));
    }
    
    @Test
    public void korttiostoPalauttaaTrueKunOstaaEdullisen() {
        assertTrue(kassapaate.syoEdullisesti(kortti));
    }
    
    @Test
    public void korttiostoPalauttaaTrueKunOstaaMaukkaan() {
        assertTrue(kassapaate.syoMaukkaasti(kortti));
    }
    
    @Test
    public void korttiostoPalauttaaFalseKunEiTarpeeksiRahaa() {
        kassapaate.syoEdullisesti(kortti);
        kassapaate.syoEdullisesti(kortti);
        kassapaate.syoMaukkaasti(kortti);
        //saldo 1e
        
        assertFalse(kassapaate.syoMaukkaasti(kortti));
        assertFalse(kassapaate.syoEdullisesti(kortti));
    }
    
    @Test
    public void korttiOstoKasvattaaLounaidenMaaraOikein() {
        kassapaate.syoEdullisesti(kortti);
        kassapaate.syoMaukkaasti(kortti);
        
        assertEquals(1, kassapaate.edullisiaLounaitaMyyty());
        assertEquals(1, kassapaate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void kassanRahamaaraEiMuutuKortillaOstettaessa() {
        kassapaate.syoEdullisesti(kortti);
        kassapaate.syoMaukkaasti(kortti);
        
        assertEquals(100000, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void kortinSaldoEiMuutuKunEiTarpeeksiRahaa() {
        kassapaate.syoMaukkaasti(kortti);
        kassapaate.syoMaukkaasti(kortti);
        //Saldo 2e
        kassapaate.syoMaukkaasti(kortti);
        assertEquals(200, kortti.saldo());
    }
    
    @Test
    public void lounaidenMaaraEiMuutuJosMaksuEiRiittäväKorttiostossa() {
        kassapaate.syoEdullisesti(kortti);
        kassapaate.syoEdullisesti(kortti);
        kassapaate.syoMaukkaasti(kortti);
        //saldo 1e
        kassapaate.syoMaukkaasti(kortti);
        assertEquals(2, kassapaate.edullisiaLounaitaMyyty());
        assertEquals(1, kassapaate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void kortinSaldoMuuttuuOikeinKorttiaLadattaessa() {
        kassapaate.lataaRahaaKortille(kortti, 1000);
        assertEquals(2000, kortti.saldo());
    }
    
    @Test
    public void kassanRahamaaraMuuttuuOikeinKorttiaLadattaessa() {
        kassapaate.lataaRahaaKortille(kortti, 1000);
        assertEquals(101000, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void kortilleEiVoiLadataNegatiivistaArvoa() {
        kassapaate.lataaRahaaKortille(kortti, -1000);
        assertEquals(1000, kortti.saldo());
    }
    
    
}
