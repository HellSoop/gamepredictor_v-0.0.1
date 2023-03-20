from .ml_model import tree, games_iloc

def get_characteristics(game):
    return [game.shooter, game.rpg, game.story, game.gloominess, game.aesthetics,
                            game.survival, game.fullness_of_world, game.creative_potential,
                            game.fighting_system, game.puzzles, game.quests, game.difficulty,
                            game.moral, game.horror, game.action, game.emotionality, game.reality,
                            game.atmosphere]

def get_closest(game_characteristics, k=3):
    '''Финаальная функция для получения названий игр'''

    _, ind = tree.query([game_characteristics], k=k + 2)  # нахождение индексов игр
    print(ind)
    games = [games_iloc[i] for i in ind[0]]  # нахождение игр в датафрейме

    return [g[1] for g in games]  # Возврат названий игр
