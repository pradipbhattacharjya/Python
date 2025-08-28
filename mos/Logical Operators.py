#if applicat has high income AND good credit Eligible for loan

has_high_income = True
has_good_credit = False
has_criminal_record = False


if has_high_income and has_good_credit:
    print("Eligible for loan")

#if applicat has high income or good credit Eligible for loan

if has_good_credit or has_high_income:
    print("Eligible for loan")


if has_good_credit and not has_criminal_record:
    print("Eligible for loan")