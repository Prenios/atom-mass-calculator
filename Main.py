# Indication des masses de base du proton et du neutron
masse_protons = float(1.6726E-27)
masse_neutron = float(1.6749E-27)


# L'utilisateur doit entrer un nombre de protons et de neutrons
n_protons = float(input("entrez le nombre de protons: "))
n_neutrons = float(input("entrez le nombre de neutrons: "))


# On cherche la masse totale que représente les protons et les neutrons
m_p = masse_protons*n_protons
m_n = masse_neutron*n_neutrons


# Calcul de la masse totale de l'atome
print(m_p+m_n)

