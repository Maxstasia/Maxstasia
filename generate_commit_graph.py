# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generate_commit_graph.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mstasiak <mstasiak@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/26 12:32:07 by mstasiak          #+#    #+#              #
#    Updated: 2025/02/26 18:05:43 by mstasiak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import numpy as np
import git
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

""" import os
import requests
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime, timedelta

github_username = "Maxstasia"
github_repo = "Maxstasia"
github_token = os.getenv("GH_PATH") or os.getenv("GH_PAT") or os.getenv("GITHUB_TOKEN")
if not github_token:
    raise ValueError("GH_PATH n'est pas défini. Assurez-vous qu'il est configuré dans les secrets GitHub Actions.")

# Récupérer les commits quotidiens sur 1 an
def get_commit_counts():
    headers = {"Authorization": f"token {github_token}"}
    commit_counts = []
    dates = []
    today = datetime.today()
    
    for i in range(365):
        day = today - timedelta(days=i)
        date_str = day.strftime("%Y-%m-%d")
        url = f"https://api.github.com/repos/{github_username}/{github_repo}/commits?since={date_str}T00:00:00Z&until={date_str}T23:59:59Z"
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            commit_counts.append(len(response.json()))
            dates.append(day)
        else:
            commit_counts.append(0)
            dates.append(day)
    
    return dates[::-1], commit_counts[::-1]

# Générer un graphique 3D en fil de fer
def generate_3d_graph(dates, commit_counts):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.arange(len(dates))  # Jours
    y = np.zeros_like(x)  # Un seul fil
    z = np.array(commit_counts)
    
    ax.plot_wireframe(x.reshape(1, -1), y.reshape(1, -1), z.reshape(1, -1), color='cyan')
    ax.set_xlabel('Jours')
    ax.set_ylabel('')
    ax.set_zlabel('Commits')
    ax.set_title('Visualisation 3D des Commits GitHub')
    
    plt.savefig("commit_graph.png", dpi=300, bbox_inches='tight')
    plt.close()

# Exécution
if __name__ == "__main__":
    dates, commit_counts = get_commit_counts()
    generate_3d_graph(dates, commit_counts)
    print("✅ Graphique mis à jour avec succès !")
 """
