import matplotlib.colors as mcolors

# wsp_lev = [0,4,6,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,36,38,40,43,46,49,52,55,58,61,64,67,70,73,76,79,82,85]
# wsp_color = ['#ffffff','#80ffff','#6fedf1','#5fdde4','#50cdd5','#40bbc7','#2facba','#1f9bac','#108c9f','#007a92',
#              '#00b432','#33c341','#67d251','#99e060','#cbf06f','#ffff80','#ffdd52','#ffdc52','#ffa63e','#ff6d29','#ff3713','#ff0000','#d70000','#af0000','#870000','#5f0000',
#              '#aa00ff','#b722fe','#c446ff','#d46aff','#e38dff','#f1b1ff','#ffd3ff',
#              '#ffc6ea','#ffb6d5','#ffa6c1','#ff97ac','#ff8798','#fe7884','#ff696e','#ff595a','#e74954','#cc3a4c','#b22846','#9a1941']


def clist_WS():
    clist = [
        (0, "#ffffff"),
        (3 / 40, "#80ffff"),
        (6 / 40, "#6fedf1"),
        (8 / 40, "#5fdde4"),
        (10 / 40, "#50cdd5"),
        (12 / 40, "#40bbc7"),
        (13 / 40, "#2facba"),
        (14 / 40, "#1f9bac"),
        (15 / 40, "#108c9f"),
        (16 / 40, "#007a92"),
        (17 / 40, "#00b432"),
        (18 / 40, "#33c341"),
        (19 / 40, "#67d251"),
        (20 / 40, "#99e060"),
        (21 / 40, "#cbf06f"),
        (22 / 40, "#ffff80"),
        (23 / 40, "#ffdd52"),
        (24 / 40, "#ffdc52"),
        (25 / 40, "#ffa63e"),
        (26 / 40, "#ff6d29"),
        (27 / 40, "#ff3713"),
        (28 / 40, "#ff0000"),
        (29 / 40, "#d70000"),
        (30 / 40, "#af0000"),
        (31 / 40, "#870000"),
        (32 / 40, "#5f0000"),
        (34 / 40, "#aa00ff"),
        (36 / 40, "#b722fe"),
        (38 / 40, "#c446ff"),
        (40 / 40, "#d46aff"),
    ]
    #  (43/85, '#e38dff'),
    #  (46/85, '#f1b1ff'),
    #  (49/85, '#ffd3ff'),
    #  (52/85, '#ffc6ea'),
    #  (55/85, '#ffb6d5'),
    #  (58/85, '#ffa6c1'),
    #  (61/85, '#ff97ac'),
    #  (64/85, '#ff8798'),
    #  (67/85, '#fe7884'),
    #  (70/85, '#ff595a'),
    #  (73/85, '#e74954'),
    #  (76/85, '#cc3a4c'),
    #  (79/85, '#b22846'),
    #  (82/85, '#9a1941'),
    #  (85/85, '#9a1941')]
    return clist


def clist_temp():
    clist = [
        (0, "#a8acdf"),
        (1 / 40, "#9092d4"),
        (2 / 40, "#777acc"),
        (3 / 40, "#5f63c3"),
        (4 / 40, "#4949b6"),
        (5 / 40, "#4655c3"),
        (6 / 40, "#435aca"),
        (7 / 40, "#3b6ddf"),
        (8 / 40, "#3979ef"),
        (9 / 40, "#3386f5"),
        (10 / 40, "#2d99fe"),
        (11 / 40, "#22affe"),
        (12 / 40, "#1bc2ff"),
        (13 / 40, "#0ee6fe"),
        (14 / 40, "#07fbff"),
        (15 / 40, "#6ee699"),
        (16 / 40, "#65e08d"),
        (17 / 40, "#4fd06f"),
        (18 / 40, "#45c65f"),
        (19 / 40, "#34bd4b"),
        (20 / 40, "#28b338"),
        (21 / 40, "#16a71f"),
        (22 / 40, "#16a111"),
        (23 / 40, "#43b121"),
        (24 / 40, "#66c034"),
        (25 / 40, "#78c63c"),
        (26 / 40, "#9ad54d"),
        (27 / 40, "#c5e763"),
        (28 / 40, "#e1f26f"),
        (29 / 40, "#fef87b"),
        (30 / 40, "#fdeb76"),
        (31 / 40, "#fad66a"),
        (32 / 40, "#f9c662"),
        (33 / 40, "#f8b558"),
        (34 / 40, "#f6a24e"),
        (35 / 40, "#ef9043"),
        (36 / 40, "#e4692c"),
        (37 / 40, "#e15f27"),
        (38 / 40, "#cc3513"),
        (39 / 40, "#c8250a"),
        (40 / 40, "#c8250a"),
    ]
    return clist


def make_cmap(clist_name):
    clist = globals()[clist_name]()
    cmap = mcolors.LinearSegmentedColormap.from_list("my_cmap", clist)
    return cmap