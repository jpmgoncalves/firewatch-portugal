# Firewatch Portugal

Portugal Fire Lookout Towers (Postos de Vigia) — Viewshed Analysis

Interactive map showing 250 fire lookout towers across Portugal with viewshed computation capabilities. Uses Mapbox GL JS with terrain data to calculate line-of-sight visibility from each tower.

## Data Sources

- **ICNF** (Instituto da Conservação da Natureza e das Florestas) — tower registry with codes, locations, and metadata
- **OpenStreetMap** — tower names, precise coordinates, and structural details

## Towers Requiring Identification

The following 70 towers lack OSM data and have coordinates converted from the Hayford ellipsoid. Their positions may be less precise and they need to be identified/validated on the ground or via satellite imagery.

| PV Code | Distrito | Concelho | Freguesia |
|---------|----------|----------|-----------|
| 21-07 | Aveiro | Castelo de Paiva | Raiva |
| 22-01 | Aveiro | Arouca | Moldes |
| 22-02 | Aveiro | Vale de Cambra | Arões |
| 47-02 | Aveiro | Sever do Vouga | Talhadas |
| 62-01 | Beja | Moura | Amareleja |
| 62-02 | Beja | Moura | Restauração |
| 63-06 | Beja | Odemira | S. Luís |
| 63-07 | Beja | Odemira | Santinho das Amoreiras |
| 12-01 | Bragança | Bragança | França |
| 12-02 | Bragança | Bragança | Deilão |
| 12-04 | Bragança | Vinhais | Travanca |
| 12-05 | Bragança | Vinhais | Vale de Janeiro |
| 15-01 | Bragança | Macedo de Cavaleiros | Grijó de Vale Benfeito |
| 32-03 | Castelo Branco | Covilhã | Covilhã (Santinho) |
| 36-03 | Castelo Branco | Oleiros | Oleiros |
| 36-04 | Castelo Branco | Sertã | Pedrógão Pequeno |
| 36-06 | Castelo Branco | Sertã | Ermida |
| 41-01 | Coimbra | Pampilhosa da Serra | Pessegueiro |
| 41-02 | Coimbra | Arganil | Teixeira |
| 41-04 | Coimbra | Arganil | Piódão |
| 41-08 | Coimbra | Penacova | Sazes do Lorvão |
| 41-09 | Coimbra | Vila Nova de Poiares | Lavegadas |
| 63-08 | Faro | Monchique | Monchique |
| 83-01 | Faro | Loulé | Salir |
| P-1 | Faro | Aljezur | Aljezur |
| P-2 | Faro | Aljezur | Aljezur |
| P-3 | Faro | Vila do Bispo | Vila do Bispo |
| 35-01 | Guarda | Manteigas | Sameiro |
| 35-03 | Guarda | Sabugal | Quadrazais |
| 45-06 | Guarda | Aguiar da Beira | Aguiar da Beira |
| 42-01 | Leiria | Castanheira de Pêra | Coentral |
| 42-07 | Leiria | Alvaiázere | Alvaiázere |
| 44-01 | Leiria | Leiria | Coimbrão |
| 44-02 | Leiria | Marinha Grande | Marinha Grande |
| 44-03 | Leiria | Marinha Grande | Marinha Grande |
| 44-04 | Leiria | Alcobaça | Pataias |
| 51-01 | Leiria | Nazaré | Nazaré |
| P-01 | Leiria | Porto de Mós | Serro Ventoso |
| P-02 | Leiria | Porto de Mós | Arrimal |
| 52-02 | Lisboa | Torres Vedras | Monte Redondo |
| 52-03 | Lisboa | Alenquer | Ota |
| 54-01 | Lisboa | Cascais | Alcabideche |
| 54-03 | Lisboa | Sintra | Sintra (Santinho) |
| 54-05 | Lisboa | Sintra | Belas |
| 54-06 | Lisboa | Cascais | Alcabideche |
| 21 | Porto | Amarante | Ansiães |
| 21-01 | Porto | Amarante | Fregim |
| 21-05 | Porto | Paredes | Vandoma |
| Valongo-2 | Porto | Valongo | Valongo |
| 53-01 | Santarém | Coruche | Coruche |
| P-03 | Santarém | Alcanena | Minde |
| 57-02 | Setúbal | Almada | Charneca da Caparica |
| 0-72 | Viana do Castelo | Ponte da Barca | Lindoso |
| 25-02 | Viana do Castelo | Monção | Riba de Mouro |
| 25-04 | Viana do Castelo | Paredes de Coura | Bico |
| 25-06 | Viana do Castelo | Caminha | Dem |
| 28 | Viana do Castelo | Viana do Castelo | Montaria |
| 0-83 | Vila Real | Montalegre | Cabril |
| 11-01 | Vila Real | Montalegre | Viade de Baixo |
| 11-02 | Vila Real | Boticas | Bobadela |
| 13-02 | Vila Real | Chaves | Vilar de Nantes |
| 13-04 | Vila Real | Valpaços | Vilarandelo |
| 18-01 | Vila Real | Vila Pouca de Aguiar | Pensalvos |
| 18-04 | Vila Real | Murça | Carva |
| 45-02 | Viseu | Viseu | Cota |
| 45-03 | Viseu | Viseu | Cota |
| 46-01 | Viseu | Oliveira de Frades | Arca |
| 46-04 | Viseu | Tondela | Guardão |
| 46-08 | Viseu | São Pedro do Sul | Santinho das Moitas |
| 68-01 | Évora | Estremoz | Glória |
