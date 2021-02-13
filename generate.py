from typing import List

PUZZLE_TITLE: str = 'Vive la Ré...'

DATE_CLUEPHRASE: str = 'G_EATADDTHIS'
FINAL_CLUEPHRASE: str = 'L_s Mis Song'

RESISTOR_CODES = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

REVOLUTIONARY_CALENDAR = '''1	22 Sep	Raisin (Grape)
2	23 Sep	Safran (Saffron)
3	24 Sep	Châtaigne (Chestnut)
4	25 Sep	Colchique (Autumn Crocus)
5	26 Sep	Cheval (Horse)
6	27 Sep	Balsamine (Impatiens)
7	28 Sep	Carotte (Carrot)
8	29 Sep	Amaranthe (Amaranth)
9	30 Sep	Panais (Parsnip)
10	1 Oct	Cuve (Vat)
11	2 Oct	Pomme de terre (Potato)
12	3 Oct	Immortelle (Strawflower)
13	4 Oct	Potiron (Winter squash)
14	5 Oct	Réséda (Mignonette)
15	6 Oct	Âne (Donkey)
16	7 Oct	Belle de nuit (Four o'clock flower)
17	8 Oct	Citrouille (Pumpkin)
18	9 Oct	Sarrasin (Buckwheat)
19	10 Oct	Tournesol (Sunflower)
20	11 Oct	Pressoir (Wine-Press)
21	12 Oct	Chanvre (Hemp)
22	13 Oct	Pêche (Peach)
23	14 Oct	Navet (Turnip)
24	15 Oct	Amaryllis (Amaryllis)
25	16 Oct	Bœuf (Ox)
26	17 Oct	Aubergine (Eggplant)
27	18 Oct	Piment (Chili pepper)
28	19 Oct	Tomate (Tomato)
29	20 Oct	Orge (Barley)
30	21 Oct	Tonneau (Barrel)
1	22 Oct	Pomme (Apple)
2	23 Oct	Céleri (Celery)
3	24 Oct	Poire (Pear)
4	25 Oct	Betterave (Beetroot)
5	26 Oct	Oie (Goose)
6	27 Oct	Héliotrope (Heliotrope)
7	28 Oct	Figue (Common fig)
8	29 Oct	Scorsonère (Black Salsify)
9	30 Oct	Alisier (Chequer Tree)
10	31 Oct	Charrue (Plough)
11	1 Nov	Salsifis (Salsify)
12	2 Nov	Mâcre (Water caltrop)
13	3 Nov	Topinambour (Jerusalem artichoke)
14	4 Nov	Endive (Endive)
15	5 Nov	Dindon (Turkey)
16	6 Nov	Chervis (Skirret)
17	7 Nov	Cresson (Watercress)
18	8 Nov	Dentelaire (Leadworts)
19	9 Nov	Grenade (Pomegranate)
20	10 Nov	Herse (Harrow)
21	11 Nov	Bacchante (Baccharis)
22	12 Nov	Azerole (Azarole)
23	13 Nov	Garance (Madder)
24	14 Nov	Orange (Orange)
25	15 Nov	Faisan (Pheasant)
26	16 Nov	Pistache (Pistachio Nut)
27	17 Nov	Macjonc (Tuberous pea)
28	18 Nov	Coing (Quince)
29	19 Nov	Cormier (Service tree)
30	20 Nov	Rouleau (Roller)
1	21 Nov	Raiponce (Rampion)
2	22 Nov	Turneps (Cattle turnip)
3	23 Nov	Chicorée (Chicory)
4	24 Nov	Nèfle (Medlar)
5	25 Nov	Cochon (Pig)
6	26 Nov	Mâche (Lamb's lettuce)
7	27 Nov	Chou-fleur (Cauliflower)
8	28 Nov	Miel (Honey)
9	29 Nov	Genièvre (Juniper)
10	30 Nov	Pioche (Pickaxe)
11	1 Dec	Cire (Wax)
12	2 Dec	Raifort (Horseradish)
13	3 Dec	Cèdre (Cedar tree)
14	4 Dec	Sapin (Fir)
15	5 Dec	Chevreuil (Roe deer)
16	6 Dec	Ajonc (Gorse)
17	7 Dec	Cyprès (Cypress Tree)
18	8 Dec	Lierre (Ivy)
19	9 Dec	Sabine (Savin Juniper)
20	10 Dec	Hoyau (Grub-hoe)
21	11 Dec	Érable à sucre (Sugar Maple)
22	12 Dec	Bruyère (Heather)
23	13 Dec	Roseau (Reed plant)
24	14 Dec	Oseille (Sorrel)
25	15 Dec	Grillon (Cricket)
26	16 Dec	Pignon (Pine nut)
27	17 Dec	Liège (Cork)
28	18 Dec	Truffe (Truffle)
29	19 Dec	Olive (Olive)
30	20 Dec	Pelle (Shovel)
1	21 Dec	Tourbe (Peat)
2	22 Dec	Houille (Coal)
3	23 Dec	Bitume (Bitumen)
4	24 Dec	Soufre (Sulphur)
5	25 Dec	Chien (Dog)
6	26 Dec	Lave (Lava)
7	27 Dec	Terre végétale (Topsoil)
8	28 Dec	Fumier (Manure)
9	29 Dec	Salpêtre (Saltpeter)
10	30 Dec	Fléau (Flail)
11	31 Dec	Granit (Granite)
12	1 Jan	Argile (Clay)
13	2 Jan	Ardoise (Slate)
14	3 Jan	Grès (Sandstone)
15	4 Jan	Lapin (Rabbit)
16	5 Jan	Silex (Flint)
17	6 Jan	Marne (Marl)
18	7 Jan	Pierre à chaux (Limestone)
19	8 Jan	Marbre (Marble)
20	9 Jan	Van (Winnowing fan)
21	10 Jan	Pierre à plâtre (Gypsum)
22	11 Jan	Sel (Salt)
23	12 Jan	Fer (Iron)
24	13 Jan	Cuivre (Copper)
25	14 Jan	Chat (Cat)
26	15 Jan	Étain (Tin)
27	16 Jan	Plomb (Lead)
28	17 Jan	Zinc (Zinc)
29	18 Jan	Mercure (Mercury)
30	19 Jan	Crible (Sieve)
1	20 Jan	Lauréole (Spurge-laurel)
2	21 Jan	Mousse (Moss)
3	22 Jan	Fragon (Butcher's Broom)
4	23 Jan	Perce-neige (Snowdrop)
5	24 Jan	Taureau (Bull)
6	25 Jan	Laurier-thym (Laurustinus)
7	26 Jan	Amadouvier (Tinder polypore)
8	27 Jan	Mézéréon (Daphne mezereum)
9	28 Jan	Peuplier (Poplar)
10	29 Jan	Coignée (Axe)
11	30 Jan	Ellébore (Hellebore)
12	31 Jan	Brocoli (Broccoli)
13	1 Feb	Laurier (Bay laurel)
14	2 Feb	Avelinier (Filbert)
15	3 Feb	Vache (Cow)
16	4 Feb	Buis (Box Tree)
17	5 Feb	Lichen (Lichen)
18	6 Feb	If (Yew tree)
19	7 Feb	Pulmonaire (Lungwort)
20	8 Feb	Serpette (Billhook)
21	9 Feb	Thlaspi (Pennycress)
22	10 Feb	Thimelé (Rose Daphne)
23	11 Feb	Chiendent (Couch grass)
24	12 Feb	Trainasse (Common Knotgrass)
25	13 Feb	Lièvre (Hare)
26	14 Feb	Guède (Woad)
27	15 Feb	Noisetier (Hazel)
28	16 Feb	Cyclamen (Cyclamen)
29	17 Feb	Chélidoine (Celandine)
30	18 Feb	Traîneau (Sleigh)
1	19 Feb	Tussilage (Coltsfoot)
2	20 Feb	Cornouiller (Dogwood)
3	21 Feb	Violier (Matthiola)
4	22 Feb	Troène (Privet)
5	23 Feb	Bouc (Billygoat)
6	24 Feb	Asaret (Wild Ginger)
7	25 Feb	Alaterne (Italian Buckthorn)
8	26 Feb	Violette (Violet)
9	27 Feb	Marceau (Goat Willow)
10	28 Feb	Bêche (Spade)
11	1 Mar	Narcisse (Narcissus)
12	2 Mar	Orme (Elm)
13	3 Mar	Fumeterre (Common fumitory)
14	4 Mar	Vélar (Hedge mustard)
15	5 Mar	Chèvre (Goat)
16	6 Mar	Épinard (Spinach)
17	7 Mar	Doronic (Doronicum)
18	8 Mar	Mouron (Pimpernel)
19	9 Mar	Cerfeuil (Chervil)
20	10 Mar	Cordeau (Twine)
21	11 Mar	Mandragore (Mandrake)
22	12 Mar	Persil (Parsley)
23	13 Mar	Cochléaria (Scurvy-grass)
24	14 Mar	Pâquerette (Daisy)
25	15 Mar	Thon (Tuna)
26	16 Mar	Pissenlit (Dandelion)
27	17 Mar	Sylvie (Wood Anemone)
28	18 Mar	Capillaire (Maidenhair fern)
29	19 Mar	Frêne (Ash tree)
30	20 Mar	Plantoir (Dibber)
1	21 Mar	Primevère (Primrose)
2	22 Mar	Platane (Plane Tree)
3	23 Mar	Asperge (Asparagus)
4	24 Mar	Tulipe (Tulip)
5	25 Mar	Poule (Hen )
6	26 Mar	Bette (Chard)
7	27 Mar	Bouleau (Birch)
8	28 Mar	Jonquille (Daffodil)
9	29 Mar	Aulne (Alder)
10	30 Mar	Couvoir (Hatchery)
11	31 Mar	Pervenche (Periwinkle)
12	1 Apr	Charme (Hornbeam)
13	2 Apr	Morille (Morel)
14	3 Apr	Hêtre (Beech Tree)
15	4 Apr	Abeille (Bee)
16	5 Apr	Laitue (Lettuce)
17	6 Apr	Mélèze (Larch)
18	7 Apr	Ciguë (Hemlock)
19	8 Apr	Radis (Radish)
20	9 Apr	Ruche (Hive)
21	10 Apr	Gainier (Judas tree)
22	11 Apr	Romaine (Romaine lettuce)
23	12 Apr	Marronnier (Horse chestnut)
24	13 Apr	Roquette (Arugula or Rocket)
25	14 Apr	Pigeon (Pigeon)
26	15 Apr	Lilas (Lilac)
27	16 Apr	Anémone (Anemone)
28	17 Apr	Pensée (Pansy)
29	18 Apr	Myrtille (Bilberry)
30	19 Apr	Greffoir (Grafting knife)
1	20 Apr	Rose (Rose)
2	21 Apr	Chêne (Oak Tree)
3	22 Apr	Fougère (Fern)
4	23 Apr	Aubépine (Hawthorn)
5	24 Apr	Rossignol (Nightingale)
6	25 Apr	Ancolie (Common Columbine)
7	26 Apr	Muguet (Lily of the valley)
8	27 Apr	Champignon (Button mushroom)
9	28 Apr	Hyacinthe (Hyacinth)
10	29 Apr	Râteau (Rake)
11	30 Apr	Rhubarbe (Rhubarb)
12	1 May	Sainfoin (Sainfoin)
13	2 May	Bâton d'or (Wallflower)
14	3 May	Chamerisier (Fan Palm tree)
15	4 May	Ver à soie (Silkworm)
16	5 May	Consoude (Comfrey)
17	6 May	Pimprenelle (Salad burnet)
18	7 May	Corbeille d'or (Basket of Gold)
19	8 May	Arroche (Orache)
20	9 May	Sarcloir (Garden hoe)
21	10 May	Statice (Thrift)
22	11 May	Fritillaire (Fritillary)
23	12 May	Bourrache (Borage)
24	13 May	Valériane (Valerian)
25	14 May	Carpe (Carp)
26	15 May	Fusain (Spindle (shrub))
27	16 May	Civette (Chive)
28	17 May	Buglosse (Bugloss)
29	18 May	Sénevé (Wild mustard)
30	19 May	Houlette (Shepherd's crook)
1	20 May	Luzerne (Alfalfa)
2	21 May	Hémérocalle (Daylily)
3	22 May	Trèfle (Clover)
4	23 May	Angélique (Angelica)
5	24 May	Canard (Duck)
6	25 May	Mélisse (Lemon balm)
7	26 May	Fromental (Oat grass)
8	27 May	Martagon (Martagon lily)
9	28 May	Serpolet (Wild Thyme)
10	29 May	Faux (Scythe)
11	30 May	Fraise (Strawberry)
12	31 May	Bétoine (Woundwort)
13	1 Jun	Pois (Pea)
14	2 Jun	Acacia (Acacia)
15	3 Jun	Caille (Quail)
16	4 Jun	Œillet (Carnation)
17	5 Jun	Sureau (Elderberry)
18	6 Jun	Pavot (Poppy plant)
19	7 Jun	Tilleul (Linden or Lime tree)
20	8 Jun	Fourche (Pitchfork)
21	9 Jun	Barbeau (Cornflower)
22	10 Jun	Camomille (Camomile)
23	11 Jun	Chèvrefeuille (Honeysuckle)
24	12 Jun	Caille-lait (Bedstraw)
25	13 Jun	Tanche (Tench)
26	14 Jun	Jasmin (Jasmine)
27	15 Jun	Verveine (Verbena)
28	16 Jun	Thym (Thyme)
29	17 Jun	Pivoine (Peony)
30	18 Jun	Chariot (Hand Cart)
1	19 Jun	Seigle (Rye)
2	20 Jun	Avoine (Oat)
3	21 Jun	Oignon (Onion)
4	22 Jun	Véronique (Speedwell)
5	23 Jun	Mulet (Mule)
6	24 Jun	Romarin (Rosemary)
7	25 Jun	Concombre (Cucumber)
8	26 Jun	Échalote (Shallot)
9	27 Jun	Absinthe (Wormwood)
10	28 Jun	Faucille (Sickle)
11	29 Jun	Coriandre (Coriander)
12	30 Jun	Artichaut (Artichoke)
13	1 Jul	Girofle (Clove)
14	2 Jul	Lavande (Lavender)
15	3 Jul	Chamois (Chamois)
16	4 Jul	Tabac (Tobacco)
17	5 Jul	Groseille (Redcurrant)
18	6 Jul	Gesse (Hairy Vetchling)
19	7 Jul	Cerise (Cherry)
20	8 Jul	Parc (Park)
21	9 Jul	Menthe (Mint)
22	10 Jul	Cumin (Cumin)
23	11 Jul	Haricot (Bean)
24	12 Jul	Orcanète (Alkanet)
25	13 Jul	Pintade (Guineafowl)
26	14 Jul	Sauge (Sage)
27	15 Jul	Ail (Garlic)
28	16 Jul	Vesce (Tare)
29	17 Jul	Blé (Wheat)
30	18 Jul	Chalémie (Shawm)
1	19 Jul	Épeautre (Spelt)
2	20 Jul	Bouillon blanc (Common mullein)
3	21 Jul	Melon (Melon)
4	22 Jul	Ivraie (Ryegrass)
5	23 Jul	Bélier (Ram)
6	24 Jul	Prêle (Horsetail)
7	25 Jul	Armoise (Mugwort)
8	26 Jul	Carthame (Safflower)
9	27 Jul	Mûre (Blackberry)
10	28 Jul	Arrosoir (Watering can)
11	29 Jul	Panic (Foxtail millet)
12	30 Jul	Salicorne (Common Glasswort)
13	31 Jul	Abricot (Apricot)
14	1 Aug	Basilic (Basil)
15	2 Aug	Brebis (Ewe)
16	3 Aug	Guimauve (Marshmallow)
17	4 Aug	Lin (Flax)
18	5 Aug	Amande (Almond)
19	6 Aug	Gentiane (Gentian)
20	7 Aug	Écluse (Lock)
21	8 Aug	Carline (Carline thistle)
22	9 Aug	Câprier (Caper)
23	10 Aug	Lentille (Lentil)
24	11 Aug	Aunée (Inula)
25	12 Aug	Loutre (Otter)
26	13 Aug	Myrte (Myrtle)
27	14 Aug	Colza (Rapeseed)
28	15 Aug	Lupin (Lupin)
29	16 Aug	Coton (Cotton)
30	17 Aug	Moulin (Mill)
1	18 Aug	Prune (Plum)
2	19 Aug	Millet (Millet)
3	20 Aug	Lycoperdon (Puffball)
4	21 Aug	Escourgeon (Six-row Barley)
5	22 Aug	Saumon (Salmon)
6	23 Aug	Tubéreuse (Tuberose)
7	24 Aug	Sucrion (Winter Barley)
8	25 Aug	Apocyn (Apocynum)
9	26 Aug	Réglisse (Liquorice)
10	27 Aug	Échelle (Ladder)
11	28 Aug	Pastèque (Watermelon)
12	29 Aug	Fenouil (Fennel)
13	30 Aug	Épine vinette (European Barberry)
14	31 Aug	Noix (Walnut)
15	1 Sep	Truite (Trout)
16	2 Sep	Citron (Lemon)
17	3 Sep	Cardère (Teasel)
18	4 Sep	Nerprun (Buckthorn)
19	5 Sep	Tagette (Mexican Marigold)
20	6 Sep	Hotte (Harvesting basket)
21	7 Sep	Églantier (Wild Rose)
22	8 Sep	Noisette (Hazelnut)
23	9 Sep	Houblon (Hops)
24	10 Sep	Sorgho (Sorghum)
25	11 Sep	Écrevisse (Crayfish)
26	12 Sep	Bigarade (Bitter orange)
27	13 Sep	Verge d'or (Goldenrod)
28	14 Sep	Maïs (Maize or Corn)
29	15 Sep	Marron (Sweet Chestnut)
30	16 Sep	Panier (Pack Basket)'''.split('\n')


