def get_water_usage(category, items):
    print(f"\nEnter {category} Water Usage (in liters per person per day):")
    total = 0
    for item in items:
        value = float(input(f"  {item}: "))
        total += value
    print(f"  Total {category} Water Usage: {total} liters\n")
    return total

def main():
    print("💧 Water Footprint Calculator 💧\n")

    direct_items = [
        "Drinking Water",
        "Cooking (Food and Drink)",
        "Bathing or Showering",
        "Flushing the Toilet (per flush)",
        "Handwashing and personal hygiene",
        "Laundry (washing machine)",
        "Cleaning and general household use"
    ]

    virtual_items = [
        "Food (diet-dependent)",
        "Clothing (varies based on consumption)",
        "Energy (varies based on source)"
    ]

    indirect_items = [
        "Clothing (textile production)",
        "Electricity (varies by source)",
        "Other products and services"
    ]

    direct_total = get_water_usage("Direct", direct_items)
    virtual_total = get_water_usage("Virtual", virtual_items)
    indirect_total = get_water_usage("Indirect", indirect_items)

    total_water_footprint = direct_total + virtual_total + indirect_total
    print("🌊 Total Water Footprint Calculation 🌊")
    print(f"  Direct Water Usage   : {direct_total} liters")
    print(f"  Virtual Water Usage  : {virtual_total} liters")
    print(f"  Indirect Water Usage : {indirect_total} liters")
    print(f"\n🔵 Total Water Footprint: {total_water_footprint:.2f} liters per day 🔵")

if _name_ == "_main_":
    main()
