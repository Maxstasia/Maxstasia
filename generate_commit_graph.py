# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generate_commit_graph.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mstasiak <mstasiak@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/26 12:32:07 by mstasiak          #+#    #+#              #
#    Updated: 2025/02/26 14:44:35 by mstasiak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import numpy as np
import git
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime

# Récupérer l'historique des commits
repo = git.Repo(".")
commits = list(repo.iter_commits())

# Convertir les dates des commits en jours
dates = [datetime.fromtimestamp(commit.committed_date) for commit in commits]
days = [(date - min(dates)).days for date in dates]

# Générer des coordonnées en 3D
x = np.array(days)
y = np.linspace(0, len(dates), len(dates))
z = np.random.rand(len(dates)) * 10  # Altitude aléatoire

# Création du graphique en 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x[:, np.newaxis], y[:, np.newaxis], z[:, np.newaxis], color='blue')

ax.set_xlabel("Jours depuis le premier commit")
ax.set_ylabel("Nombre de commits")
ax.set_zlabel("Random Height")

plt.title("Visualisation 3D des commits GitHub")
plt.savefig("commit_graph.png")
