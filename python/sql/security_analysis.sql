-- ==========================================================
-- IT SECURITY DATA ANALYSIS
-- Financial Services Case Study
-- ==========================================================

-- 1. Total number of security events

SELECT
    COUNT(*) AS total_security_events
FROM security_events;


-- 2. Security events by severity

SELECT
    severity,
    COUNT(*) AS number_of_events
FROM security_events
GROUP BY severity
ORDER BY number_of_events DESC;


-- 3. Security events by department

SELECT
    department,
    COUNT(*) AS number_of_events
FROM security_events
GROUP BY department
ORDER BY number_of_events DESC;


-- 4. High and Critical security events

SELECT
    department,
    COUNT(*) AS high_risk_events
FROM security_events
WHERE severity IN ('High', 'Critical')
GROUP BY department
ORDER BY high_risk_events DESC;


-- 5. Security events by technology

SELECT
    source,
    COUNT(*) AS number_of_events
FROM security_events
GROUP BY source
ORDER BY number_of_events DESC;


-- 6. Most common security events

SELECT
    event_type,
    COUNT(*) AS number_of_events
FROM security_events
GROUP BY event_type
ORDER BY number_of_events DESC;