def get_resistor_colors(r: int):
    resistor_colors: List[str] = []

    r_val: str = str(r)
    magnitude: int = 0
    while r_val[-1] == '0':
        magnitude += 1
        r_val = r_val[:-1]
    while True:
        sig_fig: int = int(r_val[0])
        resistor_colors.append(RESISTOR_CODES[sig_fig])
        if len(r_val) == 1:
            break
        else:
            r_val = r_val[1:]
    resistor_colors.append(RESISTOR_CODES[magnitude])

    return resistor_colors


def get_data_set(lang: str = 'en', enc: str = 'alpha') -> List[dict]:
    data_set: List[dict] = []
    for (i, letter_pair) in enumerate(zip(DATE_CLUEPHRASE, FINAL_CLUEPHRASE)):
        a, b = letter_pair
        if a == b == '_':
            continue

        month: int = i
        day: int = ord(a) - 64

        resistance_value: int = ord(b) - day
        if enc == 'alpha':
            resistance_value -= 64
        resistor_colors: List[str] = get_resistor_colors(resistance_value)

        calendar: str = REVOLUTIONARY_CALENDAR[month * 30 + day - 1].split('\t')[2]
        calendar_thing_fr: str = calendar[:calendar.index('(') - 1]
        calendar_thing_en: str = calendar[calendar.index('(') + 1:calendar.index(')')]

        data_set.append({
            'RESISTANCE': resistance_value,
            'MONTH': i + 1,
            'DAY': day,
            'THING': {'en': calendar_thing_en, 'fr': calendar_thing_fr}.get(lang),
            'COLORS': resistor_colors,
        })

    data_set = sorted(data_set, key=lambda x: x['THING'])
    return data_set


