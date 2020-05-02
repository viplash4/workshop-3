DECLARE
    default_year   NUMBER := 2013;
    rand_gdp       NUMBER;
    rand_rating    NUMBER;
BEGIN
--Заповнення початкових даних для таблиць states та full_city_address
    INSERT INTO states ( city_state ) VALUES ( 'Alabama' );

    INSERT INTO states ( city_state ) VALUES ( 'Alaska' );

    INSERT INTO states ( city_state ) VALUES ( 'Arkansas' );

    INSERT INTO states ( city_state ) VALUES ( 'California' );

    INSERT INTO full_city_address (
        city_name,
        city_state
    ) VALUES (
        'Autauga',
        'Alabama'
    );

    INSERT INTO full_city_address (
        city_name,
        city_state
    ) VALUES (
        'Baldwin',
        'Alabama'
    );

    INSERT INTO full_city_address (
        city_name,
        city_state
    ) VALUES (
        'Bethel Census Area',
        'Alaska'
    );

    INSERT INTO full_city_address (
        city_name,
        city_state
    ) VALUES (
        'Los Angeles',
        'California'
    );

--цикл Autaga,Alabama

    FOR i IN 1..5 LOOP
        rand_gdp := dbms_random.value(1, 10000);
        rand_rating := dbms_random.value(1, 100);
        INSERT INTO city_info (
            city_name,
            city_state,
            stat_year,
            city_gdp,
            city_rating
        ) VALUES (
            'Autauga',
            'Alabama',
            default_year + i,
            rand_gdp,
            rand_rating
        );

    END LOOP;
--Bethel Census Area, Alaska

    FOR i IN 1..5 LOOP
        rand_gdp := dbms_random.value(1, 10000);
        rand_rating := dbms_random.value(1, 100);
        INSERT INTO city_info (
            city_name,
            city_state,
            stat_year,
            city_gdp,
            city_rating
        ) VALUES (
            'Bethel Census Area',
            'Alaska',
            default_year + i,
            rand_gdp,
            rand_rating
        );

    END LOOP;

END;


