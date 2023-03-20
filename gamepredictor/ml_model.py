import sqlite3
import pandas as pd
import pathlib
from sklearn.neighbors import BallTree
# Файл создаёт модель на основе таблицы из базы данных
db_dir = pathlib.Path(__file__).resolve().parent.parent
con = sqlite3.connect(str(db_dir) + '/' + 'db.sqlite3')

games = pd.read_sql('select * from gamepredictor_games', con)  # Создание и заполнение модели
games_iloc = games.iloc()
X = [g[2: -1] for g in games_iloc]
tree = BallTree(X, leaf_size=2)
