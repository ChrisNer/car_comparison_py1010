"""
Author: Christoffer N
Last updated: 2026-09-04

This program calculates and compares the cost of driving a electric and a gas driven car.
"""
days = 365          # Number of days in the year.
km = 18000          # Kilometers driven.
ins_elec = 5000     # Price of insurance for the electric car in NOK.
ins_ice = 7500      # Price of insurance for the ICE car in NOK.

# The total cost of the traffic insurance levy in NOK.
# Same for both car types.
ins_traffic = 8.38 * days

# Calculate the total running cost for the electric car.
elec_used = 0.2 * km            # The electricity consumed in kWh.
elec_price = 2.0 * elec_used    # The cost for electricity consumed in NOK.
toll_fee_elec = 0.1 * km        # The road toll fee in NOK.
# Total running cost in NOK.
elec_tot = elec_price + toll_fee_elec + ins_elec + ins_traffic

# Calculate the total running cost for the ICE car.
ice_price = 1.0 * km        # The cost of gas consumed in NOK.
toll_fee_ice = 0.3 * km     # The road toll fee in NOK.
# Total running cost in NOK.
ice_tot = ice_price + toll_fee_ice + ins_ice + ins_traffic  

cost_diff = ice_tot - elec_tot      # Cost difference between electric and ICE car.

# Present all the information.
print(f"All costs are calculated on {km} km driven over the last year.")

print(f"""
{"Category":<25} {"Electric car":>13} {"ICE car":>18}
{"-" * 62}
{"Energy/Fuel:":<25} {elec_price:>9.2f} NOK {ice_price:>17.2f} NOK
{"Road Toll:":<25} {toll_fee_elec:>9.2f} NOK {toll_fee_ice:>17.2f} NOK
{"Insurance:":<25} {ins_elec:>9.2f} NOK {ins_ice:>17.2f} NOK
{"Traffic Insurance levy:":<25} {ins_traffic:>9.2f} NOK {ins_traffic:>17.2f} NOK
{"-" * 62}
{"Total cost:":<25} {elec_tot:>9.2f} NOK {ice_tot:>17.2f} NOK

Annual cost difference: {cost_diff:.2f} NOK
""")