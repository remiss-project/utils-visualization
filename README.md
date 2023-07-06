# Data visualization utils

Alguns petits codis útils per a visualitzar dades obtingudes amb [utils-data-processing].

## plot\_community\_sizes.py

```
python3 plot_community_sizes.py -n INT COMMUNITIES OUTFILE
```

Aquest codi rep d'entrada un fitxer de comunitats (`COMMUNITIES`)
amb el format obtingut pel codi `get_network_communities.py`
i fa un gràfic de barres del nombre d'usuaris que hi ha a cada comunitat,
que el desa al fitxer `OUTFILE`.
L'opció `-n` és per a dibuixar únicament les n comunitats més grans.

## plot\_counts.py

```
python3 plot_counts.py --xlocator INT [--group] --ylabel TEXT INFILE OUTFILE
```

Aquest codi rep d'entrada un fitxer (`INFILE`) CSV de counts
amb el format obtingut pels codis `get_counts_jsonl.py` o `get_counts_twarc.py`
i fa un gràfic del nombre de tweets per finestra temporal,
que el desa al fitxer `OUTFILE`.
L'opció `--xlocator` és cada quants dies es vol posar un locator a l'eix de les x,
que per defecte és 7.
Aquesta opció pot ser útil en funció de quina sigui l'amplada de les finestres temporals del fitxer d'entrada.
Si el fitxer de counts prové de `get_counts_twarc.py`,
tindrà el nombre de tweets per cada mot clau, també.
En aquest cas, per defecte fa una línia per cada mot.
Si es vol fer un simple gràfic de barres agrupant tots els mots,
es pot fer servir l'opció `--group`.
L'opció `--ylabel` és senzillament per canviar el label de l'eix de les y,
que per defecte és "tweets".

## plot\_network.py

```
python3 plot_network.py --colors FILE --size INT LAYOUT COMMUNITIES OUTFILE
```

Aquest codi rep d'entrada un fitxer de layout (`LAYOUT`)
amb el format obtingut pel codi `get_network_layout.py`
i un fitxer de comunitats (`COMMUNITIES`)
amb el format obtingut pel codi `get_network_communities.py`
i pinta una xarxa d'usuaris
on cada usuari és a la posició que diu el layout
i el seu color depèn de la comunitat on és.
Com que les xarxes que utilitzem són molt grans, no pintem les arestes,
que computacionalment seria lent i igualment només afegirien una negror de fons poc aclaridora.
El dibuix es desa a `OUTFILE.png` i a `OUTFILE.pdf`.
Els colors predeterminats estan definits a `default_community_colors.json`,
però es poden canviar passant un fitxer amb el mateix format a l'opció `--colors`.
L'opció `--size` indica senzillament la mida dels dibuixos, que per defecte té un valor de 10.

## print\_community\_centers.py

```
python3 print_community_center.py --colors FILE --weight TEXT NETWORK COMMUNITIES OUTFILE
```

Aquest codi rep d'entrada un fitxer gml de xarxa (`NETWORK`)
amb el format obtingut amb [twarc-network]
i un fitxer de comunitats (`COMMUNITIES`)
amb el format obtingut pel codi `get_network_communities.py`
i escriu a `OUTFILE` un simple fitxer txt on per cada comunitat escriu els 10 usuaris més centrals
segons la centralitat de grau d'entrada.
Les arestes de les xarxes d'usuaris de Twarc són pesades.
Per defecte, es fa servir el pes `weight`,
que correspon al nombre total d'interaccions d'un usuari a l'altre
(retweets, citacions, respostes i mencions).
Si es vol usar un pes concret, com per exemple els retweets,
es pot fer amb l'opció `--weight retweet`.
Per identificar millor les comunitats, s'identifiquen amb el color que es deuen haver pintat.
Per defecte es fa servir `default_community_colors.json`,
però es pot fer servir un altre fitxer de colors amb l'opció `--colors`.
Les comunitats considerades són únicament les comunitats que tenen un color definit.

## print\_community\_popular\_tweet.py

```
python3 print_community_popular_tweet.py -n INT COMMUNITIES TWEETS OUTFILE
```

Aquest codi rep d'entrada un fitxer de comunitats (`COMMUNITIES`)
amb el format obtingut pel codi `get_network_communities.py`
i un fitxer jsonl de tweets (`TWEETS`) obtingut amb alguna consulta de [twarc]
i escriu a `OUTFILE` el tweet més retweetat de les n (segons l'opció `-n`) comunitats més grans.

[utils-data-processing]: https://github.com/remiss-project/utils-data-processing
[twarc]: https://github.com/DocNow/twarc
[twarc-network]: https://github.com/DocNow/twarc-network
