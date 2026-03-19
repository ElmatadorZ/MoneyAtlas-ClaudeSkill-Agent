class DecisionEngine:

    def advise(self, insights, risks, scenarios):

        return {
            "insight_summary": insights,
            "risk_summary": risks,
            "possible_scenarios": scenarios,
            "note": "ระบบนี้ไม่ได้ให้คำแนะนำซื้อขาย แต่ช่วยให้คุณเข้าใจภาพรวมเพื่อการตัดสินใจ"
        }
