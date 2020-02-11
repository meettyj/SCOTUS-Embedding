
from textacy.datasets.supreme_court import SupremeCourt
sc = SupremeCourt()
sc.download()
print(sc.info)