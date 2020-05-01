CREATE VIEW city_data AS
    SELECT
        c1.city_name
        || ', '
        || c1.city_state AS city_name,
        stat_year,
        city_gdp,
        city_rating
    FROM
        city_info           c1
        JOIN full_city_address   c2 ON c1.city_name = c2.city_name
        JOIN states              s ON c2.city_state = s.city_state;
        

        

