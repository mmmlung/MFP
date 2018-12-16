import sys
sys.path.insert(0, r'C:/Users/adm-mlung/Desktop/Projekte/MFP/Scripts')
import budget_planner as bp
import pandas as pd
import datetime

Start = pd.Timestamp(2019,1,1).normalize()
End = Start + datetime.timedelta(weeks= 32)
Anfangssaldo = 5000


budget_calendar = pd.DataFrame(index=pd.date_range(start=Start, end=End))
budget_calendar = bp.init_anfangssaldo(budget_calendar, Anfangssaldo)
budget_calendar = bp.init_fixe_einkommen(budget_calendar)
budget_calendar = bp.init_fixe_ausgaben(budget_calendar)
budget_calendar = bp.init_salden(budget_calendar)

bp.write_budget(budget_calendar)
bp.visualize_budget(budget_calendar)