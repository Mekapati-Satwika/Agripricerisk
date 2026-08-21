import rdflib

class AgroScope:
    def __init__(self):
        self.graph = rdflib.Graph()
        # Add simple knowledge triples
        self.graph.parse(data="""
            @prefix ex: <http://example.org/> .
            ex:HighTemp ex:affects ex:CropYield .
            ex:LowMoisture ex:affects ex:MarketPrice .
            ex:HighHumidity ex:causes ex:FungalRisk .
        """, format="turtle")

    def explain(self, data):
        if data["temperature"] > 35:
            return "High temperature affects crop yield."
        elif data["soil_moisture"] < 20:
            return "Low soil moisture increases price risk."
        elif data["humidity"] > 70:
            return "High humidity may cause fungal issues."
        else:
            return "Conditions stable — no major risks."
