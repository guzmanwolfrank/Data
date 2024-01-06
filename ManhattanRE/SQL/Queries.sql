 
 
 
 # Query 1: Number of properties sold per neighborhood? 

        query1 = """
        SELECT NEIGHBORHOOD, COUNT(*) AS num_sales
        FROM sales_data
        GROUP BY NEIGHBORHOOD
        ORDER BY num_sales DESC
        """
        
        # Query 2: What is the distribution of Sale Prices by Building Category? 
        
        query2 = """
        SELECT BLDGCAT, SALE_PRICE
        FROM sales_data
        WHERE SALE_PRICE IS NOT NULL;      
        """

        # Query 3:  What is the Sales distribution over Time? 

        query3 = """
        SELECT SALE_DATE, SALE_PRICE
        FROM sales_data
        WHERE SALE_PRICE IS NOT NULL;
        """

        # Query 4: What is the Sales Price distribution by Neighborhood? 

        query4 = """
        SELECT NEIGHBORHOOD, SALE_PRICE
        FROM sales_data
        WHERE SALE_PRICE IS NOT NULL;
        """

        # Query 5: What is the number of properties sold by tax class?
        query5 = """
        SELECT TAXCLP, COUNT(*) AS num_sales
        FROM sales_data
        GROUP BY TAXCLP;
        """
       

        # Query 6: What is the Average GROSS SF by Neighborhood?
        
        query6 = """
        SELECT NEIGHBORHOOD, AVG(GROSSSF) AS avg_gross_sf
        FROM sales_data
        GROUP BY NEIGHBORHOOD;
        """

    