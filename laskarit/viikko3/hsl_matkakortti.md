## HSL-matkakortin sekvenssikaavio

```mermaid
sequenceDiagram
  participant main
  participant laitehallinto
  participant rautaietori
  participant ratikka6
  participant bussi244
  participant lippu_luukku
  participant uusi_kortti
  participant kallen_kortti

  main->>laitehallinto: HKLLaitehallinto()
  main->>rautatietori: Lataajalaite()
  main->>ratikka6: Lukijalaite()
  main->>bussi244: Lukijalaite()
  main->>laitehallinto: lisaa_lataaja(rautatientori)
  main->>laitehallinto: lisaa_lukija(ratikka6)
  main->>laitehallinto: lisaa_lukija(bussi244)
  main->>lippu_luukku: Kioski()
  main->>lippu_luukku: osta_markakortti("Kalle")

  lippu_luukku->>uusi_kortti: Matkakortti("kalle")
  lippu_luukku-->>kallen_kortti: uusi_kortti

  main->>rautatietori: lataa_arvoa(kallen_kortti, 3)
  main->>ratikka6: osta_lippu(kallen_kortti, 0)

  ratikka6->>kallen_kortti: arvo
  kallen_kortti-->>ratikka6: 3
  ratikka6->>kallen_kortti: vahenna_arvoa(hinta)
  ratikka6-->>main: True

  main->>bussi244: osta_lippu(kalle_kortti,2)
  bussi244->>kallen_kortti: arvo
  kallen_kortti-->bussi244: 1.5
  bussi244-->main: False
```
