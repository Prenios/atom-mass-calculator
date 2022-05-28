# Indication des masses de base du proton et du neutron
MASSE_PROTONS = 1.6726E-27
MASSE_NEUTRON = 1.6749E-27


# L'utilisateur doit entrer un nombre de protons et de neutrons
n_protons = float(input("entrez le nombre de protons: "))
n_neutrons = float(input("entrez le nombre de neutrons: "))


# On cherche la masse totale que représente les protons et les neutrons
m_p = MASSE_PROTONS * n_protons
m_n = MASSE_NEUTRON * n_neutrons


# Calcul de la masse totale de l'atome
print(m_p+m_n)
