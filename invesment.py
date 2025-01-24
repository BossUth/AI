class InvestmentExpertSystem:
    def __init__(self):
        self.rules = [
            {"conditions": {"risk_tolerance": "high", "time_horizon": "short"}, "recommendation": "Cryptocurrency"},
            {"conditions": {"risk_tolerance": "low", "time_horizon": "long"}, "recommendation": "Government Bonds"},
            {"conditions": {"risk_tolerance": "medium", "time_horizon": "medium"}, "recommendation": "Mutual Funds"},
            {"conditions": {"risk_tolerance": "high", "time_horizon": "long"}, "recommendation": "Stocks"},
            {"conditions": {"risk_tolerance": "low", "time_horizon": "short"}, "recommendation": "Money Market Funds"},
        ]

    def recommend_investment(self, profile):
        for rule in self.rules:
            if all(profile.get(condition) == value for condition, value in rule["conditions"].items()):
                return rule["recommendation"]
        return "No suitable investment found."

    def refine_rules(self, new_rule):
        self.rules.append(new_rule)

investment_system = InvestmentExpertSystem()

profile = {
    "risk_tolerance": "high",
    "time_horizon": "short",
}

recommendation = investment_system.recommend_investment(profile)
print(f"Recommended Investment: {recommendation}")

new_rule = {"conditions": {"risk_tolerance": "medium", "time_horizon": "long"}, "recommendation": "Index Funds"}
investment_system.refine_rules(new_rule)

new_profile = {
    "risk_tolerance": "medium",
    "time_horizon": "long",
}
new_recommendation = investment_system.recommend_investment(new_profile)
print(f"New Recommended Investment: {new_recommendation}")