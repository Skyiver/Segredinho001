from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importar todos os modelos
from .aluno import Aluno
from .professor import Professor
from .turma import Turma