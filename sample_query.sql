-- Sample SQL query to analyze campaign performance

SELECT 
    campaign_name,
    COUNT(user_id) AS total_signups,
    ROUND(AVG(conversion_rate), 2) AS avg_conversion_rate
FROM marketing_campaigns
WHERE signup_date BETWEEN '2025-01-01' AND '2025-12-31'
GROUP BY campaign_name
ORDER BY avg_conversion_rate DESC;
