def generate_recommendations(kpis):

    recommendations = []

    if kpis["Average Order Value"] < 120:
        recommendations.append(
            "Increase Average Order Value using combo offers."
        )

    if kpis["Total Sellers"] < 3000:
        recommendations.append(
            "Expand Seller Network."
        )

    if kpis["Total Products"] < 30000:
        recommendations.append(
            "Increase Product Catalogue."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Business is performing very well."
        )

    return recommendations