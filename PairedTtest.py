# Sergen KAHRAMAN - 23835101 -İstatistiksel Yöntemler Ve Veri Analizi Ödevi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
# Read data from xlsx
dataset = pd.read_excel("AssessmentAnalytics_TestData.xlsx")

# Data Groups
quizData = dataset["QuizOrtalama"]
araSinavData = dataset["AraSinav"]
finalSinavData = dataset["FinalSinav"]

# Describe
stats1 = quizData.describe()
print("Quiz: ",stats1);
print("Basıklık (Kurtosis):", stats.kurtosis(quizData))
print("Çarpıklık (Skewness):", stats.skew(quizData))

stats2 = araSinavData.describe()
print("Ara Sınav: ",stats2);
print("Basıklık (Kurtosis):", stats.kurtosis(araSinavData))
print("Çarpıklık (Skewness):", stats.skew(araSinavData))

stats3 = finalSinavData.describe()
print("Final Sınavı: ",stats3);
print("Basıklık (Kurtosis):", stats.kurtosis(finalSinavData))
print("Çarpıklık (Skewness):", stats.skew(finalSinavData))

# Shapiro-Wilk Anlamlılık Testi 
dataSetNames = ['QuizOrtalama', 'AraSinav', 'FinalSinav']
for dataSetName in dataSetNames:
    data = dataset[dataSetName]
    statsShapiro, pValueShapiro = stats.shapiro(data)
    if pValueShapiro > 0.05:
        print(f"{dataSetName} için P-değeri: {pValueShapiro}. {dataSetName} için veriler normal dağılıma sahiptir.\n")
    else:
        print(f"{dataSetName} için P-değeri: {pValueShapiro}. {dataSetName} için veriler normal dağılıma uygun değildir.\n")

# Histogram grafikleri
# Quiz
plt.hist(quizData, bins=5, color='blue', edgecolor='black')  
plt.title('Quiz Histogram Grafiği')
plt.xlabel('Değerler')
plt.ylabel('Frekans')
# plt.show()

# Ara Sınav
plt.hist(araSinavData, bins=5, color='blue', edgecolor='black')  
plt.title('Ara Sınav Histogram Grafiği')
plt.xlabel('Değerler')
plt.ylabel('Frekans')
# plt.show()

# Final Sınavı
plt.hist(finalSinavData, bins=5, color='blue', edgecolor='black')  
plt.title('Final Sınavı Histogram Grafiği')
plt.xlabel('Değerler')
plt.ylabel('Frekans')
# plt.show()


# Quiz&Final Normal dağılıma yakın --> parametrik --> Paired T-Testi
# Quiz&AraSınav Normal dağılıma yakın değil --> non-parametrik --> Wilcoxon İşaretli Sıralar Testi
stats1, pValue1 = stats.ttest_rel(quizData, finalSinavData)
sigValue = 0.05
if pValue1 < sigValue:
    print(f"QuizOrtalama ve AraSinav için aralarında anlamlı bir fark vardır. Sig. Value: {round(pValue1,3)}")
else:
    print(f"QuizOrtalama ve AraSinav için aralarında anlamlı bir fark yoktur. Sig. Value: {round(pValue1,3)}")

stats2, pValue2 = stats.wilcoxon(quizData, araSinavData)
if pValue2 < sigValue:
    print(f"QuizOrtalama ve FinalSınav için aralarında anlamlı bir fark vardır. Sig. Value: {round(pValue2,3)}")
else:
    print(f"QuizOrtalama ve FinalSınav için aralarında anlamlı bir fark yoktur. Sig. Value: {round(pValue2,3)}")


