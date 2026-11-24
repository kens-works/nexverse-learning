transactions = [ ('CUST-001', 250.0, True), ('CUST-002', 40.0, True), ('CUST-003', 120.0, False), ('CUST-004', 80.0, True), ('CUST-005', 15.0, False) ]

def loyalty_assessment(transaction_logs:list[tuple]):
  loyalty_records = []
  sum_points = 0.0
  for each_trans in transaction_logs:
    a = list(each_trans)
    # points = 0
    # tier = ""
    '''points calculation condition
    If is_member is True and purchase_amount >= 50, calculate points as purchase_amount * 0.10 (10%).
    If is_member is True and purchase_amount < 50, calculate points as purchase_amount * 0.05 (5%).
    If is_member is False, points are 0.'''
    if a[2] and a[1] >= 50:
      points = a[1] * 0.10
    elif a[2] and a[1] < 50:
      points = a[1] * 0.05      
    else:
      points = 0
    '''tier criteria
    Determine tier: points >= 20 -> 'Gold', points >= 5 -> 'Silver', else -> 'Standard' 
    '''
    if points >= 20:
      tier = 'Gold'
    elif points >=5:
      tier = 'Sliver'
    else:
      tier = 'Standard'
    # Append point and tier to list. Convert it to tuple for persistence and append to the list loyalty_records
    a.append(points)
    a.append(tier)
    sum_points = sum_points + points
    print(tuple(a))
    loyalty_records.append(tuple(a))
  print("Total points : ", sum_points)
  return f"{loyalty_records}"

loyalty_records = loyalty_assessment(transactions)
print ("Final loyalty records :", loyalty_records )