# Sergen KAHRAMAN - 23835101 -İstatistiksel Yöntemler Ve Veri Analizi Ödevi

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Helper Methods


def GroupBy(dataset, indipendent, dependent):
    return [dataset[dataset[indipendent] == bolum][dependent] for bolum in dataset[indipendent].unique()]


def TestWithANOVA(dataset, indipendent, dependent):
    from scipy.stats import f_oneway
    # ANOVA testi
    stats, pValue = f_oneway(*GroupBy(dataset, indipendent, dependent))
    alpha = 0.05  # Anlamlılık düzeyi
    if pValue < alpha:
        print(f"{dependent} verileri için ANOVA testi sonucu: Gruplar arasında anlamlı bir fark var. (p-değeri: {pValue})\n")
    else:
        print(f"{dependent} verileri için ANOVA testi sonucu: Gruplar arasında anlamlı bir fark yok. (p-değeri: {pValue})\n")


def TestWithKruskal(dataset, indipendent, dependent):
    from scipy.stats import kruskal
    # Non-Parametrik test (Kruskal-Wallis-H test)
    stats, pValue = kruskal(*GroupBy(dataset, indipendent, dependent))
    alpha = 0.05  # Anlamlılık düzeyi
    if pValue < alpha:
        print(f"{dependent} için Kruskal-Wallis-H testi sonuçları istatistiksel olarak anlamlıdır. Gruplar arasında fark vardır.\n")
    else:
        print(f"{dependent} için Kruskal-Wallis-H testi sonuçları istatistiksel olarak anlamlı değildir. Gruplar arasında fark yoktur.\n")


# Read data from xlsx
dataset = pd.read_excel("AssessmentAnalytics_TestData.xlsx")

# Declare check list
independentVariable = 'Bölüm'
dependentVariableList = ['OnBilgi', 'AraSinav', 'FinalSinav',
                         'OrtalamaCalismaSuresi', 'CanliDersToplamSure', 'Aktivite Tamamlama Oranı']

# Gruplara Göre OnBilgi puanlarının Levene Testi - Homojenlik testi ( > 0.05)
for dependentVariable in dependentVariableList:
    from scipy.stats import levene
    stats, pValue = levene(
        *GroupBy(dataset, independentVariable, dependentVariable))
    if pValue > 0.05:
        print(
            f"{dependentVariable} verileri için Levene testi sonucu: p-değeri:{pValue} ve homojenlik varsayımını karşılıyor.")
        TestWithANOVA(dataset, independentVariable, dependentVariable)
    else:
        TestWithKruskal(dataset, independentVariable, dependentVariable)
