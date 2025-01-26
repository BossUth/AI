class InvestmentExpertSystem:
    def __init__(self):
        self.rules = [
            {"conditions": {"risk_tolerance": "high", "time_horizon": "short", "market_condition": "bullish"}, 
            "recommendation": "Crypto"},
            {"conditions": {"risk_tolerance": "low", "time_horizon": "long", "market_condition": "stable"}, 
            "recommendation": "Government Bonds"},
            {"conditions": {"risk_tolerance": "medium", "time_horizon": "long", "diversification": "low"}, 
            "recommendation": "Funds"},
            {"conditions": {"risk_tolerance": "high", "time_horizon": "long", "diversification": "high"}, 
            "recommendation": "Common Stocks"},
            {"conditions": {"risk_tolerance": "low", "time_horizon": "long", "market_condition": "bearish"}, 
            "recommendation": "Money Market Funds"},
            {"conditions": {"risk_tolerance": "medium", "time_horizon": "long", "diversification": "moderate"}, 
            "recommendation": "Exchange-Traded Funds"},
        ]

    def recommend_investments(self, profile):
        recommendations = []
        for rule in self.rules:
            if all(profile.get(condition) == value for condition, value in rule["conditions"].items()):
                recommendations.append(rule)
        return recommendations if recommendations else ["No suitable investment found."]

    def refine_rules(self, new_rule):
        self.rules.append(new_rule)

    def choose_rule(self, profile):
        matching_rules = self.recommend_investments(profile)
        if not matching_rules or matching_rules == ["No suitable investment found."]:
            return "No suitable investment found."
        print("Matching rules:")
        for idx, rule in enumerate(matching_rules, start=1):
            print(f"{idx}. {rule['recommendation']} ({rule['conditions']})")
        choice = int(input("Choose a rule by entering the number: "))
        if 1 <= choice <= len(matching_rules):
            return matching_rules[choice - 1]["recommendation"]
        return "Invalid choice."

    def add_rule_via_input(self):
        print("Add a new rule:")
        conditions = {}
        while True:
            key = input("Enter condition name (or 'done' to finish): ").strip()
            if key.lower() == 'done':
                break
            value = input(f"Enter value for condition '{key}': ").strip()
            conditions[key] = value
        recommendation = input("Enter the recommendation for this rule: ").strip()
        new_rule = {"conditions": conditions, "recommendation": recommendation}
        self.refine_rules(new_rule)
        print("New rule added successfully!")

investment_system = InvestmentExpertSystem()

profile = {
    "risk_tolerance": "high",
    "time_horizon": "short",
    "market_condition": "bullish",
}

recommendations = investment_system.recommend_investments(profile)
print(f"Recommended Investments: {', '.join(r['recommendation'] for r in recommendations if isinstance(r, dict))}")

choice = investment_system.choose_rule(profile)
print(f"You chose: {choice}")

investment_system.add_rule_via_input()

new_profile = {
    "risk_tolerance": "low",
    "time_horizon": "medium",
    "diversification": "low",
}
new_recommendations = investment_system.recommend_investments(new_profile)
print(f"New Recommended Investments: {', '.join(r['recommendation'] for r in new_recommendations if isinstance(r, dict))}")

new_choice = investment_system.choose_rule(new_profile)
print(f"You chose: {new_choice}")