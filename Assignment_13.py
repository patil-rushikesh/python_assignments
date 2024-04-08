from tabulate import tabulate

def calc_emi(p, r, n, c):
    m_rate = r / 1200
    emi = p * m_rate / (1 - 1 / (1 + m_rate) ** n)
    
    print(f"EMI: {emi:.2f}\n")
    bal = p
    data = [] 
    
    for i in range(1, n + 1):
        int_part = bal * m_rate
        prin_part = emi - int_part
        bal -= prin_part
        data.append([i, f"{int_part:.2f}", f"{prin_part:.2f}", f"{bal:.2f}"])
    
    print(tabulate(data, headers=["Month", "Interest", "Principal", "Balance"], tablefmt="plain"))

p = float(input("Principal: "))
m = int(input("Loan tenure (months): "))
c = int(input("CIBIL score: "))

r = 7.5 if c >= 800 else 8.3
calc_emi(p, r, m, c)
