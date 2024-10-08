print('Bolds All In One System')
print('For MIS525')
print('September 2024 Session')
print('By Andriana Bolds')
laborCost = float(input('Enter Labor Cost'))
materialCost = float(input('Enter Material Cost'))
overheadCost = float(input('Enter Overhead Cost'))
projectBenefit = float(input('Enter Project Benefits'))
totalProjectCost = materialCost + (laborCost + overheadCost)
projectProfit = projectBenefit - totalProjectCost
projectProfitPercent = projectProfit / totalProjectCost
print(input('---Project Summary Report---'))
print(input('Prepared by Andriana Bolds'))
print(input('Material Cost') + str(materialCost))
print(input('Labor Cost') + str(laborCost))
print(input('Overhead Cost') + str(overheadCost))
print(input('Total Cost') + str(totalProjectCost))
print('Cost Savings or Revenue Increase' + str(projectBenefit))
print('Project Profit' + str(projectProfit))
print('Project Return' + str(projectProfitPercent))
if projectProfitPercent < 0:
    print(input('Interpretation: Project not recommended for approval'))
elif projectProfitPercent == 0:
    print(input('Interpretation: Neutral'))
elif projectProfitPercent <= 0.05:
    print(input('Interpretation: Recommended for approval.'))
else:
    print(input('Interpretation: Highly recommended for approval. '))
continueAnalysis = 'Y'
while continueAnalysis == 'Y':
    laborCost = float(input('Enter Labor Cost'))
    materialCost = float(input('Enter Material Cost'))
    overheadCost = float(input('Enter Overhead Cost'))
    projectBenefit = float(input('Enter Projected Benefit'))
    projectProfit = projectBenefit - totalProjectCost
    projectProfitPercent = projectProfit / totalProjectCost
    totalProjectCost = materialCost + (laborCost + overheadCost)
    continueAnalysis = input('Would you like to analyze another project? (Y/N)')
