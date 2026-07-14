def print_report(kpis, score, status, recommendations):

    print("\n" + "="*60)
    print("          BUSINESS MRI REPORT")
    print("="*60)

    print("\nBUSINESS KPIs\n")

    for key, value in kpis.items():

        if isinstance(value, float):

            print(f"{key:<25}: {value:,.2f}")

        else:

            print(f"{key:<25}: {value:,}")

    print("\n" + "-"*60)

    print(f"Business Score         : {score}/100")
    print(f"Business Status        : {status}")

    print("\nRecommendations\n")

    for i, recommendation in enumerate(recommendations, 1):

        print(f"{i}. {recommendation}")

    print("="*60)