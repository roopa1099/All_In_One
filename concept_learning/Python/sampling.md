## Sampling

1. We sample to:

    preserve distributions

    preserve patterns

    preserve relationships

    reduce compute cost

2. When Would We Choose Different Sampling?

Just conceptually (for your learning):

    If data is small

         → no sampling

    If rare events matter

        → oversample rare class

    If class imbalance

        → stratify by class label

    If time series

        → stratify by time (like your case)

3. Distribution Preservation

    Sample should preserve:

       - mean

       - variance

       - category proportions

       - time distribution

       - class ratios

4. Important Driver Variables:

    Time-driven system

        → stratify by time

        Taxi demand → stratify by:

        hour + day

    Geography-driven system

        → stratify by region

        Retail → stratify by:

        store location

    Class-driven system

        → stratify by class label

        Fraud detection:

        fraud vs non-fraud

6. Rare Events Presence

    If rare events exist:

        random sampling may remove them

        must ensure representation

7. Common Sampling Methods:

    Simple Random Sampling

        Pick rows randomly.

        df.sample(frac=0.1)


        Use when:

            data uniform

            no strong subgroups
        
   Stratified Sampling

    Sample within each subgroup.

        groupby(category) → sample per group


        Use when:

        subgroup balance matters

        Example

        sample per hour
        sample per region
        sample per class label

    Systematic Sampling

        Pick every kth row.

        every 10th row

        Use when:

            data randomly ordered

            quick sampling needed

    Cluster Sampling

        Sample entire clusters.

            Example

            select 5 cities → take all rows from them


            Used in:

                survey sampling

                geo studies

    Time-Bucket Sampling

    Stratify by time window.

        Example

        sample per day/hour


        Used in:

            traffic data

            logs

            taxi trips

            IoT data

8. Example Scenarios
    🚕 Taxi Dataset

        Driver variable = time
        → stratify by hour

    💳 Fraud Detection

        Driver variable = fraud label
        → stratify by class

    🏥 Hospital Data

        Driver variable = hospital region
        → stratify by region

    🛒 Retail Sales

        Driver variable = store type
        → stratify by store category
        

