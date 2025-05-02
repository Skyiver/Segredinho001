from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .aluno import Aluno
from .professor import Professor
from .turma import Turma