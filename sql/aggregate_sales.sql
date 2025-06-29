DROP TABLE IF EXISTS monthly_sales_summary;

CREATE TABLE monthly_sales_summary AS
SELECT
    TO_CHAR(order_date, 'YYYY-MM') AS year_month,
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM raw_sales_data
GROUP BY TO_CHAR(order_date, 'YYYY-MM'), category
ORDER BY year_month, category;