def get_puzzle_html(data_set: List[dict]):
    html: str = f'''
<html>
<head>
<title>{PUZZLE_TITLE}</title>
<style>
p span {{ -webkit-text-stroke-width:1.2px; }}
p {{ letter-spacing:1.2px; font-size:30px; font-family:sans-serif; font-weight:bold; color:tan; }}
body {{ background-color:#eee; }}
</style>
</head>
<body>'''

    for row in data_set:
        colors: List[str] = row['COLORS']
        thing: str = row['THING'].upper()
        html += '\n<p>'
        for i in range(len(colors)):
            html += f'<span style="-webkit-text-stroke-color:{colors[i].lower()}">{thing[i] if thing[i].strip() else "&nbsp;"}</span>'
        html += thing[len(colors):]
        html += '</p>'

    html += '''
</body>
</html>'''

    return html.lstrip().rstrip()


def solve(data_set: List[dict], enc: str = 'alpha'):
    data_set = sorted(data_set, key=lambda x: x['MONTH'])
    date_extract: str = ''
    soln_extract: str = ''
    for (i, row) in enumerate(data_set):
        date_extract += chr(row['DAY'] + 64)
        soln_extract += chr(row['RESISTANCE'] + row['DAY'] + (64 if enc == 'alpha' else 0))

    assert date_extract == DATE_CLUEPHRASE.replace('_', '')
    assert soln_extract == FINAL_CLUEPHRASE.replace('_', '')

    return True


if __name__ == '__main__':
    assert len(RESISTOR_CODES) == 10
    assert len(REVOLUTIONARY_CALENDAR) == 360

    ENCODING: str = 'ascii'
    # ENCODING: str = 'alpha'

    LANG: str = 'en'
    # LANG: str= 'en'

    DATA_SET: List[dict] = get_data_set(lang=LANG, enc=ENCODING)
    # print('\n'.join([f'{d}' for d in DATA_SET]))
    assert solve(DATA_SET, enc=ENCODING)

    PUZZLE_HTML: str = get_puzzle_html(DATA_SET)

    with open('vive_la_re.html', 'w') as f:
        f.write(PUZZLE_HTML)
