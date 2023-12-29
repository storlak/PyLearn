data = [
    {"symbol": "ABCD", "name": "ABCD Company", "ranking": 2, "risk": 0.2},
    {"symbol": "BCDE", "name": "BCDE Company", "ranking": 5, "risk": 0.2},
    {"symbol": "CDEF", "name": "CDEF Company", "ranking": 8, "risk": 0.5},
    {"symbol": "DEFG", "name": "DEFG Company", "ranking": 7, "risk": 0.8},
    {"symbol": "EFGH", "name": "EFGH Company", "ranking": 9, "risk": 0.6},
    {"symbol": "FGHI", "name": "FGHI Company", "ranking": 10, "risk": 0.1},
    {"symbol": "GHIJ", "name": "GHIJ Company", "ranking": 3, "risk": 0.6},
    {"symbol": "HIJK", "name": "HIJK Company", "ranking": 5, "risk": 0.5},
    {"symbol": "IJKL", "name": "IJKL Company", "ranking": 5, "risk": 0.7},
    {"symbol": "JKLM", "name": "JKLM Company", "ranking": 6, "risk": 0.9},
    {"symbol": "KLMN", "name": "KLMN Company", "ranking": 6, "risk": 0.4},
    {"symbol": "LMNO", "name": "LMNO Company", "ranking": 8, "risk": 0.4},
    {"symbol": "MNOP", "name": "MNOP Company", "ranking": 8, "risk": 0.2},
    {"symbol": "NOPQ", "name": "NOPQ Company", "ranking": 1, "risk": 0.5},
    {"symbol": "OPQR", "name": "OPQR Company", "ranking": 9, "risk": 0.2},
    {"symbol": "PQRS", "name": "PQRS Company", "ranking": 10, "risk": 0.9},
    {"symbol": "QRST", "name": "QRST Company", "ranking": 3, "risk": 0.4},
    {"symbol": "RSTU", "name": "RSTU Company", "ranking": 7, "risk": 0.3},
    {"symbol": "STUV", "name": "STUV Company", "ranking": 8, "risk": 0.1},
    {"symbol": "TUVW", "name": "TUVW Company", "ranking": 7, "risk": 0.9},
]

result = [d for d in data if d["ranking"] >= 6 and d["risk"] < 0.6]
print(result)
