import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from highlight_text import ax_text
import pandas as pd

# Supondo que você tenha os dados necessários
# top_chutes_sorted e top_chutes_with_coords devem ser DataFrames do pandas

# Configuração do pitch (campo de futebol)
fig, axs = pitch.grid(nrows=3, ncols=4, figheight=30,
                      endnote_height=0.03, endnote_space=0,
                      axis=False, title_height=0.08, grid_height=0.84)

# Obtém os top 12 jogadores
top12_ids = top_chutes_sorted[['playerName', 'playerId']].reset_index(drop=True)

for idx, ax in enumerate(axs['pitch'].flat):
    if idx >= len(top12_ids):
        ax.axis('off')
        continue

    player_name = top12_ids.loc[idx, 'playerName']
    player_id = top12_ids.loc[idx, 'playerId']

    # Filtra os chutes do jogador atual
    player_chutes = top_chutes_with_coords[
        (top_chutes_with_coords['playerName'] == player_name) &
        (top_chutes_with_coords['playerId'] == player_id)
        ]

    # Separa os tipos de chute
    goal_shot = player_chutes[player_chutes['type'] == 'Goal']
    goalon_shot = player_chutes[player_chutes['type'] == 'SavedShot']
    goaloff_shot = player_chutes[
        (player_chutes['type'] == 'MissedShots') |
        (player_chutes['type'] == 'ShotOnPost')
        ]

    # Plota os chutes no campo
    pitch.scatter(goal_shot.x, goal_shot.y,
                  color='green', s=300, edgecolors='black', ax=ax)
    pitch.scatter(goalon_shot.x, goalon_shot.y,
                  color='gold', s=300, edgecolors='black', ax=ax)
    pitch.scatter(goaloff_shot.x, goaloff_shot.y,
                  color='red', s=300, edgecolors='black', ax=ax)

    # Calcula estatísticas
    total_shot = len(goal_shot) + len(goalon_shot) + len(goaloff_shot)
    efic_pct = (100 * len(goal_shot) / total_shot) if total_shot > 0 else 0
    conv_pct = (100 * len(goalon_shot) / total_shot) if total_shot > 0 else 0

    # Texto de anotação
    annotation_string = (
        f'{player_name} | '
        f'<{len(goal_shot)}>/{total_shot} - '
        f'{round(efic_pct, 1)}% | '
        f'<{len(goalon_shot)}>/{total_shot} - '
        f'{round(conv_pct, 1)}%'
    )

    ax_text(
        0, -5, annotation_string,
        ha='left', va='center', fontsize=35,
        fontproperties=fm_scada.prop,
        highlight_textprops=[
            {"color": 'green'},
            {"color": 'gold'}
        ],
        ax=ax
    )

# Configuração do título
axs['title'].text(0.5, 0.75, 'Os 12 Jogadores com mais Finalizações no Brasileirão',
                  fontsize=55, fontproperties=fm_scada.prop,
                  va='center', ha='center')

SUB_TEXT = ('ShotMap dos jogadores com mais Finalizações no Brasileirão\n'
            '<Gol> | <Chute no Alvo> | <Chute para Fora> \n')

ax_text(0.5, 0.28, SUB_TEXT, fontsize=35,
        fontproperties=fm_scada.prop, va='center', ha='center',
        ax=axs['title'],
        highlight_textprops=[
            {"color": "green"},
            {"color": "gold"},
            {"color": "red"}
        ])

# Adiciona logotipo
logo = mpimg.imread("Brasileirão.png")
ax_img = fig.add_axes([0.25, 0.90, 0.1, 0.1])
ax_img.imshow(logo)
ax_img.axis("off")

plt.show()